
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# from django.conf import settings
# import os
# key_location = os.path.join(settings.BASE_DIR, 'key.json')

key_location = "/etc/secrets/key.json"
cred = credentials.Certificate(key_location)
firebase_admin.initialize_app(cred, {
    "databaseURL":"https://cushare-785-default-rtdb.firebaseio.com"
})

codes = db.reference("/CODE/")
code_path = db.reference("CODEPATH")
server = db.reference("/SERVER/")

## Upload the code
def upload_code(server_id, code_id, title, code):
    path = server_id + "/" + code_id
    new_code = codes.child(path)
    data = {
        "title":title,
        "code":code
    }
    new_code.set(data)
    new_path = code_path.child(code_id)
    new_path.set({"path":path})
    print("Uploaded record [{}]".format(path))

def delete_file(server_id, code_id):
    path = server_id + "/" + code_id
    new_path = code_path.child(code_id)
    new_code = codes.child(path)

    if not new_code.get():
        return False

    new_code.delete()
    new_path.delete()
    print("Deleted record [{}]".format(path))
    return True

def get_code(code_id):
    path = code_path.child(code_id).get()
    if not path:
        return None
    code = codes.child(path["path"])
    return code.get()

def create_server(server_id, secret_key):
    new_server = server.child(server_id)
    new_server.set({'secret_key':secret_key})
    print("Server is created [{}]".format(server_id))

def change_password(server_id, secret_key):
    new_server = server.child(server_id)
    new_server.set({'secret_key':secret_key})
    print("Password changed [{}]".format(server_id))

def get_server_code(server_id):
    server_code = codes.child(server_id).get()
    return server_code

def check_login(server_id, secret_key):
    new_server = server.child(server_id).get()
    if not new_server or new_server['secret_key'] != secret_key:
        return False
    return True

def get_all_codeID():
    return code_path.get().keys()

def check_server(server_id):
    return True if server.child(server_id).get() else False

def delete_server(server_id):
    ## Delete all the code.
    try:
        all_codes = codes.child(server_id)
        for key in all_codes.get().keys():
            path = code_path.child(key)
            path.delete()
        all_codes.delete()
        login_server = server.child(server_id)
        login_server.delete()
        return True
    except:
        return False