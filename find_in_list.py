from typing import TypeVar, Iterable, Callable

T = TypeVar('T')


def find_first(i: Iterable[T], f: Callable[[T], bool]) -> T | None:
    return next(iter(o for o in i if f(o)), None)


def find_index(i: Iterable[T], f: Callable[[T], bool]) -> int | None:
    return next(iter(indx for indx, o in enumerate(i) if f(o)), None)
