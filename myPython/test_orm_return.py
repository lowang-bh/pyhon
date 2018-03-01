import json

file_list=["xtc_spec.json", "xtc4_spec.json", "xtc2_spec.json", "xtc2e_spec.json", "mtc6_spec.json",\
           "mtc9_spec.json", "itc_spec.json", "fmx_spec.json", "dtc_spec.json", "otc_spec.json"]
path = "/opt/infinera/etc/json/"
new_path ="/opt/infinera/json/"
from collections import OrderedDict
for file in file_list:
# for file in ["fmx_spec.json"]:
    file_path = path + file
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
    #write json str to file
    fname= new_path + file
    fobj=open(fname, 'w')
    fobj.write(json_file_str)
    fobj.close()








ite = get_subslot_tbl_by_vm("OTM 2-A-1")

# tim_list=get_all_tim_spec_tbls()
# tim1=tim_list[1].name
# 
# for item in tim_list:
#     print item
#     
# for item in tim_list:
#     print item.name
#     
# for item in tim_list:
#     print item.maxPortNum