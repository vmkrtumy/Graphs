import numpy as np


def position(l_i, l_j, n):
    i = 0
    while i < n:
        l_i.append(int(input("i: ")))
        l_j.append(int(input("j: ")))
        i += 1

def m_main(m, l_i, l_j):
    matrix = np.zeros((m, m))
    i = 0
    while i < m:
        if l_j[i] != 0:
            matrix[l_i[i] - 1][l_j[i] - 1] = 1
        i += 1
    return matrix


def t_1(l_i, l_j, n, mutq_l):
    i = 0
    while i < n:
        if l_i[i] not in l_j and l_j[i] != 0:
            mutq_l.append(l_i[i])
        i += 1
    return len(set(mutq_l))


def t_2(l_i, l_j, mij_l):
    for i in l_i:
        if i in l_j:
            mij_l.append(i)
    return len(set(mij_l))


def t_3(l_j):
    t3 = 0
    for i in l_j:
        if i == 0:
            t3 += 1
    return t3


def t_4(matrix, m):
    t4 = 0
    i, j = 0, 0
    while j < m:
        c = 0
        while i < m:
            if matrix[i][j] == 0:
                c += 1
                i += 1
        if c == m:
            t4 += 1
        j += 1

    return t4


def t_5(t3, mutq_l, n):
    return n - t3 - len(mutq_l)


def t_6(l_i, l_j, n):
    i = 0
    t6 = 0
    while i < n:
        if l_j[i] == 0 and l_j[i] in l_i:
            t6 += 1
        i += 1
    return t6


def t_7(t4, n):
    return t4 - n


def k_m_o(t7, t4):
    return t7/t4


def k_m_o_mij(k_m_l):
    return sum(k_m_l)/len(k_m_l)


def k_m(t2, m):
    return t2/m


def k_n_k(t5, t3, n):
    return t5/(n-t3)


def k_krk(t6, t3):
    return 2*t6/(t3*(t3 - 1))


def is_zero(matrix):
    return not np.any(matrix)