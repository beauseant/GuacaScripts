import os
import mysql.connector

import sys


class DB:

    db = ''

    def __init__ ( self, server, user, password, dbName):

        try:
            self.db = mysql.connector.connect(host=server, user=user,password= password,database= dbName,
                charset='utf8', use_unicode=True)
            print ('Connection with MySql Database successful')

            
        except Exception as E:
            print ('Connection with Database failed')
            print (str(E))
            exit ()

    def __del__ (self):
        print ('closing database')
        self.db.close();


    def insertConnection (self,connection):

        cursor = self.db.cursor()
        
        fields = ['connection_name', 'parent_id', 'protocol','proxy_port', 'proxy_hostname', 
                  'proxy_encryption_method', 'max_connections', 'max_connections_per_user','connection_weight','failover_only'
                 ]

        values = 'VALUES ('

        sql = 'INSERT INTO guacamole_connection ('

        for f in fields:
            sql = sql+f+','
            if type(connection[f])== str:
                if ( connection[f] == 'None' or connection[f] == ''):
                    values = values + 'NULL,'
                else:
                    values = values + '"' + connection[f] + '",'
            else:
                values = values + str(connection[f]) + ','

        values = values[:-1] + ')'

        sql = sql[:-1] + ') ' + values

        cursor.execute(sql)

        lastId = cursor.lastrowid


        #import ipdb ; ipdb.set_trace()


        fields = ['domain', 'hostname','ignore-cert', 'password', 'username', 'wol-broadcast-addr', 'wol-mac-addr', 'wol-send-packet']
        values = []
        
        for f in fields:
            values.append ([lastId, f, connection[f]])


        #import ipdb ; ipdb.set_trace()

        sql = 'INSERT INTO guacamole_connection_parameter (connection_id,parameter_name, parameter_value) VALUES (%s,%s,%s)'

        cursor.executemany (sql, values)

        self.db.commit()
