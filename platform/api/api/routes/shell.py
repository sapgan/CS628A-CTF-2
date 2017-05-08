from flask import Flask, request, session, send_file, render_template
from flask import Blueprint
import api
import os.path

from api.common import WebSuccess, WebError
from api.annotations import api_wrapper, require_login, check_csrf
from api.annotations import block_before_competition, block_after_competition
from api.annotations import log_action

log = api.logger.use(__name__)

blueprint = Blueprint("shell api", __name__)

@blueprint.route('/getkey')
@require_login
def serve_private_key_hook():
    # return WebSuccess(data="Hello")
    db = api.common.get_conn()
    user = api.user.get_user()
    tid = user["tid"]
    shell_account = db.ssh.find_one({"tid": tid}, {"_id": 0, "tid": 0})
    if shell_account is None:
        return WebError(data="Team {} was not assigned a shell account.".format(tid))
    username = shell_account["username"]
    priv_key_path = os.path.abspath("./priv_keys")
    priv_key_file = os.path.join(priv_key_path,username)
    # data = open(priv_key_file,"r").readlines()
    # return WebSuccess(data)
    if os.path.exists(priv_key_file):
        # data = open(priv_key_file,"r").readlines()
        # return WebSuccess(data)
        return send_file(priv_key_file, mimetype='text/csv', as_attachment=True, attachment_filename="ctf.key")
    else:
        return WebError(data="Private key not generated for Team {}".format(tid))
