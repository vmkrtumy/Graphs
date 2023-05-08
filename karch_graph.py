def min_(u_l, item, l_i, l_j, d, n):
    i = 0
    index = []
    while i < n:
        if l_j[i] == item:
            index.append(i)
        i+=1
    minimum = u_l[l_i[index[0]] - 1][0] + d[index[0]]
    min_i = index[0]
    for k in range(1, len(index)):
        min1 = u_l[l_i[index[k]] - 1][0] + d[index[k]]
        if min1 < minimum:
            minimum = min1
            min_i = index[k]
    min_l = [minimum, l_i[min_i]]
    return min_l

def u_calc(u_l, bubbles, l_i, l_j, d):
    for i in range(1, bubbles):
        u_l.append(min_(u_l, i + 1, l_i, l_j, d, n))

def position_2(l_i, l_j, d, n):
    i = 0
    while i < n:
        l_i.append(int(input("i: ")))
        l_j.append(int(input("j: ")))
        d.append(int(input("d: ")))
        i += 1
l_i = []
l_j = []
d = []
u_l = [[0, 1]]
bubbles = int(input("input bubble num: "))
n = int(input("input ties num: "))
position_2(l_i, l_j, d, n)
u_calc(u_l, bubbles, l_i, l_j, d)
print("Ամենակարճ ճանապարհն է։ ")
i = bubbles
res = []
while i != 1:
    res.append(i)
    res.append("->")
    i = u_l[i - 1][1]
res.append(1)
for i in res:
    print(i, end='')