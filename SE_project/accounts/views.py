from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.db import connection
    
from django.db.models import Q
from .models import Posts

from .models import Jobs
from .models import *

def index(request):
    #return HttpResponse('Hello from posts')
    #posts = '123'
    #posts = Jobs.objects.filter(category=1)
    
    posts = Jobs.objects.all()[:10]
    
    posts = Jobs.objects.filter(title__icontains='Designer')

    context = {
        'title': 'Latest Posts1',
        'posts': posts

    }

    return render(request, 'posts/index.html', context)


def index2(request):
    #return HttpResponse('Hello from posts')

    return render(request, 'posts/index2.html')

def hassan(request):
    #return HttpResponse('Hello from posts')

    return render(request, 'posts/hassan.html')    


def post_job(request):
    #return HttpResponse('Hello from posts')

    return render(request, 'posts/post_job.html')  

#sign2_recruiter  

def sign2_recruiter(request):
    #return HttpResponse('Hello from posts')

    return render(request, 'posts/sign2_recruiter.html')  
def send_requsts(request):
    #return HttpResponse('Hello from posts')

    return render(request, 'posts/send_requsts.html') 

def edit_profile(request):
    #return HttpResponse('Hello from posts')

    user = Users.objects.get(id = 3)


    context = {
        'user': user,
        
    }

    return render(request, 'posts/edit_profile.html', context) 


def sign2(request):
    #return HttpResponse('Hello from posts')

    return render(request, 'posts/sign2.html') 

def login(request):
    #return HttpResponse('Hello from posts')

    return render(request, 'posts/login.html') 


def attempt_log_in(request):    
    posts = Jobs.objects.all()[:10]
    real_posts = Posts.objects.all()[:10]
    
    #posts = Jobs.objects.filter(category=1)
    
    id = request.POST.get("email", "asdasd")
    pwd = request.POST.get("password", "asdasd")
    

    user = Users.objects.get(id=int(id))
    
    if (user.password_hash == int(pwd)):

        context = {
            'title': 'Latest Posts1',
            'posts': posts,
            'real_posts':real_posts,
        }
        return render(request, 'posts/wall.html' , context)     


    #button = request.POST.get("button")


    
 

    #request = redirect('/index.html')
    #return request
    return render(request, 'posts/login.html')     



def wall(request):
    #return HttpResponse('Hello from posts')
    
    posts = Job.objects.all()
    real_posts = Posts.objects.all()[:10]
    
    #posts = Jobs.objects.filter(category=1)
    
    email = request.POST.get("email", "asdasd")
    button = request.POST.get("button")

    

    context = {
        'title': 'Latest Posts1',
        'posts': posts,
        'email': email,
        'button':button,
        'real_posts':real_posts,
    }

 

    #request = redirect('/index.html')
    #return request
    return render(request, 'posts/wall.html' , context)     


def sign_up_applicant(request):
    name = request.POST.get("full_name", "asdasd")
    email = request.POST.get("email", "asdasd")
    pwd = request.POST.get("password", "asdasd")
    pwd_r = request.POST.get("password_repeat", "asdasd")
    city = request.POST.get("city", "asdasd")
    country = request.POST.get("country", "asdasd")
    degree = request.POST.get("degree", "asdasd")
    major = request.POST.get("major", "asdasd")
    date_degree = request.POST.get("date", "asdasd")

    new_entry = Users(username=name, password_hash = 32, user_type=1)
    new_entry.save()


    #button = request.POST.get("button")

    return render(request, 'posts/wall.html')   

def sign_up_recruiter(request):
    name = request.POST.get("full_name", "asdasd")
    email = request.POST.get("email", "asdasd")
    pwd = request.POST.get("password", "asdasd")
    pwd_r = request.POST.get("password_repeat", "asdasd")
    city = request.POST.get("city", "asdasd")
    country = request.POST.get("country", "asdasd")
    degree = request.POST.get("degree", "asdasd")
    major = request.POST.get("major", "asdasd")
    date_degree = request.POST.get("date", "asdasd")

    new_entry = Users(username=name, password_hash = 32, user_type=2)
    new_entry.save()


    #button = request.POST.get("button")

    return render(request, 'posts/wall.html')   


