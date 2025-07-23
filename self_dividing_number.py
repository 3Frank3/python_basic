

a = input("type your input1 :" )
b = input("type your input2 :" )

d = []
for i in range(int(a), int(b)+1):
    is_self_dividing = True
    for j in str(i):
        if j == '0' or i % int(j) != 0:
            is_self_dividing = False
            break
    if is_self_dividing:
        d.append(i)

max_gap = 0
max_pair = ()

for i in range(len(d)-1):
    c = d[i+1] - d[i]
    if c > max_gap:
        max_gap = c
        max_pair = (d[i], d[i+1])

print("output:")
print("max_gap:", max_gap, "between", max_pair)