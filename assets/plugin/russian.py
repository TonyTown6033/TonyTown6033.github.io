def localization_length(B: str) -> int:
    # B is a '0'/'1' string representing a cycle
    m = len(B)
    bits = [int(c) for c in B]

    # R(i): rotation starting at i, length m (tuple as signature)
    R = []
    for i in range(m):
        R.append(tuple(bits[(i + t) % m] for t in range(m)))

    # try l from 1..m
    for l in range(1, m + 1):
        seen = {}
        ok = True
        for i in range(m):
            W = tuple(bits[(i + t) % m] for t in range(l))
            sig = R[i]
            if W not in seen:
                seen[W] = sig
            else:
                if seen[W] != sig:
                    ok = False
                    break
        if ok:
            return l

    # theoretically l=m always works for this "relative" definition,
    # but keep a fallback
    return m


print(localization_length("001001001"))  # -> 3
print(localization_length("001000101"))  # -> 5
