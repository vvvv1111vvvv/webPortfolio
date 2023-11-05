# Purpose: read KOSPI.list file and put to local mysql
import pymysql,csv
import sys,os
import config
class DB_Access:
    def __init__(self):
        self.predict_KOSPI=[] 
        self.actual_KOSPI= []
        self.predict_KOSPI_fromDB=[] 
        self.actual_KOSPI_fromDB=[]
    def csv_to_list(self):
        with open('predict_KOSPI.csv','r', encoding='utf-8') as f:
            csvfile=csv.reader(f)
            tmp=list(csvfile)
            for i in range (len(tmp[0])):
                self.predict_KOSPI.append(tmp[0][i])   
        with open('actual_KOSPI.csv','r', encoding='utf-8') as f:
            csvfile=csv.reader(f)
            tmp=list(csvfile)
            for i in range (len(tmp[0])):
                self.actual_KOSPI.append(tmp[0][i])

        return self.predict_KOSPI, self.actual_KOSPI
    
    def checkDB(self) :
        self.predict_KOSPI, self.actual_KOSPI =self.csv_to_list()   
        conn = pymysql.connect(host=config.host,  user=config.user, 
                            passwd=config.password,  charset='utf8')
        cursor = conn.cursor() #cursor 객체를 통해 데이터베이스의 데이터에 접근    
        sql = 'CREATE DATABASE IF NOT EXISTS %s' % config.db
        cursor.execute(sql)
        conn.commit() #db complete
        conn.close()   #db close
        return self.checkTable()

    def checkTable(self):
        conn = pymysql.connect(host=config.host,  user=config.user, 
                            password=config.password, db = 'dbForChart',charset='utf8')
        cursor = conn.cursor() #cursor 객체를 통해 데이터베이스의 데이터에 접근    
        sql = 'CREATE TABLE IF NOT EXISTS %s (%s)'%(config.table,config.tableSet)
        cursor.execute(sql)
        conn.commit() #db complete
        conn.close()   #db close
        return self.checkNull()
    
    def checkNull(self):
        conn = pymysql.connect(host=config.host,  user=config.user, 
                            password=config.password, db = 'dbForChart', charset='utf8')
        cursor = conn.cursor() #cursor 객체를 통해 데이터베이스의 데이터에 접근   
        #sql = "SELECT EXISTS ( SELECT %s FROM %s WHERE id = %s)"%(config.tableColumn[1], config.table, 1)
        sql = "SELECT %s FROM %s WHERE %s IS NOT NULL"%(config.tableColumn[1], config.table, config.tableColumn[1])
        result=cursor.execute(sql)
        conn.commit()
        conn.close()
        if result == 0:
            self.writeOnDB() 
        return 0
    
            


    def writeOnDB(self):        
        conn = pymysql.connect(host=config.host,  user=config.user, 
                            password=config.password, db = 'dbForChart', charset='utf8')
        cursor = conn.cursor() #cursor 객체를 통해 데이터베이스의 데이터에 접근  
        for i in range(1,len(self.predict_KOSPI)+1):
            sql = "INSERT INTO %s (%s, %s, %s) VALUES(%s, %s, %s)"%(config.table, config.tableColumn[0],config.tableColumn[1],config.tableColumn[2],i,self.predict_KOSPI[i-1], self.actual_KOSPI[i-1])
            cursor.execute(sql)
        conn.commit() #db complete
        conn.close()   #db close

    def getFromDB(self):
        conn = pymysql.connect(host=config.host,  user=config.user, 
                            password=config.password, db = 'dbForChart', charset='utf8')
        cursor = conn.cursor() #cursor 객체를 통해 데이터베이스의 데이터에 접근
        for i in range(1,len(self.predict_KOSPI)+1):
            sql = "SELECT * FROM %s"%config.table
            cursor.execute(sql)
            result = cursor.fetchall()
            for data in result:
                self.predict_KOSPI_fromDB.append(data[1])
                self.actual_KOSPI_fromDB.append(data[2])
        conn.commit() #db complete
        conn.close()   #db close
        return self.predict_KOSPI_fromDB, self.actual_KOSPI_fromDB
