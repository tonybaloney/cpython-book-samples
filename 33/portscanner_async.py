import time
import asyncio

timeout = 1.0


async def check_port(host: str, port: int, results: list):
    try:
        future = asyncio.open_connection(host=host, port=port)
        r, w = await asyncio.wait_for(future, timeout=timeout)
        results.append(port)
        w.close()
    except OSError:  # do not throw an exception when port is not open
        pass
    except asyncio.TimeoutError:
        pass # closed


async def scan(start, end, host):
    tasks = []
    results = []
    for port in range(start, end):
        tasks.append(check_port(host, port, results))
    await asyncio.gather(*tasks)
    return results


if __name__ == '__main__':
    start = time.time()
    host = "localhost"
    results = asyncio.run(scan(80, 100, host))
    for result in results:
        print("Port {0} is open".format(result))
    print("Completed scan in {0} seconds".format(time.time() - start))
