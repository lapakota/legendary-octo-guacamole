import base64


def base64string(msg):
    return base64.b64encode(msg.encode()).decode()
