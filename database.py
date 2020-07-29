import mysql.connector
from mysql.connector import Error

import yaml

cfg = yaml.safe_load(open("config.yml"))

def query(queryString, data = None, returnData = False):
    results = None
    try:
        connection = mysql.connector.connect(host=cfg["db"]["host"],
                                            database=cfg["db"]["database"],
                                            user=cfg["db"]["username"],
                                            password=cfg["db"]["password"])
        if connection.is_connected():
            cursor = connection.cursor()
            if (data == None):
                cursor.execute(queryString)
            else:
                cursor.execute(queryString, data)
            if (returnData):
                results = cursor.fetchall()
            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
    return results