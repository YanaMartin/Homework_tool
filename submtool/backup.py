import shutil
from datetime import datetime

now = datetime.now()
timestamp = str(now.strftime("%Y%m%d"))
filename = "homework_" + timestamp
shutil.copyfile('homework_data.csv', './backups/{}.csv'.format(filename))