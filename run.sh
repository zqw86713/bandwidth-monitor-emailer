#!/bin/bash

# Load environment variables (optional, if needed)
source /root/.bashrc

# Move into the project directory
cd /root/band-bandwidth-monitor-emailer/ || exit 1

# Activate virtual environment
source venv/bin/activate

# Run main.py using the venv's Python
python main.py >> logfile.log 2>&1
