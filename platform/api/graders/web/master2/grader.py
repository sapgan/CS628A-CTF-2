from hashlib import md5

def grade(autogen, key):
    secretkey = "asdasd98a9ndand987a83nuindna9721n9n923"
    if "flagIsWhoKilLeDHaRamBeNatrajNotAGoodPass" in key.strip():
        return True, "You sir are a master hacker!"
    else:
        return False, "Try Again."
