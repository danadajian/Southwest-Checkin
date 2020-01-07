import datetime


def convertDateToCronExpression(dateTimeUTC):
    dateTimeObj = datetime.datetime.strptime(dateTimeUTC, '%a, %d %b %Y %H:%M:%S %Z')
    return 'cron(' + \
           str(dateTimeObj.minute) + " " + \
           str(dateTimeObj.hour) + " " + \
           str(dateTimeObj.day) + " " + \
           str(dateTimeObj.month) + \
           " ? " + \
           str(dateTimeObj.year) + ')'


def convertCredentialsToJson(recordLocator, firstName, lastName):
    return '{\\"recordLocator\\":\\"' + recordLocator + \
           '\\",\\"firstName\\":\\"' + firstName + \
           '\\",\\"lastName\\":\\"' + lastName + '\\"}'
