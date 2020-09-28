#-*- coding = utf-8 -*-
#@Time : 2020/9/28 17:51
#@Author : 赵玉琦
#@software : PyCharm

from .base import * #NOQA

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
