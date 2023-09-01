# def Task1_2():
#     lst=['0001','0011','0101','1011']
#     new_lst=[]
#     for i in lst:
#         new_lst.append(int(i,2))
#     print(new_lst)
#     for i in range(0,len(new_lst),1):
#         if len(new_lst) > 2 :
#             sum = new_lst[0]+new_lst[1]
#             del new_lst[0:2]
#             new_lst.append(sum)
#             print(new_lst)
# Task1_2()
# from itertools import combinations

# lst = ['0001', '0011', '0101', '1011', '1101', '1111']
# new_lst = [int(i, 2) for i in lst]

# a = []
# for r in range(1,len(new_lst)):
#     for c in combinations(new_lst,r):
#         a.append(c)

# diff = []
# for items in a:
#     res = [i for i in new_lst if i not in items]
#     c = abs(sum(res)-sum(items))
#     diff.append(c)
#     if c==0:
#         break

#print(f"The least difference is: {sorted(diff)[0]}")

def task1_2():
    lst=['0001','0011','0101','1011','1101','1111']
    new_lst=[]
    for i in lst:
        new_lst.append(int(i,2))
    print(new_lst)
    for i in range(0,len(new_lst),1):
        if len(new_lst)>2:
            sum = new_lst[0]+new_lst[1]
            del new_lst[0:2]
            new_lst.append(sum)
    new_lst.sort()        
    print(new_lst)
task1_2()