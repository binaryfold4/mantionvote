#!/bin/sh

pyvenv env
source env/bin/activate
pip install -r requirements.txt

python scrape.py

