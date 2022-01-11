# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
if __name__ == "__main__":
    d = int(input("Day: "))
    m = int(input("Month: "))
    y = int(input("Year: "))
    if d * m == y - y // 100 * 100:
        print(True)
    else:
        print(False)