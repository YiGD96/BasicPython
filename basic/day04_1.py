import re
p = re.compile('ab*')

print(p.match('cabcde')) 
print(p.match('abcde')) # 첫글자부터 같은 것만 찾아줌
print(p.search('cabsdaf')) # 중간에 같기만하면됨
