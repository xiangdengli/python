import pymysql
cons=pymysql.connect(host='127.0.0.1',user='root',password='Mysql@20211101',db='test')
con=cons.cursor()
#sql='create table info(id tinyint primary key auto_increment,name varchar(50),usr varchar(300),back_ip varchar(50),front_file varchar(100),nginx_ip varchar(50),public_ip varchar(50),back_file varchar(100) ,costumer  varchar(30) ,status varchar(20));'
# con.execute(sql)