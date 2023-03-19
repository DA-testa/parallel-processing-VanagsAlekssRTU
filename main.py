# python3
from queue import PriorityQueue

def parallel_processing(n, m, data):
    output = []
    threads = PriorityQueue()

    for i in range(n):
        threads.put((0, i))

    for i in range(m):
        time, thread = threads.get()
        output.append((thread, time))
        threads.put((time + data[i], thread))

    return output

def main():
    n, m = map(int, input().split())

    if not ((1 <= n <= 10**5) or (1 <= m <= 10**5)):
        print("Invalid input for n or m")
        exit()

    data = list(map(int, input().split()))

    if not (len(data) == m):
        print("m and data lengths don't match")
        exit()
    for i in range(m):
        if not (0 <= data[i] <= 10**9):
            print("Invalid input for data")
            exit()
    
    result = parallel_processing(n,m,data)

    for i, j in result:
        print(i, j)



if __name__ == "__main__":
    main()
