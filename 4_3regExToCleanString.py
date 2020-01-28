# 17: \d*


# $17: \$\d* -- because '$' has its own meaning in RegEx, we need to use '\' to escape the '$' sign
# $17.00: \$\d*\.\d*: '.' match any characters -> escape '.' by '\'
# $17.89: \$\d*\.\d*{2}: because monetary value usually has 2 demcimals

# 'I have 17.89 USD'
# $17.895: ^\$\d*\.\d{2}$: '^' indicates where to start, '$' indicates where to end

# compile the pattern - use pattern to match value - reuse pattern
# Example:
# import re
# pattern = re.compile('\$\d*\.\d{2}')
# result = pattern.match('17.89') # NOTE: passing the pattern to the string we wanna match

import re
prog = re.compile('\d{3}-\d{3}-\d{4}')

result = prog.match('123-456-7890')
print(bool(result))
result2 = prog.match('1123-456-7890')
print(bool(result2))

# '+' is to find the next value, '\d*' is to take the both 1 and 0 as 10
matches = re.findall('\d'+'\d*','the recipe calls for 10 strawberries and 1 banana')
print(matches)

# revision:
# match phone number:
pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
print('phone_pattern', pattern1)
#match numerical monetary values:
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$12.32'))
print('money_pattern', pattern2)
#match a capital letter, followed by arbitrary number of alphanumeric characters
pattern3 = bool(re.match('[A-Z]\w*', 'Australia'))
print('capital_letter', pattern3)
