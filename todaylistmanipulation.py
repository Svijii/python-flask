num = [2,3,4,5,6]
print("initial list:",num)
sqr_num = [x **2 for x in num]
print("sqr_num:",sqr_num)
sorted_num = sorted(sqr_num, reverse=True)
print("sorted numbers:",sorted_num)
filtered_num = [x for x in sorted_num if x %2!=0]
print("filtered_num:",filtered_num)
