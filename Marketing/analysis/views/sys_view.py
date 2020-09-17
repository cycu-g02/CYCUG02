from django.shortcuts import render
from django.contrib import auth
from analysis.sys import get_enable_site_note, select_users

#Sys--------------------------------------------------------------------------------------------------------------------
def logon(request):
    return render(request, "backend/signin.html", locals())

def signin(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=name, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if user.is_authenticated:
                site_notes = get_enable_site_note()
                if site_notes is not None:
                    arr = []
                    for site_note in site_notes:
                        nos = {}
                        nos['name'] = site_note.name
                        nos['eng_name'] = site_note.eng_name
                        nos['url'] = site_note.url
                        nos['data_feather'] = site_note.data_feather
                        arr.append(nos)
                    request.session["site_notes"] = arr
                    users = select_users(2)
                    return render(request, "backend/company.html", locals())
                #return render(request, "signin.html", locals())
            #return render(request, "signin.html", locals())
        #return render(request, "signin.html", locals())
    return render(request, "backend/signin.html", locals())

def signout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return render(request, "backend/signin.html", locals())
