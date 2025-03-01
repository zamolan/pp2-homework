import re

test = "a ab abb abbb axyzb lower_case_words UPPERlower CamelCaseString AnotherCamelCase some_text_with_underscores ThisIsATest"
test7 = "snake_case_example"
test8 = "SplitThisStringAtUppercaseLetters"
test10 = "CamelCaseExample"

pat1 = r"\ba{1}b*\b"
pat1res = re.findall(pat1, test)
print(*pat1res)

pat2 = r"\ba{1}b{2,3}\b"
pat2res = re.findall(pat2, test)
print(*pat2res)

pat3 = r"\b[a-z]\b"
pat3res = re.findall(pat3, test)
print(*pat1res, sep='_')

pat4 = r"\b(?:[A-Z]*[a-z]+)[A-Z][a-z]+(?:[A-Z]*[a-z]*)\b"
pat4res = re.findall(pat4, test)
print(*pat4res)

pat5 = r"\ba[^ ].+b\b" 
pat5res = re.findall(pat5, test)
print(*pat5res)

pat6 = re.sub("\s", ":", test)
pat6res = re.sub(",", ":", pat6)
pat6 = re.sub(".", ":", pat6res)
print(pat6res)

pat7 = re.split("_", test7)
for i in pat7:
    print(i[0].upper()+i[1:], end="")
print('\n')

pat8 = re.findall(r'[A-Z][a-z]*', test8)
print(*pat8) #9

pat10 = re.findall(r'[A-Z][a-z]*', test10)
for i in pat10:
    print(i[0].lower()+i[1:], end='')
    if(i != pat10[len(pat10) - 1]):
        print('_', end='')