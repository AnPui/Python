from MysqlPython import MysqlHelp
from hashlib import sha1
username = input("请输入用户名：")
password = input("请输入密码：")
#password加密
s1=sha1()
s1.update(password.encode("utf-8")) #转码
password2=s1.hexdigest() #返回十六进制加密的结果
# 和数据库中表记录进行匹配
mysql=MysqlHelp("db2")
sql_select="select password from user where username=%s"
result=mysql.getAll(sql_select,[username])
if len(result)==0:
    print("用户名不存在!")
elif password2==result[0][0]:
    print("登录成功!")
else:
    print("密码错误!")
