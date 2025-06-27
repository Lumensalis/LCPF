#!/bin/bash

rm LCPFImage.zip
zipOpts="-r -x.git -x*.pyc -x*.pyi -x*__pycache__* -x*audio/*"
targetFile="../LCPF_CP_Install.zip"

cd CircuitPyDependencies
zip ${zipOpts} ${targetFile} *
cd ../lumensaliscplib
zip ${zipOpts} ${targetFile} *
cd ..   
