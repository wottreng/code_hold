import base64

def encrypt(message):
    num = 3
    x = 0
    while x < num:
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        message = base64_bytes.decode('ascii')
        x += 1
    return message

def decrypt(message):
    num = 3
    x = 0
    while x < num:
        base64_message = message
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        x += 1
    return message
