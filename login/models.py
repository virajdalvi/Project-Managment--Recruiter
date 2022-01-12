from django.db import models

# Create your models here.


class Sreg(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Treg(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class nproj(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    sem = models.CharField(max_length=100)
    rno = models.IntegerField()
    div = models.CharField(max_length=5)
    pname = models.CharField(max_length=100)
    subj = models.CharField(max_length=100)
    tuser = models.CharField(max_length=100)
    desc = models.TextField()
    git = models.URLField(max_length=200)
    pmem = models.CharField(max_length=200)
    file = models.ImageField(upload_to='images/')


class Newproj(models.Model):
    Student_name = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Semester = models.CharField(max_length=100)
    Roll_no = models.IntegerField()
    Div = models.CharField(max_length=5)
    Project_name = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    Teacher_username = models.CharField(max_length=100)
    Project_description = models.TextField()
    Git_link = models.URLField(max_length=200)
    Project_members = models.CharField(max_length=200)
    Output_Image = models.ImageField(upload_to='images/')


class Grade(models.Model):
    pid = models.IntegerField()
    suggestions = models.TextField()
    avgtotal = models.IntegerField()
    endorsement = models.IntegerField()


class StudentsProfile(models.Model):
    student_id = models.FloatField()
    student_username = models.CharField(max_length=50)
    project_score = models.IntegerField()
    sem_average_marks = models.IntegerField()
    language = models.CharField(max_length=100)
    current_sem = models.CharField(max_length=30)
    eq=models.IntegerField(default=0)
    resume = models.FileField(upload_to="resumes/")


class TestSeries(models.Model):
    student_id = models.IntegerField()
    student_username = models.CharField(max_length=50)
    gaming_score = models.IntegerField()
    aptitude_score = models.IntegerField()
    coding_score = models.IntegerField()
    avg_test_score = models.IntegerField()


class Testscore(models.Model):
    username = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    score = models.IntegerField()
    testkey = models.CharField(max_length=10)


class Questionbank(models.Model):

    semester = models.CharField(max_length=50)
    question = models.CharField(max_length=5000)
    optionA = models.CharField(max_length=500)
    optionB = models.CharField(max_length=500)
    optionC = models.CharField(max_length=500)
    optionD = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    testkey = models.CharField(max_length=10)
    teacher_username = models.CharField(max_length=50)
    quizname = models.CharField(max_length=500)
