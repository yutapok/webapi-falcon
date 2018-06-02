import configparser
class Swooper:
    config = configparser.SafeConfigParser()
    config.read('/vagrant/libs/falcon.ini', encoding='utf-8')

    @classmethod
    def load_config(cls):
        return cls.config
