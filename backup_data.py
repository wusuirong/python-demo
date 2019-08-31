import os
import zipfile
import sys

def zipDir(startDir, zipFileName):
	if os.path.exists(zipFileName):
		os.remove(zipFileName)

	z = zipfile.ZipFile(zipFileName, 'w', zipfile.ZIP_DEFLATED)
	for dirpath, dirnames, filenames in os.walk(startDir):
		fpath = dirpath.replace(startDir, '')
		fpath = fpath and fpath + os.sep or ''

		for filename in filenames:
			z.write(os.path.join(dirpath, filename), fpath + filename)
			print ('zipped: ' + dirpath + filename)
	z.close()

if __name__=="__main__":
	startDir = sys.argv[1]
	zipFileName = sys.argv[2]
	zipDir(startDir, zipFileName)