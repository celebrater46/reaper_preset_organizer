import re
import os
import logging
from datetime import datetime

BACKUP_DIL = "backup"
BACKUP_MAX = 50

fmt = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.INFO, format=fmt)
# logging.info('Hello World.')

def output_log(log_type, msg):
    print(msg)
    if log_type == "info":
        logging.info(msg)
    elif log_type == "error":
        logging.error(msg)
    else:
        logging.critical("Failed to output the log file.")

#     fmt = "%(asctime)s - %(levelname)s - %(message)s"
#     logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.INFO, format=fmt)
#     logging.info('Hello World.')

    # logging.debug('Debug')
    # logging.info('Informarion')
    # logging.warning('Warning')
    # logging.error('Error')
    # logging.critical('Critical')

def get_backup(file_name, lines):
    now = datetime.now()
    datestr = now.strftime("%Y%m%d%H%M%S")
    f = open(f"{BACKUP_DIL}/bak-{datestr}-{file_name}.ini", "w")
    for line in lines:
        f.write(line)
    # logging.info(f'Backed up "{file_name}".')
    output_log("info", f'Backed up "{file_name}".')
    f.close()

def delete_backup():
    # dir_path = "mypackage21"
    file_names = [
        f for f in os.listdir(BACKUP_DIL) if os.path.isfile(os.path.join(BACKUP_DIL, f))
    ]
    print(file_names)

    files = len(file_names)
    if files > BACKUP_MAX:
        num = files - BACKUP_MAX
        for i in range(num):
            os.remove(f'{BACKUP_DIL}/{file_names[i]}')
            # logging.info(f'Deleted "{file_names[i]}".')
            output_log("info", f'Deleted "{file_names[i]}".')


def get_header(lines):
    tempstr = ""
    for line in lines:
        if line.find("[Preset") < 0:
            tempstr = tempstr + line
        else:
            return tempstr

def organize_presets(path, file_name):
    f = open(f"{path}{file_name}", "r") # r = readonly
    # print(f.read()) # success
    lines = f.readlines()
    get_backup(file_name, lines)
    f.close()

    presets = {}
    tempstr = ""
    # print(lines[1])
    f2 = open(f"{path}{file_name}", "w") # w = create or overwrite
    for line in lines:
        # tempstr = line.replace("[Preset", "[EditedPreset")
        obj_mutch = re.search(r'\[Preset\d+\]', line)
        if obj_mutch:
            tempstr = obj_mutch.group() + "\n" # Preset03
            # tempstr = tempstr.replace("Preset", "pre")
        elif line.find("Name=") > -1:
            preset_name = line.replace("Name=", "").replace("\n", "")
            presets[preset_name] = tempstr + line
            # tempstr = ""
        else:
            tempstr = tempstr + line
        # f2.write(tempstr) # success
    
    print(presets)
    presets_sorted = sorted(presets.items())
    print(presets_sorted)

    f2.write(get_header(lines))

    num = 0
    for preset in presets_sorted:
        converted_preset = re.sub(r'\[Preset\d+\]', f'[Preset{num}]', preset[1]) + "\n"
        f2.write(converted_preset)
        num += 1

    # f.close()
    f2.close()

def main():
    # print("Hello world!!!!!!!!!")
    # test/vst3-bx_console Focusrite SC.ini
    print("### read a file")
    f_target_path = open("target_path.ini", "r")
    f_target_files = open("target_files.ini", "r")
    target_path = f_target_path.readlines()
    target_files = f_target_files.readlines()
    for file in target_files:
        target = f"{target_path[0]}{file}"
        # organize_presets(target_path[0], file)
        # logging.info(f'Organized "{target}".')
        try:
            with open(target) as f:
                # print("ファイルが存在する")
                # print(f"target_path_0: {target_path[0]}")
                organize_presets(target_path[0], file)
                # logging.info(f'Organized "{target}".')
                output_log("info", f'Organized "{target}".')

        except FileNotFoundError:
            # print("ファイルが存在しません")
            # output_log("error", f"{target_path}{target_files} does not exists.")
            # tempstr = f"{target} does not exists."
            # print(tempstr)
            # logging.error(tempstr)
            output_log("error", f"{target} does not exists.")

def test():
    f = open("test/test.txt", "r")
    lines = f.readlines()
    get_backup("test", lines)
    f.close()

# organize_presets()

# output_log()
# test()
# delete_backup()
main()