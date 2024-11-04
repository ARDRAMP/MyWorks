from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect , get_object_or_404
from django.urls import reverse
from  django.core.files.storage import FileSystemStorage
from .models import *
from razorpay import Client

def index(request):
    a=course_details.objects.all()
    return render(request,'index.html',{'assigned_courses':a})

def index1(request):
    a=course_details.objects.all()
    return render(request,'index.html',{'assigned_courses':a})

def register(request):
    return render(request,'register.html')


def addstudent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        place = request.POST.get('place')
        address = request.POST.get('address')
        st_type = request.POST.get('st_type')
        disability_status = request.POST.get('disability_status')
        disability_certificate = request.FILES.get('certification') 
        password = request.POST.get('password')
        

        if studentreg.objects.filter(email=email).exists():
         
            return render(request, 'index.html', {'message': 'Email already exists. Please use a different email.'})
        elif facultyreg.objects.filter(email=email).exists():
           
            return render(request, 'index.html', {'message': 'Email already exists. Please use a different email.'})

        ins = studentreg(name=name, email=email, phone=phone, city=city, place=place, password=password,st_type=st_type, address=address,status='pending',disability_status=disability_status,disability_certificate=disability_certificate )
        ins.save()

        return render(request, 'index.html', {'message': 'Successfully Registered'})

    return render(request, 'index.html')


def login(request):
    return render(request,'login.html')


def addlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['logintdetail'] = email
        request.session['admin'] = 'admin'
        return redirect(index)

    elif studentreg.objects.filter(email=email,password=password,status='approved').exists():
        userdetails=studentreg.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['sid'] = userdetails.id
            request.session['sname'] = userdetails.name

            request.session['semail'] = email
            return redirect(index)
    elif facultyreg.objects.filter(email=email,password=password).exists():
        userdetails=facultyreg.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['fid'] = userdetails.id
            request.session['fname'] = userdetails.name
            request.session['femail'] = email


            return redirect(index)

    
    else:
        return render(request, 'login.html', {'message':'Invalid Email or Password'})
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index1)

def register_faculty(request):
    return render(request,'register_faculty.html')

