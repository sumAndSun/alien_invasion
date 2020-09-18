# print('Hello World！')
# message = 'Hello World！'
# message = 'he he !'
# print(message.title())
# print(message.upper())
# print(message.lower())
# print('\t' + message.lower())
# name = ' 大傻子 ';
# print(name + 'say ' + message)
# print(name)
# # print(name.rstrip())
# print(name.lstrip())
# # print(name.strip())

# name = ' 大傻子 '.strip()
# name = 'eric'.title()
# name = 'eric'.upper()
# name = 'Eric'.lower()
# message = 'Hello \n\t' + name + ',would you like to learn some Python today?'
# print(message)

# age = 26
# print('the '+str(age)+' younter')
#
# print(5+3)
# print(16-8)
# print(64/8)
# print(2*4)
# message = '我最喜欢的数字是' + str(2*4)
# print(message)
#
# import this

# fruits = ['苹果', '梨子', '香蕉', '板栗']
# str = '是有营养的水果';
# # print(fruits)
# # print(fruits[0]+str)
# # print(fruits[1]+str)
# # print(fruits[2]+str)
# # print(fruits[-1]+str)
#
# fruits[-1] = '自行车'
# print(fruits[-1]+str)
# print(fruits)
# fruits.append("地铁")
# print(fruits)
#
# # 在输出中，直接在数组中追加效果是无效的，输出是None
# # print(fruits.append("地铁A"))
#
# # 在索引为2的地方插入
# fruits.insert(2, '猕猴桃')
# print(fruits)
#
# # 在输出中，直接在数组中插入效果是无效的，输出是None
# # print(fruits.insert(2, '猕猴桃A'))
#
# # del语句
# del fruits[-1]
# print(fruits)
#
# # pop()方法删除末尾
# del_fruit = fruits.pop()
# print(fruits)
# print(del_fruit)
# print('--------------------')
# del_fruit = fruits.pop(0)
# print(fruits)
# print(del_fruit)
# print('--------------------')
# fruits.remove('猕猴桃')
# print(fruits)
#
# print('--------------------')
# fruits = ['苹果', '梨子', '苹果', '苹果']
# # 只删除第一个存在的值，如全部相同值移除利用循环
# fruits.remove('苹果')
# print(fruits)

# family = ['妈妈', '爸爸', '哥哥', '姐姐', '弟弟', '妹妹']
# thing = '共进晚餐'
# # 函数
# print('共邀请了' + str(len(family)) + '位' + thing)
# print(family[0]+thing)
# print(family[1]+thing)
# print(family[2]+thing)
# print(family[3]+thing)
# print(family[4]+thing)
# print(family[-1]+'无法参加，更换成表弟')
# family[-1] = '表弟'
# print(family[-1]+thing)
# print('新增三个家庭成员:')
# family.insert(0, '表妹')
# family.insert(3, '姨妈')
# family.append('舅妈')
# print(family)
# print('最后只能邀请2位参加:')
# family.pop(0)
# family.pop(-1)
# family.pop(-1)
# family.pop(2)
# family.pop(2)
# family.pop(2)
# family.pop(2)
# print('最后参加的是:')
# print(family)
# del family[0]
# print(family)
# family.remove('爸爸')
# print(family)


# places = ['A', 'D', 'B', 'Z', 'Y']
# print(places)
# # 并未真实改变
# print(sorted(places))
# print(places)
# places.reverse()
# #print(sorted(places, reverse=True))
# print(places)
# places.reverse()
# print(places)
# places.sort()
# print(places)
# places.sort(reverse = True)
# print(places)


# foods = ['A', 'B', 'C', 'D', 'E']
# for food in foods:
#     print(food)
#     print('I like ' + food)
# print('I really love' + foods[0])
#
# animals = ['老虎', '鳄鱼', '北极熊', '狮子']
# for animal in animals:
#     print(animal + "是动物")
# print('都非常可爱')

# nums = range(1, 21)
# # for num in nums:
# #     print(num)
# # for number in range(1, 100):
# #     print(number)
# # print(min(nums), max(nums), sum(nums))
# numList = list(nums)
# print(numList)
# print(numList[2: 3])
# newList = []
# for num in nums:
#     if num % 2 == 1:
#         print(num)
#         print("立方：" + str(num**3))
#         newList.append(num**3)
# print(newList)
# print(newList[0: 3])
# print(newList[-3: ])
# new_nums = newList[:]
# new_nums.append(22)
# for new_num in new_nums:
#     print(new_num)

