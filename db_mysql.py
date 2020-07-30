import mysql.connector

import yaml

cfg = yaml.safe_load(open("config.yml"))

def insertTelemetry(data):
    queryString = ("INSERT INTO telemetry_powr2 "
            "(topic, time, today, period, power, voltage, current, factor, apparent_power, reactive_power, yesterday, total, total_start_time) "
            "VALUES (%(Topic)s, %(Time)s, %(Today)s, %(Period)s, %(Power)s, %(Voltage)s, %(Current)s, %(Factor)s, %(ApparentPower)s, %(ReactivePower)s, %(Yesterday)s, %(Total)s, %(TotalStartTime)s);")
    query(queryString, data)
    
def query(queryString, data = None, returnData = False):
    results = None
    try:
        connection = mysql.connector.connect(host=cfg["db"]["host"],
                                            database=cfg["db"]["database"],
                                            user=cfg["db"]["username"],
                                            password=cfg["db"]["password"])
        if connection.is_connected():
            cursor = connection.cursor()
            if data == None:
                cursor.execute(queryString)
            else:
                cursor.execute(queryString, data)
            if returnData:
                results = cursor.fetchall()
            connection.commit()

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return results
