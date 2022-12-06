class Config(object):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db'

    AUTH0_DOMAIN = "dev-1ipheitoccjnh67e.us.auth0.com"
    API_AUDIENCE = "https://dev-1ipheitoccjnh67e.us.auth0.com/api/v2/"