import random
from datetime import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from onlinestore.models import *


def adminindex(request):
    return render(request,'admin index1.html')

def indexlog(request):
    obb=addart.objects.count()
    ob=addart.objects.all()
    return render(request,'index login.html',{"data":ob,'value':obb})

def log(request):
    return render(request,'login form.html')

def contact(request):
    return render(request,'contact.html')

def contact3(request):
    return render(request,'contact 3.html')

@login_required(login_url="/logoutalert")
def userhome(request):
    ob=addart.objects.all()
    return render(request,'customers.html',{"data":ob})

@login_required(login_url="/logoutalert")
def admin(request):
    return render(request,'Admin home.html')

def sign(request):
    return render(request,'signup form.html')

@login_required(login_url="/logoutalert")
def addart1(request):
    ob=addart.objects.all()
    return render(request,'add art.html',{"data":ob})

@login_required(login_url="/logoutalert")
def manageart(request):
    return render(request,'manage art.html')

@login_required(login_url="/logoutalert")
def addarts(request):
    return render(request,'manage art.html')

@login_required(login_url="/logoutalert")
def verifyuser(request):
    ob=signup.objects.all()
    return render(request,'verify customer.html',{"data":ob})

def shophome(request):
    return render(request,'shop.html')

@login_required(login_url="/logoutalert")
def sendcomp(request):
    return render(request,'send complaint.html')

@login_required(login_url="/logoutalert")
def sendfee(request):
    return render(request,'send feedback.html')

@login_required(login_url="/logoutalert")
def sendrep(request):
    return render(request,'send reply.html')

@login_required(login_url="/logoutalert")
def viewfee(request):
    ob=feedback.objects.all()
    return render(request,'view feedback.html',{"data":ob})

@login_required(login_url="/logoutalert")
def viewcom(request):
    ob=complient.objects.all()
    return render(request,'view complaint reply.html',{"data":ob})

@login_required(login_url="/logoutalert")
def viewcompli(request):
    ob=complient.objects.all()
    return render(request,'view complaints.html',{"data":ob})

def cart(request):
    return render(request,'tem/cart.html')

@login_required(login_url="/logoutalert")
def viewart(request):
    ob=addart.objects.all()
    return render(request,'view work details.html',{"data":ob})


@login_required(login_url="/logoutalert")
def viewartcam(request):
    ob=addart.objects.all()
    return render(request,'workindex/view work index camera.html',{"data":ob})

@login_required(login_url="/logoutalert")
def viewartlap(request):
    ob=addart.objects.all()
    return render(request,'workindex/view work index laptop.html',{"data":ob})

@login_required(login_url="/logoutalert")
def viewartsof(request):
    ob=addart.objects.all()
    return render(request,'workindex/view work index sofa.html',{"data":ob})

@login_required(login_url="/logoutalert")
def viewarthead(request):
    ob=addart.objects.all()
    return render (request,'workindex/view work index headphone.html',{"data":ob})

@login_required(login_url="/logoutalert")
def orderrt1(request,id):
    request.session['oid']=id
    ob=addart.objects.get(id=id)
    return render(request,'order work.html',{"data":ob})


def loginpress(request):
    uname=request.POST['textfield']
    passwd=request.POST['textfield2']
    try:
        ob=login.objects.get(username=uname,password=passwd)
        if(ob.type == "admin" ):
            request.session['lid']=ob.id
            ob1=auth.authenticate(username='admin',password='admin')
            if ob1 is not None:
                auth.login(request,ob1)
            return redirect('/adminindex')
        elif(ob.type == "user"):
            request.session['lid']=ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            if ob1 is not None:
                auth.login(request, ob1)
            return  redirect('/userhome')
        elif(ob.type == "shop"):
            request.session['lid']=ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            if ob1 is not None:
                auth.login(request, ob1)
            return  redirect('/shophome')
        else:
            return HttpResponse('''<script>alert("invalid entry");window.location="/"</script>''')
    except:
        return HttpResponse('''<script>alert("invalid entry");window.location="/"</script>''')

@login_required(login_url="/logoutalert")
def editprofile(request):
    ob=signup.objects.get(sid=request.session['lid'])
    return render(request,'editprofile form.html',{"data":ob})


