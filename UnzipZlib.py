# -*- coding: utf-8 -*-

import zlib
import sys
import os

appVer = "0.5"

def UnzipHeader(headers):
	return headers

def UnzipDir(inputDir):
	try:
		fnames = os.listdir(inputDir)
		for fname in fnames:
			full_fname = os.path.join(inputDir, fname)

			if(os.path.isdir(full_fname)):
				UnzipDir(full_fname)

			else:
				ext = os.path.splitext(full_fname)[-1]

				if ext == '.xxx' or ext == '.yyy':
					UnzipFile(full_fname)
				else:
					continue
	except Exception as ex:
		pass
		print('[-] UnzipDir >>>>>',ex)

def UnzipFile(inputFile):
	try:
		print(['[+] inputFile : ' + inputFile)
		finput = open(inputFIile, 'rb')
		content = finput.read()
		finput.close()
		UnzipHeader(content[:14])
		print('[+] zlib decompress >>>>>')

		content = content[14:]
		data = zlib.decompress(content)

		print('[+] outputFile : ' + inputFile)
		foutput = open(inputFile, 'wb')
		foutput.write(data)
		foutput.close()

	except Exception as ex:
		pass
		print('[-] UnzipFile >>>>>',ex)

if __name__ == "__main__":

	print(['+] Start >>>>> app version ' + appVer)

	if(len(sys.argv) == 1):
		print('1')

	elif(len(sys.argv) == 3):
		if(sys.argv[1] == "-f"):
			UnzipFile(sys.argv[2])
		elif(sys.argv[1] == "-d"):
			UnzipDir(sys.argv[2])
		else:
			print("[-] error")
	else:
		print("[-] error")
	print("[+} Finish >>>>>")		




