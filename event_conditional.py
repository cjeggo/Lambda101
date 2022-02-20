import json

def lambda_handler(event, context):
    myEvent = json.dumps(event, indent=2)
    print('Received event: ' + myEvent)
    if 'Lambda' in myEvent:
        print("We love Lambda really")
    else:
        print("The world is on fire! Do something else!")