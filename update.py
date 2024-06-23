import logging
from datetime import datetime

fmt = "%(asctime)s: %(message)s"
logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.INFO, format=fmt)

update_ver = input('What version is it?: ')
update_info = input('What did you update?: ')

f = open("readme.txt", 'r', encoding='utf-8')
lines = f.readlines()
f.close()

f2 = open("readme.txt", 'w', encoding='utf-8')
for line in lines:
    if line.find("バージョン情報") > -1:
        f2.write(line)
        now = datetime.now()
        datestr = now.strftime("%Y-%m-%d %H:%M:%S")
        f2.write(f"{datestr} - v{update_ver}: {update_info}\n")
    else:
        f2.write(line)
f2.close()
