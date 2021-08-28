from django.shortcuts import render, redirect
from .models import Member,Products,User,Cart
import datetime
from django.core.files.storage import FileSystemStorage
from werkzeug.utils import secure_filename

# Create your views here.

def index(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'crud/index.html', context)
	
def log(request):
    return render(request, 'crud/login.html')
	
def paybill(request):
    return render(request, 'crud/paybill.html')
	
def sign(request):
   return render(request, 'crud/signup.html')
	
def pro(request):
   return render(request, 'crud/add.html')
	
def pview(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'crud/view.html', context)
    return render(request, 'crud/add.html')
	
def create(request):
    member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    member.save()
    return redirect('/')
	

def pcreate(request):
    #myfile = request.FILES['image']
    #fs = FileSystemStorage()
    #filename = fs.save(myfile.name, myfile)
    p = Products(name=request.POST['name'], price=request.POST['price'], color=request.POST['color'], image=request.POST['image'], img=request.POST['img'], picture=request.POST['picture'], pic=request.POST['pic'], pica=request.POST['pica'],category=request.POST['category'], description=request.POST['description'], engine=request.POST['engine'], displacement=request.POST['displacement'], power=request.POST['power'], drivetrain=request.POST['drivetrain'], fuel_tank_capacity=request.POST['fuel_tank_capacity'], airbags=request.POST['airbags'])
    p.save()
    return render(request, 'crud/admin.html')
	
def signup(request):
    p = User(username=request.POST['username'], password=request.POST['password'], mobile_number=request.POST['mobile_number'], email_id=request.POST['email_id'], gender=request.POST['gender'], address=request.POST['address'])
    p.save()
    return redirect('/')
	
def login(request):
    print("====================")
    user = None
    try:
      user = User.objects.get(username=request.POST['username'],password=request.POST['password'])
    except:
      print("ooo")
    print("====================")
    print(user)
    #print(user.username)
    if(user!=None):
            request.session['username'] = request.POST['username']
            if(request.POST['username'] == 'admin'):
                return render(request, 'crud/admin.html')
            else:
                return render(request, 'crud/index.html')
    else:
         return render(request, 'crud/invalid.html')
		
def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.save()
    return redirect('/crud/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/')

def pdelete(request, id):
    p = Products.objects.get(id=id)
    p.delete()
    return render(request, 'crud/admin.html')
	
def pcartdelete(request, id):
    m= Cart.objects.get(id=id)
    m.delete()
    
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'crud/index.html', context)

def pcart(request, id):
    p = Products.objects.get(id=id)
    now = datetime.datetime.now()
    c = Cart(cust_id='Saurav', pid=id,name=p.name,price=p.price,color=p.color,image=p.image,img=p.img,picture=p.picture,pic=p.pic,pica=p.pica,category=p.category,description=p.description,engine=p.engine, displacement=p.displacement, power=p.power, drivetrain=p.drivetrain, fuel_tank_capacity=p.fuel_tank_capacity, airbags=p.airbags, dt=now)
    c.save()
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'crud/index.html', context)
	
def scart(request, id):
    products = Products.objects.get(id=id)
    context = {'products': products}
    return render(request, 'crud/scart.html', context)
	
	
def paybill(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'crud/paybill.html', context)
	
def addbill(request):
    products = Cart.objects.all()
    gross = 0
    for row in products:
      gross = gross + (int(row.price))
    con = {'gross': gross}
    context = {'products': products,'gross':gross}
    return render(request, 'crud/addbill.html', context)

def show_cars(request):
    p = Products.objects.all()
    context = {'products': p}
    return render(request, 'crud/show_cars.html',context)
	   
def viewcart(request):
    products = Cart.objects.all()
    gross = 0
    for row in products:
      gross = gross + (int(row.price))
    con = {'gross': gross}
    context = {'products': products,'gross':gross}
    return render(request, 'crud/viewcart.html', context)
	


	