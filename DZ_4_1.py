import json
file = open('purchase_log.txt','r', encoding = 'utf-8')
# for line in range(1,50):
dict = file.readlines()
print(dict[1:10])
print(type(dict))
# dict = json.loads(list)
# print(dict)
#spisok = {}
# dict_new = {}
# for line in list:
#     dict = json.loads(line)
#     dict_new.append = dict
# print(dict_new)
#
# print(list[0:5])

