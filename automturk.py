import boto3

aws_access_key_id = ""
aws_secret_access_key = ""
region_name = "us-east-1"
endpoint_url = "https://mturk-requester-sandbox.us-east-1.amazonaws.com"


client = boto3.client('mturk',
                     endpoint_url=endpoint_url,
                     region_name=region_name,
                     aws_access_key_id=aws_access_key_id,
                     aws_secret_access_key=aws_secret_access_key
                     )

print(client.get_account_balance()['AvailableBalance'])
print("Creating a new HIT")

question = open("questions.xml", "r").read()
new_hit = client.create_hit(
    Title='Classify the next image',
    Description='Choose the correct category',
    Keywords='classify, images, labeling',
    Reward='0.15',
    MaxAssignments=1,
    LifetimeInSeconds=172800,
    AssignmentDurationInSeconds=600,
    AutoApprovalDelayInSeconds=14400,
    Question=question,
)

print("A new HIT has beed created. You can preview it here:")
print("https://workersandbox.mturk.com/mturk/preview?groupId="+new_hit['HIT']['HITGroupId'])
print("HITID=  %s (Use to Get Results", new_hit['HIT']['HITId'])
