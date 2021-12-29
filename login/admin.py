from django.contrib import admin
from .models import Sreg, Testscore
from .models import Treg
from .models import nproj
from .models import Newproj
from .models import Grade
from login.models import StudentsProfile, TestSeries
# Register your models here.
admin.site.register(Sreg)
admin.site.register(Treg)
admin.site.register(nproj)
admin.site.register(Newproj)
admin.site.register(Grade)
admin.site.register(StudentsProfile)
admin.site.register(TestSeries)
admin.site.register(Testscore)
