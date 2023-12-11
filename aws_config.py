[12:29 AM] Dipesh Vilasrao Badgujar
import boto3
from botocore.exceptions import ClientError
 
class AwsConfig:
    def __init__(self,service,region_name="us-east-1"):
        self.region_name = region_name
        self.aws_access_key_id = "ASIASODG2OMIURKIHZGG"
        self.aws_secret_access_key = "Sj12GbfweClstlhmCxlpeSupjhk4dPDK49A3a3G4"
        self.aws_session_token = "FwoGZXIvYXdzEPr//////////wEaDObw5s+nylbQlMK//SLLATD3SZ8mQWEF2eyAtiUIRPFofAOXapWQXeM4QutThfyszxVy/+8CD25c1eTTTJ8O0xGBNmkWezH7Bt088nPMrZAAfuZqHqhN4dbeBs3LeUgb7iZRv3QS5Ur3Fi/BszBS042gFw2AlfNlXdkBBQI5Hok/fE+Pj9ouEo/ggouPS5iWejPsEVpTrbEiGkseZz/m05YNVh1/P5seq0bT7cb6yAwCmqSe6iOO+B0b6vI9rQWZqejeIgh/VbYc2gP+RIa0cKYu6+tJlAQPXeKQKKC8tKsGMi3fN1Z9wzi22vQ1bWTxANRcL9Dz/G5125dhyl7v1/2Yclk7L/Ieq9+fp/whDw0="
 
        session = boto3.session.Session(aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key, aws_session_token=self.aws_session_token)
        self.client = session.client(service_name=service, region_name=self.region_name)
       
        self.resource = session.resource(service_name=service, region_name=self.region_name)
   
 
    def boto3_client(self):
        return self.client
    def boto3_resource(self):
        return self.resource