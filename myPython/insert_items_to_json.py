#!/usr/bin/env python
import json
from collections import OrderedDict
chassis_spec_jsons=["clst_spec.json","cx1200_spec.json","dtc_spec.json",
"fmx_spec.json","itc_spec.json","mtc6_spec.json","mtc9_spec.json",
"otc_spec.json","xt3300_spec.json","xt3600_spec.json","xtc2e_spec.json",
"xtc2_spec.json","xtc4_spec.json","xtc_spec.json"]

board_spec_jsons=["clst_boards_spec.json","cx1200_boards_spec.json","dtc_boards_spec.json",
"fmx_boards_spec.json","itc_boards_spec.json","otc_boards_spec.json","xt3600_boards_spec.json",
"xtc2_boards_spec.json","xtc_boards_spec.json"]


file_list=["xtc_spec.json", "xtc4_spec.json", "xtc2_spec.json", "xtc2e_spec.json", "mtc6_spec.json",\
           "mtc9_spec.json", "itc_spec.json", "fmx_spec.json", "dtc_spec.json", "otc_spec.json"]

path = "D:\\myPython\\old_json\\"

new_path = "D:\\myPython\\new_json\\"

def update_chassis_spec_jsons():
    '''
    insert new items to chassis spec json, or change the items' order
    '''
    for json_file in file_list:
    # for json_file in ["fmx_spec.json"]:
        file_path = path + json_file
    #     json_obj = IJSON(file_path)
    #     json_dict = json_obj.read()
        origal_dic = open(file_path, "r").read()
        json_dict = json.loads(origal_dic)
        new_json_dic=[]
        for d in json_dict:
            boards_list=[]
            for board in d["Boards"]:
                if "slot_num" in board:
                    board["slot_id"]=board["slot_num"]
                if d["Category"]=="ITC" or d["Category"] == "MTC9" or d["Category"]=="MTC6":
                    board["slot_id"] = str("%x" %(int(board["slot_num"], 16) - 70))
                listitems=[("board_spec_name",board["board_spec_name"]), ("slot_num",board["slot_num"]), \
                           ("slot_id",board["slot_id"])]
                if "no_of_slots" in board:
                    listitems.append(("no_of_slots", board["no_of_slots"]))
                if "is_mandatory" in board:
                    listitems.append(("is_mandatory", board["is_mandatory"]))
                if "present_bit" in board:
                    listitems.append(("present_bit", board["present_bit"]))
                listitems.append(("aid", board["aid"]))
                ord_board = OrderedDict(listitems)
                boards_list.append(ord_board)
            new_d = OrderedDict([("Category", d["Category"]), ("BackupName",d["BackupName"]),\
                                ("Flag",d["Flag"]), ("Boards",boards_list)])
            new_json_dic.append(new_d)
    #     print new_json_dic
        #dump json dict to str
        json_file_str=json.dumps(new_json_dic, skipkeys=True, indent=3)
        # write json str to json_file
        fname = new_path + json_file
        fobj=open(fname, 'w')
        fobj.write(json_file_str)
        fobj.close()

def update_board_spec_jsons():
    '''
    insert new items to board spec jsons
    '''
    for json_file in board_spec_jsons:
        if json_file == "cx1200_boards_spec.json":
            continue
        file_path = path + json_file
        origal_json_dict = json.loads(open(file_path, "r").read())
        new_json_dic = []
        for d in origal_json_dict:
            entry_list = []
            for entry in d["Entries"]:
                listitems = [("EntryName", entry["EntryName"]), ("Editable", entry["Editable"])]
                if "Values" in entry:
                    listitems.append(("Values", entry["Values"]))
                if "ValueNames" in entry:
                    listitems.append(("ValueNames", entry["ValueNames"]))
                listitems.append(("DefaultValue", entry["DefaultValue"]))
                if "BoardSubType" in entry:
                    listitems.append(("BoardSubType", entry["BoardSubType"]))
                listitems.extend([("Flag", entry["Flag"]),("Type", entry["Type"])])
                if "AllowOverride" in entry:
                    listitems.append(("AllowOverride", entry["AllowOverride"]))

                entry_list.append(OrderedDict(listitems))

            listitems = [("EntryName", "VIBoot"), ("Editable", "True"), ("DefaultValue", "none"),
                         ("Flag", "R.I"), ("Type", "str")]
            entry_list.append(OrderedDict(listitems))

            new_dict = OrderedDict([("Category", d["Category"]), ("BackupName", d["BackupName"]),
                                    ("Flag", d["Flag"]), ("CpuRsv", d["CpuRsv"]), ("CpuLimit", d["CpuLimit"]),
                                    ("MemSize", d["MemSize"]), ("MemRsv", d["MemRsv"]), ("MemLimit", d["MemLimit"]),
                                    ("OS", d["OS"]), ("Entries", entry_list)])
            new_json_dic.append(new_dict)

        json_file_str = json.dumps(new_json_dic, skipkeys=True, indent=3)
        # write json str to json_file
        fname = new_path + json_file
        fobj=open(fname, 'w')
        fobj.write(json_file_str)
        fobj.close()
    print "success"


if __name__=="__main__":
    update_board_spec_jsons()
