module.exports = function(str) {
    if (window.django === undefined) {
        return str;
    } else if (typeof window.django.gettext === "function") {
        return django.gettext(str);
    } else {
        return str;
    }
};
