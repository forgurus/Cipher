import base64
from Crypto.Cipher import AES


AESC_KEY="1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik," 
class AESCipher(object):
    """
    https://github.com/dlitz/pycrypto
    """
    def __init__(self, key):
        self.key = key
        self.BS = 16
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS).encode()
        self.unpad = lambda s: s[:-ord(s[len(s)-1:])]
        self.iv=chr(0) * 16

    def encrypt(self, message):
        """
        It is assumed that you use Python 3.0+
        , so plaintext's type must be str type(== unicode).
        """
        message = message.encode("utf-8")
        raw = self.pad(message)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        dec = cipher.decrypt(enc)
        return self.unpad(dec).decode('utf-8')

#return self.unpad(dec).decode('utf-8')


if __name__ == "__main__":
    aesCipher = AESCipher(AESC_KEY)
        