def signuppress(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    age=request.POST['textfield3']
    gender=request.POST['radiobutton']
    place=request.POST['textfield5']
    post=request.POST['textfield6']
    pin=request.POST['textfield7']
    email=request.POST['textfield8']
    phone=request.POST['textfield9']
    unaem=request.POST['textfield10']
    passw=request.POST['textfield11']
    lp=login()
    lp.username=unaem
    lp.password=passw
    lp.type='pending'
    lp.save()

    sp=signup()
    sp.firstname=fname
    sp.lastname=lname
    sp.age=age
    sp.gender=gender
    sp.place=place
    sp.post=post
    sp.pin=pin
    sp.email=email
    sp.phone=phone
    sp.sid=lp
    sp.save()
    return HttpResponse('''<script>alert("successfully registered");window.location="/"</script>''')

@login_required(login_url="/logoutalert")
def accept(request,id):
     ob=login.objects.get(id=id)
     ob.type='user'
     ob.save()
     return HttpResponse('''<script>alert("user accepted");window.location="/verifyuser"</script>''')

@login_required(login_url="/logoutalert")
def reject(request,id):
     ob=login.objects.get(id=id)
     ob.type='rejected'
     ob.save()
     return HttpResponse('''<script>alert("user rejected");window.location="/verifyuser"</script>''')

@login_required(login_url="/logoutalert")
def submit(request):
    fname = request.POST['textfield']
    lname = request.POST['textfield2']
    age = request.POST['textfield3']
    gender = request.POST['radiobutton']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    email = request.POST['textfield7']
    phone = request.POST['textfield8']
    ob=signup.objects.get(sid=request.session['lid'])
    ob.firstname=fname
    ob.lastname=lname
    ob.age=age
    ob.gender=gender
    ob.place=place
    ob.post=post
    ob.pin=pin
    ob.email=email
    ob.phone=phone
    ob.save()
    return HttpResponse('''<script>alert("sucessfully updated");window.location="/userhome"</script>''')

@login_required(login_url="/logoutalert")
def sendcomplientpress(request):
    comp=request.POST['messages']
    ob=complient()
    ob.complients=comp
    ob.date=datetime.today()
    ob.reply='pending'
    ob.userid=signup.objects.get(sid__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("complient sent");window.location="/userhome"</script>''')

@login_required(login_url="/logoutalert")
def sendreply(request):
    repl=request.POST['textarea']
    ob=complient.objects.get(id=request.session['lid'])
    ob.reply=repl
    ob.save()
    return HttpResponse('''<script>alert("reply send");window.location="/admin"</script>''')

@login_required(login_url="/logoutalert")
def sendfeedbackpress(request):
    feed=request.POST['textarea']
    ob=feedback()
    ob.feedbacks=feed
    ob.date=datetime.today()
    ob.userid=signup.objects.get(sid__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("feedback sent");window.location="/userhome"</script>''')


@login_required(login_url="/logoutalert")
def addclick(request):
    photo = request.FILES['file']
    cp = FileSystemStorage()
    fs = cp.save(photo.name, photo)
    name = request.POST['textfield']
    price = request.POST['textfield2']
    stock = request.POST['textfield3']
    disc=request.POST['textfield6']
    type=request.POST['textfield7']
    ar=addart()
    ar.art=fs
    ar.name=name
    ar.price=price
    ar.quantity=stock
    ar.discription=disc
    ar.type=type
    ar.save()
    return HttpResponse('''<script>alert("successfully added");window.location="/admin" </script>''')


@login_required(login_url="/logoutalert")
def addtocart(request):
    product=addart.objects.get(id=request.session['lid'])
    customr=signup.objects.get(sid__id=request.session['lid'])
    ob=carttable()
    ob.userid=customr
    ob.prdt=product
    ob.quantity="1  "
    ob.save()
    return HttpResponse('''<script>alert("iteam added to cart");window.location="/userhome"</script>''')


@login_required(login_url="/logoutalert")
def delete(request,id):
    request.session['lid']=id
    ob=addart.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/addart1"</script>''')


# @login_required(login_url="/logoutalert")
# def edit1(request,id):
#     request.session['lid']=id
#     ob=addart.objects.get(id=id)
#     return render(request,'updateart.html',{"data":ob})

@login_required(login_url="/logoutalert")
def edit1(request,id):
    request.session['lid']=id
    ob=addart.objects.get(id=id)
    return render(request,'view edit prodect.html',{"data":ob})


@login_required(login_url="/logoutalert")
def artupdate(request):
    try:
        photo = request.FILES['file']
        cp = FileSystemStorage()
        fs = cp.save(photo.name, photo)
        name = request.POST['textfield']
        price = request.POST['textfield2']
        stock = request.POST['textfield3']
        disc = request.POST['textfield6']
        ar = addart.objects.get(id=request.session['lid'])
        ar.art = fs
        ar.name = name
        ar.price = price
        ar.quantity = stock
        ar.discription = disc
        ar.save()
    except:
        name = request.POST['textfield']
        price = request.POST['textfield2']
        stock = request.POST['textfield3']
        disc = request.POST['textfield6']
        ar = addart.objects.get(id=request.session['lid'])
        ar.name = name
        ar.price = price
        ar.quantity = stock
        ar.discription = disc
        ar.save()
    return HttpResponse('''<script>alert("successfully updated");window.location="/adminindex" </script>''')



@login_required(login_url="/logoutalert")
def artorder(request):
    art=addart.objects.get(id=request.session['oid'])
    customer=signup.objects.get(sid__id=request.session['lid'])
    price=request.POST['textfield6']
    quantity=request.POST['textfield5']
    fs=ordertable()
    fs.quantity=quantity
    fs.price=price
    fs.cakeid=art
    fs.date=datetime.today()
    fs.userid=customer
    fs.save()
    return HttpResponse('''<script>alert("order confirmed");window.location="/viewart"</script>''')

@login_required(login_url="/logoutalert")
def getintouch(request):
    mssg=request.POST['messages']
    nme=request.POST['name']
    mail=request.POST['email']
    subj=request.POST['subject']
    ob=usermessege()
    ob.messege=mssg
    ob.name=nme
    ob.email=mail
    ob.subject=subj
    ob.save()
    return HttpResponse('''<script>alert ("messege sent");window.location="/contact"</script>''')

def submitem(request):

    return HttpResponse('''<script>alert("email sent");window.location="/contact"</script>''')

def submitem1(request):

    return HttpResponse('''<script>alert("email sent");window.location="/"</script>''')

def submitem2(request):

    return HttpResponse('''<script>alert("item booked");window.location="/"</script>''')

def search(request):
    ser=request.POST['textfield']
    ob=addart.objects.filter(type__startswith=ser)
    return render(request,'search index home.html',{"data":ob})

@login_required(login_url="/logoutalert")
def cart1(request):
    obb=carttable.objects.filter(userid__sid=request.session['lid'])
    ob= carttable.objects.aggregate(Sum('sprice'))
    return render(request,'cart2.html',{"data":obb,"value":ob})

def singleproduct(request,id):
    request.session['pid'] = id
    ob=addart.objects.get(id=id)
    return  render(request,'single-product .html',{"data":ob})

@login_required(login_url="/logoutalert")
def singleproduct2(request,id):
    request.session['pid']=id
    ob=addart.objects.get(id=id)
    return  render(request,'single-product 2.html',{"data":ob})

def adcr(request):
    return HttpResponse('''<script>alert("please log in to add into cart");window.location="/cart"</script>''')

@login_required(login_url="/logoutalert")
def adcrt(request):
    quantit=request.POST['textfield']
    gtotal=request.POST['total']
    ob=carttable()
    ob.userid=signup.objects.get(sid_id=request.session['lid'])
    ob.prdt=addart.objects.get(id=request.session['pid'])
    ob.quanity=quantit
    ob.sprice=gtotal
    ob.save()
    return HttpResponse('''<script>alert("item moved to cart");window.location="/userhome"</script>''')

@login_required(login_url="/logoutalert")
def contactcust(request):
    return render(request,'contact cust.html')

@login_required(login_url="/logoutalert")
def feedbackindex(request):
    ob=complient.objects.all()
    return render(request,'feedback index.html',{"data":ob})

@login_required(login_url="/logoutalert")
def updatecart(request):
    ob = carttable.objects.all()
    return render(request,'cartupdate.html',{"data":ob})


@login_required(login_url="/logoutalert")
def updatecartedit(request,id):
    request.session['eid']=id
    ob=carttable.objects.get(id=id)
    return render(request,'single-product 2 edit.html',{"data":ob})

def updatecartdelete(request,id):
    request.session['did']=id
    ob=carttable.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("item removed from cart");window.location="/updatecart"</script>''')


@login_required(login_url="/logoutalert")
def carteditupdate(request):
    quantit = request.POST['textfield']
    ob = carttable.objects.get(id=request.session['eid'])
    ob.userid = signup.objects.get(sid__id=request.session['lid'])
    ob.prdt = addart.objects.get(id=request.session['pid'])
    ob.quanity = quantit
    ob.save()
    return HttpResponse('''<script>alert("item moved to cart");window.location="/userhome"</script>''')

# def orderiteams(request):
#     ob=carttable.objects.get(id=request.session)

def logout(request):
    auth.logout(request)
    return redirect('/')

def logoutalert(request):
    return HttpResponse('''<script>alert("please login to continue");window.location="/"</script>''')

@login_required(login_url="/logoutalert")
def categories(request):
    ob=addart.objects.all()
    return render(request,'category.html',{"data":ob})

@login_required(login_url="/logoutalert")
def  search2(request):
    ser=request.POST['textfield1']
    ob=addart.objects.filter(type__startswith=ser)
    return render(request,'search index home.html',{"data":ob})

def forgotpass(request):
    return render(request,'forgotpass.html')

def forgotpasswordpress(request):
    uname=request.POST['textfield7']
    email=request.POST['textfield8']
    reset = login.objects.get(username=uname)
    if reset is not None:
        a = random.randint(0000, 9999)
        reset.password = (str(a))
        reset.save()
        send_mail('forgot password', "YOUR NEW PASSWORD IS  -" + str(a), 'projectdemo369@gmail.com', [email],
                  fail_silently=False)
        return HttpResponse('''<script>alert("messege sent");window.location="/"</script>''')

    else:
        return HttpResponse('''<script>alert("invalid");window.location="forgotpassword"</script>''')

def likepost(request):
    username = request.GET['username']
    print(username)
    data = {
        'is_taken': login.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = "A user with this username already exists."
    return JsonResponse(data)

def viewpro(request):
    ob = addart.objects.all()
    return render(request,'view prodect.html',{"data":ob})

def viewedpr(request):

    return render(request,'view edit prodect.html')

@login_required(login_url="/logoutalert")
def  search3(request):
    ser=request.POST['textfield1']
    ob=addart.objects.filter(name__startswith=ser)
    return render(request,'search index admin.html',{"data":ob})