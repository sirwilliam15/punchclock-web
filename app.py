from flask import Flask, request
from flask_api import status
#from flask_restful import Resource, Api, reqparse
import pymysql, re
from math import floor

API_VERSION = 1
API_PATH = '/app/timeclock/api/v%d'%API_VERSION
app = Flask(__name__)
regx = r'-|\'|"|\t|\r|'

class AuthenticationError(Exception):
    def __init__(self, message):
        super().__init__(message)

def auth():
    
    try:
        user = request.authorization['username']
        user = re.sub(regx, '', user)
        passwd = request.authorization['password']
        passwd = re.sub(regx, '', passwd)
    except TypeError:
        raise AuthenticationError('Authentication Failed')
    q = '''SELECT * FROM users 
    WHERE username=%s and password=%s;'''%(user, passwd)
    return user

@app.route('%s/'%API_PATH, methods=['GET'])
def home():
    return 'Timeclock API Version %d'%API_VERSION


@app.route('%s/timecards'%API_PATH, methods=['GET'])
def get_timecards():
    # authentication

    # get parameters
    # - username
    try:
        username = auth()
    except AuthenticationError as e:
        return e, status.HTTP_403_FORBIDDEN

    # - page start (increments of 10 per page)
    start = request.args.get('pageStart')
    if start == None:
        limit = '10'
    elif int(start) < 10:
        limit = '10'
    else:
        s = floor(int(start)/10) * 10
        e = s + 10
        limit = '%d, %d'%(s, e)

    q = '''SELECT date,in,out 
    FROM timecards 
    WHERE username=%s
    limit %s;'''%(username, limit)
    # SQL query

    # return results
    return q

@app.route('%s/punch'%API_PATH, methods=['POST'])
def punch():
    username = auth()

    # get parameters
    # - username
    # - time

    # get timecard id
    # SQL query
    q = '''SELECT id
    FROM timecards
    WHERE username=%s and open=true;'''%username

    if _id is None:
        q = '''INSERT INTO timecards'''
    else:
        q = '''UPDATE timecards
        SET out = NOW(), open = false
        WHERE id = %s;'''%_id

    # execute query

    # return status
    return q

if __name__ == "__main__":
    app.run()