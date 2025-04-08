import sys, shutil, os.path
print( f"args = {sys.argv}" )

targetDir = "F:\\lib"
submoduleDir = 'lumensaliscplib'

def syncFile():
    #with open('fss.log', 'a' ) as fssLog:
    #    def writeLog( s:str ):
    #        print( s, file = fssLog )
    def writeLog( s:str ):
        print( s )
    filename = sys.argv[1]
    if not filename.startswith(submoduleDir):
        writeLog( f"skipping {filename}, not in {submoduleDir}" )
        return
    inLibFilename = filename[len(submoduleDir)+1:]
    target = os.path.join( targetDir,inLibFilename )
    writeLog( f"updating {filename} to {target}" )
    shutil.copy( filename, target )


if __name__ == "__main__":
    syncFile()