import sys; r = sys.stdin.readline

def sol():
    N = int(r())
    dis = [*map(int, r().split())]
    cost = [*map(int, r().split())]
    s, m = 0, 1e9
    for d, c in zip(dis, cost[:-1]):
        if c < m:
            m = c
        s += d * m
    print(s)

if __name__ == "__main__":
    sol()