from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Student
from .models import IssuedBook

admin.site.register(Book)
admin.site.register(Student)
admin.site.register(IssuedBook)
