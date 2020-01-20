require('es6-promise').polyfill();

const { src, dest, series} = require('gulp');
const browserify = require('browserify');
const concatCss = require('gulp-concat-css');
const cleanCSS = require('gulp-clean-css');
const sass = require('gulp-sass');
const uglify = require('gulp-uglify');
const buffer = require('vinyl-buffer');
const source = require('vinyl-source-stream');
const sourcemaps = require('gulp-sourcemaps');
const merge = require('merge-stream');
const postcss = require('gulp-postcss');
const pxtorem = require('postcss-pxtorem');
const autoprefixer = require('autoprefixer');
const shell = require('gulp-shell');
const replace = require('gulp-replace');

var cssProcessors = [
    autoprefixer(),
    pxtorem({
        rootValue: 14,
        replace: false,
        propWhiteList: []
    })
];

function scripts() {
    return browserify('./jet/static/jet/js/src/main.js')
        .bundle()
        .on('error', function(error) { console.error(error); })
        .pipe(source('bundle.min.js'))
        .pipe(buffer())
        .pipe(uglify())
        .pipe(dest('./jet/static/jet/js/build/'));
}

function styles() {
    return src('./jet/static/jet/css/**/*.scss')
        .pipe(sourcemaps.init())
        .pipe(sass({outputStyle: 'compressed'}))
        .on('error', function(error) { console.error(error); })
        .pipe(postcss(cssProcessors))
        .on('error', function(error) { console.error(error); })
        .pipe(sourcemaps.write('./'))
        .pipe(dest('./jet/static/jet/css'));
}

function vendorStyles() {
    return merge(
        src('./node_modules/jquery-ui/themes/base/images/*')
            .pipe(dest('./jet/static/jet/css/jquery-ui/images/')),
        merge(
            src([
                './node_modules/select2/dist/css/select2.css',
                './node_modules/timepicker/jquery.ui.timepicker.css'
            ]),
            src('./node_modules/jquery-ui/themes/base/all.css')
                .pipe(cleanCSS()) // needed to remove jQuery UI comments breaking concatCss
                .on('error', function(error) { console.error(error); })
                .pipe(concatCss('jquery-ui.css', {rebaseUrls: false}))
                .on('error', function(error) { console.error(error); })
                .pipe(replace('images/', 'jquery-ui/images/'))
                .on('error', function(error) { console.error(error); }),
            src('./node_modules/perfect-scrollbar/src/css/main.scss')
                .pipe(sass({outputStyle: 'compressed'}))
                .on('error', function(error) { console.error(error); })
        )
            .pipe(postcss(cssProcessors))
            .on('error', function(error) { console.error(error); })
            .pipe(concatCss('vendor.css', {rebaseUrls: false}))
            .on('error', function(error) { console.error(error); })
            .pipe(cleanCSS())
            .on('error', function(error) { console.error(error); })
            .pipe(dest('./jet/static/jet/css'))
    )
}

function vendorTranslations() {
    return merge(
        src('./node_modules/jquery-ui/ui/i18n/*.js')
            .pipe(dest('./jet/static/jet/js/i18n/jquery-ui/')),
        src('./node_modules/timepicker/i18n/*.js')
            .pipe(dest('./jet/static/jet/js/i18n/jquery-ui-timepicker/')),
        src('./node_modules/select2/dist/js/i18n/*.js')
            .pipe(dest('./jet/static/jet/js/i18n/select2/'))
    )
}

function compileLocales() {
    return shell(" python manage.py compilemessages");
}

exports.locales = series(compileLocales);
exports.default = series(scripts, styles, vendorStyles, vendorTranslations);
