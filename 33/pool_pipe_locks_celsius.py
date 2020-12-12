import multiprocessing as mp


def to_celcius(child_pipe: mp.Pipe, child_lock: mp.Lock):
    child_lock.acquire(blocking=False)
    try:
        f = child_pipe.recv()
    finally:
        child_lock.release()
    # time-consuming task ... release lock before processing
    c = (f - 32) * (5/9)
    # reacquire lock when done
    child_lock.acquire(blocking=False)
    try:
        child_pipe.send(c)
    finally:
        child_lock.release()


if __name__ == '__main__':
    mp.set_start_method('spawn')
    pool_manager = mp.Manager()
    with mp.Pool(2) as pool:
        parent_pipe, child_pipe = mp.Pipe()
        child_lock = pool_manager.Lock()
        results = []
        for i in range(110, 150, 10):
            parent_pipe.send(i)
            results.append(pool.apply_async(to_celcius, args=(child_pipe, child_lock)))
            print(parent_pipe.recv())
        parent_pipe.close()
        child_pipe.close()
