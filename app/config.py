"""Config file."""

import os


class Config(object):
    """Default configuration options."""

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    BCRYPT_LOG_ROUNDS = 15
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'add-your-random-key-here'


class ProductionConfig(Config):
    """Production configuration options."""

    DEBUG = False


class StagingConfig(Config):
    """Staging configuration options."""

    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    """Development configuration options."""

    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = False


class TestingConfig(Config):
    """TESTING configuration options."""

    TESTING = True
    WTF_CSRF_ENABLED = False
