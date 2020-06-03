import hashlib


def md5(raw):
    hl = hashlib.md5()
    hl.update(raw.encode('utf8'))
    return hl.hexdigest()
