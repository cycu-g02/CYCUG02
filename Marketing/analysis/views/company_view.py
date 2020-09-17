from django.shortcuts import render

#Company---------------------------------------------------------------------------------------------------------------
def company(request):
    if request.user.is_authenticated and request.method == 'GET':
        return render(request, "backend/company.html", locals())
    else:
        return render(request, "backend/signin.html", locals())