import shutil
import os 
from datetime import datetime

wd = os.getcwd()
now = datetime.now()
timestamp = str(now.strftime("%Y%m%d"))
filename = "homework_" + timestamp
shutil.copy(wd+"/homework_data.csv", wd+"/backups/{}.csv".format(filename))