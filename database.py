import mysql.connector
import sqlite3

import yaml

cfg = yaml.safe_load(open("config.yml"))

def query(queryString, data = None, returnData = False):
    if cfg["db"]["engine"] == "mysql":
        return mySqlQuery(queryString, data, returnData)
    elif cfg["db"]["engine"] == "sqlite":
        return sqLiteQuery(queryString, data, returnData)
    else:
        raise Exception("DB engine is not supported")

def insertTelemetry(data):
    if cfg["db"]["engine"] == "mysql":
        queryString = ("INSERT INTO telemetry_powr2 "
                "(device_id, time, today, period, power, voltage, current, factor, apparent_power, reactive_power, yesterday, total, total_start_time) "
                "VALUES (%(DeviceId)s, %(Time)s, %(Today)s, %(Period)s, %(Power)s, %(Voltage)s, %(Current)s, %(Factor)s, %(ApparentPower)s, %(ReactivePower)s, %(Yesterday)s, %(Total)s, %(TotalStartTime)s);")
        mySqlQuery(queryString, data)
    elif cfg["db"]["engine"] == "sqlite":
        queryString = ("INSERT INTO telemetry_powr2 "
                "(device_id, time, today, period, power, voltage, current, factor, apparent_power, reactive_power, yesterday, total, total_start_time) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);")
        dataTuple = (data["DeviceId"], data["Time"], data["Today"], data["Period"], data["Power"], data["Voltage"], data["Current"], data["Factor"], data["ApparentPower"], data["ReactivePower"], data["Yesterday"], data["Total"], data["TotalStartTime"])
        sqLiteQuery(queryString, dataTuple)

def mySqlQuery(queryString, data = None, returnData = False):
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

def sqLiteQuery(queryString, data = None, returnData = False):
    results = None
    try:
        connection = sqlite3.connect(cfg["db"]["filename"])
        cursor = connection.cursor()
        
        if data == None:
            cursor.execute(queryString)
        else:
            cursor.execute(queryString, data)
            
        if returnData:
            results = cursor.fetchall()
        connection.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

    return results