# foods = ('A', 'B', 'C', 'D', 'E')
# for food in foods:
#     print(food)
# # foods[0] = 'AA'
# # print(foods)
# foods = ('AA', 'BB', 'C', 'D', 'E')
# for food in foods:
#     print(food)

# foods = ('A', 'B', 'C', 'D', 'E')
# for food in foods:
#     if food == 'A':
#         print("我最喜欢的字母")
#     else:
#         print("我不喜欢的字母")
#
#     if 'a'.lower() == 'A' and 'b'.lower() == 'B':
#         print("存在")
# if 'P' not in foods:
#     print("元组中不存在P")

# alien_color = ['green', 'yellow', 'red']
# for color in alien_color:
#     if 'green' == color:
#         print('恭喜获得5个点！')
#     elif 'yellow' == color:
#         print('恭喜获得10个点！')
#     else:
#         print('恭喜获得15个点！')

# users = ['admin', 'taming', 'Kansan', 'leis', 'wangle']
# del users[0]
# del users[1]
# users.remove('taming')
# users.pop(0)
# users.pop(0)
# print(users)
# if users:
#     for user in users:
#         print("欢迎"+user+"进入天唐部分！")
#         if 'admin' == user:
#             print('Hello '+user+' ,would ou like to see a status report?')
#         else:
#             print('Hello '+user+' thank you for logging in again.')
#
# else:
#     print('我们需要用户~')

# current_users = ['A', 'B', 'C', 'D', 'E']
# new_users = ['AA', 'BB', 'CC', 'd', 'e']
# current_users_upper = [i.upper() for i in current_users]
# new_users_upper = [i.upper() for i in new_users]
# for user in new_users_upper:
#     if user in current_users_upper:
#         print(user + '请输入别的用户名称！')
#     else:
#         print('该用户名未被使用！')


# user = {'first_name': 'zhang', 'last_name': 'san', 'age': 20, 'city': 'shenzhen'}
# # print(user['first_name'] + user['last_name'] + str(user['age']) + user['city'])
# # for k, v in user.items():
# #     print(k)
# nums = {}
# nums['张三'] = '1'
# nums['李四'] = '2'
# nums['王五'] = '3'
# print(nums)

# rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china', 'mississippi': 'us'}
# for k, v in rivers.items():
#     print('The ' + k + ' runs thought ' + v + '.')
#     print(k)
#     print(v)

# user = {'zhangsna': 'Y', 'lis': 'Y', 'wangwu': 'N', 'zhaoliu': 'N'}
# for k ,v in user.items():
#     if v == 'Y':
#         print('Thank you!')
#     else:
#         print('请参加调查！')

# user_one = {'first_name': 'zhang', 'last_name': 'san', 'age': 20, 'city': 'shenzhen'}
# user_two = {'first_name': 'li', 'last_name': 'si', 'age': 10, 'city': 'shanghai'}
# user_three = {'first_name': 'wang', 'last_name': 'wu', 'age': 30, 'city': 'sichuan'}
# people = [user_one, user_two, user_three]
# for user in people:
#     print(user)

# dog = {'type': 'A', 'master': 'AA'}
# cat = {'type': 'B', 'master': 'BB'}
# pets = [dog, cat]
# for pet in pets:
#     print(pet['type'], pet['master'])

# favorite_places = {
#                       'A': ['xizang', 'yunnan', 'chengdu'],
#                       'B': ['beijing', 'shanghai', 'sichuan'],
#                       'C': ['hebei', 'guizhuo', 'henan']
#                    }
# for k, v in favorite_places.items():
#     print(k)
#     for place in v:
#         print('\t'+place)

#
# cities = {
#     'xizang':{
#         'country':'A',
#         'population':1000,
#         'fact':'AAAAAAAAAA'
#     },
#     'yunnan': {
#         'country': 'B',
#         'population': 2000,
#         'fact': 'BBBBBBB'
#     },
#     'chengdu': {
#         'country': 'C',
#         'population': 3000,
#         'fact': 'CCCCCCCC'
#     }
# }
#
# for city, info in cities.items():
#     print(city)
#     print('\t' + info['country'])
#     print('\t' + str(info['population']))
#     print('\t' + info['fact'])
#
# # 添加字典
# cities['mei'] = {
#     'country': 'D',
#     'population': 3100,
#     'fact': 'DDDDD'
# }
# print(cities)
# # 修改
# cities['chengdu'] = {
#     'country': '修改',
#     'population': 3100,
#     'fact': 'DDDDD'
# }
# print(cities)
#
# # 删除
# del cities['xizang']
# print(cities)
#
# # 单独打印chengdu
# print(cities['chengdu'])

