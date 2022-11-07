import mysql.connector
import numpy as np

def insertVal(user, password, database, valDict, tabName):
    mydb = mysql.connector.connect(
    host="localhost",
     user=user,
    password=password,
    database = database
    )

    mycursor = mydb.cursor()

    sql = getSqlInsert(tabName, valDict)
    val = createTup(valDict)

    #print(sql)
    #print(val)

    mycursor.execute(sql, val)

    mydb.commit()


def getSqlInsert(tabName, diction):
    sql = "INSERT INTO " + tabName + " ("

    #insert the col names
    for i, col in enumerate(diction):
        if i < len(diction) - 1:
            sql += col + ", "
        else:
            sql += col

    sql += ") VALUES ("

    for i, col in enumerate(diction):
        if i < len(diction) - 1:
            sql += "%s ,"
        else:
            sql += "%s)"

    return sql


def createTup(diction):
    return tuple([diction[col] for col in diction])
    