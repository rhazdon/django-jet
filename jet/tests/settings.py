import os

import django
from django.conf import global_settings


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = "!DJANGO_JET_TESTS!"

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_PROPAGATE_EXCEPTIONS = True

ROOT_URLCONF = "jet.tests.urls"

INSTALLED_APPS = [
    "jet.dashboard",
    "jet",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "jet.tests",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": (
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            )
        },
    }
]

SITE = 1

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "sqlite3.sql"}}

USE_I18N = True
USE_L10N = True

TIME_ZONE = "UTC"
LANGUAGE_CODE = "en-us"

LANGUAGES = [
    ("af", "Afrikaans"),
    ("ar", "Arabic"),
    ("ar-dz", "Algerian Arabic"),
    ("ast", "Asturian"),
    ("az", "Azerbaijani"),
    ("bg", "Bulgarian"),
    ("be", "Belarusian"),
    ("bn", "Bengali"),
    ("br", "Breton"),
    ("bs", "Bosnian"),
    ("ca", "Catalan"),
    ("cs", "Czech"),
    ("cy", "Welsh"),
    ("da", "Danish"),
    ("de", "German"),
    ("dsb", "Lower Sorbian"),
    ("el", "Greek"),
    ("en", "English"),
    ("en-au", "Australian English"),
    ("en-gb", "British English"),
    ("eo", "Esperanto"),
    ("es", "Spanish"),
    ("es-ar", "Argentinian Spanish"),
    ("es-co", "Colombian Spanish"),
    ("es-mx", "Mexican Spanish"),
    ("es-ni", "Nicaraguan Spanish"),
    ("es-ve", "Venezuelan Spanish"),
    ("et", "Estonian"),
    ("eu", "Basque"),
    ("fa", "Persian"),
    ("fi", "Finnish"),
    ("fr", "French"),
    ("fy", "Frisian"),
    ("ga", "Irish"),
    ("gd", "Scottish Gaelic"),
    ("gl", "Galician"),
    ("he", "Hebrew"),
    ("hi", "Hindi"),
    ("hr", "Croatian"),
    ("hsb", "Upper Sorbian"),
    ("hu", "Hungarian"),
    ("hy", "Armenian"),
    ("ia", "Interlingua"),
    ("id", "Indonesian"),
    ("io", "Ido"),
    ("is", "Icelandic"),
    ("it", "Italian"),
    ("ja", "Japanese"),
    ("ka", "Georgian"),
    ("kab", "Kabyle"),
    ("kk", "Kazakh"),
    ("km", "Khmer"),
    ("kn", "Kannada"),
    ("ko", "Korean"),
    ("lb", "Luxembourgish"),
    ("lt", "Lithuanian"),
    ("lv", "Latvian"),
    ("mk", "Macedonian"),
    ("ml", "Malayalam"),
    ("mn", "Mongolian"),
    ("mr", "Marathi"),
    ("my", "Burmese"),
    ("nb", "Norwegian Bokmål"),
    ("ne", "Nepali"),
    ("nl", "Dutch"),
    ("nn", "Norwegian Nynorsk"),
    ("os", "Ossetic"),
    ("pa", "Punjabi"),
    ("pl", "Polish"),
    ("pt", "Portuguese"),
    ("pt-br", "Brazilian Portuguese"),
    ("ro", "Romanian"),
    ("ru", "Russian"),
    ("sk", "Slovak"),
    ("sl", "Slovenian"),
    ("sq", "Albanian"),
    ("sr", "Serbian"),
    ("sr-latn", "Serbian Latin"),
    ("sv", "Swedish"),
    ("sw", "Swahili"),
    ("ta", "Tamil"),
    ("te", "Telugu"),
    ("th", "Thai"),
    ("tr", "Turkish"),
    ("tt", "Tatar"),
    ("udm", "Udmurt"),
    ("uk", "Ukrainian"),
    ("ur", "Urdu"),
    ("uz", "Uzbek"),
    ("vi", "Vietnamese"),
    ("zh-hans", "Simplified Chinese"),
    ("zh-hant", "Traditional Chinese"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = ""

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

JET_INDEX_DASHBOARD = "jet.tests.dashboard.TestIndexDashboard"
JET_APP_INDEX_DASHBOARD = "jet.tests.dashboard.TestAppIndexDashboard"
