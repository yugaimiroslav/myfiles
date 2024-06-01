import threading
import time
import requests


def math_solve():
    #for i in range(1000000):
    #    round((i**2 / 122) + i * 3.14)
    requests.get('https://yandex.ru')

def run(flag=False):
    start = time.time()
    if not flag:
        for _ in range(10):
            math_solve()

    else:
        threats = [threading.Thread(target=math_solve, daemon=True) for _ in range(10)]
        for threat in threats:
            threat.start()
        for threat in threats:
            threat.join()

    end = time.time()
    print(f'time in seconds: {end - start}')

run(flag=True)