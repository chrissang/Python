#This script parses through JSON and finds anything with the extentions that are listed in the extensions array and removes the file from the folder if not called in the JOSN.

import os
import json
import glob
import subprocess
import sys
import datetime

rootBundleAssets = []
specAssets = []
tempRootBundleAssets = []
tempSpecAssets = ['Default-Landcape@2x.png', 'Default~iphone.png','Default-Landscape.png','Default-Landscape@2x~iphone.png','Default-Landscape~iphone.png','Default.png','Default@2x.png','Default@2x~iphone.png','Default~iphone','Icon-48.png','Icon-72.png','Icon-Newsstand.png','Icon-Small-50.png','Icon-Small.png','Icon-Small@2x.png','Icon.png','Icon@2x.png','iTunesArtwork','listOfRemovedAssets.txt']
filesToBeRemoved = []
xFilesToBeRemoved = []
extensions = ['.png','.jpeg','.jpg','.pvr','.mov','.mp4','.pdf','.html','.doc']


localPath = os.getcwd()+'/'
print localPath
def filterPath(asset):
	subprocess.call('svn delete --force '+ asset, shell=True)
	print 'svn delete --force '+ asset
			
def filterPathX(assetX):
	subprocess.call('svn delete --force '+ assetX + '@', shell=True)
	print 'svn delete --force '+ assetX + '@'
			
def svnCommit():
	subprocess.call("svn ci -m 'removed assets'", shell=True)
	print "svn ci -m 'removed assets'"

