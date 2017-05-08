from hashlib import md5
import api

tid = api.user.get_team()["tid"]
shell_name = api.team.get_shell_account(tid)["username"]
def grade(autogen, key):
    secretkey = "asdasd98a9ndand987a83nuindna9721n9n923"
    flag = md5((secretkey + shell_name).encode('utf-8')).hexdigest()
    if flag.lower() in key.lower().strip():
        return True, "Wow you can see even being blind!"
    else:
        return False, "Try Again."
