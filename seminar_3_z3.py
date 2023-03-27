import re

print("Введите слово: ")
def isCyrillic(text):
	return bool(re.search('[а-яА-Я]', text))
points_english = {1:'AEIOULNSTR',
    2:'DG',
    3:'BCMP',
    4:'FHVWY',
    5:'K',
    8:'JX',
    10:'QZ'}
points_russian = {1:'АВЕИНОРСТ',
    2:'ДКЛМПУ',
    3:'БГЁЬЯ',
    4:'ЙЫ',
    5:'ЖЗХЦЧ',
    8:'ШЭЮ',
    10:'ФЩЪ'}

text = input().upper()
if isCyrillic(text):
	print(sum(k for i in text for k, v in points_russian.items() if i in v))
else:
	print(sum(k for i in text for k, v in points_english.items() if i in v))