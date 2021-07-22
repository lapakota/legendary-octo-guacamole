from utils import base64string


class Message:
    def __init__(self, config):
        targets_address = ','.join(f'"{x}" <{x}>' for x in config.recipients)
        self.boundary = f'BoUnD1234567890987654321BoUnD'
        self.header = f'From:{config.user_address}\n' \
                      f'To:{targets_address}\n' \
                      f'Subject: =?UTF-8?B?{base64string(config.subject or "No subject")}?=\n' \
                      f'Content-type: multipart/mixed; boundary={self.boundary}\n' \
                      f'\n'
        self.text = self.get_text(config.message_file).replace('\n.', '\n..')

    def append(self, message):
        self.text += f'{self.get_start_boundary()}\n{message}'

    def end(self):
        self.text += f'\n{self.get_end_boundary()}\n.\n'

    def get_start_boundary(self):
        return f'--{self.boundary}'

    def get_end_boundary(self):
        return f'--{self.boundary}--'

    def get_content(self):
        return f'{self.header}\n{self.text}'

    @staticmethod
    def get_text(filename):
        with open(filename, "r", encoding="utf8") as f:
            message = "".join(f.readlines())
        content = f'Content-Transfer-Encoding: 8bit\n' \
                  f"Content-Type: text/plain; charset=utf-8\n\n" \
                  f"{message}"
        return content
