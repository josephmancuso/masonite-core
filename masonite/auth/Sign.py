from cryptography.fernet import Fernet

class Sign(object):

    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            from config import application
            self.key = application.KEY
        self.encryption = None

    def sign(self, value):
        f = Fernet(self.key)
        self.encryption = f.encrypt(bytes(value, 'utf-8'))
        return self.encryption
    
    def unsign(self, value=None):
        f = Fernet(self.key)

        if not value:
            return f.decrypt(self.encryption).decode('utf-8')
        return f.decrypt(value).decode('utf-8')
