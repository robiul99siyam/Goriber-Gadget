from pathlib import Path
import dj_database_url
import environ
env = environ.Env()
environ.Env.read_env()
BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = True

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ['https://goriber-gadget.onrender.com','https://*.127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',



    # internal 
    "Blog",
    "conver_and_glass",
    "fitness_and_wearable",
    "loptob_and_desktop",
    "peripheries",
    "phone_and_tablet",
    "power_and_accessories",
    "smart_elecotorines",
    "sound_equipment",
    "uesr_Devices",
    "all_product",
    'drf_multiple_model',

    #Extranal 
    "rest_framework",
    'corsheaders',
    'django_filters', 

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]



CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]


ROOT_URLCONF = 'gadget_e_com_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gadget_e_com_project.wsgi.application'



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
SECRET_KEY = env("SECRET_KEY")
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': env("DB_NAME"),
#         'USER': env("DB_USER"),
#         'PASSWORD': env("DB_PASSWORD"),
#         'HOST': env("DB_HOST"),
#         'PORT': env("DB_PORT"),
#     }
# }


# Replace the SQLite DATABASES configuration with PostgreSQL:
DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgres://goriber_gadget_user:m2EB7Oz7YzNWcQwQEnuM5XKzcPPuIEzV@dpg-coj8ch8l6cac739sp4c0-a.oregon-postgres.render.com/goriber_gadget',
       
    )
}
# REST_FRAMEWORK = {
#     'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    
# }

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




STATIC_URL = 'static/'
MEDIA_URL = '/media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
