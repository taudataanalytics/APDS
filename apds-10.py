from multiprocessing import Pool
import math

def cpu_task(n):
    return sum(math.sqrt(i) for i in range(n))

if __name__ == "__main__":
    data = [10**7] * 4

    with Pool(4) as pool:
        results = pool.map(cpu_task, data)

    print(results)