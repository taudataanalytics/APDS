import multiprocessing as mp

def f(x):
    return x*x

if __name__ == '__main__':
    print('Number of currently available processor = ', mp.cpu_count())
    N = mp.cpu_count()
    input_ = [1, 2, 3, 4, 5, 7, 9, 10]
    print('input = ', input_)
    with mp.Pool(N) as p:
        print(p.map(f, input_))