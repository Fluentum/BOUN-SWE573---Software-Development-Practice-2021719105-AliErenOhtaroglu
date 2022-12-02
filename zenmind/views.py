from django.shortcuts import render



#helpers are called decorators. pre-written ccodes for some common tasks.
#imported below to login purpose.

#from django.contrib.auth.decorators import login_required

"""
Created the first view in app.
Then this is to be routed in urls.py file. Here we have the house, and we give the
address of the house in urls.py file. 
"""

#By adding the imported decorator, each time the below view is called,
#Caller needs to pass login stage.
#this line needs to be added before each different view.

#@login_required

#first view created for learning purposes.

#def index(request):
 #   return HttpResponse("Hello, world. Bu benim yaptigim ilk web sayfasi. Ege-Nil-Masalí cok seviyorum. Ayrica esimi ve kendimi de cok seviyorum.")

#Here below, two views functions.

#Two dummy posts created for learning purposes
posts = [
    {
        'author': 'CoreyMS',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'September 28, 1983'
    },
    {
        'author': 'Jane Doe',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'September 28, 2022'
    }
]

def home(request):
    #dummy posts are passed into template
    context = {
        'posts': posts #here you can use the posts data.
    }
    return render (request, 'zenmind/home.html', context)

def about(request):
    return render (request, 'zenmind/about.html', {'title': 'About'})

