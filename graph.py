import math
from matrix import *

l_i = []
l_j = []
mutq_l = []
mij_l = []
n = int(input("input n"))
position(l_i, l_j, n)
m = int(input("input number of bubbles"))
a1 = m_main(m, l_i, l_j)
t1 = t_1(l_i, l_j, n, mutq_l)
t2 = t_2(l_i, l_j, mij_l)
t3 = t_3(l_j)
m1 = a1
t5 = t_5(t3, mutq_l, n)
t6 = t_6(l_j, l_j, n)
t4 = []
t7 = []
N = 0
kmo = []
sigma = a1
while True:
    if is_zero(m1):
        break
    else:
        t4.append(t_4(m1, m))
        t7.append(t_7(t4[N], n))
        kmo.append(k_m_o(t7[N], t4[N]))
        N += 1
        m1 = np.dot(m1, a1)
        print(m1)
        sigma = np.add(sigma, m1)
kmo_mij = k_m_o_mij(kmo)
km = k_m(t2, m)
print("Բարդության աստիճանը հավասար է ", km)
eps = float(input("input the epsilion"))
if math.fabs(km - kmo_mij) <= eps:
    print("Կազմակերպված է ռացիոնալ կերպով")
knk = k_n_k(t5, t3, n)
print("Կապակցվածության աստիճանը հավասար է", knk)
kkrk = k_krk(t6, t3)
print("Ելքային ինֆորմացիայի ավելցուկության չափը հավասար է ", kkrk)
print("Ամենա երկար ճանապարհը հավասար է ", N)