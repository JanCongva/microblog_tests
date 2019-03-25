#!/bin/bash

function install_packages() {
    sudo apt install -y docker.io docker-compose tigervnc-viewer wait-for-it
}

function install_virtual_env() {
    virtualenv -p python3 $HOME/test_venv
    $HOME/test_venv/bin/python setup.py install
    $HOME/test_venv/bin/pip install jupyter
}

function run_everything() {
    sudo docker-compose up &
    wait-for-it -t 0 localhost:5999 -- vncviewer :99 &
    $HOME/test_venv/bin/jupyter notebook workshop.ipynb
}

install_packages
install_virtual_env
run_everything
