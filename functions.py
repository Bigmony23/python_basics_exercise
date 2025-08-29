import random

def user_name():
    name = input("Enter your name: ").lower()
    name=name[::-1]
    num_list=list(range(0,10))
    ran_num=random.choice(num_list)
    name=name+str(ran_num)
    return name



# print(user_name())

def convert_add(nums):
    nums=[int(i) for i in nums]
    return sum(nums)
print(convert_add(['1','2','3']))