def update_profile(request):
    name = request.POST.get("full_name", "asdasd")
    email = request.POST.get("email", "asdasd")
    pwd = request.POST.get("password", "asdasd")
    pwd_r = request.POST.get("password_repeat", "asdasd")
    city = request.POST.get("city", "asdasd")
    country = request.POST.get("country", "asdasd")
    degree = request.POST.get("degree", "asdasd")
    major = request.POST.get("major", "asdasd")
    date_degree = request.POST.get("date", "asdasd")


    t = Users.objects.get(id=3)
    t.username = name  
    t.save() 

    #new_entry = Users(username=name, password_hash = 32, user_type=2)
    #new_entry.save()


    #button = request.POST.get("button")

    return render(request, 'posts/wall.html')   



def job_details(request, id, uid = 1):
    #return HttpResponse('Hello from posts')

    post = Jobs.objects.get(id = id)
    context = {
        'post': post
    }

    return render(request, 'posts/job-details.html', context) 




def details(request, id = 1, uid = 1):
    post = Jobs.objects.get(id = id)


    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)

def jobapply(request, id = 1, uid = 1):
    post = Jobs.objects.get(id = id)

    new_entry = Jobs_Applications(job_id=id, applicant_id=1)
    new_entry.save()



    posts = Job.objects.all()
    real_posts = Posts.objects.all()[:10]
    
    #posts = Jobs.objects.filter(category=1)
    
    email = request.POST.get("email", "asdasd")
    button = request.POST.get("button")

    

    context = {
        'title': 'Latest Posts1',
        'posts': posts,
        'email': email,
        'button':button,
        'real_posts':real_posts,
    }

 

    #request = redirect('/index.html')
    #return request
    return render(request, 'posts/wall.html' , context)     



#    return render(request, 'posts/jobapply.html', context)
  


#    return render(request, 'posts/wall.html')

def jobposted(request, id = 1, uid = 1):
    post = Jobs.objects.get(id = id)

    #new_entry = Jobs_Applications(job_id=id, applicant_id=1)
    #new_entry.save()
    title = request.POST.get("f1-email", "asdasd")
    

    new_entry = Jobs(title=title, description="some fixed description", category = 1, posted_by=1, salary = 200, experience = 2, location="Lahore")
    new_entry.save()


    context = {
        'post': post,
        'title':title
    }

    return render(request, 'posts/jobapply.html', context)

def suggested(request, id = 1):
    #return HttpResponse('Hello from posts')
    posts = Users.objects.filter(~Q(id = id)) #filter( id != id)



    context = {
        'posts': posts,
        'id' : id,    
    }



    return render(request, 'posts/suggested.html', context) 


def request(request, id = 1, rid = 2):
    #return HttpResponse('Hello from posts')
    

    new_entry = Users_Friends_Requests(Request_Sender=id, Requst_Receiver=rid)
    new_entry.save()

    context = {
        'empty':True    
    }



    return render(request, 'posts/jobapply.html', context) 

def my_connections(request, id = 1):
    #return HttpResponse('Hello from posts')

#    posts = Users_Friends.objects.filter(user_id = id) #filter( id != id)


    #posts = Users_Friends.objects.filter(user_id__in=[item['friend_id'] for item in posts])

    #posts =  Users.objects.filter(users_friends.friend_id = 2)
    #posts = Users.objects.filter(id = Users_Friends.objects.get(user_id = id))

    cursor = connection.cursor()
    cursor.execute("  select * from posts_users u where u.id in  (select uf.friend_id from posts_users as iu join posts_users_friends as uf on iu.id = uf.user_id where iu.id = 1)")
    #select * from posts_users as u join posts_users_friends as uf on u.id = uf.user_id where u.id = 1")# + str(id)          )
    #count(*) FROM people_person''')

    rows = cursor.fetchall()
    cursor.execute("  select * from posts_users u where u.id in  (select uf.requst_receiver from posts_users as iu join posts_users_friends_requests as uf on iu.id = uf.request_sender where iu.id = 1)")
    
    requests = cursor.fetchall()
    
    
    context = {
        'posts': rows,
        'id' : id,
        'requests': requests,    
    }


    return render(request, 'posts/my_connections.html', context) 


