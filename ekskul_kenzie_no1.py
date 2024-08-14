a=input ("masukkan kata:  ")
a2 = a.casefold()
lena=len(a2)
b=[]
for i in range(lena - 1, -1, -1):
    b.append(a2[i])
rev = "".join(b)
if a2 == rev:
    print(a, "merupakan kata/kalimat polindrom")
else:
    print(a, "bukan kata/kalimat polindrom")
    
reverse = ""
for char in a:
    reverse = char + reverse
print("dibalik dengan case sensitive: " + str(reverse))
