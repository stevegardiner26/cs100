# Steven Gardiner
# CS 100 2018S Section 004
# HW 06, February 14, 2018

# Question 1
# 1a


def has_final_letter(strList, letters):
    alist = []
    for item in strList:
        if item[-1] in letters:
            alist.append(item)
    return alist


# 1b
slist = ['Hello', 'Wyat', 'JeromA', 'Appam', 'Wap']
lettas = 'Amaw'
print(has_final_letter(slist, lettas))

slist = ['Hyatt', 'NextLevel', 'Aquire', 'Appam', 'Waaall']
lettas = 'apsd1'
print(has_final_letter(slist, lettas))

slist = ['MERICA', 'IRELANAD', 'ITALY', 'Ukraine', 'Russia']
lettas = 'AEIOU'
print(has_final_letter(slist, lettas))


# Question 2
# 2a
def is_divisible(max_int, two_ints):
    alist = []
    for num in range(1, max_int):
        if (num % two_ints[0] == 0) and (num % two_ints[1] == 0):
            alist.append(num)
    return alist


# 2b

maximum = 50
two = (2, 5)
print(is_divisible(maximum, two))

maximum = 20
two = (2, 10)
print(is_divisible(maximum, two))

maximum = 10
two = (10, 12)
print(is_divisible(maximum, two))
