from hashlib import md5

def grade(autogen, key):
    secretkey = "asdasd98a9ndand987a83nuindna9721n9n923"
    if "f121629e43fd2d87c74cef231adbb192e30d501e" in key.strip():
        return True, "Awesome.Thanks for playing the game! "
    else:
        return False, "Try Again."
