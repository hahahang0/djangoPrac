

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
posts = [
    {
        'id' : 1,
        'title' : "First title",
        'content' : "First content"
    },
    {
        'id' : 2,
        'title' : "Second title",
        'content' : "Second content"
    },{
        'id' : 3,
        'title' : "Third title",
        'content' : "Third content"
    }
]
# posts = []
 
def home(request):
    # print(reverse('home',args=['hangthim']))
    html = ""
    for post in posts:
        html += f''' 
        <div>
        <a href="/posts/{post['id']}"> 
        <h1>{post['id']}{post['title']}</h1>
        </a>
        <p>{post['content']}</p>
        </div>
            '''
        name = "Hangthim Limbu ingwaba"
    return render(request,'posts/home.html',{'posts':posts,"username":"hangthim"})

def post(request,id):
    is_valid = False
    htmlResponse = ""
    post_dict = {}
    for post in posts:
        # print("this is post",post)
        if post['id'] == id:
            post_dict = post
            is_valid = True
            htmlResponse += f'''
        <h1> {post['title']} </h1>
        <p> {post['content']} </p>
         '''
    if is_valid:
        return render(request,'posts/posts.html',{'post_dict':post_dict})
    else:
        return HttpResponseNotFound("Post Not Found😭😭😭😭😭😭") 

def google(Request,id):
    url = reverse("post",args=[id])
    return HttpResponseRedirect(url) 

def t_global(request):
    return render(request,"global.html")
