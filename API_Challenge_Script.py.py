import urllib
import json
import datetime

"""
Code2040 Technical Assessment API Challenge
Author: Diana Martschenko
Date: August 19 2016
"""

def step1():
    """
    Step1 sends an HTTP post request to the API challenge endpoint. The post parameters
    include the API token and a github repo url. The response is then
    printed out.
    """
    params = urllib.urlencode({'token': '981cfd31664bfc16a250c16622fe2b44',
                               'github':'https://github.com/diana1008/Code2040-API-Challenge.git'})
    response = urllib.urlopen("http://challenge.code2040.org/api/register", params)
    print response.read()

def step2():
    """
    Step2 sends an HTTP post request to the API challenge endpoint and received a string in
    the reponse. The string is then reversed and sent back to the endpoint via another post
    request. The response is then printed out.
    """
    params = urllib.urlencode({'token': '981cfd31664bfc16a250c16622fe2b44'})
    response = urllib.urlopen("http://challenge.code2040.org/api/reverse", params)
    reversed = response.read()[::-1]
    params = urllib.urlencode({'token': '981cfd31664bfc16a250c16622fe2b44', 'string': reversed})
    response = urllib.urlopen("http://challenge.code2040.org/api/reverse/validate", params)
    print response.read()

def step3():
    """
    Step3 sends a post request to the API challenge endpoint and retrieves a dictionary containing
    two key,value pairs; an array of strings and a string to look for within the array.
    The index of the string to look for is then found and sent back to the API challenge endpoint
    through a post request.
    """
    params = urllib.urlencode({'token': '981cfd31664bfc16a250c16622fe2b44'})
    response = urllib.urlopen("http://challenge.code2040.org/api/haystack", params)
    dict = json.loads(response.read())
    haystack = dict['haystack']
    index = haystack.index(dict['needle'])
    params = urllib.urlencode({'token': '981cfd31664bfc16a250c16622fe2b44', 'needle': index})
    response = urllib.urlopen("http://challenge.code2040.org/api/haystack/validate", params)
    print response.read()

def step4():
    """
    Step4 sends an HTTP post request to the API challenge endpoint and an an array
    and prefix is returned in the response. All words in the array that do not start with the
    prefix are appended to a list which is then sent back to the end point through another
    post request.
    """
    params = urllib.urlencode({'token': '981cfd31664bfc16a250c16622fe2b44'})
    response = urllib.urlopen("http://challenge.code2040.org/api/prefix", params)
    dict = json.loads(response.read())
    prefix = dict['prefix']
    array = dict['array']
    noPrefix = []
    for word in array:
        if not word.startswith(prefix):
            noPrefix.append(word)
    params = urllib.urlencode({'token': '981cfd31664bfc16a250c16622fe2b44', 'array[]': noPrefix}, True)
    response = urllib.urlopen("http://challenge.code2040.org/api/prefix/validate", params)
    print response.read()

def step5():
    """
    Step5 sends an HTTP post request to the API challenge endpoint and receives an ISO
    formatted date stamp and an interval of secondsto add the to date stamp. The date stamp
    is parsed into a date object using the python datetime library, and the interval is converted
    into a timedelta which can then be added to the new date object. The new date is converted
    back to the original ISO format and sent back to the endpoint via another post request.
    """
    params = urllib.urlencode({'token': '981cfd31664bfc16a250c16622fe2b44'})
    response = urllib.urlopen("http://challenge.code2040.org/api/dating", params)
    dict = json.loads(response.read())
    date = dict['datestamp']
    dateObj = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    interval = dict['interval']
    newDate = dateObj+ datetime.timedelta(seconds=interval)
    isoNewDate= newDate.isoformat()+"Z"
    params = urllib.urlencode({'token': '981cfd31664bfc16a250c16622fe2b44', 'datestamp': isoNewDate})
    response = urllib.urlopen("http://challenge.code2040.org/api/dating/validate", params)
    print response.read()

def main():
    step1()
    step2()
    step3()
    step4()
    step5()
main()