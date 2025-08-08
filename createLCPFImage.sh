#!/bin/bash

targetFile="LCPF_CP_Install.zip"
rm ${targetFile}
zipOpts="-r -x.git -x*.pyc -x*.pyi -x*__pycache__* -x*audio/*"

cd CircuitPyDependencies
zip ${zipOpts} ../${targetFile} *
cd ../lumensaliscplib/out
zip ${zipOpts} ../../${targetFile} *
cd ..   
