import re

def organize_presets():
    # print("Hello world!!!!!!!!!")
    # test/vst3-bx_console Focusrite SC.ini
    print("### read a file")
    f = open("test/vst3-bx_console Focusrite SC.ini", "r") # r = readonly
    # print(f.read()) # success
    lines = f.readlines()
    # print(lines[1])
    f2 = open("test/test.txt", "w") # w = create or overwrite
    for line in lines:
        # tempstr = line.replace("[Preset", "[EditedPreset")
        obj_mutch = re.search(r'\[Preset\d+\]', line)
        tempstr = ""
        if obj_mutch:
            tempstr = obj_mutch.group() + "\r" # Preset03
            tempstr = tempstr.replace("Preset", "pre")
        else:
            tempstr = line
        f2.write(tempstr) # success

    f.close()
    f2.close()

organize_presets()
