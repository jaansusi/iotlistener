import sqlite3

import yaml

cfg = yaml.safe_load(open("config.yml"))

def insertTelemetry(data):
    queryString = ("INSERT INTO telemetry_powr2 "
            "(topic, time, today, period, power, voltage, current, factor, apparent_power, reactive_power, yesterday, total, total_start_time) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);")
    dataTuple = (data["Topic"], data["Time"], data["Today"], data["Period"], data["Power"], data["Voltage"], data["Current"], data["Factor"], data["ApparentPower"], data["ReactivePower"], data["Yesterday"], data["Total"], data["TotalStartTime"])
    sqLiteQuery(queryString, dataTuple)

def query(queryString, data = None, returnData = False):
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
