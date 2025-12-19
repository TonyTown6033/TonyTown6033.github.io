import math
from itertools import combinations


def windows_for_phases(w, l):
    p = len(w)
    W = []
    for s in range(p):
        W.append(tuple(w[(s + t) % p] for t in range(l)))
    return W


def loc_len_of_period_word(w):
    p = len(w)
    for l in range(1, p + 1):  # 只需到 p，一般够区分相位
        W = windows_for_phases(w, l)
        if len(set(W)) == p:
            return l
    return None  # 说明无法区分所有相位（通常是 w 本身还有更小周期）


def build_cycle_from_period(w, m):
    p = len(w)
    return w * (m // p)


def find_best(m, n):
    best = None  # (l, p, w, cycle)

    # enumerate divisors p of m from small to large
    for p in sorted([d for d in range(1, m + 1) if m % d == 0]):
        k_num = n * p
        if k_num % m != 0:
            continue
        k = k_num // m  # ones in period word

        # brute force all binary words of length p with k ones (use pruning in practice)
        # represent word as list of 0/1
        for ones_pos in combinations(range(p), k):
            w = [0] * p
            for idx in ones_pos:
                w[idx] = 1

            l = loc_len_of_period_word(w)
            if l is None:
                continue

            cycle = build_cycle_from_period(w, m)

            if best is None or l < best[0]:
                best = (l, p, w, cycle)

        # 如果已经找到了理论下界 ceil(log2 p) ，可以提前停（可选）
        if best and best[1] == p and best[0] == math.ceil(math.log2(p)):
            pass

    return best


if __name__ == "__main__":
    m, n = input("请输入子弹总数和实弹总数，使用空格分开:  ").split(" ")
    print(f"m is {m}, n is {n}")
    result = find_best(int(m), int(n))
    print(f"最小长度为{result[0]}, 子弹装填序列为{result[-1]}，其中1为实弹0为空包弹")
