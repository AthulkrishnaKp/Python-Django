
import pymysql
db=pymysql.connect(host='localhost',user='root',password='2205',db='db2')
# prepare cursor object using cursor() method.
cur1=db.cursor()
#sql="create table student2(Adno int,name varchar(15),average int,sex char(4),scode int)"
# sql="insert into student2 values(501,'R.Jain',98,'M',111)"
# sql="insert into student2 values(545,'Kavitha',73,'F',333)"
# sql="insert into student2 values(705,'K.Rashika',85,'F',111)"
# sql="insert into student2 values(754,'Rahul goel',60,'M',444)"
# sql="insert into student2 values(892,'Sahil jain',78,'M',333)"
# sql="insert into student2 values(935,'Rohan saini',85,'M',222)"
# sql="insert into student2 values(955,'Anjali',64,'F',444)"
# sql="insert into student2 values(983,'Sneha aggarwal',80,'F',222)"
# sql="select * from student2 group by sex"
sql="select * from student2"
cur1.execute(sql)
rows=cur1.fetchall()
# db.commit()




#1. Display Full Data of student2 table?

# sql="select * from student2"
# cur1.execute(sql)
# rows=cur1.fetchall()
# for i in rows:
#     print(i[0],i[1],i[2],i[3],i[4])

# 2. Display Rohan saini's infos only ?

# sql="select * from student2 where name='Rohan saini'"
# cur1.execute(sql)
# row=cur1.fetchone()
# if row:
#     print(row[0], row[1], row[2], row[3], row[4])

# 3.Display no: students in table?

# sql="select * from student2"
# cur1.execute(sql)
# rows=cur1.fetchall()
# c=0
# for i in rows:
#     c=c+1
# print(c)

# 4. display no: students in each sex ?

# sql="select sex,count(*) from student2 group by sex"
# cur1.execute(sql)
# rows=cur1.fetchall()
# for i in rows:
#     print(i)

# 5.display students info in ascending order using name ?

# sql="select * from student2 order by name asc"
# cur1.execute(sql)
# rows=cur1.fetchall()
# for i in rows:
#     print(i[0], i[1], i[2], i[3], i[4])

# 6. Display students info in descending order using avg marks ?

# sql="select * from student2 order by average desc"
# cur1.execute(sql)
# rows=cur1.fetchall()
# for i in rows:
#     print(i[0], i[1], i[2], i[3], i[4])

# 7. Display students name starting with letter k ?

# sql="select * from student2 where name like 'K%'"
# cur1.execute(sql)
# rows=cur1.fetchall()
# for i in rows:
#     print(i[0], i[1], i[2], i[3], i[4])

# 8.Display students infos whose name ends with l ?

# sql="select * from student2 where name like '%l'"
# cur1.execute(sql)
# rows=cur1.fetchall()
# for i in rows:
#     print(i[0], i[1], i[2], i[3], i[4])