from hashlib import md5
import api

tid = api.user.get_team()["tid"]
shell_name = api.team.get_shell_account(tid)["username"]
def grade(autogen, key):
    secretkey = "MeraGharKaSecretHaiBabuBhaiya"
    flag = md5((secretkey + shell_name).encode('utf-8')).hexdigest()
    if flag.lower() in key.lower().strip():
        return True, "Correct!"
    else:
        return False, "Try Again."
