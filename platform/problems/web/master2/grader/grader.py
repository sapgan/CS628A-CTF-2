from hashlib import md5

def grade(autogen, key):
    if "flagIsWhoKilLeDHaRamBeNatrajNotAGoodPass" in key.strip():
        return True, "Awesome.Thanks for playing the game! "
    else:
        return False, "Try Again."
