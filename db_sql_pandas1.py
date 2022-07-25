import mysql.connector as conn
import pandas as pd
from logging_class import lg

#import tables from sql directly to pandas
try:
    mydb = conn.connect(host="localhost", user="root", passwd="Failsafeauto#1")
    cursor = mydb.cursor()

    df = pd.read_sql_query("SELECT * FROM dbtask1.dress_attribute",con=mydb)
    lg.info("data frame : %s",df)

    df1 = pd.read_sql("SELECT * FROM dbtask1.dress_sales",con=mydb)

    lg.info("data frame : %s",df1)
except Exception as e:

    print(e)