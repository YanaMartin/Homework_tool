import shutil
import os 
from datetime import datetime

now = datetime.now()
timestamp = str(now.strftime("%Y%m%d"))
filename = "homework_" + timestamp
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
os.makedirs('backups', exist_ok=True)
shutil.copy("homework_data.csv", os.path.join("backups","{}.csv".format(filename)))