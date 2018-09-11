#定义数据文件
people={
    'A':{
        'phone':'1234',
        'age':'20'
        },
    'B':{
        'phone':'3333',
        'age': '24'
        },
    'C':{
        'phone':'3214',
        'age': '26'
        }
    }

#定义标签
labels={
    'phone':'phone number',
    'age':'years old'
    }

name = input('Please input your name:')

request = input('1)P:phone number \n2)O:years old\nPlease input:')

if request=='P': key ='phone'
if request=='O': key ='age'

if name in people:print("{0}'s {1} is {2}".format( name, labels[key], people[name][key]))