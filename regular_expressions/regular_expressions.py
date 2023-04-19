# https://regex101.com/  -- to test regex
# https://regexone.com/  -- interactive tutorial and exercises

import re

string = 'search this inside of this text'

pattern = re.compile('this')
pattern2 = re.compile('search this inside')

a = re.search('this', string)
print(f'span: {a.span()}')
print(f'start: {a.start()}')

print(f'pattern-findall: {pattern.findall(string)}')
print(f'pattern-match: {pattern2.match(string)}')  # matches from start, not 'till the end
print(f'pattern-fullmatch: {pattern.fullmatch(string)}')  # matches from start to end

# r: raw string - ignores special characters, like '\'
# ([a-zA-Z]).([a]) --> search for [any letter] followed by [anything] followed by [a]
pattern3 = re.compile(r'([a-zA-Z]).([a])')
b = pattern3.search(string)
print(f'pattern-search-regex: {b.group()}')
print(f'pattern-search-regex: {b.group(1)}')
print(f'pattern-search-regex: {b.group(2)}')


email = 'juan@python.com'
email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
e = email_regex.search(email)
print(f'email-validator: {e}')

password = '$mostsaf-#e123'
pwd_regex = re.compile(r'([A-Za-z0-9$%#@]{8,})')  # accept letters and numbers, symbols $%#@ and 8+ char long
check = pwd_regex.fullmatch(password)
print(f'password-validator: {check}')
