n = int(input())
s=[]
for i in range(n):
    p = int(input())
    s.append(p)

even_total = 0
odd_total = 0
for i in range(n):
    if s[i] % 2 == 0:
        even_total += s[i]
    else:
        odd_total += s[i]

print('sum of even :',even_total)
print('sum of odd :',odd_total)
