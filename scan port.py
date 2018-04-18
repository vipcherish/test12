#!/usr/bin/python
#-*- coding:utf-8 -*-
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((conn_ip,conn_port))
    logging.info('IP:'+str(conn_ip)+',PORT:'+str(conn_port)+',connect successful')
except Exception as e:
    logging.warning('IP:'+str(conn_ip)+',PORT:'+str(conn_port)+',connect failed!!check the client!!')
    send_msg(conn_ip,conn_port) #发送报警短信
finally:
    s.close()