import re
import os
import logging
from datetime import datetime

BACKUP_DIL = "backup"
BACKUP_MAX = 50

fmt = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.INFO, format=fmt)

def output_log(log_type, msg):
    print(msg)
    if log_type == "info":
        logging.info(msg)
    elif log_type == "error":
        logging.error(msg)
    else:
        logging.critical("Failed to output the log file.")

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
    output_log("info", f'Backed up "{file_name}".')
    f.close()

def delete_backup():
    file_names = [
        f for f in os.listdir(BACKUP_DIL) if os.path.isfile(os.path.join(BACKUP_DIL, f))
    ]
    print(file_names)

    files = len(file_names)
    if files > BACKUP_MAX:
        num = files - BACKUP_MAX
        for i in range(num):
            os.remove(f'{BACKUP_DIL}/{file_names[i]}')
            output_log("info", f'Deleted "{file_names[i]}".')


def get_header(lines):
    tempstr = ""
    for line in lines:
        if line.find("[Preset") < 0:
            tempstr += line
        else:
            break
    return tempstr

def escape_br(lines):
    new_lines = []
    for line in lines:
        new_lines.append(line.replace("\n", ""))
    return new_lines

def escape_backslash(dir):
    # print(dir)
    tempstr = str(dir)
    return tempstr.replace("\\", "/")

def add_final_slash(dir):
    if dir[-1:] == "/":
        return dir
    else:
        return f"{dir}/"

def get_path():
    f = open("target_path.ini", "r")
    lines = f.readlines()
    dir = escape_backslash(lines[0])
    dir = add_final_slash(dir)
    f.close()
    return dir

def get_file_names():
    f = open("target_files.ini", "r")
    file_names = f.readlines()
    file_names = escape_br(file_names)
    f.close()
    return file_names

def get_preset_dictionary(dir, lines):
    presets = {}
    tempstr = ""
    # f = open(dir, "r")
    # lines = f.readlines()
    for line in lines:
        obj_mutch = re.search(r'\[Preset\d+\]', line)
        if obj_mutch:
            tempstr = obj_mutch.group() + "\n" # Preset03
        elif line.find("Name=") > -1:
            preset_name = line.replace("Name=", "").replace("\n", "")
            presets[preset_name] = tempstr + line
        else:
            tempstr = tempstr + line
    # f.close()
    return presets

def rewrite_file(dir, header, presets):
    f2 = open(dir, "w") # w = create or overwrite
    # f2.write(get_header(lines))
    f2.write(header)
    num = 0
    for preset in presets:
        converted_preset = re.sub(r'\[Preset\d+\]', f'[Preset{num}]', preset[1]) + "\n"
        f2.write(converted_preset)
        num += 1
    f2.close()

def organize_presets(path, file_name):
    f = open(f"{path}{file_name}", "r") # r = readonly
    lines = f.readlines()
    get_backup(file_name, lines)
    f.close()

    presets = get_preset_dictionary(f"{path}{file_name}", lines) # get array of presets
    # presets = {}
    # tempstr = ""
    # f2 = open(f"{path}{file_name}", "w") # w = create or overwrite
    # for line in lines:
    #     obj_mutch = re.search(r'\[Preset\d+\]', line)
    #     if obj_mutch:
    #         tempstr = obj_mutch.group() + "\n" # Preset03
    #     elif line.find("Name=") > -1:
    #         preset_name = line.replace("Name=", "").replace("\n", "")
    #         presets[preset_name] = tempstr + line
    #     else:
    #         tempstr = tempstr + line
    
    presets_sorted = sorted(presets.items()) # reorder
    # f2 = open(f"{path}{file_name}", "w") # w = create or overwrite
    # f2.write(get_header(lines))
    # num = 0
    # for preset in presets_sorted:
    #     converted_preset = re.sub(r'\[Preset\d+\]', f'[Preset{num}]', preset[1]) + "\n"
    #     f2.write(converted_preset)
    #     num += 1
    # f2.close()
    header = get_header(lines)
    rewrite_file(f"{path}{file_name}", header, presets_sorted)

def reaper_preset_organizer():
    # f_target_path = escape_backslash(open("target_path.ini", "r"))
    # f_target_path = add_final_slash(f_target_path)
    # f_target_path = add_final_slash(f_target_path)
    # f_target_files = open("target_files.ini", "r")
    # print(f_target_path)
    # target_path = f_target_path.readlines()
    target_path = get_path()
    # target_files = escape_br(f_target_files.readlines())
    # target_files = escape_br(f_target_files.readlines())
    target_files = get_file_names()
    for file in target_files:
        target = f"{target_path}{file}"
        try:
            with open(target) as f:
                organize_presets(target_path, file)
                output_log("info", f'Organized "{target}".')

        except FileNotFoundError:
            output_log("error", f"{target} does not exists.")

def test():
    f = open("target_path.ini", "r")
    lines = f.readlines()
    dir = escape_backslash(lines[0])
    dir = add_final_slash(dir)
    print(dir)
    f.close()

# test()
reaper_preset_organizer()