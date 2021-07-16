import logging

import mysql.connector
from mysql.connector import Error
import configparser
import utilities.custom_logging as cl

log = cl.log(logging.DEBUG)

def getconfig():
    config = configparser.ConfigParser()
    config.read("C:\\Users\\Punam\\workspace_python\\apianddeletepracticebook\\utilities\\properties.ini")
    return config

conset={
    'host': getconfig()['SQL']['hostname'],
    'database': getconfig()['SQL']['database'],
    'user': getconfig()['SQL']['username'],
    'password': getconfig()['SQL']['password']
}


def getconn():
    try:
        conn= mysql.connector.connect(**conset)
        if conn.is_connected():
            log.info("DB Connected")
            return conn
    except Error as e:
        log.error(e)


def updatequery(uquery,data):
    conn = getconn()
    cursor = conn.cursor()
    cursor.execute(uquery,data)
    conn.commit()
    conn.close()


def getquery(gquery):
    conn = getconn()
    cursor = conn.cursor()
    cursor.execute(gquery)
    row=cursor.fetchone()
    conn.close()
    return row


