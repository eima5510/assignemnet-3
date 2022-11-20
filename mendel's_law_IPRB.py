def iprb(k, m, n):
    i = m * m + 4 * n * n + 4 * m * n - 4 * n - m
    j = 4 * (k + m + n) * (k + m + n - 1)
    rst = 1 - float(i) / j
    return rst

if __name__ == "__main__":
    data_set = "22 17 26"
    k, m, n = map(int, data_set.strip().split(" "))
    print(iprb(k, m, n))