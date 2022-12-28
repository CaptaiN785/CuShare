from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import ServerForm
from .models import Server, Code
import string
import random
from .import firebase

## Server id key
serverID = 'LoginServerID'
## On changing this variable:
# Also change in: 1. core/base.html, 2. server/base.html, 3. manage_server.html

## Time in second for expiery of session
session_expiry = 14400

# Create your views here.
def home(request):
    if request.method == "POST":
        if request.POST['type'] == "code":
            code_id = request.POST['code_id']
            return redirect('server-code', code_id)
        else:
            server_id = request.POST['server_id']
            return redirect('server-code-list', server_id)
    return render(request, 'server/index.html')

def login(request):
    if request.method == "POST":
        server_id = request.POST['server_id']
        secret_key = request.POST["secret_key"]

        for c in server_id:
            if not str(c).isalnum():
                messages.error(request, "Invalid server id")
                return redirect('server-create')

        server_detail = firebase.check_login(server_id, secret_key)
        if not server_detail:
            messages.error(request ,"Incorrect server id or secret key")
            return redirect('server-create')
        request.session[serverID] = server_id
        request.session.set_expiry(session_expiry) ## session is expired here.
        return redirect('server-manage')
    return redirect('server-create')

def manage_server(request):
    context={'data':None}
    if request.session.get(serverID, False):
        server_id = request.session.get(serverID)
        data = firebase.get_server_code(server_id)
        context['data'] = data
    else:
        return redirect('server-create')
    return render(request, 'server/manage_server.html', context=context)

def delete(request, id):
    if request.session.get(serverID, False):
        server_id = request.session.get(serverID)
        res = firebase.delete_file(server_id, id)
        if res:
            messages.success(request, "Code deleted successfully")
            return redirect('server-manage')
        else:
            messages.error(request, "Unauthorized code ID")
            return redirect('server-manage')
    return redirect('server')

def upload(request):
    context = {'isError':False}
    try:
        if request.session.get(serverID, False):
            server_id = request.session.get(serverID)
            if request.method == "POST":
                title = request.POST['title']
                upload_type = request.POST['upload_type']
                if upload_type == "code":
                    code = request.POST['code']
                else:
                    file = request.FILES['code_file']
                    code = file.read().decode("utf-8")
                code_id = generate_code_id()

                if len(code) < 7:
                    context['isError'] = True
                    context['message'] = "Very less code."
                    return render(request, 'server/upload.html', context)
                firebase.upload_code(server_id, code_id, title, code)
                messages.success(request, "Code uploaded successfully")
                return redirect('server-manage')
        else:
            context['isError'] = True
            context['message'] = "Please login first"
    except Exception as e:
        context['isError'] = True
        context['message'] = "Unable to upload the file."
        print(e)
    return render(request, 'server/upload.html', context)

def change_password(request):
    if request.session.get(serverID, False):
        server_id = request.session.get(serverID)
        if request.method == "POST":
            sec1 = request.POST['sec1']
            sec2 = request.POST['sec2']
            if sec1 != sec2:
                messages.error(request, "Password didn't match")
                return redirect('server-manage')
            firebase.change_password(server_id=server_id, secret_key=sec1)
            messages.success(request, 'Password changed successfully')
            return redirect('server-manage')
    return redirect('server-create')

def create_server(request):
    form = ServerForm()
    context = {'form':form}
    if request.method == "POST":
        form = ServerForm(request.POST)
        if form.is_valid():
            server_id = form.cleaned_data['server_id']
            secret_key = form.cleaned_data['secret_key']
            secret_key_cnf = form.cleaned_data['secret_key_cnf']
            
            server_val = True
            for c in server_id:
                if not str(c).isalnum():
                    context['server_id_error'] = True
                    server_val = False
                    break
            
            pass_val = True
            if secret_key != secret_key_cnf:
                context['password_error'] = True
                pass_val = False

            if server_val and pass_val:
                
                server_check = firebase.check_server(server_id)
                if not server_check:
                    firebase.create_server(server_id=server_id, secret_key=secret_key)
                    request.session[serverID] = server_id
                    request.session.set_expiry(session_expiry)  ## session is expiring here.
                    return redirect("server-manage")
                else:
                    context['duplicate_server_error'] = True
            else:
                context['form'] = form
    return render(request, 'server/create.html', context=context)



def code(request, code_id):
    if not str(code_id).upper().isalpha():
        messages.error(request, "Invalid code ID")
        return redirect('server')

    code = firebase.get_code(code_id)
    if not code:
        messages.error(request, "Code not found")
        return redirect('server')

    return render(request, 'server/code.html', {'codes':code})

def code_list(request, server_id):
    if not str(server_id).isalnum():
        messages.error(request, "Invalid server id")
        return redirect("server")
    
    codes = firebase.get_server_code(server_id=server_id)
    if not codes:
        messages.error(request, "Server not found")
        return redirect("server")
    
    return render(request, 'server/codelist.html',{'data':codes})

def delete_server(request):
    if request.session.get(serverID, False):
        server_id = request.session.get(serverID)
        res = firebase.delete_server(server_id)
        if res:
            messages.success(request, "Server deleted successfully")
            return redirect('server')
        else:
            messages.error(request, "Unable to delete server")
            return redirect('server-manage')
    return redirect('server-create')

### helper function
def generate_code_id():
    codeID = firebase.get_all_codeID()
    letters = string.ascii_uppercase

    key = ""
    for i in range(6):
        key += random.choice(letters)

    while key in codeID:
        key = ""
        for i in range(6):
            key += random.choice(letters)
    return key
