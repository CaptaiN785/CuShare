
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("../key.json")
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

    new_code.delete()
    new_path.delete()
    print("Deleted record [{}]".format(path))

def get_code(code_id):
    path = code_path.child(code_id).get()
    if not path:
        return None
    code = codes.child(path["path"])
    return code.get()

print(get_code("HYRBSE"))