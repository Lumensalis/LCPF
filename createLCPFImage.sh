#!/bin/bash

rm LCPFImage.zip

cd CircuitPyDependencies
zip -r -x.git ../LCPFImage.zip *
cd ../lumensaliscplib
zip -r -x.git ../LCPFImage.zip *
cd ..   
