from django.shortcuts import render

#Record---------------------------------------------------------------------------------------------------------------
def record(request):
    if request.user.is_authenticated and request.method == 'GET':
        return render(request, "backend/record.html", locals())
    else:
        return render(request, "backend/signin.html", locals())