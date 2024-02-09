mydict = {'ravi': 10,'raji':9,'sanjeev':15,'yash':2,'suji': 32}
sorted_keys = sorted(mydict)
print(sorted_keys)
sorted_keys = {i:mydict[i] for i in sorted_keys}
print(sorted_keys)
