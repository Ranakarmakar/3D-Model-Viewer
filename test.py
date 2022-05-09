credentials = {
    "apikey": "GzO_sSx_zYUJy5kkP7PB0oMy1kHR5nOSNWQyL0O8tDHJ",
    "endpoints": "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
    "iam_apikey_description": "Auto-generated for key crn:v1:bluemix:public:cloud-object-storage:global:a/2dd3f82b131e4c2e96630606947f4bae:b7366f45-94d2-45c4-8603-5315022b5fed:resource-key:68d3e6a5-7492-4200-9dc0-36f808483f9f",
    "iam_apikey_name": "cloud-object-storage-xh-cos-standard-7x7",
    "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer",
    "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/2dd3f82b131e4c2e96630606947f4bae::serviceid:ServiceId-af88c7bf-178c-44dc-83f0-e71ed305da12",
    "resource_instance_id": "crn:v1:bluemix:public:cloud-object-storage:global:a/2dd3f82b131e4c2e96630606947f4bae:b7366f45-94d2-45c4-8603-5315022b5fed::"
}
from ibm_botocore.client import Config
import ibm_boto3


def download_file_cos(credentials, local_file_name, key):
    cos = ibm_boto3.client(service_name='s3',
                           ibm_api_key_id=credentials['apikey'],
                           ibm_service_instance_id=credentials['IAM_SERVICE_ID'],
                           ibm_auth_endpoint=credentials['IBM_AUTH_ENDPOINT'],
                           config=Config(signature_version='oauth'),
                           endpoint_url=credentials['ENDPOINT'])
    try:
        res = cos.download_file(Bucket=credentials['BUCKET'], Key=key, Filename=local_file_name)
    except Exception as e:
        print(Exception, e)
    else:
        print('File Downloaded')
