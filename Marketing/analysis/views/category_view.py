from django.shortcuts import render

#Category---------------------------------------------------------------------------------------------------------------
def category(request):
    if request.user.is_authenticated and request.method == 'GET':
        return render(request, "backend/category.html", locals())
    else:
        return render(request, "backend/signin.html", locals())