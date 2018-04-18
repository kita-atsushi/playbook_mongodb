from pymongo import MongoClient, WriteConcern, InsertOne
from pymongo.errors import BulkWriteError
from pprint import pprint
from datetime import datetime
import ConfigParser
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

inifile = ConfigParser.SafeConfigParser()
inifile.read( SCRIPT_DIR + '/client.ini')
mongo_url = inifile.get('con', 'mongo_url')
max_data_num = int(inifile.get('insert', 'bulk_max_count'))
wtime_out_millsec = int(inifile.get('insert', 'w_concern_repl_timeout_milisec'))
write_concern_opt = inifile.get('insert', 'w_concern_opt')

client = MongoClient(mongo_url)
timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S%f")
db = client.repltestdb

print "@@@ Inserting bulk data %s with write_concern ..." % (max_data_num)
coll = db.get_collection(
	'testcol01', write_concern=WriteConcern(w=write_concern_opt, wtimeout=wtime_out_millsec))
try:
    coll.bulk_write([InsertOne({"timestamp": timestamp, 'id': i}) for i in range(max_data_num)])
    print "OK."

except BulkWriteError as bwe:
     pprint(bwe.details)

data_count = db.testcol01.find({}).count()
print "count = %s" % data_count

print "Done!"
