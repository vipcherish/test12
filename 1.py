
# -*- coding:utf8 -*-

# print ('hello,world!')
# print (10**3)

# user_name = input('请输入用户名：')
# if user_name == 'alex':
#     print('管理员')
# elif user_name == 'bob':
#     print('user')
# else:
#     print ('非法用户')
# print('logout')


# while True:
#     user = input('用户名：')
#     pwd = input('密码：')
#     if user == 'alex' and pwd == '123456':
#             print('登录成功')
#             break
#     else:
#             print('用户名或者密码错误')
#
#
# i = 1
# while True:
#     if i == 7:
#         i =i + 1
#         continue
#     else:
#         print(i)
#     i = i + 1
#     if i == 11:
#         break

# value = 0
# i = 1
# while i<101:
#     value =value+i
#     #print(i)
#     i=i+1
# print(value)


# i=1
# while i<101:
#     if i%2==0:
#         print(i)
#     i=i+1


# value=0
# i=1
# while i<100:
#     if i%2==1:
#         value+=i
#     else:
#         value-=i
#     i+=1
# print(value)

# i=0
# while i<3:
#     user = input('>')
#     pwd = input('>')
#     if user == 'alex' and pwd == '123456':
#         print('success')
#         break
#     else:
#         print('login error')
#         i=i+1

# %s占位符，字符串格式化
# name='姓名：Alex,性别:%s,年龄:%s'
# new_name=name %('男',20)
# print(new_name)

# name='Name:Alex，Sex:%s，Age:%s'%('男',20)
# print(name)
# 移除空白
# val=' alex '
# new_val=val.strip()
# new_val=val.lstrip()
# new_val=val.rstrip()
# print(new_val)

# 传入值在字符串中出现的次数
# 参数1：要查找的值（子序列）
# 参数2：起始位置（索引）
# # 参数3：结束位置（索引）
# name="dfkljsdjfkjslakgg"
# v=name.count('k',8,12)
# # 从8开始到12结束，字符串k出现的次数
# print(v)


# 是否已某个字符串结束和开始
# name='alex'
# v1=name.endswith('ex')
# v2=name.startswith('al')
# print(v1)
# print(v2)


# 找到制表符(\t)、换行符(\n),包含前面的值
# name="alex\tbob\ntom\tjarry"
# v=name.expandtabs(10)
# print(v)


# # 找到指定子序列的索引位置，如果不存在返回-1
# #index如果不存在直接报错
# name="alex"
# v=name.find('le')
# print(v)
# v=name.index('b')
# print(v)


# 是否表示标识符
# n='class'
# v=n.isidentifier()
# print(v)

# #字符串格式化
# #占位符%s;{}
# # tpl = "我是:%s;年龄:%s"
# tpl = "我是:{0};\n年龄:{1};"
# v = tpl.format('alex','20')
# print(v)
# a="=========================="
# print(a)
# tpl="我是:{name}\n年龄:{age}\n性别:{gender}"
# v=tpl.format(name="李杰",age="20",gender="M")
# print(v)
# a="=========================="
# print(a)
# tpl="我是:{name}\n年龄:{age}\n性别:{gender}"
# v=tpl.format_map({'name':"alex","age":"21","gender":"F"})
# print(v)


# # 判断是否为数字和汉字
# name="alex88汉字"
# v=name.isalnum()#字，数字
# print(v)
# v=name.isalpha()
# print(v)


# 判断是否为数字
# num="123"
# v1=num.isdecimal()
# v2=num.isdigit()
# v3=num.isnumeric()
# print(v1,v2,v3)


# 是否都是全部大、小写
# name='ALEX'
# v=name.islower()#全部小写
# print(v)
# v=name.isupper()# 全部大写
# print(v)


# # 是都全部变成大小写
# name='alex,BOB'
# v=name.upper()#全部变大写
# print(v)
# v=name.lower()#全部变小写
# print(v)
# 大小写相互转换
# name="Alex"
# v=name.swapcase()
# print(v)


# 是否包含隐含的内容
# name='123456,\nabcdefg'
# v=name.isprintable()
# print(v)


