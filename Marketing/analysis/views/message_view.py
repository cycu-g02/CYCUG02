from django.shortcuts import render

#Message---------------------------------------------------------------------------------------------------------------
def message(request):
    if request.user.is_authenticated and request.method == 'GET':
        return render(request, "backend/message.html", locals())
    else:
        return render(request, "backend/signin.html", locals())