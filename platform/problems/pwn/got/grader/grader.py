from hashlib import md5
import api

tid = api.user.get_team()["tid"]
shell_name = api.team.get_shell_account(tid)["username"]
def grade(autogen, key):
    secretkey = "ee718f8f4gh39fr80df8h498592ce40f"
    flag = md5((secretkey + "got" + shell_name).encode('utf-8')).hexdigest()
    if flag.lower() in key.lower().strip():
        return True, "Correct!"
    else:
        return False, "Try Again."
