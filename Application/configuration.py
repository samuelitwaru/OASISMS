class BaseConfig(object):
    'Base config class'
    SECRET_KEY = "A590LTGhyGRsXvcz25NNNVxfdJBxz359nF"


class ProductionConfig(BaseConfig):
    'Production specific config'
    DEBUG = False
    TESTING = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'amobittechnologiez@gmail.com'
    MAIL_PASSWORD = '@_AmoBit2020'
    MAIL_DEFAULT_SENDER = 'amobittechnologiez@gmail.com'


class DevelopmentConfig(BaseConfig):
    'Development environment specific config'
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'samuelitwaru@gmail.com'
    MAIL_PASSWORD = 'helloitwaru'
    MAIL_DEFAULT_SENDER = 'samuelitwaru@gmail.com'
