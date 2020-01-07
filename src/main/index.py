from converter import *
from command import *


def handler(input, context):
    cronExpression = convertDateToCronExpression(input.get('dateTimeUTC'))
    credentialsJsonString = convertCredentialsToJson(
        input.get('recordLocator'),
        input.get('firstName'),
        input.get('lastName')
    )
    run_command('/opt/aws events put-rule --name FlightTimeRule --schedule-expression ' + cronExpression)
    run_command(
        '/opt/aws events put-targets --rule FlightTimeRule --targets Id="1",' + \
        'Arn="arn:aws:lambda:us-east-2:062130427086:function:southwest-checkin",' + \
        'Input="' + credentialsJsonString + '"'
    )
