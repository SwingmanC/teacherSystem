class Config:
    SECRET_KEY = "test"

    SQLALCHEMY_TRACK_MODIFICATIONS=False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@127.0.0.1:3306/teachSystem?charset=utf8"

config = {
    'default':DevelopmentConfig
}