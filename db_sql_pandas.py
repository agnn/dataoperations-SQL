import mysql.connector as conn
import pandas as pd
from logging_class import lg

#inserting tables from sql and convert to pandas DataFrame
try:
    mydb = conn.connect(host = "localhost", user = "root", passwd = "Failsafeauto#1")
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM dbtask1.dress_attribute")
    table = cursor.fetchall()
    df = pd.DataFrame(table)
    lg.info("data frame : %s",df)

    cursor.execute("SELECT * FROM dbtask1.dress_sales")
    table1 = cursor.fetchall()
    df1 = pd.DataFrame(table1)

    lg.info("data frame : %s",df1)
except Exception as e:

    lg.error(e)