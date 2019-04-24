from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class Hr_Manger(models.Model):
        name=models.CharField(max_length=20)
        image = models.ImageField(
            upload_to = 'images/',
            default = 'no-img.jpg',
            blank=True
        )
        date_of_birth = models.DateField(default='1999-12-31')
        gender =models.CharField(max_length=2, default='M')
        contact_num1=models.CharField(max_length=12)
        contact_num2=models.CharField(max_length=12)
        address=models.CharField(max_length=264)
        city = models.CharField(max_length=255, default='')
        country = models.CharField(max_length=255, default='')

        def __str__(self):
            return self.name


class Applicant(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        image = models.ImageField(
                upload_to = 'images/',
                default = 'no-img.jpg',
                blank=True
            )
        date_of_birth = models.DateField(default='1999-12-31')
        gender =models.CharField(max_length=2, default='M')
        contact_num1=models.CharField(max_length=12)
        contact_num2=models.CharField(max_length=12)
        address=models.CharField(max_length=264)
        city = models.CharField(max_length=255, default='')
        country = models.CharField(max_length=255, default='')

        def __str__(self):
            return self.user.username



class Reference(models.Model):
      applicant = models.ForeignKey(Applicant, on_delete=models.PROTECT)
      name_of_refrence=models.CharField(max_length=20)
      affiliation_of_reference=models.CharField(max_length=20)
      contact_of_reference=models.PositiveIntegerField()
      email_of_reference=models.EmailField(default='fast@gmail.com')
      hr_manager=models.ForeignKey(Hr_Manger, on_delete=models.PROTECT)

      def __str__(self):
          return self.name_of_refrence


class Job(models.Model):
    title =models.CharField(max_length=20)
    descriptions=models.CharField(max_length=20)
    designation=models.CharField(max_length=50)
    required_skills=models.CharField(max_length=50)
    locations=models.CharField(max_length=50)
    min_education=models.CharField(max_length=50)
    min_experience=models.CharField(max_length=50)
    age_requirements=models.CharField(max_length=50)
    gender =models.CharField(max_length=2,default='M')
    closing_date=models.DateField()
    status=models.CharField(max_length=2)
    salary=models.PositiveIntegerField()
    additional_benefits=models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Internship(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    duration=models.TimeField()
    required_skills=models.CharField(max_length=20)
    locations=models.CharField(max_length=20)
    start_date=models.DateField()
    end_date=models.DateField()
    details_document= models.ImageField(
            upload_to = 'images/',
            default = 'no-img.jpg',
            blank=True
        )


class Resume(models.Model):
    applicant=models.OneToOneField(Applicant, on_delete=models.CASCADE)
    job=models.ForeignKey(Job,on_delete=models.PROTECT)
    internship=models.ForeignKey(Internship,on_delete=models.PROTECT)
    current_employer=models.CharField(max_length=20)
    current_designation=models.CharField(max_length=20)
    current_organization_experience =models.CharField(max_length=10)
    objective=models.CharField(max_length=20)
    department=models.CharField(max_length=20)
    joining_date=models.DateField()
    skills=models.CharField(max_length=20)
    min_salary=models.PositiveIntegerField()
    extra_curricular=models.CharField(max_length=50)
    other_interests=models.CharField(max_length=50)

    def __str__(self):
        return self.applicant.username


class InterviewQuestion(models.Model):
    interview_question=models.CharField(max_length=50)
    question_correct_answer=models.CharField(max_length=100)

    def __str__(self):
        return self.interview_question

class Interview(models.Model):
    applicant=models.ForeignKey(Applicant,on_delete=models.PROTECT)
    job =models.ForeignKey(Job,on_delete=models.PROTECT)
    time_acknowledged=models.CharField(max_length=2)
    started_at =models.DateTimeField()
    interview_question_candidate_answer =models.PositiveIntegerField()
    interview_question_id=models.ForeignKey(InterviewQuestion,on_delete=models.PROTECT)
    job_status=models.CharField(max_length=20)


class Experience(models.Model):
    applicant=models.ForeignKey(Applicant,on_delete=models.PROTECT)
    hr_manger=models.ForeignKey(Hr_Manger,on_delete=models.PROTECT)
    experience_summary=models.TextField()
    experience_years=models.FloatField()
    previous_employer=models.CharField(max_length=50)
    previous_designation=models.CharField(max_length=50)
    previous_organization_experience=models.CharField(max_length=50)
    previous_responsibilities=models.CharField(max_length=50)
    date_of_leaving_job=models.DateField()

class Qualification(models.Model):
    applicant=models.ForeignKey(Applicant,on_delete=models.PROTECT)
    hr_manger=models.ForeignKey(Hr_Manger,on_delete=models.PROTECT)
    name_of_last_degree=models.CharField(max_length=50)
    institute_last_degree=models.CharField(max_length=50)
    performance_second_last_degree=models.FloatField()
    performance_last_degree=models.FloatField()

class Databackup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    datasize=models.CharField(max_length=50)
    lastUse_date=models.DateField()
    notification_sent_status=models.PositiveIntegerField()
    notification_date=models.DateField()
    notification_time=models.TimeField()

# Note this is Profile for the User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(default='none@email.com')
    sequarity_question=models.CharField(max_length=255, default='')
    sequarity_answer=models.CharField(max_length=255, default='')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
