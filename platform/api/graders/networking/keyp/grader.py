
def grade(autogen, key):
    if "cs628a{Take_y0Ur_candy_D0nt_interrupt_m3}" == key.strip():
        return True, "Correct!"
    else:
        return False, "Try Again."
