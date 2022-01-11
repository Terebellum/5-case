# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
if __name__ == "__main__":
    n = int(input())
    s = set(range(2, n+1))
    l = []
    while s:
        m = min(s)
        l.append(m)
        s -= set(range(m, n+1, m))
    if n in l:
        print(True)
    else:
        print(False)