from pymongo import MongoClient
from pprint import pprint
from datetime import datetime
import ConfigParser
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


inifile = ConfigParser.SafeConfigParser()
inifile.read( SCRIPT_DIR + '/client.ini')
mongo_url = inifile.get('con', 'mongo_url')
client = MongoClient(mongo_url)

db = client.repltestdb
cursor = db.testcol01.find({})
for doc in cursor:
    print(doc)
