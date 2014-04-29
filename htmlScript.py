# Instructions 
# Create a folder with all of your default icons and an info.plist
# Add all of your HTML files
# Note you do not need a ContentSpec the script will generate one for you
# Add this script to your bundle
# Open terminal and cd into bundle
# Type python htmlScript.py and hit enter
# A ContentSpec.json will appear in your bundle
# Now run xcode

import os
import json
import glob
import subprocess
import sys
import datetime

#Array that holds paths to html files
htmlFiles = []

#ContentSpec object
ContentSpec = {}

#Array that holds each page name
pageNamesArray = []

#variable that holds the path of the bundle to remove from paths to html files 
localPath = os.getcwd()+'/'

#ContentSpec
ContentSpec = {
	"animations": {},
	"actions": {},
	"metaData": {
		"applicationStartPage": "App_Pages",
		"flurryAPIKey": "",
		"shortTitle": "",
		"startPage": "App_Pages",
		"title": "",
		"_version": "",
		"_checkLogin": 1,
		"_applicationLoginPage": "",
		"serverPaths": {}
	},
	"overlays": {
	},
	"pageSets": {
		"App_Pages": {
			"pages": [],
			"transitionDuration": "0.5",
			"transitionTypeNext": "slide",
			"transitionTypePrevious": "slideBack"
		}
	},
	"pages": {
	},
	"screenSupport": {
		"screens": [
			{
				"fonts": [
					{
						"fontName": "georgia",
						"fontSize": 14,
						"name": "Normal"
					}
				],
				"height": 768,
				"orientation": "landscape",
				"suffix": "",
				"width": 1024
			}
		],
		"useScreenRatio": "true"
	}
}

#Variable that holds path to folder user drags into input without white space
root = localPath

#Loop to find all html files
for r,d,f in os.walk(root):
    for files in f:
        if files.endswith(".html"):
        	 htmlFiles.append(os.path.join(r,files).lstrip(localPath))

#ContentSpec template 
for key in ContentSpec:
	if key == 'overlays':
		ContentSpec[key]["webview"] = {
			"type": "webview",
			"url": "",
			"x": "50%",
			"y": "50%",
			"width": "100%",
			"height": "100%",
			"horizontalAlign": "center",
			"verticalAlign": "center",
			"scaleToFit": "true",
			"bouncesDisabled": "true"
		}

#Loop to create pages for each html file
for key in ContentSpec:
	if key == 'pages':
		for index,item in enumerate(htmlFiles):
			ContentSpec[key]['Page'+str(index)] = {
				"frames": [],
				"overlays": [
					{
						"overlayId": "webview",
						"url": htmlFiles[index]
					}
				],
				"thumbnail": "Page001-toc.png",
				"transitionTypeForward": "pageFlip",
				"backgroundColor": "#ffffff",
				"title": "Page 1"
			}

#Loop add page names to pageNamesArray
for key in ContentSpec:
	if key == 'pages':
		for pageNames in ContentSpec[key]:
			pageNamesArray.append(pageNames)
pageNamesArray.sort()

#Loop to create pageset
for key in ContentSpec:
	if key == 'pageSets':
		for i in ContentSpec[key]:
			for j in ContentSpec[key][i]:
				if j == 'pages':
					for x in pageNamesArray:
						ContentSpec[key][i][j].append(x)

json_file = open('ContentSpec.json', "w")
json_file.write(json.dumps(ContentSpec, indent=4, sort_keys=True))
json_file.close()


