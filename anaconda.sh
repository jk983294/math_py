#!/bin/bash

bash Anaconda-latest-Linux-x86_64.sh
# change /root/anaconda3 to /opt/anaconda3
conda update -n base conda                  # update conda

# uninstall
rm -rf /opt/anaconda3
rm -rf ~/.condarc ~/.conda ~/.continuum

conda search PACKAGENAME                    # check if installed this package
conda list                                  # list all installed packages
conda list | grep numpy
conda install PACKAGENAME
conda update PACKAGENAME

# create an environment
conda create --name myenv
conda create -n myenv python=3.4            # create an environment with a specific version of Python
conda install python=3.5                    # change base env's python version
conda activate myenv                        # switch between environment
conda activate                              # switch to default env (base)
conda install -n myenv scipy=0.15.0         # install a specific version of a package in given an environment
conda info --envs                           # check current venv, active environment marked with *
python --version                            # check current python version of current environment

# install package
conda install -n myenv pip
source activate myenv
pip <pip_subcommand>

# upgrade to latest python
conda update python

# conda mixed with pip, you should first try conda install over pip intall
conda install pip
pip install --upgrade setuptools

# change source
conda config --set ssl_verify false
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes

# remove source
conda config --show channels
conda config --remove-key channels
conda config --remove channels defaults
conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

# requirements.txt
pip freeze > requirements.txt
conda install --file requirements.txt
pip install -r requirements.txt

# uninstall anaconda
rm -rf /opt/anaconda3
rm -rf ~/.condarc ~/.conda
vim ~/.bashrc  # edit path of anaconda

# pip source
mkdir ~/.pip
cd ~/.pip
vim pip.conf
[global]
index-url = https://pypi.mirrors.ustc.edu.cn/simple/
index-url = http://mirrors.aliyun.com/pypi/simple/

# pip security
pip install QScintilla --trusted-host mirrors.aliyun.com
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple numpy
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple --upgrade --force-reinstall numpy
