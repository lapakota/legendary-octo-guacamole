import json


class ConfigData:
    def __init__(self, path: str):
        self.port = 465
        with open(path, encoding="utf8") as file:
            config = json.load(file)
            self.host_address = config["host_address"]
            self.user_address = config["user_address"]
            self.user_name = self.user_address.split('@')[0]
            self.password = config["password"]
            self.recipients = config["recipients"]
            self.message_file = config["message_file"]
            self.subject = config["subject"]
            self.attachments = config["attachments"]
