import multiprocessing as mp

def f_sum(a, b):
    return a + b

if __name__ == '__main__':
    data = [(1, 1), (2, 1), (3, 1), (6, 9)]
    process_pool = mp.Pool(4)
    output = process_pool.starmap(f_sum, data)
    print("input = ", data)
    print("output = ", output)