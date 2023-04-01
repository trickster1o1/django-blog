from django.shortcuts import render


posts = [
    {
        'author': 'Nischal Tuladhar',
        'title': 'The Fox',
        'content': 'A quick brown fox jumps over the lazy dog',
        'date_posted': '2022-12-12'
    },
    {
        'author': 'Sumnima Sakya',
        'title': 'Fire Fox',
        'content': 'A quick fire fox jumps over the lazy dog',
        'date_posted': '2023-2-12'
    },
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'mainBlog/home.html',context)

def about(request):

    return render(request, 'mainBlog/about.html', {'title': 'About'})