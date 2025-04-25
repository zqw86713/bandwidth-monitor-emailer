#!/bin/bash

source /root/.bashrc

# Run the Python script
/root/myvenv/justmysocks_env/bin/python /root/justmysocks/main.py >> /root/justmysocks/logfile.log 2>&1
