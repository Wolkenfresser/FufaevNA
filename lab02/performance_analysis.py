"""
performance_analysis.py
Простой замер времени: вставка в начало для list и для LinkedList.
"""
import timeit
from lab02.linked_list import LinkedList


SETUP_LIST = "l = []"
CODE_LIST_INSERT = "for i in range(N): l.insert(0, i)"

SETUP_LL = "from linked_list import LinkedList\nll = LinkedList()"
CODE_LL_INSERT = "for i in range(N): ll.insert_at_start(i)"


def measure(N=1000, repeats=5):
    globals_map = {'N': N}
    t_list = timeit.timeit(stmt=CODE_LIST_INSERT, setup=SETUP_LIST, number=1, globals=globals_map)
    t_ll = timeit.timeit(stmt=CODE_LL_INSERT, setup=SETUP_LL, number=1, globals=globals_map)
    print(f"N={N}")
    print(f"list.insert(0, x): {t_list:.6f} sec")
    print(f"LinkedList.insert_at_start: {t_ll:.6f} sec")


if __name__ == '__main__':
    for N in [100, 1000, 5000]:
        measure(N=N)