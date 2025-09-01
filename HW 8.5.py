nums = [2, 7, 11, 15]
target = 9
for num in nums: #перебираем все числа в списке
    for num2 in nums: #вновь перебираем все числа в списке
        if num2 > num and num + num2 == target: #первое условие - чтобы избежать дублирования; второе - чтобы приравнять к target
            print(nums.index(num), nums.index(num2))