import logging
from datetime import datetime

fmt = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.INFO, format=fmt)

# update_ver = input('What version is it?: ')
# update_info = input('What did you update?: ')

# f = open("readme.txt", "r")
with open("readme.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)

# f.close()