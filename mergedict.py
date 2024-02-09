dict1 = {'mango':9,'orange':6,'apple':5}
dict2 = {'banana':5,'cherry':3}
#dict2.update(dict1)
#print(dict2)
merged_list = {**dict2,**dict1}
print(merged_list)
