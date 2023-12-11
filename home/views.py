from django.shortcuts import render, redirect
from booktable.models import Booktable
from create_boto_obj import CreateBotoObj

boto3_obj = CreateBotoObj()

# Create your views here.
def home(request):
    return render(request, 'home.html')

def booktable(request):
    reservation = Booktable.object.all()
    return render(request, 'booktable/booktable.html', {"booktables":reservation})

def aboutus(request):
    return render(request, 'aboutus.html')

def send_updates(self):
    print('send_updates')
    s3_obj = boto3_obj.boto3_obj_resource('s3')
    s3_obj.Bucket('bookbistro-22216456').download_file(Key='SNSemailtemplate/snstemplate.txt', Filename='snstemplate.txt')
    
    sns_obj = boto3_obj.boto3_obj_client('sns')
    arn = 'arn:aws:sns:us-east-1:167719367441:bookbistro'
    subject = 'Updates from BookBistro'
    with open('snstemplate.txt') as f:
        data = f.read()
        
    sns_obj.publish(TopicArn=arn, Subject=subject, Message=data)
    return redirect('aboutus')