#!/bin/bash

source /root/.bashrc

# Run the Python script
/root/myvenv/bin/python bandwidth_logger.py >> logfile.log 2>&1
