import pymysql
import xlwt
import xlrd
import time
data=xlrd.open_workbook('sf.xlsx')
table=data.sheets()[0]
nrow=table.nrows
ncloum=table.ncols
cons=pymysql.connect(host='127.0.0.1',user='root',password='Mysql@20211101',db='test')
con=cons.cursor()
sql0='drop table  if exists info'
sql='create table info(id tinyint primary key auto_increment, name varchar(200) ,url text ,back_ip varchar(200) ,front_file varchar(200) ,nginx_ip varchar(200), public_ip varchar(200) ,back_file varchar(200),costumer  varchar(200),status varchar(200));'
con.execute(sql0)
time.sleep(5)
con.execute(sql)
time.sleep(5)
sql1='insert into info(name,url,back_ip,front_file,nginx_ip,public_ip,back_file,costumer,status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
for i in range(0,ncloum,1):
    values=(table.cell(i,0).value,table.cell(i,1).value,table.cell(i,2).value,table.cell(i,3).value,table.cell(i,4).value,table.cell(i,5).value,table.cell(i,6).value,table.cell(i,7).value,table.cell(i,8).value)
    con.execute(sql1,values)
cons.commit()
con.close()
print('youxi'+str(i)+' sucess')


