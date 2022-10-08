
import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


# 3rd party secret_key and url
GH_ID = "4afdb2edb0701a9e9733"
GH_SECRET = "0bb365e7f34c7df81746aa14e23c5f4f1a0f613c"

KAKAO_ID = "f80de15ab872ae0d2e61bdfb1eeee521"
KAKAO_SECRET = ""

# URL = "http://127.0.0.1:8000"
URL = "http://ec2-3-38-94-90.ap-northeast-2.compute.amazonaws.com"
# URL = "https://aircl.fatexyzea.ml"


""" Email Configuration """
GMAIL_USERNAME = "testnova0713@gmail.com"
GMAIL_PASSWORD = "78915qwr"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = GMAIL_USERNAME
EMAIL_HOST_PASSWORD = GMAIL_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_FROM = "myemail@gmail.com"  # 설정하고 싶은 이메일로


# 0: debug mode, 1:local db mode, 2: dev mode, 3: server mode
DEBUG = False
MODE = 1

# local db
RDS_HOST = "localhost"
RDS_NAME = "postgres"
RDS_USER = "postgres"
RDS_PASSWORD = "1234"
RDS_PORT = "5432"

# dev db
# RDS_HOST = "airbnb-clone.c3zvy5tas55z.ap-northeast-2.rds.amazonaws.com"
# RDS_NAME = "postgres"
# RDS_USER = "postgres"
# RDS_PASSWORD = "15945qwa!#"
# RDS_PORT = "5432"

if MODE > 0:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": RDS_HOST,
            "NAME": RDS_NAME,
            "USER": RDS_USER,
            "PASSWORD": RDS_PASSWORD,
            "PORT": "5432",
        }
    }


""" s3 셋팅 """
if MODE > 1:

    DEFAULT_FILE_STORAGE = "config.custom_storages.UploadStorage"
    STATICFILES_STORAGE = "config.custom_storages.StaticStorage"
    AWS_ACCESS_KEY_ID = "AKIAYI4MZFLBCQDVIFOX"
    AWS_SECRET_ACCESS_KEY = "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"
    AWS_STORAGE_BUCKET_NAME = "airbnb-clone12"
    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"

    if not DEBUG:
        # Sentry
        sentry_sdk.init(
            dsn="https://6dffb457726b409694bd90659250e59b@o1066154.ingest.sentry.io/6058707",
            integrations=[DjangoIntegration()],
            traces_sample_rate=1.0,
            send_default_pii=True,
        )


DJANGO_ADMIN = "xyza/"

DJANGO_SECRET = "AFrjs#^~)ai$]YaS{V5mHFvyi[rCr_b"
SECRET_KEY = DJANGO_SECRET


ADMIN_PW = "12396qawsed"


REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}


if not DEBUG:
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
        "rest_framework.renderers.JSONRenderer",
    ]
