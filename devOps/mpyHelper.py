import sys, os.path, subprocess, shutil

submoduleDir = 'lumensaliscplib/lib'
submoduleOutDir = 'lumensaliscplib/out'

def writeLog( s:str ): 
    print( s )

class MpyFileHelper:
    def __init__(self, filename:str):
        self.filename = filename.replace('\\', '/')
        assert filename.startswith(submoduleDir), f"Filename {filename} does not start with {submoduleDir}"
        self.inLibFilenameBase = os.path.splitext(filename[len(submoduleDir)+1:])[0]
        self.sourceEmbeddedFilename = f"{self.inLibFilenameBase}.py"
        if self.inLibFilenameBase.endswith("RL"):
            self.mpyExtension = ".py"
        else:
            self.mpyExtension = ".mpy"
        self.mpyCrossOutputFilename = f"{submoduleOutDir}/{self.inLibFilenameBase}{self.mpyExtension}"
        self.mpyFileDir = os.path.dirname(self.mpyCrossOutputFilename)
        self.mpyTarget = self.inLibFilenameBase + self.mpyExtension

def makeMpyFile( mpyFile :MpyFileHelper ):
    
    assert os.path.exists(mpyFile.filename), f"Source file {mpyFile.filename} does not exist"
 
    if not os.path.exists(mpyFile.mpyFileDir):
        writeLog( f"Creating directory {mpyFile.mpyFileDir}" )
        os.makedirs(mpyFile.mpyFileDir, exist_ok=True)
    
    writeLog( f"creating {mpyFile.mpyCrossOutputFilename} from {mpyFile.filename}" )
    try:
        if os.path.exists(mpyFile.mpyCrossOutputFilename):
            os.remove(mpyFile.mpyCrossOutputFilename)
        if mpyFile.mpyExtension == ".mpy":
            commandParts = [
                'run-mpy-cross.bat', 
                "-o", mpyFile.mpyCrossOutputFilename,
                '-s', mpyFile.sourceEmbeddedFilename,
                mpyFile.filename
            ]
            writeLog( f"Running command: {' '.join(commandParts)}" )
            subprocess.run( commandParts, check=True, shell=True )
        else:
            assert mpyFile.mpyExtension == ".py", f"Unsupported extension {mpyFile.mpyExtension}"
            writeLog( f"Copying {mpyFile.filename} to {mpyFile.mpyCrossOutputFilename}" )
            shutil.copy(mpyFile.filename, mpyFile.mpyCrossOutputFilename)
        assert os.path.exists(mpyFile.mpyCrossOutputFilename), f"Failed to create {mpyFile.mpyCrossOutputFilename}"
    except Exception as inst:
        writeLog( f"Failed to create {mpyFile.mpyCrossOutputFilename}: {inst}" )
        sys.exit    
    

def main():
    assert os.path.exists(submoduleDir), f"Submodule directory {submoduleDir} does not exist"
    
    for dirpath, dirnames, filenames in os.walk(submoduleDir):
        if '__pycache__' in dirnames:
            dirnames.remove('__pycache__')

        #print(f"Current Directory: {dirpath}")
        #print(f"Subdirectories: {dirnames}")
        #print(f"Files: {filenames}")
        #print("-" * 30)
        assert dirpath.startswith(submoduleDir), f"Directory {dirpath} is not in {submoduleDir}"
        dirpath = dirpath.replace('\\', '/')

        for fileName in filenames:
            if fileName.endswith('.py'):
                source  = f"{dirpath}/{fileName}"
                mpy = MpyFileHelper(source)
                print( f"{source} : {mpy.mpyCrossOutputFilename}")
                makeMpyFile(mpy)
             

    
if __name__ == "__main__":
    main()
