def double_agr_function(arg1, arg2):
     if type(arg1) in (int, float):
         if type(arg2) in (int, float):
             res = arg1 * arg2
             return res
     elif type(arg1) is (str):
         if type(arg2) is (str):
             res = arg1 + arg2
             return res
     else:
         res = tuple((arg1, arg2))
         return res



result1 = double_agr_function(5, 3)
print(f'Результат 1: {result1}')

result2 = double_agr_function('Hello, ', 'world!')
print(f'Результат 2: {result2}')

result3 = double_agr_function(7, 'string')
print(f'Результат 3: {result3}')
