# -*- coding: utf8 -*-

# -----------------------------------------------------------
# A sleep-sort algorithm implemented as a multi-threaded
# program to check a maximal performance of this sorting.
#
# (C) 2022 Naive Experimentalist, Gdańsk, Poland
# Released under GNU Public License (GPL)
# -----------------------------------------------------------


from time import sleep, time
from queue import Queue
from threading import Thread, Event
import random


def spit_it_out(n: int, que: Queue, gl: Event) -> None:
    gl.wait()  # waiting for the green light from the main thread
    sleep(n/20)  # carefully calibrated
    que.put(n)


if __name__ == "__main__":
    a = random.choices(range(0, 40), k=4095)  # the wider range, the less likely it's going to be sorted properly
    print(a)
    threads = []
    q = Queue(len(a))
    green_light = Event()
    p2 = time()
    for i, k in enumerate(a):
        t = Thread(target=spit_it_out, args=(k, q, green_light))
        threads.append(t)
        t.start()
    p3 = time()
    # green light for threads to start sleep&return procedure
    green_light.set()
    for t in threads:
        t.join()
    p4 = time()
    b = list(q.queue)
    p5 = time()
    # sort with built-in implementation
    c = sorted(a)
    p6 = time()

    if b != c:
        print('FALSE!')
    else:
        print(f'         total time: {p4-p2}')
        print(f'thread warm-up time: {p3-p2}')
        print(f'    sleep&sort time: {p4-p3}')

        print(f'   python sort time: {p6-p5}')