#
# 是否全部是空格
# name='    '
# v=name.isspace()
# print(v)


# 元素拼接（字符串）
# name='a_b_c'
# v="_".join(name)#内部循环每个元素,只能是字符串，不能是数字。
# print(v)


#
# 左右填充 rjust、ljust
# name='alex'
# v=name.ljust(20,'*')
# print(v)

# # 用0填充
# name="alex"
# v=name.zfill(20)
# print(v)


#
# 对应关系加翻译
# m=str.maketrans('asdfh','12345')#一一对应
# name='asdhfkepoh'
# v=name.translate(m)
# print(v)


# 分割、保留分割的元素
# content="ptyhon是最好的语言？"
# v=content.partition('是')
# print(v)


# 替换
# content="bob is B is b"
# v=content.replace("is","是",2)#“2”依次替换两个类
# print(v)

#
# # 移除空白、\n、\t，自定义内容
# name='alex\t'
# v=name.strip()#空白、\n、\t
# print(v)

# 追加字符串
# v1='1'
# v2='2'
# v=v1+v2#执行v1的add功能并非“+”的功能
# print(v)


# 转换成字节
# name='李杰'
# v=name.encode(encoding='utf-8')#3个字符代表一个字节
# print(v)
# v=name.encode(encoding='gbk')#2个字符代表一个字节
# print(v)

###### int ######
# 当前整数的二进制表示，最少位数
# age=4
# print(age.bit_length())
# # 获取当前字节表示
# age=15
# v1=age.to_bytes(5,byteorder='big')
# v2=age.to_bytes(5,byteorder='little')
# print(v1)
# print(v2)


###### bool ######
# 空内容的时候都是false

###### list ######
# int str list
# 追加
# user_list=['张三','李四','王五']#可变类型
# user_list.append('李四')
# print(user_list)
# 清空
# user_list.clear()
# print(user_list)
# (浅)拷贝
# v=user_list.copy()
# print(v)
# print(user_list)
# 计数
# print(user_list)
# v=user_list.count('李四')
# print(v)

# # 扩展原列表同append
# user_list=['张三','李四','王五']#可变类型
# user_list.extend(['周伯通','项少龙'])
# print(user_list)
# # 查找元素的索引，如果没有就报错
# v=user_list.index('zhangsan')
# print(v)
# # 删除并且获取元素
# v=user_list.pop(1)
# print(v)
# print(user_list)
# # 删除（根据值）
# v=user_list.remove('李四')
# print(v)
# print(user_list)
# # 反转（逆序）
# user_list.reverse()
# print(user_list)

# # 排序
# nums=[11,22,55,2,6,8]
# print(nums)
# nums.sort()#从小到大
# nums.sort(reverse=True)#从大到小
# print(nums)


#####额外功能######
# user_list=['张三','李四','王五']
# user_list[0]
# user_list[1:0:2]
# del user_list[2]
# for i in user_list:
#     print(i)
# user_list[1]='张三丰'
# user_list=['张三','李四','王五',['段誉','小龙女','乔峰'],'虚竹']
# print(user_list)


# Python2.7会立即生成，Python3.X不会立即生成，只有循环迭代时，才一个一个生成
# python2.7
# v=range(1,11)
# print(v)
# xrange()#不会立即生成，迭代之后才一个一个生成
# =================
# python3.x
# for i in range(1,11):
#     print(i)

# 基于基数的显示
# for i in range(1,11,2):
#     print(i)
# 逆序显示
# for i in range(10,0,-1):
#     print(i)

# enumrate生成一列有序的数字
# li=['显示器','主机','键盘','鼠标']
# # for i in li:
# #     print(li)
# ===============
# # for i in range(0,len(li)):
# #     print(i+1,li[i])
# ==============
# for i,ele in enumerate(li,1):#1指从1开始
#     print(i,ele)
# v=input('输入序号：')
# v=int(v)#字符转换为数字
# item=li[v-1]
# print(item)

