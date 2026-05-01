from django.db import models
class Student(models.Model):
    student_name = models.CharField(max_length=100, verbose_name="اسم الطالب")
    email = models.EmailField(unique=True, verbose_name="البريد الالكتروني")
    phonenumber = models.CharField(max_length=15, verbose_name="رقم الهاتف")
    major = models.CharField(max_length=100, verbose_name="التخصص")
    added_date = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    def __str__ (self):
        return self.student_name

# Create your models here.