def addfaculty(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course = request.POST.get('course')
        address = request.POST.get('address')
        password = request.POST.get('password')

        # Check if the email already exists in the member table
        if facultyreg.objects.filter(email=email).exists():
            # Email already exists, display an alert message
            return render(request, 'index.html', {'message': 'Email already exists. Please use a different email.'})
        elif studentreg.objects.filter(email=email).exists():
            # Email already exists, display an alert message
            return render(request, 'index.html', {'message': 'Email already exists. Please use a different email.'})

        ins = facultyreg(name=name, email=email, phone=phone, course=course, password=password, address=address)
        ins.save()

        return render(request, 'index.html', {'message': 'Successfully Registered'})

    return render(request, 'index.html')

def view_students_admin(request):
    a=studentreg.objects.all()
    return render(request,'view_students_admin.html',{'result':a})

def approve_stud(request, id):
    survey = get_object_or_404(studentreg, id=id)
    survey.status = 'approved'
    survey.save()
    return redirect(view_students_admin)

def reject_stud(request,id):
    survey = get_object_or_404(studentreg, id=id)
    survey.status = 'rejected'
    survey.save()
    return redirect(view_students_admin)


def assign(request):
    approved_registrations = studentreg.objects.filter(status='approved').exclude(id__in=assigned_studentreg.objects.values('sid'))
    sel1=facultyreg.objects.all()
    return render(request,'assign.html',{'result':approved_registrations,'res':sel1})

def addassign(request):
    if request.method=="POST":
        sid=request.POST.get('sid')
        fid=request.POST.get('fid')
        s=studentreg.objects.get(id=sid)
        a=s.city
        b=s.place
        c=s.email
        d=s.phone
        e=s.name
        ins=assigned_studentreg(sid=sid,fid=fid,city=a,place=b,email=c,phone=d,name=e)
        ins.save()
        return render(request,'index.html',{'message':'Assigned Successfully'})
    
def view_faculty_admin(request):
    a=facultyreg.objects.all()
    return render(request,'view_faculty_admin.html',{'result':a})

def remove_fac(request,id):
    a=facultyreg.objects.get(id=id)
    a.delete()
    return redirect(view_faculty_admin)


def profile(request):
    a=facultyreg.objects.get(id=request.session['fid'])
    return render(request,'profile.html',{'result':a})

def profile_up(request):
    a=facultyreg.objects.get(id=request.session['fid'])
    return render(request,'profile_up.html',{'result':a})


def addfaculty_up(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course = request.POST.get('course')
        address = request.POST.get('address')
        password = request.POST.get('password')

        ins = facultyreg(name=name, email=email, phone=phone, course=course, password=password, address=address,id=id)
        ins.save()

        return render(request, 'index.html', {'message': 'Successfully Updated'})

    return render(request, 'index.html')


def class_schedule(request):
    fid=request.session['fid']
    sel=assigned_studentreg.objects.filter(fid=fid)
    return render(request,'class_schedule.html',{'result':sel})

def addschedule(request):
    if request.method == 'POST':
        typee = request.POST.get('typee')
        fid = request.session['fid']
        date = request.POST.get('date')
        link = request.POST.get('link')
        message = request.POST.get('message')
        host_key = request.POST.get('host_key')
        password = request.POST.get('password')

        ins = class_schedules(typee=typee,host_key=host_key,password=password, date=date, link=link, message=message,fid=fid,status='pending')
        ins.save()

        return render(request, 'index.html', {'message': 'Successfully Added'})

    return render(request, 'index.html')

def edit_class(request,id):
    sel=class_schedules.objects.get(id=id)
    return render(request,'edit_class.html',{'result':sel})

def edit_class_up(request,id):
    if request.method == 'POST':
        typee = request.POST.get('typee')
        fid = request.session['fid']
        date = request.POST.get('date')
        link = request.POST.get('link')
        message = request.POST.get('message')
        host_key = request.POST.get('host_key')
        password = request.POST.get('password')

        ins = class_schedules(typee=typee,host_key=host_key,password=password, date=date, link=link, message=message,fid=fid,status='pending',id=id)
        ins.save()

        return render(request, 'index.html', {'message': 'Successfully Updated'})

    return render(request, 'index.html')

def viewclass(request):
    sid=request.session['sid']
    try:
        stud=assigned_studentreg.objects.get(sid=sid)
    except:
        return render(request, 'index.html', {'message': 'Not Assigned any Faculty'})
    stud_fac=stud.fid
    sel=class_schedules.objects.filter(fid=stud_fac)
    sel1=facultyreg.objects.all()
    for i in sel:
        for j in sel1:
            if str(i.fid)==str(j.id):
                i.fid=j.name
    return render(request,'viewclass.html',{'result':sel})


def apply_leave(request):
    sid = request.session.get('sid') 

    if sid is not None:
        try:
            assigned_student = assigned_studentreg.objects.get(sid=sid)
            faculty_id = assigned_student.fid
            return render(request, 'apply_leave.html', {'faculty_id': faculty_id})
        except assigned_studentreg.DoesNotExist:
            return render(request, 'apply_leave.html', {'message': 'Faculty id not found for the given student id'})
    else:
        return render(request, 'apply_leave.html', {'error': 'Student id not found in the session'})
    

def addapply_leave(request):
    if request.method == 'POST':
        fid = request.POST.get('fid')
        sid = request.session['sid']
        date = request.POST.get('date')
        reason = request.POST.get('reason')

        ins = leave_applications(sid=sid, date=date, reason=reason,fid=fid,status='pending')
        ins.save()

        return render(request, 'index.html', {'message': 'Successfully Requested'})

    return render(request, 'index.html')

def view_leave_status(request):
    sid=request.session['sid']
    sel=leave_applications.objects.filter(sid=sid)
    return render(request,'view_leave_status.html',{'result':sel})


def stud_profile(request):
    a=studentreg.objects.get(id=request.session['sid'])
    return render(request,'stud_profile.html',{'result':a})

def stud_profile_up(request):
    a=studentreg.objects.get(id=request.session['sid'])
    return render(request,'stud_profile_up.html',{'result':a})


def addstudent_up(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        place = request.POST.get('place')
        address = request.POST.get('address')
        password = request.POST.get('password')
        st_type = request.POST.get('st_type')


        ins = studentreg(name=name, email=email,st_type=st_type, phone=phone, city=city, place=place, password=password, address=address,status='approved',id=id)
        ins.save()

        return render(request, 'index.html', {'message': 'Successfully Updated'})

    return render(request, 'index.html')

def leave_request(request):
    fid=request.session['fid']
    sel=leave_applications.objects.filter(fid=fid)
    return render(request,'leave_request.html',{'result':sel})

def approve_leave(request, id):
    survey = get_object_or_404(leave_applications, id=id)
    survey.status = 'approved'
    survey.save()
    return redirect(leave_request)

def reject_leave(request,id):
    survey = get_object_or_404(leave_applications, id=id)
    survey.status = 'rejected'
    survey.save()
    return redirect(leave_request)

def admin_viewleave(request):
    sel=leave_applications.objects.all()
    return render(request,'admin_viewleave.html',{'result':sel})

def admin_viewclass(request):
    sel=class_schedules.objects.all()
    sel1=facultyreg.objects.all()
    for i in sel:
        for j in sel1:
            if str(i.fid)==str(j.id):
                i.fid=j.name

    return render(request,'admin_viewclass.html',{'result':sel})

def course(request):
    return render(request,'course.html')


def addcourse(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        details = request.POST.get('details')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        amount = request.POST.get('amount')

        ins = course_details(details=details, startdate=startdate, enddate=enddate,name=name,amount=amount)
        ins.save()

        return render(request, 'index.html', {'message': 'Successfully Added'})

    return render(request, 'index.html')

def view_course(request):
    sel1=course_details.objects.all()
    return render(request,'view_course.html',{'result':sel1})

def assign_course(request,id):
    sel1=studentreg.objects.get(id=id)
    sel2=course_details.objects.all()
    return render(request,'assign_course.html',{'result':sel1,'res':sel2})

def addassign_course(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        std_name = request.POST.get('std_name')
        sid = request.POST.get('sid')

        ins = course_assign(std_name=std_name, sid=sid, course_id=course_id)
        ins.save()

        return render(request, 'index.html', {'message': 'Successfully Assigned'})

    return render(request, 'index.html')

def view_assign_course(request):
    crs=course_details.objects.all()
    return render(request, 'view_assign_course.html', {'result': crs})

    

def c_payment(request,id):
    sel2=course_details.objects.get(id=id)
    return render(request,'c_payment.html',{'result':sel2})

# def addpayment(request):
#     if request.method == 'POST':
#         course = request.POST.get('course')
#         sid = request.session['sid']
#         c_id = request.POST.get('c_id')
#         amount = int(request.POST.get('amount'))*100
#         client=Client(auth=("rzp_test_Emp8plnrikaWvE","G1BOhC1vHW9peZ5nUdJaNr68"))
#         payment=client.order.create({"amount":amount, "currency":'INR',"payment_capture":'1'})
#         if course_payment.objects.filter(sid=sid,c_id=c_id).exists():
#             return render(request, 'index.html', {'message': 'You already paid for this course'})
#         ins = course_payment(course=course, c_id=c_id, amount=amount,sid=sid, payment_id=payment['id'],paid=True)
#         print(payment)
#         ins.save()
#         return render(request, 'c_payment.html',{'payment':payment})
#     return render(request, 'index.html')





def addpayment(request):
    if request.method == 'POST':
        course = request.POST.get('course')
        sid = request.session['sid']
        c_id = request.POST.get('c_id')
        amount = int(request.POST.get('amount')) * 100
        client = Client(auth=("rzp_test_SWZuIWsXN3E85N", "1jQcV6TDoXuX2PudIZjBITWx"))
        payment = client.order.create({"amount": amount, "currency": 'INR', "payment_capture": '1'})
        if course_payment.objects.filter(sid=sid, c_id=c_id).exists():
            return render(request, 'index.html', {'message': 'You already paid for this course'})
        ins = course_payment(course=course, c_id=c_id, amount=amount, sid=sid, payment_id=payment['id'], paid=True)
        
        # Store the attributes of the instance in session data
        request.session['pending_payment'] = {
            'course': ins.course,
            'c_id': ins.c_id,
            'amount': ins.amount,
            'sid': ins.sid,
            'payment_id': ins.payment_id,
            'paid': ins.paid
        }
        
        return render(request, 'c_payment.html', {'payment': payment})
    return render(request, 'index.html')

def success(request):
    if request.method == 'POST':
        # Retrieve the pending payment attributes from session data
        pending_payment_data = request.session.get('pending_payment')
        if pending_payment_data:
            # Reconstruct the course_payment instance
            ins = course_payment(
                course=pending_payment_data['course'],
                c_id=pending_payment_data['c_id'],
                amount=int(pending_payment_data['amount'])/100,
                sid=pending_payment_data['sid'],
                payment_id=pending_payment_data['payment_id'],
                paid=pending_payment_data['paid']
            )
            # Save the instance
            ins.save()
            # Clear the pending payment from session data
            del request.session['pending_payment']
            return render(request, 'success.html', {'message': 'Payment successful'})
        else:
            return render(request, 'success.html', {'message': 'No pending payment found'})
    return render(request, 'success.html')

def view_payments(request):
    sid = request.session['sid']
    sel2=course_payment.objects.filter(sid=sid)
    return render(request,'view_payments.html',{'result':sel2})

def viewpayments(request):
    sel2=course_payment.objects.all()
    return render(request,'viewpayments.html',{'result':sel2})


def my_class_schedule(request):
    fid = request.session['fid']
    sel2=class_schedules.objects.filter(fid=fid)
    return render(request,'my_class_schedule.html',{'result':sel2})

def add_stdy_mtr(request):
    return render(request,'stdy_mtr.html')

def stdy_mtr(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        details = request.POST.get('details')
        c_id = request.POST.get('c_id')
        file = request.FILES['filee']
        video_link = request.POST.get('video_link')  # Get video link from form

        fs=FileSystemStorage()
        upld=fs.save(file.name,file)
        ins = study_materials(name=name, details=details, file=upld, c_id=c_id, video_link=video_link)
        ins.save()
        return render(request, 'index.html', {'message': 'Successfully Added'})
    
def view_stdy_mtr(request):
    current_user_sid = request.session['sid']

    # Filter course_payment for the current user and paid courses
    paid_course_ids = course_payment.objects.filter(sid=current_user_sid, paid=True).values_list('c_id', flat=True)

    # Fetch study materials for the paid courses of the current user
    sel2 = study_materials.objects.filter(c_id__in=paid_course_ids)
    
    return render(request, 'view_stdy_mtr.html', {'result': sel2}) 



def view_mystudents(request):
    fid = request.session['fid']
    std=assigned_studentreg.objects.filter(fid=fid)
    return render(request,'view_mystudents.html',{'result':std})

def view_stdy_mtr_fclty(request):
    sid=study_materials.objects.all()
    return render(request,'view_stdymt.html',{'result':sid})

def chatuser(request):
    s_id = request.session['sid']
    try:
        booked_student = assigned_studentreg.objects.get(sid=s_id)
        mentor_id = booked_student.fid
    except assigned_studentreg.DoesNotExist:
        mentor_id = None  # Handle the case where the student is not found

    mentor_name = None
    if mentor_id is not None:
        try:
            mentor = facultyreg.objects.get(id=mentor_id)
            mentor_name = mentor.name
        except facultyreg.DoesNotExist:
            mentor_name = None  
    cht = chats.objects.filter(s_id=s_id, m_id=mentor_id)     

    return render(request,'chat_user.html', {'chat': cht,'mntr':mentor_name})

def addchat_std(request):
    if request.method == 'POST':
        s_id = request.session['sid']
        message = request.POST.get('message')
        
        # Retrieve the mentor ID for the corresponding student
        try:
            booked_student = assigned_studentreg.objects.get(sid=s_id)
            mentor_id = booked_student.fid
        except assigned_studentreg.DoesNotExist:
            mentor_id = None  # Handle the case where the student is not found
        
        ins = chats(s_id=s_id, s_msg=message,  m_id=mentor_id)  # Assuming you have a mentor_id field in the 'chats' model
        ins.save()
                
    return redirect(chatuser)

def chatmentor(request,id):
    m_id = request.session['fid']
    st_id = studentreg.objects.get(id=id)    
    s_id=st_id.id
    # print (s_id)
    s_name = st_id.name
    cht = chats.objects.filter(s_id=s_id, m_id=m_id)     
    return render(request,'chat_mentor.html', {'chat': cht,'stud':s_name,'student':s_id})

def addchat_mnt(request):
    if request.method == 'POST':
        m_id = request.session['fid']
        message = request.POST.get('message') 
        s_id = request.POST.get('s_id') 
        ins = chats(s_id=s_id, m_msg=message, m_id=m_id)
        ins.save()
        
        # Redirect to 'chatmentor' with the required 'id' parameter
        return redirect('chatmentor', id=s_id)
    
def progress(request):
    return render(request,'progress.html')

def certificate(request):
    return render(request,'certificate.html')
def signlanguage(request):
    return render(request,'signlanguage.html')