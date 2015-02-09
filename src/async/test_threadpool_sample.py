from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=1)              # Start a worker processes.
    result = pool.apply_async(f, [10], callback) # Evaluate "f(10)" asynchronously calling callback when finish