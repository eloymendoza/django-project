import os

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Application definition

BASE_APPS = [
    'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'sslserver',
    # 'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.mycore',
    'apps.areas',
    'apps.rfacial',
    'apps.sistemas',
    'apps.componentes',
    'apps.ActiveDirectory',
    'apps.AsignarUsuario'
]

THIRD_APPS = [
    # 'material',
    # 'material.admin',
    "django_components",
    "django_components.safer_staticfiles",
    'drf_yasg',
    'rest_framework',
    'rest_framework_simplejwt'
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS



BASE_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_components.middleware.ComponentDependencyMiddleware',
    'querycount.middleware.QueryCountMiddleware'
    
]

LOCAL_MIDDLEWARE =[

]

THIRD_MIDDLEWARE =[
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

MIDDLEWARE = BASE_MIDDLEWARE + LOCAL_MIDDLEWARE + THIRD_MIDDLEWARE



ROOT_URLCONF = 'config.urls'
 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,),
                 os.path.join(BASE_DIR, 'apps/ActiveDirectory/templates'),
                 os.path.join(BASE_DIR, 'components', 'templates'),
                 
                 os.path.join(BASE_DIR, 'apps/AsignarUsuario/templates'),
                 ],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders':[(
                'django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    'django_components.template_loader.Loader',
                ]
            )],
            'builtins': [
                'django_components.templatetags.component_tags',
            ]
        },
    },
]

COMPONENTS = { 'RENDER_DEPENDENCIES': True }



WSGI_APPLICATION = 'config.wsgi.application'

 
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_PERMISSION_MODEL = 'apps.areas.Permisos'

