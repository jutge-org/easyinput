import timeit

import colorama
from termcolor import colored

import jutge
import jutge_old

colorama.init()


def time_new_1():
    for _ in jutge.keep_reading(file=open('../text/long.txt')):
        pass


def time_old_1():
    file = open('../text/long.txt')
    word = jutge_old.read(file=file)
    while word is not None:
        word = jutge_old.read(file=file)


def time_new_2():
    with open('../text/source5.txt') as file:
        nums = []
        for line in jutge.keep_reading(int, file=file, amount=100, astuple=True):
            nums.append(line)


def time_old_2():
    with open('../text/source5.txt') as file:
        tup = tuple(jutge_old.read(*(int,) * 100, file=file))
        nums = [tup]
        while tup[-1] is not None:
            tup = tuple(jutge_old.read(*(int,) * 100, file=file))
            nums.append(tup)


def time_new_3():
    with open('../text/source5.txt') as file:
        sum(jutge.read(int, amount=1000, file=file))


def time_old_3():
    with open('../text/source5.txt') as file:
        sum(jutge_old.read(*(int,) * 1000, file=file))


def time_new_4():
    with open('../text/long.txt') as file:
        jutge.read(chr, amount=1000, file=file, astuple=True)


def time_old_4():
    with open('../text/long.txt') as file:
        jutge_old.read(*(chr,) * 1000, file=file)


class Job:
    def __init__(self, title, id, reps):
        self.title = title
        self.id = id
        self.reps = reps


repeats = 10  # (constant) Number of repetitions per job

if __name__ == '__main__':
    comparisons = (
        Job("Sum over int", 3, 300),
        Job("Read/iterate sequences of int", 2, 35),
        Job("Read chars", 4, 500),
        Job("Read long file", 1, 1),
    )
    for comp in comparisons:
        for v in "old", "new":
            func = "time_{}_{}".format(v, comp.id)
            print("[{}] \t{}... ".format(v.upper(), comp.title))
            t = timeit.Timer(stmt="{}()".format(func),
                             setup="from timing import {}".format(func))
            print("\t\tRepeating {} times...".format(repeats), end='')
            times = []
            for i in range(repeats):
                times.append(t.timeit(number=comp.reps))
                print(" {:.4f}".format(times[-1]), end='')
            print(colored("\n\t\tBEST: {:.4f} s".format(min(times)), color='red', attrs=('bold',)))

        print('\n')
