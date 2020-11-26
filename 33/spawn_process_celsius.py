import multiprocessing as mp
import os


def to_celsius(f):
    c = (f - 32) * (5/9)
    pid = os.getpid()
    print(f"{f}F is {c}C (pid {pid})")


if __name__ == '__main__':
    mp.set_start_method('spawn')
    p = mp.Process(target=to_celsius, args=(110,))
    p.start()