from hashlib import sha1


def grade(autogen, key):
    secret = "jfryabsdhii753hyaf68db6"
    n = autogen.instance
    flag = "cs628a{" + sha1((str(n) + secret).encode('utf-8')).hexdigest()[:22]+"}"
    if flag.lower() in key.lower().strip():
        return True, "Correct!"
    else:
        return False, "Try Again."
