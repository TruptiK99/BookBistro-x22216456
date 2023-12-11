from django.shortcuts import render,redirect
from .models import Booktable
from booktable.models import Booktable
from .forms import BooktableForm
from managebookings.models import Managebookings
from django.contrib.auth.models import User
from create_boto_obj import CreateBotoObj
from datetime import datetime
import requests
import json
from library import CustomLib

booktable_lib = CustomLib(Booktable)
user_lib = CustomLib(User)

boto3_obj = CreateBotoObj()

# Create your views here.
def booktable(request):
    data= Booktable.objects.all()
    return render(request,'booktable/booktable.html', {'booktable':data})


def delete_booktable(request,id):
    # data = Booktable.objects.get(id=id)
    data = booktable_lib.get_id_specific_data(id)
    data.delete()
    return redirect('booktable')
 
def booktable_form(request,id=0):
    if request.method=="GET":
        if id==0:
            a_form=BooktableForm()
            return render(request,'booktable/booktable_form.html', {'booktable_form':a_form})
        else:
            # data=Booktable.objects.get(id=id)
            data = booktable_lib.get_id_specific_data(id)
            a_form=BooktableForm(instance=data)
            return render(request,'booktable/booktable_form.html', {'booktable_form':a_form})
 
    if request.method=="POST":
        if id==0:
            a_form=BooktableForm(request.POST, request.FILES)
        else:
            # data=Booktable.objects.get(id=id)
            data = booktable_lib.get_id_specific_data(id)
            a_form=BooktableForm(request.POST, request.FILES, instance=data)
        if a_form.is_valid():
            a_form.save()
        print("invalid form", a_form.errors)
        return redirect('booktable')
    return render(request,'booktable/booktable_form.html')
 
def book_booktable(request,id):
    # data = booktable.objects.get(id=id)
    data = booktable_lib.get_id_specific_data(id)
    return render(request,'booktable/book_booktable.html', {'book_booktable':data})
 
def create_booktable(request,id):
    # table_id = Booktable.objects.get(id=id)
    # user = User.objects.get(id=request.user.id)
    table_id = booktable_lib.get_id_specific_data(id)
    user = user_lib.get_id_specific_data(request.user.id)
    book = Managebookings(user=user,table_id=table_id,booking_confirm=False)
    
    data = f'''
    User: {request.user.username}
    Table Id: {table_id.id}
    No of People: {table_id.no_of_people}
    Description: {table_id.description}
    '''
    
    with open('booking_data.txt', 'w') as f:
        f.write(data)
        
    s3_obj = boto3_obj.boto3_obj_resource('s3')
    date = datetime.now().strftime('%Y-%m-%d %H:%m')
    key = f'booking_details/{request.user.username}/booking_data-{date}.txt'
    s3_obj.Bucket('bookbistro-22216456').put_object(Key=key, Body=open('booking_data.txt', 'rb'))
    
    payload = {
        "email": request.user.email,
        "filename": key
        }
    
    
    headers = {
        'Content-Type':'application/json',
        'x-api-key': 'HfiuSrWkAf5BM7FOnCAXY2rLqgjTS4N84BuGHThP'
    }
    
    url = 'https://cs6yu3us0b.execute-api.us-east-1.amazonaws.com/bookbistro/bookbistro'
    
    res = requests.post(url, data=json.dumps(payload), headers=headers)
    print(res)
    book.save()
    return redirect('view_managebookings')