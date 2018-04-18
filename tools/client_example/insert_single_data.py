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

timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")
db = client.repltestdb
test_doc = { "key": "timestamp", "value": timestamp }

print "@@@ Insert single data..."
db.testcol01.insert_one(test_doc)
data_count = db.testcol01.find({}).count()
print "count = %s" % data_count

print "Done!"
