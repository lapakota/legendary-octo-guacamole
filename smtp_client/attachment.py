import base64
import mimetypes
import os

from utils import base64string

mimetypes.init()


class Attachment:
    def __init__(self, filename):
        file_extension = os.path.splitext(filename)[1]
        content_type = mimetypes.types_map[file_extension]
        name = filename.split('/')[-1]
        base64_filename = f"=?UTF-8?B?{base64string(name)}?="
        base64_attachment = self.get_file_content(filename)
        self.content = f'Content-Type: {content_type}; name="{base64_filename}"\n' \
                       f'Content-Disposition: attachment; filename="{base64_filename}"\n' \
                       f'Content-Transfer-Encoding: base64\n' \
                       f'\n' \
                       f'{base64_attachment}'

    @staticmethod
    def get_file_content(filename):
        with open(filename, "rb") as f:
            return base64.b64encode(f.read()).decode()
