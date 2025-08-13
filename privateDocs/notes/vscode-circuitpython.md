
RANDOM notes from trying to get vscode-circuitpython building


clone https://github.com/jbrelwof/vscode-circuitpython.git ***in WSL2 filesystem***

```bash
sudo apt-get update
sudo apt-get upgrade npm
```

./scripts/build-stubs.py


------------

windows

make sure node-gyp is installed and working... https://github.com/nodejs/node-gyp#on-windows

(or uninstall nodejs, odwnload https://nodejs.org/en/download/ , reinstall with the 
native build tool options enabled
)


in circuitpython  setup.py-stubs
`    setup_requires=["setuptools_scm", "setuptools>=38.6.0"],`
**setuptools_scm** causes problems


in admin...
```
choco install make
choco upgrade nodejs



## python requirements

# requests, bs4



sudo apt update && sudo apt upgrade -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.13
sudo apt install python3.13-venv
sudo apt install python3.13-dev

sudo apt install python3.11 python3.11-venv python3.11-dev


 python3.11 -m venv .venv.3.11
source .venv.3.11/bin/activate


sudo apt-get install curl
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
nvm install --lts
Installing latest LTS version.
Downloading and installing node v22.18.0...
Downloading https://nodejs.org/dist/v22.18.0/node-v22.18.0-linux-x64.tar.xz...
######################################################