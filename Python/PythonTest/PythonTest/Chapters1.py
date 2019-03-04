###List
#bob = ['Bob Smith', 42, 30000, 'SoftWare']
#sue = ['Sue Jones', 45, 45000, 'HardWare']

#print("Bob's Name:" + bob[0])

#print("Sue's Money:" + str(sue[2]))



#数据库列表
#people =[bob, sue]
#for person in people:
#    print(person)

#print(people[1][0])


#获取薪酬信息----方案1
#people =[bob, sue]
#pays = [person[2] for person in people]
#print(pays)

#获取薪酬信息----方案2
#people =[bob, sue]
#pays = map((lambda x: x[2]), people)
#print(list(pays))

#获取薪酬信息----输出总薪酬
#people=[bob, sue]
#MoneyCount = sum(person[2] for person in people)
#print(MoneyCount)





import string 

#去除空格
#s = '   abc   de  fg '
#print(s.strip());
#print(s.lstrip());
#print(s.rstrip());

s="a1,a2,a3"
s_1 = s.split(',')
print(s_1)
