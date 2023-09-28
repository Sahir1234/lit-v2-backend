#!/bin/bash

# RUN THIS SCRIPT TO START THE SERVER FROM SC

echo "CREATING VIRTUAL ENVIRONMENT..."
python3 -m venv env
source env/bin/activate
echo "VIRTUAL ENVIRONMENT ACTIVATED!"

echo "INSTALLING DEPENDENCIES..."
pip install -r requirements.txt
echo "DEPENDENCIES SUCCESSFULLY INSTALLED!"

echo "RUNNING APP NOW..."
python3 app.py