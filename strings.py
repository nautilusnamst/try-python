s = "Hello world, this is special"
res = s.split(",")
print(res)

print('C:\new\text.dat')

# Пример неформатированной строки (символ r перед строкой) - в ней спецсимволы не работают
print(r'C:\new\text.dat')

myjob = "hacker"
for c in myjob: print(c, end=' ')     # Step through items

print()
print("k" in myjob)
print("z" in myjob)

#
# Доступ по индексам и извлечение подстроки
#

print('-----------------------------------')

S = 'spam'
print(S[0], S[-2])               # Indexing from front or end
print(S[1:3], S[1:], S[:-1])     # Slicing: extract a section

S = 'abcdefghijklmnop'
print(S[1:10:2])
print(S[::2])
S = 'hello'
print(S[::-1])
S = 'abcedfg'
print(S[5:1:-1])
print('spam'[1:3])              # Slicing syntax
print('spam'[slice(1, 3)])      # Slice objects
print('spam'[::-1])
print('spam'[slice(None, None, -1)])

# преобразование строк

print(int("42"), str(42))      # Convert from/to string
print(repr(42))                # Convert to as-code string
print(str('spam'), repr('spam'))

#
# Строковые методы
#

print("----------------------------")

S = 'spammy'
print(S.replace('mm', 'xx'))
print('aa$bb$cc$dd'.replace('$', 'SPAM'))

S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')                # Search for position
print(where)                          # Occurs at offset 4
S = S[:where] + 'EGGS' + S[(where+4):]
print(S)

S = 'xxxxSPAMxxxxSPAMxxxx'
print(S.replace('SPAM', 'EGGS'))         # Replace all
print(S.replace('SPAM', 'EGGS', 1))      # Replace one
'xxxxEGGSxxxxSPAMxxxx'

S = 'spammy'
L = list(S)
print(L)
L[3] = 'x'                         # Works for lists, not strings
L[4] = 'x'
print(L)
S = ''.join(L)
print(S)
print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))

#
# Форматирование строк
#

print("--------------------")

print('That is %d %s bird!' % (1, 'dead'))      # Format expression
# ADDED: the new method equivalent
print('That is {0:d} {1:s} bird!'.format(1, 'dead'))
exclamation = "Ni"
print("The knights who say %s!" % exclamation)
print("%d %s %d you" % (1, 'spam', 4))
print("%s -- %s -- %s" % (42, 3.14159, [1, 2, 3]))
x = 1234
print("integers: ...%d...%-6d...%06d" % (x, x, x))

x = 1.23456789
print(x)
print('%e | %f | %g' % (x, x, x))
print('%E' % x)
print('%-6.2f | %05.2f | %+06.1f' % (x, x, x))
print("%s" % x, str(x))
print('%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0))
print("%(n)d %(x)s" % {"n":1, "x":"spam"})
reply = """
Greetings...
Hello %(name)s!
Your age squared is %(age)s
"""

values = {'name': 'Bob', 'age': 40}       # Build up values to substitute
print(reply % values)
template = '{0}, {1} and {2}'                    # By position
print(template.format('spam', 'ham', 'eggs'))
template = '{motto}, {pork} and {food}'          # By keyword
print(template.format(motto='spam', pork='ham', food='eggs'))
template = '{motto}, {0} and {food}'             # By both
print(template.format('ham', motto='spam', food='eggs'))
print('{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2]))
print('{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2]))

# UTF-8

print("Тест русского")