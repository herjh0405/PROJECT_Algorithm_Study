# import collections
# alpha = list(input().upper())
# result_list = collections.Counter(alpha)
# value_list = []
# for key, value in result_list.items():
#     value_list.append(value)
#
# sort_value = sorted(collections.Counter(value_list).items(), reverse=True)
# print(sort_value)
# for k, v in sort_value:
#     if v == 1 :
#         print(result_list.most_common(1)[0][0])
#         break
#     else :
#         print('?')
#         break

n = input().upper()
_sum = []
_sum2 = []

for i in set(n):
    _sum.append((n.count(i), i))
    _sum2.append(n.count(i))


a = len(_sum2)
b = len(set(_sum2))
if a == b :
    x = [max(_sum)]
    print(x[0][-1])
else:
    print('?')