# 输入回答
# car = input('请问租赁什么样的汽车？\n')
# print('Let me see if I can find you a'+car)

# num = input('请问有多少人用餐？\n')
# if int(num) > 8:
#     print('没有空桌~')
# else:
#     print('有空桌~')

# num = input('请输入一个数字：\n')
# if int(num) % 10 == 0:
#    print('能被10整除')
# else:
#     print('不能被10整除')

# name = '请输入你喜欢的披萨配料\n'
# name += '(Enter "quit" when you are finished)'
# # flag = True
# names = []
# while True:
#     say = input(name)
#     if say != 'quit':
#         # flag = False
#         print('我们会将['+say + ']加入到你的披萨中~')
#         names.append(str(say))
#         continue
#     else:
#         break
# print(names)

# question = '请问你的年龄是多少？\n(Enter "quit" when you are finished)'
# active = True
# while active:
#     age = input(question)
#     if str(age) == 'quit':
#         break
#     if int(age) < 3:
#         print('免费')
#     elif 3 < int(age) < 12:
#         print('$10')
#     else:
#         print('$15')

# sandwich_orders = ['A', 'B', 'C', 'A', 'A', 'A']
# print('去除列表中存在的重复值之后：')
# print(set(sandwich_orders))
# print(sandwich_orders)
# finisded_sandwiches = []
# print('A已经卖完了~')
# while 'A' in sandwich_orders:
#     sandwich_orders.remove('A')
# for sandwich in sandwich_orders:
#     print('I made your ' + sandwich)
#     finisded_sandwiches.append(sandwich)
# print(finisded_sandwiches)

# 函数
# def display_message():
#     print('本章学习函数定义和调用~')
# display_message()

# def favorite_book(title):
#     print('One of my favorite books is ' + title)
# favorite_book('Alice in Wonderland')


# def make_shirt(size, logo):
#     print('制作的尺寸：' + str(size) + ' 字样：' + logo)
#
#
# make_shirt(size='M', logo='A')
# make_shirt('M', 'I love Python')

# def decribe_city(city, location = 'Iceland'):
#     print(city+location)
# decribe_city('Reykjavik')
#
# decribe_city('ci','A')


# def city_contry(name,age):
#     return name + str(age)
#
# print(city_contry('A',23))
# zhuanji = []
# def make_album():
#     music = [{'name': 'A', 'zhuanji': 'AA'}, {'name': 'B', 'zhuanji': 'BB'}, {'name': 'C', 'zhuanji': 'CC'}]
#     for a in music:
#         a['num'] = ''
#         zhuanji.append(a['zhuanji'])
#         if a['name'] == 'A':
#             a['num'] = 10
#     print(music)
#     return zhuanji
# print(make_album())


#
# def make_album():
#     singers = {}
#     flag = True
#     while flag:
#         singer =input('请输入你喜欢的歌手：\n')
#         zhuanji = input('请输入'+singer+'的专辑\n')
#         singers[singer] = zhuanji
#         if input('是否退出？ Y/N') == 'Y':
#             flag = False
#     """ 打印 """
#     print(singers)
#     return singers
#
# for k,v in make_album().items():
#     print('喜欢' + k + '的' + v)


# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician)
# def make_great(magicians):
#     new_magicians = []
#     for magician in magicians:
#         new_magicians.append(magician + 'the Great')
#     return new_magicians
#
# magicians = ['A', 'B', 'C']
# show_magicians(make_great(magicians))

# def print_models(lista,listb):
#     while lista:
#         a = lista.pop()
#         listb.append(a)
# def show_models(listb):
#     for b in listb:
#         print(b)
#
# lista = ['A', 'B' ,'C']
# listb = []
# print_models(lista[:],listb)
# show_models(listb)
# print(lista)
# print(listb)

# def make_sandwisheds(*topping):
#     for a in topping:
#         print(a)
# 实参
# make_sandwisheds('a', 'B', 'C')
# make_sandwisheds('asa', 'sdd', 'sdsd')
# make_sandwisheds('qw', 'we', 'e')

# 关键字实参
# def car(make,xingh,**infos):
#     str = ''
#     print(infos)
#     for k, v in infos.items():
#         str += k + v
#     print(make+xingh+str)
# car('subaru','outback',color='blue',top_color='black')