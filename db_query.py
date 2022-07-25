import mysql.connector as conn
import pandas as pd
from logging_class import lg

try:
    mydb = conn.connect(host = "localhost", user = "root", passwd = "Failsafeauto#1")
    cursor = mydb.cursor()

    # left join operation on two tables

    query = (''' select da.* ,ds.* from dbtask.dress_attribute as da
            left join dbtask.dress_sales as ds 
            on da.Dress_ID = ds.Dress_ID''')

    df = pd.read_sql_query(query,con=mydb)
    lg.info("query result : %s",(df))

except Exception as e:

    lg.error(e)