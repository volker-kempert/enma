# -*- coding: utf-8 -*-
import os

os_env = os.environ

class Config(object):
    SECRET_KEY = os_env['ENMA_SECRET']  # TODO: Change me
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.

    MAIL_SERVER = 'localhost'
    if 'MAIL_SERVER' in os_env.keys():
        MAIL_SERVER = os_env['MAIL_SERVER']
    MAIL_PORT = 25
    if 'MAIL_PORT' in os_env.keys():
        MAIL_PORT = int(os_env['MAIL_PORT'])
    MAIL_USE_SSL = False
    if 'MAIL_USE_SSL' in os_env.keys():
        MAIL_USE_SSL = True
    MAIL_USE_TLS = True
    if 'MAIL_USE_TLS' in os_env.keys():
        MAIL_USE_TLS = True
    MAIL_USERNAME = os_env['MAIL_USERNAME']
    MAIL_PASSWORD = os_env['MAIL_PASSWORD']
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    MAIL_SUBJECT_PREFIX = '[ENMA] '


class ProdConfig(Config):
    """Production configuration. -  aligned to openshift """
    ENV = 'prod'
    DEBUG = False

    DB_USER = 'enma'
    if 'OPENSHIFT_POSTGRESQL_DB_USERNAME' in os_env.keys():
        DB_USER = os_env['OPENSHIFT_POSTGRESQL_DB_USERNAME']
    DB_PASSWORD = 'enma-password'
    if 'OPENSHIFT_POSTGRESQL_DB_PASSWORD' in os_env.keys():
        DB_PASSWORD = os_env['OPENSHIFT_POSTGRESQL_DB_PASSWORD']
    DB_HOST = 'localhost'
    if 'OPENSHIFT_POSTGRESQL_DB_HOST' in os_env.keys():
        DB_HOST = os_env['OPENSHIFT_POSTGRESQL_DB_HOST']
    DB_PORT = '5432'
    if 'OPENSHIFT_POSTGRESQL_DB_PORT' in os_env.keys():
        DB_PORT = os_env['OPENSHIFT_POSTGRESQL_DB_PORT']
    DB_NAME = 'enma'
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + DB_USER + ':' + DB_PASSWORD \
                              + '@' + DB_HOST + ':' + DB_PORT + '/' + DB_NAME
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class TestConfig(Config):
    # suppresses evaluation login_required decorator
    #  also suppresses sending emails
    TESTING = True
    DEBUG = True
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USE_SSL = False
    MAIL_USE_TLS = False
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_DEFAULT_SENDER = 'test@test.org'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 1  # For faster tests
    WTF_CSRF_ENABLED = False  # Allows form testing