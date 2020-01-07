from converter import *
from command import *


def handler(input, context):
    credentialsJsonString = convertCredentialsToJson(
        input.get('recordLocator'),
        input.get('firstName'),
        input.get('lastName')
    )
    cronExpression = convertDateToCronExpression(input.get('dateTimeUTC'))
    credentialsUpdated = run_command(
        '/opt/aws events put-targets --rule FlightTimeRule --targets Id="1",' + \
        'Arn="arn:aws:lambda:us-east-2:062130427086:function:southwest-checkin",' + \
        'Input="' + credentialsJsonString + '"'
    )
    checkinScheduled = run_command(
        '/opt/aws events put-rule --name FlightTimeRule --schedule-expression ' + cronExpression
    )
    if credentialsUpdated and checkinScheduled:
        return {
            'statusCode': 200,
            'body': 'Checkin preparations complete.'
        }
    else:
        return {
            'statusCode': 500,
            'body': 'An error occurred.'
        }
