#!/usr/bin/env python3

import threading


def schedule(workfunc, n):
    timer = threading.Timer(n, workfunc)
    timer.start()
    return
