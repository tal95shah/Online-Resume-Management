from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from accounts import models
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Job
from .models import Intern
from django.contrib.auth.models import User
from .models import Department,Institute,Degree,Field,Applicant,InternshipReference,InternshipExperience,InternshipResume



# Create your views here.
def home(request):
	return render(request,"layout/home.html")
def sign_in(request):
	return render(request,"layout/sign_in.html")

def resume(request):
    """Display Applicant Resume"""
    username = 'john'
    password = 'johnpassword'
    customUser = authenticate(request, username=username, password=password)
    resume = None
    if customUser.is_authenticated:
    	user = customUser
    	resume = None
    return render(request, 'accounts/resume.html', {
        'resume': resume,
        'user':user
    })

def edit_resume(request):
    username = 'john'
    password = 'johnpassword'
    customUser = authenticate(request, username=username, password=password)
    resume = None

    if customUser.is_authenticated:
    	userG = customUser
    applicant = models.Applicant.objects.filter(user=userG)[0]
    resume = get_object_or_404(models.Resume, applicant=applicant)
    form = forms.ResumeForm(instance=resume)

    if request.method == 'POST':
        form = forms.ResumeForm(instance=resume, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated the Resume Successfully!")
            return HttpResponseRedirect(reverse('accounts:resume'))

    return render(request, 'accounts/edit_resume.html', {
        'form': form
    })

def index(request):

    return render(request,'layout/home.html')

def form(request):
    if request.method== 'POST':
        f=request.POST.get('f_name')
        l=request.POST.get('l_name')
        u = request.POST.get('user_name')
        e = request.POST.get('u_email')
        pwd = request.POST.get('psw')
        s_que = request.POST.get('sq')
        s_ans = request.POST.get('s_answer')
        a = signup(first_name=f, last_name=l,user_type='candidate' ,username=u, email=e,password=pwd,security_question='What is your Nickname?',security_answer='name')
        a.save()
        return render(request, 'layout/home.html')

    else:
        return render(request,'accounts/sign_up.html')

def SignIn(request):
    if request.method == 'POST':
        un = request.POST.get['uname']
        password = request.POST.get['psw']
        user = authenticate(request, username=un, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                session_key = '8cae76c505f15432b48c8292a7dd0e54'
                session = Session.objects.get(session_key=session_key)
                uid = session.get_decoded().get('_auth_user_id')
                user = signup.objects.get(pk=uid)
                request.session["uid"] = uid
                if user.user_type == 'candidate':
                    return render(request, 'accounts/candidates.html')
                elif user.user_type == 'hr':
                    return render(request, 'accounts/hr.html')
    return render(request, 'accounts/sign_in.html')

def ChangeP(request):
    uid = request.session["uid"]
    user = signup.objects.get(pk=uid)
    return render(request, 'accounts/Security.html', {'content': [user.security_question]})

def SecurityC(request):
    if request.method == 'POST':
        uid = request.session["uid"]
        user = signup.objects.get(pk=uid)
        sa = request.POST.get('s_answer')
        psw = request.POST.get('old_psw')
        npsw = request.POST.get('new_psw')
        if user.security_answer == sa:
            if user.password == psw:
                user.password = npsw
                user.save()
                messages.success(request,'Password Changed Successfully Changed')
                return render(request, 'accounts/candidates.html')
            else:
                messages.warning(request, 'Security answer or Old Password does not match')
                return render(request, 'accounts/Security.html', {'content': [user.security_question]})
        else:
            messages.warning(request, 'Security answer or Old Password does not match')
            return render(request, 'accounts/Security.html', {'content': [user.security_question]})


################################TEAM ALPHA #####################################

def index(request):
    Jobss = Job.objects.all()
    context = {'Jobss': Jobss}
    return render(request, 'accounts/CreateJob.html', context)
	
def create(request):
    job = Job(title=request.POST['jobtitle'], descriptions=request.POST['decrpition'],designation=request.POST['designation'],required_skills=request.POST['skills'],locations=request.POST['city'],min_education=request.POST['minEdu'],min_experience=request.POST['experience'],age_requirements=request.POST['minAge'],gender=request.POST['gender'],closing_date=request.POST['date'],status=request.POST['jobstatus'],salary=request.POST['salary'],additional_benefits=request.POST['benefits'],document=request.POST['fileDoc'])
    job.save() 
    Jobss = Job.objects.all()
    return redirect('/show')

def edit(request, id):
    Jobs = Job.objects.get(id=id)
    context = {'Jobs': Jobs}
    return render(request, 'accounts/edit.html', context)

def update(request, id):
    
	Jobs = Job.objects.get(id=id)
	Jobs.title = request.POST['jobtitle']
	Jobs.descriptions=request.POST['decrpition']
	Jobs.designation=request.POST['designation']
	Jobs.required_skills=request.POST['skills']
	Jobs.locations=request.POST['city']
	Jobs.min_education=request.POST['minEdu']
	Jobs.min_experience=request.POST['experience']
	Jobs.age_requirements=request.POST['minAge']
	Jobs.gender=request.POST['gender']
	Jobs.closing_date=request.POST['date']
	Jobs.status=request.POST['jobstatus']
	Jobs.salary=request.POST['salary']
	Jobs.additional_benefits=request.POST['benefits']
	Jobs.document=request.POST['fileDoc']

	Jobs.save()
	return redirect("/show")  
	 
def delete(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    return redirect('/show')

def show(request):  
    Jobss = Job.objects.all() 
    return render(request,"accounts/showJobs.html",{'Jobss':Jobss})  
	
def index1(request):
    int = Intern.objects.all()
    c = {'int': int}
    return render(request, 'accounts/CreateInternship.html', c)
	
def createinternship(request):
    print("asdasdasda")
    intern = Intern(title=request.POST['title'], duration = request.POST['duration'],description = request.POST['description'],skills = request.POST['skills'],department = request.POST['dept'],status = request.POST['status'],city = request.POST['city'],location = request.POST['location'],startdate = request.POST['startdate'],enddate = request.POST['enddate'],closing_date = request.POST['date'],attached_file = request.POST['fileDoc'] )
    intern.save() 
    return redirect('/display')
	
def display(request):  
    int = Intern.objects.all()
    cc = {'int': int}
    return render(request, 'accounts/showIntern.html', {'int':int})
		
def edit1(request, id):
    intern = Intern.objects.get(id=id)
    context = {'intern': intern}
    return render(request, 'accounts/editIntern.html', context)

def update1(request, id):
    
	intern = Intern.objects.get(id=id)
	intern.title = request.POST['title']
	intern.duration = request.POST['duration']
	intern.description = request.POST['description']
	intern.skills = request.POST['skills']
	intern.department = request.POST['dept']
	intern.status = request.POST['status']
	intern.city = request.POST['city']
	intern.location = request.POST['location']
	intern.startdate = request.POST['startdate']
	intern.enddate = request.POST['enddate']
	intern.closing_date = request.POST['date']
	intern.attached_file = request.POST['fileDoc'] 

	intern.save()
	return redirect("/display")  
	 
def delIntern(request, id):
    intern = Intern.objects.get(id=id)
    intern.delete()
    return redirect('/display')



################################    TEAM Galoters   #####################################

def intershipresume(request):

    user = User.objects.filter(first_name='Faiq').first()
    resume = InternshipResume.objects.filter(applicant=user).first()

    if resume == None:

        if request.method == 'POST':

            allDict = request.POST
            fname = request.POST['fname']
            lname = request.POST['lname']
            mname = request.POST['mname']
            dob = request.POST['dob']
            cnic = request.POST['cnic']
            phone1 = request.POST['phone1']
            phone2 = request.POST['phone2']
            nation = request.POST['nation']
            email = request.POST['email']
            address = request.POST['address']
            country = request.POST['country']
            city = request.POST['city']
            weeks = request.POST['period']
            jdate = request.POST['tdate']
            skills = request.POST['skills']
            obj = request.POST['obj']
            extra = request.POST['extra']
            interests = request.POST['interests']
            dep = request.POST['dep']
            otherDep = request.POST['otherdep']
            field = request.POST['field']
            otherField = request.POST['otherField']

            cdeg = request.POST['cdeg']
            otherCdeg = request.POST['otherCdeg']
            cins = request.POST['cins']
            otherCins = request.POST['otherCins']
            cdate = request.POST['cdate']
            ldeg = request.POST['ldeg']
            otherLdeg = request.POST['otherLdeg']
            lins = request.POST['lins']
            otherLins = request.POST['otherLins']
            lgrade = request.POST['lgrade']
            sdeg = request.POST['sdeg']
            otherSdeg = request.POST['otherSdeg']
            sins = request.POST['sins']
            otherSins = request.POST['otherSins']
            sgrade = request.POST['sgrade']
            otherqual = request.POST['addqual']

            rnames =  allDict.getlist('rname')
            remails = allDict.getlist('remail')
            affils = allDict.getlist('affil')
            rcontacts = allDict.getlist('rcontact')

            intsums = allDict.getlist('intsum')
            orgnames = allDict.getlist('orgname')
            resps = allDict.getlist('responsiblities')
            monthss = allDict.getlist('months')

            for x in range(len(intsums)):
                intsum = intsums[x]
                orgname = orgnames[x]
                resp = resps[x]
                months = monthss[x]

                internship  = InternshipExperience(

                    applicant=user,
                    summary=intsum,
                    months=months,
                    responsibilities=resp,
                    organization=orgname
                )

                internship.save()

            for x in range(len(rnames)):
                rname = rnames[x]
                affil = affils[x]
                remail = remails[x]
                rcontact = rcontacts[x]

                reference  = InternshipReference(

                    applicant=user,
                    name_of_refrence=rname,
                    affiliation_of_reference=affil,
                    contact_of_reference=rcontact,
                    email_of_reference=remail
                )
                reference.save()

            if dep == "Other":
                dep = otherDep
                newDep = Department(name=dep)
                newDep.save()

            if field == "Other":
                field = otherField
                newField = Field(name=dep)
                newField.save()

            if cdeg == "Other":
                cdeg = otherCdeg
                newDeg = Degree(name=cdeg)
                newDeg.save()

            if cins == "Other":
                cins = otherCins
                newIns = Institute(name=cins)
                newIns.save()

            if ldeg == "Other":
                ldeg = otherLdeg
                newDeg = Degree(name=ldeg)
                newDeg.save()

            if lins == "Other":
                lins = otherLins
                newIns = Institute(name=lins)
                newIns.save()

            if sdeg == "Other":
                sdeg = otherSdeg
                newDeg = Degree(name=sdeg)
                newDeg.save()

            if sins == "Other":
                sins = otherSins
                newIns = Institute(name=sins)
                newIns.save()


            resume = InternshipResume(
                applicant=user,
                fName=fname,
                mName=mname,
                lName=lname,
                email=email,
                dob = dob,
                cnic=cnic,
                nationality=nation,
                contact1=phone1,
                contact2=phone2,
                address=address,
                country=country,
                city=city,
                objective=obj,
                department=dep,
                field=field,
                skills=skills,
                extra_curricular=extra,
                other_interests=interests,

                cdeg_name=cdeg,
                cdeg_inst=cins,
                cdeg_date=cdate,
                ldeg_name=ldeg,
                ldeg_inst=lins,
                ldeg_grade=lgrade,
                sdeg_name=sdeg,
                sdeg_inst=sins,
                sdeg_grade=sgrade,
                add_qual=otherqual
            )
            resume.save()
    
        context={
            "departments" : Department.objects.all(),
            "degrees" : Degree.objects.all(),
            "institutes" : Institute.objects.all(),
            "fields" : Field.objects.all(),
            "user": user,
        }

        return render(request, 'accounts/res.html',context)

    else:
        context={
            "resume":resume,
            "refs": InternshipReference.objects.filter(applicant=user),
            "exps": InternshipExperience.objects.filter(applicant=user)
        }

        return render(request, 'accounts/res2.html',context)
    
def edit_intershipresume(request):

    user = User.objects.filter(first_name='Faiq').first()
    resume = InternshipResume.objects.filter(applicant=user).first()

    context={
            "departments" : Department.objects.all(),
            "degrees" : Degree.objects.all(),
            "institutes" : Institute.objects.all(),
            "fields" : Field.objects.all(),
            "resume":resume,
            "refs": InternshipReference.objects.filter(applicant=user),
            "exps": InternshipExperience.objects.filter(applicant=user),
            "user": user
        }

    return render(request, 'accounts/res3.html',context)
