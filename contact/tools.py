from hashlib import sha512


def gen_secret(passwd):
    sha1 = sha512()
    sha1.update(passwd.encode("utf-8"))
    return sha1.hexdigest()