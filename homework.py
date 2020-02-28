import re

f = open("test","r")
f = f.read()
words = re.findall(r"[A-Za-z]+",f)
# print (words)
new_words = set(words)
new_words = list(new_words)
dic = {}
for key in new_words:
    dic[str(key)] = 0
# print("new_words:",new_words)
# print("words:",words)
# print("olddic:",dic)
for r in words:
    for c in new_words:
        if r == c:
            dic[r] = dic[r]+1
print("dic",dic)

print("dic.items:",dic.items())
#sort I can't do it,how use sorted and what about x:x[1]
dic2 = sorted(dic.items(),key=lambda x:x[1],reverse=True)
print(dic2)



