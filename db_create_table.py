import mysql.connector as conn
from logging_class import lg

try:
    mydb = conn.connect(host = "localhost", user = "root", passwd = "Failsafeauto#1")
    cursor = mydb.cursor()
    lg.info("Connection successful")

    cursor.execute("show databases")                           #to check existing databases
    lg.info("databases: %s",cursor.fetchall())
    cursor.execute("create database if not exists dbtask1")     # one time operation to create database if not exists
    lg.info("database created/exists")
    #create table dress_attribute
    s="create table if not exists dbtask1.dress_attribute(Dress_ID varchar(80),Style varchar(80),Price varchar(80),Rating varchar(80),Size varchar(80),Season varchar(80),NeckLine varchar(80),SleeveLength varchar(80),waiseline varchar(80),Material varchar(80),FabricType varchar(80),Decoration varchar(80),Pattern_Type varchar(80),Recommendation int(10))"
    cursor.execute(s)
    lg.info("table created/exists")
    #create table dress_sales with data type as varchar
    s="create table if not exists dbtask1.dress_sales(Dress_ID varchar(80),`29/8/2013` varchar(80),`31/8/2013` varchar(80),`09/02/2013` varchar(80),	`09/04/2013` varchar(80),	`09/06/2013` varchar(80),	`09/08/2013` varchar(80),	`09/10/2013` varchar(80),	`09/12/2013` varchar(80),	`14/9/2013` varchar(80),	`16/9/2013` varchar(80),	`18/9/2013` varchar(80),	`20/9/2013` varchar(80),	`22/9/2013` varchar(80),	`24/9/2013` varchar(80),	`26/9/2013` varchar(80),	`28/9/2013` varchar(80),	`30/9/2013` varchar(80),	`10/02/2013`varchar(80),	`10/04/2013` varchar(80),	`10/06/2013` varchar(80),	`10/08/2010` varchar(80),	`10/10/2013` varchar(80),	`10/12/2013` varchar(80))"
    lg.info("table created/exists")
    #create table dress_sales with data type as int, but it is a problem with uncleaned data table
    # s="create table if not exists dbtask.dress_sales1(Dress_ID varchar(80),`29/8/2013` int,`31/8/2013` int,`09/02/2013` int,	`09/04/2013` int,	`09/06/2013` int,	`09/08/2013` int,	`09/10/2013` int,	`09/12/2013` int,	`14/9/2013` int,	`16/9/2013` int,	`18/9/2013` int,	`20/9/2013` int,	`22/9/2013` int,	`24/9/2013` int,	`26/9/2013` int,	`28/9/2013` int,	`30/9/2013` int,	`10/02/2013`int,	`10/04/2013` int,	`10/06/2013` int,	`10/08/2010` int,	`10/10/2013` int,	`10/12/2013` int)"
    #both tables created
    cursor.execute(s)
    lg.info("table created/exists")

except Exception as e:

    print(e)