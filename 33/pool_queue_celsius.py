import multiprocessing as mp


def to_celsius(input: mp.Queue, output: mp.Queue):
    f = input.get()
    # time-consuming task ...
    c = (f - 32) * (5/9)
    output.put(c)


if __name__ == '__main__':
    mp.set_start_method('spawn')
    pool_manager = mp.Manager()
    with mp.Pool(2) as pool:
        inputs = pool_manager.Queue()
        outputs = pool_manager.Queue()
        input_values = list(range(110, 150, 10))
        for i in input_values:
            inputs.put(i)
            pool.apply(to_celsius, (inputs, outputs))

        for f in input_values:
            print(outputs.get(block=False))
