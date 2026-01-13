

class SecretManager:
    def __init__(self):
        self.secrets = {}

    def store_secret(self, key, value):
        self.secrets[key] = value

    def retrieve_secret(self, key):
        return self.secrets.get(key, None)

    def delete_secret(self, key):
        if key in self.secrets:
            del self.secrets[key]
