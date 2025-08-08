import sys, shutil
from mpyHelper import *

#print( f"args = {sys.argv}" )
targetDir = "D:\\lib"


def syncFile():

    filename = sys.argv[1]
    filename = filename.replace('\\', '/')
    if not filename.startswith(submoduleDir):
        writeLog( f"skipping {filename}, not in {submoduleDir}" )
        return
    ext = os.path.splitext(filename)[1]
    if ext in [".pyc", ".pyo", ".pyd", ".so", '.pyi', ".mpy"]:
        writeLog( f"skipping {filename}, not a python source file" )
        return

    mpyFile = MpyFileHelper(filename)
    writeLog("---" )
    writeLog( f"detected save of {filename}" )
    makeMpyFile( mpyFile )
    
    sourcePath = mpyFile.mpyCrossOutputFilename
    
    destPath = os.path.join( targetDir, mpyFile.mpyTarget )
    destTargetDir = os.path.dirname(destPath)
    if not os.path.exists( destTargetDir ):
        writeLog( f"making  {destTargetDir}" )
        os.makedirs( destTargetDir )

    writeLog( f"copying {sourcePath} to {destPath}" )
    try:
        shutil.copy( sourcePath, destPath )
    except Exception as inst:
        writeLog( f"Failed to copy {sourcePath} to {destPath}: {inst}" )


if __name__ == "__main__":
    syncFile()