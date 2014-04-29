#This script parses the ActemeraRedesign.json file and looks for the text property and replaces it with and html property

import os
import json
import glob
import subprocess
import sys
import datetime


timestamp = str(datetime.datetime.now())

files = []
textOverlaysObject = []
textOverlays = []
textOverlayContent = []
studioJson = {}

jsonFile = raw_input("Drag your JSON file here: ")

root = os.path.dirname(os.path.abspath(jsonFile))

for dirpath, dirnames, filenames in os.walk(root):
    for fname in filenames:
        if fname.endswith(".json"):
            path = os.path.join(dirpath,fname)
            files.append(path)

for f in files:
    log = open(f)
    json_data = json.load(log)
    log.close()
    for i in json_data:
        if i == 'overlays':
            for key in json_data['overlays']:
                for subKey in json_data['overlays'][key]:
                    if subKey == "text":
                        textOverlays.append(str(key))
                        textOverlayContent.append(str(json_data['overlays'][key][subKey]))
                        textOverlaysObject.append({str(key):str(json_data['overlays'][key][subKey])})


for i in textOverlaysObject:
    for key in i:
        studioJson[key] = {
            "bouncesDisabled": "true",
            "height": "90px",
            "horizontalAlign": "center",
            "html": "<!DOCTYPE HTML><html><head><style type=\"text/css\" media=\"screen, print\"></style></head><body style=\"margin:0;padding:0;line-height:normal;\"><div style=\"text-align: center;\"><font face=\"verdana, arial, helvetica, sans-serif\"><span style=\"font-size: 40px;\">" + i[key] + "</span></font></div>\n</body></html>",
            "relative": "screen",
            "type": "webview",
            "verticalAlign": "center",
            "width": "400px",
            "x": "50%",
            "y": "50%"
        }
#print studioJson

json_file = open('studioText.json', "w")
json_file.write(json.dumps(studioJson, indent=4, sort_keys=True))
json_file.close()

'''json_file = open('textOverlays.json', "w")
json_file.write(json.dumps(textOverlaysObject, indent=4, sort_keys=True))
json_file.close()'''


#print textOverlays

#print textOverlayContent

#print textOverlaysObject

#print len(textOverlays)




#print os.path.basename('ContentSpec.json')
#print os.path.abspath('ContentSpec.json')
#print os.path.dirname(var)