# ==============tuple：元组===================
# # 不可被修改的，不可变类型，只有找和索引功能
# user_tuple=('alex','eric','steven','alex')
# v=user_tuple.count('alex')#获取个数
# print(v)
# v=user_tuple.index('eric')#获取值得索引位置
# print(v)
# 额外功能
# for i in user_tuple:
#     print(i)
# v=user_tuple[0]# 索引取值
# print(v)
# v=user_tuple[0:2]#区间取值
# print(v)
# user_tuple=('alex','eric',['wangwu','zhaoliu','guijiaoqi'],'steven','alex')
# # user_tuple[0]=123#错误写法
# # user_tuple[2]=[11,22,33]#错误写法，整体不允许被修改
# user_tuple[2][1]='11'#可变元素可以被修改
# print(user_tuple)
# ********元组的最后必须加逗号******
li=(11)
# print(li)
# #=====区别
# li=(11,)
# print(li)


# ==============dict：字典===================
dic={'k1':'V1','k2':'v2'}
# 清空
# dic.clear()
# print(dic)
# # 浅拷贝
# v=dic.copy()
# print(v)
# 根据key获取指定的value，不存在不报错
# dic={'K1':'v1','K2':'v2'}
# v=dic.get('k111')#不存在的时候返回为None（更好）
# # v=dic['k1111']#不存在的时候返回keyerror错误提示
# print(v)
# v=dic.get('k56356','1111')#当值不存在的时候返回指定的值111
# print(v)

# # 删除并获取对应的value值
# dic={'k1':'v1','k2':'v2'}
# # dic.pop('k1')
# v=dic.pop('k1')
# print(dic)
# print(v)

# 随机删除一个键值对，并且获取到删除的键值
# dic={'k1':'v1','k2':'v2','k3':'v3'}
# v=dic.popitem()
# print(dic)
# print(v)
# k,v=dic.popitem() # ('k2','v2')根据逗号接收键值
# # print(dic)
# print(k,v)
# ==============
#  v=dic.popitem() # ('k2','v2')
# print(dic)
# print(v[0],v[1])


# 增加，如果存在不做操作
# dic={'k1':'v1','k2':'v2'}
# dic.setdefault('k3','v3')
# print(dic)
# #========
# dic.setdefault('k1','111111111')
# print(dic)


# # 批量增加或修改
# dic={'k1':'v1','k2':'v2'}
# dic.update({'k3':'v3','k1':'v10'})
# print(dic)
#

# dic=dict.fromkeys(['k1','k2','k3'],123)
# print(dic)
# dic=dict.fromkeys(['k1','k2','k3'],123)
# dic['k1']='111111111'
# print(dic)

# dic=dict.fromkeys(['k1','k2','k3'],[111,])
# # #{存储的时候都对应了列表
# # k1:111,[1,]
# # k2:111,[1,]
# # k3:111,[1,]
# # # }
# dic['k1'].append(222)
# print(dic)


# ============额外功能
# 字典可以嵌套
# 字典key必须是不可变类型;元组是不可变的，所以能作为key
#
# dic={'k1':'v1',
#      'k2':'v2',
#     (1,2,):'1111'
# }
# print(dic)

# key:
# -不可变
# -true,1


# ========set集合，不可重复的列表，可变类型==========
# se1={"alex","bob","tom"}
# se2={"alex","eric","tony"}
# # se1中存在，se2中不存在
# v=se1.difference(se2)
# # se2中存在，se1中不存在
# # v=se2.difference(se1)
# print(v)

# # se1中存在，se2中不存在，然后对se1清空，在重新赋值
# se1.difference_update(se2)
# print(se1)

# # se2中存在，se1不存在
# # se1中存在，se2不存在
# # (相互不存在的)
# v=se1.symmetric_difference(se2)
# print(v)

# # 取交集(取相同的)
# v=se1.intersection(se2)
# print(v)

# # 取并集(取所有)
# v=se1.union(se2)
# print(v)

# # 移除元素
# se1={"alex","bob","tom"}
# se1.discard('alex')
# print(se1)
# # 更新
# se1.update({'alex','luck','lili'})
# print(se1)
# ========额外功能
# v=se1[0]
# print(v)#不支持
# se1={"alex","bob","tom",(11,22,33)}#嵌套
# # 循环
# for i in se1:
#     print(i)

