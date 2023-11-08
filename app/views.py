from django.shortcuts import render


def main(request):
    return render(request, 'html/main.html', {})


def post(request):
    return render(request, 'html/post.html', {})
