import re

def get_header(lines):
    tempstr = ""
    for line in lines:
        if line.find("[Preset") < 0:
            tempstr = tempstr + line
        else:
            return tempstr

def organize_presets():
    # print("Hello world!!!!!!!!!")
    # test/vst3-bx_console Focusrite SC.ini
    print("### read a file")
    f = open("test/vst3-bx_console Focusrite SC.ini", "r") # r = readonly
    # print(f.read()) # success
    lines = f.readlines()
    presets = {}
    tempstr = ""
    # print(lines[1])
    f2 = open("test/test.txt", "w") # w = create or overwrite
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

    f.close()
    f2.close()


organize_presets()