def cleanBundle(json_data):
	if "overlays" in json_data:
		for k,v in json_data['overlays'].iteritems():
			for i in json_data['overlays'][k]:
				if i == 'backgroundImage' or i == 'attachmentFile' or i == 'attachmentFilename' or i == 'attachmentImage' or i == 'shareImage' or i == 'file' or i == 'pagingIndicatorOff' or i == 'pagingIndicatorOn' or i == 'indicatorOffImage' or i == 'indicatorOnImage' or i == 'emitterFile' or i == 'maskImage' or i == 'buttonImage' or i == 'trackImage' or i == 'trackMaxImage' or i == 'trackMinImage' or i == 'video' or i == 'url' or i == 'preview' or i == 'thumbnailSelectedImage':
					tempSpecAssets.append(json_data['overlays'][k][i])
				if i == 'images' or i == 'imagesDown':
					for imagesArray in json_data['overlays'][k][i]:
						tempSpecAssets.append(imagesArray)

			if "overlays" in json_data['overlays'][k]:
				for i in json_data['overlays'][k]['overlays']:
					for x in i:
						if x == 'backgroundImage' or x == 'attachmentFile' or x == 'attachmentFilename' or x == 'attachmentImage' or x == 'shareImage' or x == 'file' or x == 'pagingIndicatorOff' or x == 'pagingIndicatorOn' or x == 'indicatorOffImage' or x == 'indicatorOnImage' or x == 'emitterFile' or x == 'maskImage' or x == 'buttonImage' or x == 'trackImage' or x == 'trackMaxImage' or x == 'trackMinImage' or x == 'video' or x == 'url' or x == 'preview' or x == 'thumbnailSelectedImage':
							objectIndex = json_data['overlays'][k]['overlays'].index(i)
							tempSpecAssets.append(json_data['overlays'][k]['overlays'][objectIndex][x]) 
						if x == 'images' or x == 'imagesDown':
							objectIndex = json_data['overlays'][k]['overlays'].index(i)
							for imagesArray in json_data['overlays'][k]['overlays'][objectIndex][x]:
								tempSpecAssets.append(imagesArray) 

			if "actions" in json_data['overlays'][k]:
				for i in json_data['overlays'][k]['actions']:
					for x in i:
						if x == 'data':
							objectIndex = json_data['overlays'][k]['actions'].index(i)
							for overlays in json_data['overlays'][k]['actions'][objectIndex][x]:
								if overlays == 'backgroundImage' or overlays == 'attachmentFile' or overlays == 'attachmentFilename' or overlays == 'attachmentImage' or overlays == 'shareImage' or overlays == 'file' or overlays == 'pagingIndicatorOff' or overlays == 'pagingIndicatorOn' or overlays == 'indicatorOffImage' or overlays == 'indicatorOnImage' or overlays == 'emitterFile' or overlays == 'maskImage' or overlays == 'buttonImage' or overlays == 'trackImage' or overlays == 'trackMaxImage' or overlays == 'trackMinImage' or overlays == 'video' or overlays == 'url' or overlays == 'preview' or overlays == 'thumbnailSelectedImage':
									tempSpecAssets.append(json_data['overlays'][k]['actions'][objectIndex][x][overlays])
								if overlays == 'images' or overlays == 'imagesDown':
									for imagesArray in json_data['overlays'][k]['actions'][objectIndex][x][overlays]:
										tempSpecAssets.append(imagesArray)

								if overlays == 'overlays':
									for overlayIds in json_data['overlays'][k]['actions'][objectIndex][x]['overlays']:
										for j in overlayIds:
											if j == 'backgroundImage' or j == 'attachmentFile' or j == 'attachmentFilename' or j == 'attachmentImage' or j == 'shareImage' or j == 'file' or j == 'pagingIndicatorOff' or j == 'pagingIndicatorOn' or j == 'indicatorOffImage' or j == 'indicatorOnImage' or j == 'emitterFile' or j == 'maskImage' or j == 'buttonImage' or j == 'trackImage' or j == 'trackMaxImage' or j == 'trackMinImage' or j == 'video' or j == 'url' or j == 'preview' or j == 'thumbnailSelectedImage':
												objectIndexData = json_data['overlays'][k]['actions'][objectIndex][x]['overlays'].index(overlayIds)
												tempSpecAssets.append(json_data['overlays'][k]['actions'][objectIndex][x]['overlays'][objectIndexData][j]) 
											if j == 'images' or overlays == 'imagesDown':
												objectIndexData = json_data['overlays'][k]['actions'][objectIndex][x]['overlays'].index(overlayIds)
												for imagesArray in json_data['overlays'][k]['actions'][objectIndex][x]['overlays'][objectIndexData][j]:
													tempSpecAssets.append(imagesArray) 

	if "pages" in json_data:
		for k,v in json_data['pages'].iteritems():
			for i in json_data['pages'][k]:
				if i == 'image' or i == 'thumbnail' or i == 'backgroundImage':
					tempSpecAssets.append(json_data['pages'][k][i])
				if i == 'overlays':
					for x in json_data['pages'][k][i]:
						for j in x:
							if j == 'backgroundImage' or j == 'attachmentFile' or j == 'attachmentFilename' or j == 'attachmentImage' or j == 'shareImage' or j == 'file' or j == 'pagingIndicatorOff' or j == 'pagingIndicatorOn' or j == 'indicatorOffImage' or j == 'indicatorOnImage' or j == 'emitterFile' or j == 'maskImage' or j == 'buttonImage' or j == 'trackImage' or j == 'trackMaxImage' or j == 'trackMinImage' or j == 'video' or j == 'url' or j == 'preview' or j == 'thumbnailSelectedImage':
								objectIndexData = json_data['pages'][k][i].index(x)
								tempSpecAssets.append(json_data['pages'][k][i][objectIndexData][j]) 
							if j == 'images' or j == 'imagesDown':
								objectIndexData = json_data['pages'][k][i].index(x)
								for imagesArray in json_data['pages'][k][i][objectIndexData][j]:
									tempSpecAssets.append(imagesArray) 

				if i == 'actions':
					for i in json_data['pages'][k]['actions']:
						for x in i:
							if x == 'data':
								objectIndex = json_data['pages'][k]['actions'].index(i)
								for overlays in json_data['pages'][k]['actions'][objectIndex][x]:
									if overlays == 'backgroundImage' or overlays == 'attachmentFile' or overlays == 'attachmentFilename' or overlays == 'attachmentImage' or overlays == 'shareImage' or overlays == 'file' or overlays == 'pagingIndicatorOff' or overlays == 'pagingIndicatorOn' or overlays == 'indicatorOffImage' or overlays == 'indicatorOnImage' or overlays == 'emitterFile' or overlays == 'maskImage' or overlays == 'buttonImage' or overlays == 'trackImage' or overlays == 'trackMaxImage' or overlays == 'trackMinImage' or overlays == 'video' or overlays == 'url' or overlays == 'preview' or overlays == 'thumbnailSelectedImage':
										tempSpecAssets.append(json_data['pages'][k]['actions'][objectIndex][x][overlays]) 
									if overlays == 'images' or overlays == 'imagesDown':
										for imagesArray in json_data['pages'][k]['actions'][objectIndex][x][overlays]:
											tempSpecAssets.append(imagesArray) 

									if overlays == 'overlays':
										for overlayIds in json_data['pages'][k]['actions'][objectIndex][x]['overlays']:
											for j in overlayIds:
												if j == 'backgroundImage' or j == 'attachmentFile' or j == 'attachmentFilename' or j == 'attachmentImage' or j == 'shareImage' or j == 'file' or j == 'pagingIndicatorOff' or j == 'pagingIndicatorOn' or j == 'indicatorOffImage' or j == 'indicatorOnImage' or j == 'emitterFile' or j == 'maskImage' or j == 'buttonImage' or j == 'trackImage' or j == 'trackMaxImage' or j == 'trackMinImage' or j == 'video' or j == 'url' or j == 'preview' or j == 'thumbnailSelectedImage':
													objectIndexData = json_data['pages'][k]['actions'][objectIndex][x]['overlays'].index(overlayIds)
													tempSpecAssets.append(json_data['pages'][k]['actions'][objectIndex][x]['overlays'][objectIndexData][j])  
												if j == 'images' or overlays == 'imagesDown':
													objectIndexData = json_data['pages'][k]['actions'][objectIndex][x]['overlays'].index(overlayIds)
													for imagesArray in json_data['pages'][k]['actions'][objectIndex][x]['overlays'][objectIndexData][j]:
														tempSpecAssets.append(imagesArray)

	for element in tempRootBundleAssets:
		if element not in tempSpecAssets:
			filesToBeRemoved.append(localPath+element)

	for a in filesToBeRemoved:
		if a.endswith('@2x.png'):
			filesToBeRemoved.index(a)
			filesToBeRemoved.remove(a)
			
	for X in filesToBeRemoved:
		xFilesToBeRemoved.append(X.replace('.png','@2x.png'))

	for twoX in xFilesToBeRemoved:
		filesToBeRemoved.append(twoX)

	
	myfile = open("listOfRemovedAssets.txt", "a") 
	for item in filesToBeRemoved:
		myfile.write('\n'+ item)
	myfile.close()


	for f in filesToBeRemoved:
		try:
			print f
			os.remove(f)
		except OSError:
			pass

var = raw_input("Do you want to commit? yes or no?: ")

if var == 'yes':
	for svn in filesToBeRemoved:
		filterPath(svn)
	svnCommit()
	for svnX in xFilesToBeRemoved:
		filterPathX(svnX)
	svnCommit()
if var == 'no':
	print 'Fuck That Shit'
	
for r,d,f in os.walk(localPath):
	for files in f:
		for extension in extensions:
			if files.endswith(extension):
				rootBundleAssets.append(os.path.join(r,files))

for removePath in rootBundleAssets:
	#tempRootBundleAssets.append(removePath.lstrip(localPath))
	tempRootBundleAssets.append(removePath.replace(localPath, ''))

for r,d,f in os.walk(localPath):
	for spec in f:
		if spec == 'include.json':
			print 'include'
			json_data = open(spec)
			dataInclude = json.load(json_data)
			json_data.close()
			for f in dataInclude:
				log = open(f)
				json_data = json.load(log)
				log.close()
				cleanBundle(json_data)
		if spec == 'ContentSpec.json':
			print 'ContentSpec'
			log = open(spec)
			json_data = json.load(log)
			log.close()
			cleanBundle(json_data)










