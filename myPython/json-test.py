import json

class IJSON:
    """
    This class is used to convert a json file into a list of dictionaries
    """
    def __init__(self, path):
        """
        Path to the JSON file
        """
        self.path = path
        self.f = open(self.path, 'r')

    def read(self):
        """
        Returns a list of dictionaries
        """
        d = json.loads(self.f.read())
        
        return d
    
    def __del__(self):
        self.f.close()
#jsonFile =  "itc_boards_spec.json"        
jsonFile =  "tim_spec.json"        
json_obj = IJSON(jsonFile)
json_dict=json_obj.read()
for item in json_dict:
    print item
    if "portMap" in item:
        for shelf in item["portMap"]:
            print shelf
            print item["portMap"][shelf]
            slot ="11"
            if slot in item["portMap"][shelf]:
                print "slot:%s,slotname:%s" %(slot,item["portMap"][shelf][slot])
#     for item in board["subTypes"]:
#         for key in item:
#             print key, item[key][0],item[key][1]
            print "\n"

    