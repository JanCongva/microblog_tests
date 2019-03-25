#!/bin/bash

function install_docker() {
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker `whoami`
}

function install_docker_compose() {
    sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
}

function install_vnc_viewer() {
    sudo apt install -y tigervnc-viewer wait-for-it
}

function install_virtual_env() {
    virtualenv -p python3 $HOME/test_venv
    $HOME/test_venv/bin/python setup.py install
    $HOME/test_venv/bin/pip install jupyter
}

function run_everything() {
    docker-compose up &
    wait-for-it localhost:5999 -- vncviewer :99 &
    $HOME/test_venv/bin/jupyter notebook workshop.ipynb
}

install_docker
install_docker_compose
install_vnc_viewer
install_virtual_env
run_everything
