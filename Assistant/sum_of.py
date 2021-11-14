n = int(input())
s=[]

# append elements in list
for i in range(n):
    p = int(input())
    s.append(p)

even_total = 0
odd_total = 0
for i in range(n):
    if s[i] % 2 == 0: # even
        even_total += s[i]
    else: # odd
        odd_total += s[i]

# result of Code
print('sum of even :',even_total)
print('sum of odd :',odd_total)
