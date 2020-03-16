import multiprocessing as mp

def to_celcius(child_pipe: mp.Pipe, parent_pipe: mp.Pipe,
               child_write_lock: mp.Lock, parent_read_lock: mp.Lock):
    parent_read_lock.acquire()
    try:
        f = parent_pipe.recv()
    finally:
        parent_read_lock.release()
    # time-consuming task ...
    c = (f - 32) * (5/9)

    child_write_lock.acquire()
    try:
        child_pipe.send(c)
    finally:
        child_write_lock.release()

if __name__ == '__main__':
    mp.set_start_method('spawn')
    pool_manager = mp.Manager()
    with mp.Pool(2) as pool:
        parent_pipe, child_pipe = mp.Pipe()
        parent_read_lock = mp.Lock()
        child_write_lock = mp.Lock()
        results = []
        for i in range(110, 150, 10):
            parent_pipe.send(i)
            pool.apply_async(to_celcius, args=(child_pipe, parent_pipe,
                                               child_write_lock,
                                               parent_read_lock))
            print(child_pipe.recv())
        parent_pipe.close()
        child_pipe.close()