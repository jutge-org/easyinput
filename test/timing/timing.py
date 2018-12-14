import jutge
import jutge_old
import timeit


def time_new_1():
    for _ in jutge.keep_reading(file=open('../text/long.txt', 'r')):
        pass


def time_old_1():
    file = open('../text/long.txt', 'r')
    word = jutge_old.read(file=file)
    while word is not None:
        word = jutge_old.read(file=file)


def time_new_2():
    with open('../text/source5.txt', 'r') as file:
        nums = []
        for line in jutge.keep_reading(int, file=file, amount=100):
            nums.append(tuple(line))


def time_old_2():
    with open('../text/source5.txt', 'r') as file:
        tup = tuple(jutge_old.read(*(int,) * 100, file=file))
        nums = [tup]
        while tup[-1] is not None:
            tup = tuple(jutge_old.read(*(int,) * 100, file=file))
            nums.append(tup)


def time_new_3():
    with open('../text/source5.txt', 'r') as file:
        sum(jutge.read(int, amount=1000, file=file))


def time_old_3():
    with open('../text/source5.txt', 'r') as file:
        sum(jutge_old.read(*(int,) * 1000, file=file))


class Job:
    def __init__(self, title, id, reps):
        self.title = title
        self.id = id
        self.reps = reps


if __name__ == '__main__':
    comparisons = (
        Job("Sum over int", 3, 1000),
        Job("Read/iterate sequences of int", 2, 500),
        Job("Read long file", 1, 1)
    )
    for comp in comparisons:
        for v in ("new", "old"):
            func = "time_{}_{}".format(v, comp.id)
            print("[{}] {}... ".format(v.upper(), comp.title), end='')
            print(timeit.timeit(stmt="{}()".format(func),
                                setup="from timing import {}".format(func),
                                number=comp.reps))
        print()
