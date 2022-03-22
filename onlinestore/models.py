from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=30)

class signup(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    post=models.CharField(max_length=30)
    pin=models.IntegerField()
    email=models.EmailField()
    phone=models.BigIntegerField()
    sid=models.ForeignKey(login,on_delete=models.CASCADE)


class complient(models.Model):
    complients=models.CharField(max_length=100)
    date=models.DateField()
    reply=models.CharField(max_length=100)
    userid=models.ForeignKey(signup,on_delete=models.CASCADE)

class feedback(models.Model):
    feedbacks=models.CharField(max_length=100)
    date=models.DateField()
    userid=models.ForeignKey(signup,on_delete=models.CASCADE)

class addart(models.Model):
    art=models.FileField()
    name=models.CharField(max_length=100)
    discription=models.CharField(max_length=200)
    price=models.BigIntegerField()
    type=models.CharField(max_length=100)
    quantity=models.BigIntegerField()

class usermessege(models.Model):
    messege=models.CharField(max_length=1000)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)

class carttable(models.Model):
    userid = models.ForeignKey(signup, on_delete=models.CASCADE)
    prdt=models.ForeignKey(addart,on_delete=models.CASCADE)
    quanity=models.IntegerField()
    sprice=models.IntegerField()

class ordertable(models.Model):
    userid = models.ForeignKey(signup, on_delete=models.CASCADE)
    prdtid = models.ForeignKey(addart, on_delete=models.CASCADE)
    quantity = models.ForeignKey(carttable,on_delete=models.CASCADE)
    date = models.DateField()
    price = models.BigIntegerField()