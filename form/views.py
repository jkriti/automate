from django.shortcuts import render

def post_list(request):
    return render(request, 'form/post_list.html', {})

