import yaml
import mysql.connector
import sqlite3

cfg = yaml.safe_load(open("config.yml"))

if cfg["db"]["engine"] == "mysql":
    try:
        connection = mysql.connector.connect(host=cfg["db"]["host"],
                                            database=cfg["db"]["database"],
                                            user=cfg["db"]["username"],
                                            password=cfg["db"]["password"])
        if connection.is_connected():
            cursor = connection.cursor()
            sql = open("db/init_mysql.sql", "r", encoding="utf-8").read()
            print(sql.split(';'))
            for query in sql.split(';'):
                if query.strip() != "":
                    cursor.execute(query)
            
            connection.commit()
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
elif cfg["db"]["engine"] == "sqlite":
    connection = sqlite3.connect(cfg["db"]["filename"])
    cursor = connection.cursor()
    cursor.executescript(open("db/init_sqlite.sql", "r", encoding="utf-8").read())
    connection.commit()
    cursor.close()
    connection.close()