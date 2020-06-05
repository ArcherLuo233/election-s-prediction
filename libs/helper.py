import hashlib


def md5(raw):
    if isinstance(raw, str):
        raw = raw.encode('utf8')
    return hashlib.md5(raw).hexdigest()
