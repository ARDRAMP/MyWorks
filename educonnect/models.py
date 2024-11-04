from django.db import models

class studentreg(models.Model):
    name=models.CharField(max_length=150)
    place=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    st_type=models.CharField(max_length=150)
    disability_status = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no', 'No')], default='no')
    disability_certificate = models.FileField(upload_to='certificates/', null=True, blank=True)


class facultyreg(models.Model):
    name=models.CharField(max_length=150)
    course=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    password=models.CharField(max_length=150)

class assigned_studentreg(models.Model):
    name=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    place=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    sid=models.CharField(max_length=150)
    fid=models.CharField(max_length=150)
 
class class_schedules(models.Model):
    typee=models.CharField(max_length=150)
    fid=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    link=models.CharField(max_length=150)
    message=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    host_key=models.CharField(max_length=150)
    status=models.CharField(max_length=150)

class leave_applications(models.Model):
    sid=models.CharField(max_length=150)
    fid=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    reason=models.CharField(max_length=150)
    status=models.CharField(max_length=150)

class course_details(models.Model):
    name=models.CharField(max_length=150)
    details=models.CharField(max_length=150)
    startdate=models.CharField(max_length=150)
    enddate=models.CharField(max_length=150)
    amount=models.CharField(max_length=150) 

class course_assign(models.Model):
    course_id=models.CharField(max_length=150)
    std_name=models.CharField(max_length=150)
    sid=models.CharField(max_length=150)


class course_payment(models.Model):
    sid=models.CharField(max_length=150)
    course=models.CharField(max_length=150)
    c_id=models.CharField(max_length=150)
    amount=models.CharField(max_length=150)
    payment_id=models.CharField(max_length=150)
    paid=models.BooleanField(default=False) 

class study_materials(models.Model):
    name=models.CharField(max_length=150)
    details=models.CharField(max_length=150)
    file=models.CharField(max_length=150)
    c_id=models.CharField(max_length=150)
    video_link = models.URLField(max_length=200, blank=True) 


class chats(models.Model):
    s_id=models.CharField(max_length=150)
    m_id=models.CharField(max_length=150)
    s_msg=models.CharField(max_length=150)
    m_msg=models.CharField(max_length=150)