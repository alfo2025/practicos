##ej 2

import sys
from typing import List


class Stack:
    """Pila simple usando lista de Python.

    push -> append, pop -> pop() (LIFO)
    """

    def __init__(self) -> None:
        self._data: List[object] = []

    def push(self, item: object) -> None:
        self._data.append(item)

    def pop(self) -> object:
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def to_list_top_first(self) -> List[object]:
        # devuelve lista con el tope primero
        return list(reversed(self._data))


def process_file(path: str, s: Stack) -> None:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(maxsplit=1)
            cmd = parts[0].lower()
            if cmd in ("push", "apilar"):
                if len(parts) == 2:
                    s.push(parts[1])
            elif cmd in ("pop", "desapilar"):
                try:
                    s.pop()
                except IndexError:
                    # ignorar pop en pila vacía
                    pass


def main(argv=None):
    argv = argv or sys.argv[1:]
    path = argv[0] if argv else "operaciones_pilas.txt"
    s = Stack()
    try:
        process_file(path, s)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {path}")
        return 1

    print("Resultado final de la pila (tope -> base):")
    if s.is_empty():
        print("<pila vacía>")
    else:
        print(", ".join(map(str, s.to_list_top_first())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
