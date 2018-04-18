from pymongo import MongoClient
from datetime import datetime
import ConfigParser
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

inifile = ConfigParser.SafeConfigParser()
inifile.read( SCRIPT_DIR + '/client.ini')
mongo_url = inifile.get('con', 'mongo_url')
max_data_num = int(inifile.get('insert', 'bulk_max_count'))

client = MongoClient(mongo_url)
timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S%f")
db = client.repltestdb
print "@@@ Inserting bulk %s data..." % (max_data_num)
db.testcol01.insert_many([{"timestamp": timestamp, "id": i } for i in range(max_data_num)]).inserted_ids
print "OK."
data_count = db.testcol01.find({}).count()
print "count = %s" % data_count

print "Done!"
