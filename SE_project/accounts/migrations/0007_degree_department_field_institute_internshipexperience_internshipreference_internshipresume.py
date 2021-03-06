# Generated by Django 2.2 on 2019-05-06 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_auto_20190506_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='InternshipResume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=100, null=True)),
                ('mName', models.CharField(max_length=100)),
                ('lName', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField()),
                ('cnic', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('contact1', models.CharField(max_length=100)),
                ('contact2', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('objective', models.CharField(max_length=1000)),
                ('department', models.CharField(max_length=100)),
                ('field', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=1000)),
                ('extra_curricular', models.CharField(max_length=1000)),
                ('other_interests', models.CharField(max_length=1000)),
                ('cdeg_name', models.CharField(max_length=100)),
                ('cdeg_inst', models.CharField(max_length=100)),
                ('cdeg_date', models.DateField()),
                ('ldeg_name', models.CharField(max_length=100)),
                ('ldeg_inst', models.CharField(max_length=100)),
                ('ldeg_grade', models.CharField(max_length=100)),
                ('sdeg_name', models.CharField(max_length=100)),
                ('sdeg_inst', models.CharField(max_length=100)),
                ('sdeg_grade', models.CharField(max_length=100)),
                ('add_qual', models.CharField(max_length=1000)),
                ('applicant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InternshipReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_refrence', models.CharField(max_length=100)),
                ('affiliation_of_reference', models.CharField(max_length=100)),
                ('contact_of_reference', models.CharField(max_length=100)),
                ('email_of_reference', models.EmailField(default='fast@gmail.com', max_length=254)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InternshipExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=1000)),
                ('months', models.IntegerField()),
                ('responsibilities', models.CharField(max_length=1000)),
                ('organization', models.CharField(max_length=100)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
