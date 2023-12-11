import boto3


class CreateBotoObj:
    def __init__(self):
        self.aws_access_key_id='ASIASODG2OMI3JRY4OVX'
        self.aws_secret_access_key='LPvxfseHzCFzQt7Y0zJMUS9yM0QpfmjM1FpnOlbN'
        self.aws_session_token='FwoGZXIvYXdzEJ3//////////wEaDBz1aRNU5xV6qIVILiLLAez5QAFCRdWDAaYeegn1Z3nZNjIm7w62M4wa75jweZ0Wg/GqZPcekvpNcXCkOoukxCqW1wmWzaqkyYZfR4KVZwnjl6VuXcsJTtWez/HSM39JJd9SgBfgPm4JS+BgFwoNV7rEqrPf3PLvQ3On4zvVufIEt/TzxnpDQYr0AqaY4TAQqXrl+ds7ASfnZxy/dIb5aLbM2tyCr9Wz3f9Ynq/MGZG0Jb7Ke7vgwKmoJdvhj85ZWqE9GIU4sYVmOC0/QdlQUhQ3heQAAVcEeMAYKLia2KsGMi3z6OpIl3eWru1BGIqFr571I/acDBtcAjwOtvsAbqsFRDDlyj3dy7MmJau4XCw='
        self.session = boto3.session.Session(aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key, aws_session_token=self.aws_session_token)
        
    def boto3_obj_client(self, service):
        obj = self.session.client(service, region_name='us-east-1')
        return obj
    
    def boto3_obj_resource(self, service):
        obj = self.session.resource(service, region_name='us-east-1')
        return obj