1. Install pip: `sudo apt install python3-pip`
2. Install required modules: `pip3 install mysql-connector-python paho-mqtt pyyaml`
3. Add values to config.yml.template and rename it to config.yml
4. To initialize the DB: `python3 initialize_db.py`. Make sure configuration values are correct!
4. Run script: `python3 main.py`
