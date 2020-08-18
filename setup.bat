@echo off

rem Setups up the Spelling App.
rem You only need to run this once, then you can use py app.py to start.
rem Must have Python 3.8 or later installed.

pip install -r requirements.txt
py setup_db.py