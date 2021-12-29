from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Sreg, StudentsProfile
from .models import Treg
from .models import nproj
from .models import Newproj
from .models import Grade
from django.contrib import messages
from django.contrib.auth.models import auth, User
import random
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, CreateView, edit  # new
from django.urls import reverse_lazy  # new
from .forms import NewprojForm

from .forms import New_projForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from operator import itemgetter
import psycopg2
from login.forms import StudentsProfileForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


temp1 = 0
temp2 = ''


def registerstud(request):
    global temp1, temp2
    sreg = Sreg()
    if request.method == 'POST':
        name = request.POST["name"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Oops! Username taken')
                return render(request, 'registerstud.html')
            else:
                user = User.objects.create_user(
                    first_name=name, username=username, password=password2)
                sreg = Sreg(name=name, username=username, password=password2)
                sreg.save()
                temp1 = sreg.pk
                temp2 = sreg.username
                user.save()
                print('SUBMITTED')
                #form = StudentsProfileForm()

                # return render(request, 'StudentProfile.html', {'form': form})
                return render(request, 'StudentProfile.html')

        else:
            messages.info(request, 'Passwords did not match!')
            return render(request, 'registerstud.html')
    else:
        return render(request, 'registerstud.html')


def registertr(request):
    treg = Treg()
    if request.method == 'POST':
        name = request.POST["name"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Oops! Username taken')
                return render(request, 'registertr.html')
            else:
                user = User.objects.create_user(
                    first_name=name, username=username, password=password2)
                treg = Treg(name=name, username=username, password=password2)
                user.save()
                treg.save()
                print('SUBMITTED')
                return render(request, 'tlogin.html')

        else:
            messages.info(request, 'Passowords did not match!')
            return render(request, 'registertr.html')
    else:
        return render(request, 'registertr.html')


def slogin(request):
    global temp1, temp2
    print("temp", temp1)
    print("temp2", temp2)
    sreg = Sreg()

    if request.method == 'POST':
        print("entered if")
        u = []
        p = []
        con = psycopg2.connect(host="localhost", user="postgres",
                               password="Dalvi@123", database="Project Management")
        cursor = con.cursor()

        con2 = psycopg2.connect(host="localhost", user="postgres",
                                password="Dalvi@123", database="Project Management")
        cursor2 = con2.cursor()

        sqlcommand = "select username from login_Sreg"
        sqlcommand2 = "select password from login_Sreg"

        cursor.execute(sqlcommand)
        cursor2.execute(sqlcommand2)

        for i in cursor:
            u.append(i)
        for j in cursor2:
            p.append(j)

        res = list(map(itemgetter(0), u))
        res2 = list(map(itemgetter(0), p))
        #print("res value",res)
        #print("res2 value",res2)

        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        print('user', user)

        k = len(res)

        i = 0
        while i < k:
            print("entered while")
            #print('res[i],res2[i] ',res[i],res2[i])
            if res[i] == username and res2[i] == password:
                print('login Successfull')
                auth.login(request, user)
                return render(request, 'sdash.html')
            i += 1

        else:
            messages.info(request, "Check username or password")
            return redirect('slogin')

    else:
        #messages.info(request,'Invalid Credential. Try Again!')
        print("post method not found")

        return render(request, 'slogin.html')


def tlogin(request):
    treg = Treg()
    if request.method == 'POST':

        print("entered if")
        u = []
        p = []
        con = psycopg2.connect(host="localhost", user="postgres",
                               password="Dalvi@123", database="Project Management")
        cursor = con.cursor()

        con2 = psycopg2.connect(host="localhost", user="postgres",
                                password="Dalvi@123", database="Project Management")
        cursor2 = con2.cursor()

        sqlcommand = "select username from login_Treg"
        sqlcommand2 = "select password from login_Treg"

        cursor.execute(sqlcommand)
        cursor2.execute(sqlcommand2)

        for i in cursor:
            u.append(i)
        for j in cursor2:
            p.append(j)

        res = list(map(itemgetter(0), u))
        res2 = list(map(itemgetter(0), p))
        print("res value", res)
        print("res2 value", res2)

        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        print('user', user)
        i = 0
        k = len(res)
        while i < k:
            print("entered while")
            print('res[i],res2[i] ', res[i], res2[i])
            if res[i] == username and res2[i] == password:
                print('login Successfull')
                auth.login(request, user)
                return render(request, 'tinfo.html')
            i += 1

        else:
            messages.info(request, "Check username or password")
            return redirect('tlogin')

    else:
        #messages.info(request,'Invalid Credential. Try Again!')
        print("post method not found")

        return render(request, 'tlogin.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


# pid and file upload is pending
def miniprojview(request):
    current_user = str(request.user)
    newprojs = Newproj.objects.all()
    # str(current_user)))
    for i in newprojs:
        print('Entered for')

        print(str(i.Teacher_username))

    # print(newprojs.Project_name)
    return render(request, 'miniprojview.html', {'current_user': current_user, 'newprojs': newprojs})


def sdash(request):
    return render(request, 'sdash.html')


def sprojview(request):
    current_user = str(request.user)
    newprojs = Newproj.objects.all()
    #gr = Grade.objects.filter(id=pk)
    # str(current_user)))
    # print(newprojs.Project_name)
    print('current user : ', current_user)
    print('newprojs : ', newprojs)
    for i in newprojs:
        if current_user == i.Username:
            print('Entered if ')
            print('username:', i.Username)

    return render(request, 'sprojview.html', {'current_user': current_user, 'newprojs': newprojs})


class CreateNewprojView(CreateView):  # new

    model = Newproj
    form_class = NewprojForm
    template_name = 'post.html'
    #success_url = 'sdash'
    success_url = reverse_lazy('sdash')


def grades(request, pk):
    current_user = str(request.user)
    new = Newproj.objects.filter(id=pk)
    newprojs = Newproj.objects.all()
    gr = Grade(request.POST)
    if request.method == 'POST':
        print('IF')
        pid = request.POST["pid"]
        suggestions = request.POST["suggestions"]
        avgtotal = request.POST["avgtotal"]
        gr = Grade.objects.create(
            pid=pid, suggestions=suggestions, avgtotal=avgtotal)
        gr.save()
        print("Success")
        # return render(request,'Tinfo.html')
        for i in newprojs:
            print('For ')
            print(i.id)
        return render(request, 'miniprojview.html', {'current_user': current_user, 'newprojs': newprojs})
    else:

        print('else')
        return render(request, 'grades.html', {'new': new})


def fullview(request, pk):
    np = Newproj.objects.filter(id=pk)
    gr = Grade.objects.filter(pid=pk)
    print(gr)
    for i in gr:
        print('For')
        print(i.avgtotal)
    return render(request, 'fullview.html', {'np': np, 'gr': gr})

    # return render(request,'fullview.html')


def sfullview(request, pk):
    np = Newproj.objects.filter(id=pk)
    gr = Grade.objects.filter(pid=pk)
    for i in gr:
        print('Entered for')
        print(i.avgtotal)
    return render(request, 'sfullview.html', {'np': np, 'gr': gr})


def delete_proj(request, pk):
    Newproj.objects.filter(id=pk).delete()
    current_user = str(request.user)
    newprojs = Newproj.objects.all()
    return render(request, 'sprojview.html', {'current_user': current_user, 'newprojs': newprojs})


def editproj(request, pk):
    ins = get_object_or_404(Newproj, pk=pk)
    current_user = str(request.user)
    newprojs = Newproj.objects.all()
    if request.method == 'POST':
        print('Entered if')
        form = NewprojForm(request.POST, instance=ins)
        if form.is_valid():
            form.save()
            print('Saved')
            return render(request, 'sprojview.html', {'current_user': current_user, 'newprojs': newprojs})
    else:
        print('Entered else')
        form = NewprojForm(instance=ins)
        return render(request, 'editproj.html', {'form': form, 'current_user': current_user, 'newprojs': newprojs})


def Tinfo(request):
    return render(request, 'Tinfo.html')


def Student_profile(request):
    global temp1, temp2
    print("temp", temp1)
    print("temp2", temp2)
    if request.method == 'POST':
        form = StudentsProfileForm(request.POST)
        if form.is_valid():
            files = request.POST['resume']
            sd = StudentsProfile.objects.create(
                student_id=temp1, student_username=temp2, project_score=30, sem_average_marks=form['sem_average_marks'].value(), test_score=form['test_score'].value(), test_series_id=form['test_series_id'].value(), language=form['language'].value(), current_sem=form['current_sem'].value(), resume=files)
            sd.save()
            print(sd)
            print('Saved')
            return render(request, 'newproject.html')
    else:
        print('Entered else')
        form = StudentsProfileForm()
        return render(request, 'StudentProfile.html', {'form': form})


def student_profile2(request):
    if request.method == 'POST':
        global temp1, temp2
        st = StudentsProfile()
        st.student_id = temp1
        st.student_username = temp2
        st.project_score = '30'
        st.sem_average_marks = request.POST['sem_average_marks']
        st.test_score = request.POST['test_score']
        st.test_series_id = request.POST['test_series_id']
        st.language = request.POST['language']
        st.current_sem = request.POST['current_sem']
        st.resume = request.FILES['resume']
        st.save()
    return render(request, 'slogin.html')


def edit_profile(request):
    global temp1, temp2
    e_profile = get_object_or_404(StudentsProfile, student_id=temp1)
    edit_profile = StudentsProfile.objects.filter(
        student_id=temp1).values()
    if request.method == "POST":
        form = EditForm(request.POST, instance=e_profile)
        if form.is_valid():
            form.save()
            return render(request, 'sdash.html')
    else:
        form = EditForm(instance=e_profile)
        return render(request, 'emember.html', {'form': form, 'events': events, 'current_user': current_user, 'teams': teams, 'members': members})