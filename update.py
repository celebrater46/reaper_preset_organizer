# 管理用
import logging
from datetime import datetime

fmt = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.INFO, format=fmt)

def get_lines():
    f = open("readme.txt", 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    return lines

def update_note():
    lines = get_lines()
    f2 = open("readme.txt", 'w', encoding='utf-8')
    for line in lines:
        if line.find("バージョン情報") > -1:
            f2.write(line)
            now = datetime.now()
            datestr = now.strftime("%Y-%m-%d %H:%M:%S")
            allstr = f"{datestr} - v{update_ver}: {update_info}"
            f2.write(f"{allstr}\n")
            logging.info(f"Updated a release note [{allstr}]")
        else:
            f2.write(line)
    f2.close()

update_ver = input('What version is it?: ')
update_info = input('What did you update?: ')
update_note()
