

encoded_list = 
    [5,10,11,12,12,14,16,17,18,20],


    
def find_consecutive_pairs(arr):
    
 for j in arr:   
    i=0
    while i < (len(arr)-2):
                print("i:-",i)
                if(len(arr)>=3):
                    
                    pair = [arr[i],arr[i+1],arr[i+2]]
                    # print(pair)
                    if (pair[1]==(pair[0]+1) and pair[2]==pair[1]+1):
                       num1 = pair[0]
                       num2 = pair[1]
                       num3 = pair[2]
                       arr.remove(num1)
                       arr.remove(num2)
                       arr.remove(num3)
                       i = i-1
                       print(arr)
                    else:
                       i = i+1
print(find_consecutive_pairs(encoded_list))

