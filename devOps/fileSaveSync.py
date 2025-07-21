import sys, shutil, os.path
print( f"args = {sys.argv}" )

targetDir = "D:\\lib"
submoduleDir = 'lumensaliscplib\\lib'

def syncFile():

    def writeLog( s:str ): print( s )
    
    filename = sys.argv[1]
    if not filename.startswith(submoduleDir):
        writeLog( f"skipping {filename}, not in {submoduleDir}" )
        return
    ext = os.path.splitext(filename)[1]
    if ext in [".pyc", ".pyo", ".pyd", ".so", 'pyi']:
        writeLog( f"skipping {filename}, not a python source file" )
        return
    inLibFilename = filename[len(submoduleDir)+1:]
    target = os.path.join( targetDir,inLibFilename )
    writeLog( f"updating {filename} to {target}" )
    try:
        shutil.copy( filename, target )
    except Exception as inst:
        if not os.path.exists(os.path.dirname(target)):
            writeLog( f"Creating directory {os.path.dirname(target)}" )
            shutil.copy( filename, target )
        else:
            writeLog( f"Failed to copy {filename} to {target}: {inst}" )


if __name__ == "__main__":
    syncFile()