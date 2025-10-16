"""tp2_listas.py

Implementación mínima de una lista simplemente enlazada (celdas con enlace simple).
Lee un archivo de operaciones (por defecto `operaciones_listas.txt`) con comandos
simples y muestra la lista final (head -> tail).

Comandos soportados (línea por línea):
- INSERT <valor>    -> inserta en la cabeza (head)
- APPEND <valor>    -> inserta al final (tail)
- REMOVE <valor>    -> elimina la primera ocurrencia de <valor>
- POP               -> elimina la cabeza (si existe)
- Las líneas que empiezan con # se ignoran

Uso:
    python tp2_listas.py operaciones_listas.txt
"""

import sys
from typing import Optional, List


class Node:
    def __init__(self, value: object, nxt: Optional['Node'] = None) -> None:
        self.value = value
        self.next = nxt

    def __repr__(self) -> str:
        return f"Node({self.value!r})"


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def insert_head(self, value: object) -> None:
        self.head = Node(value, self.head)

    def append(self, value: object) -> None:
        if self.head is None:
            self.head = Node(value)
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def remove(self, value: object) -> bool:
        """Elimina la primera ocurrencia de value. Devuelve True si se eliminó."""
        prev = None
        cur = self.head
        while cur is not None:
            if cur.value == value:
                if prev is None:
                    # eliminar la cabeza
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return True
            prev = cur
            cur = cur.next
        return False

    def pop_head(self) -> Optional[object]:
        if self.head is None:
            return None
        v = self.head.value
        self.head = self.head.next
        return v

    def to_list(self) -> List[object]:
        out: List[object] = []
        cur = self.head
        while cur is not None:
            out.append(cur.value)
            cur = cur.next
        return out


def process_file(path: str, lst: SinglyLinkedList) -> None:
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(maxsplit=1)
            cmd = parts[0].lower()
            arg = parts[1] if len(parts) > 1 else None
            if cmd in ("insert", "ins", "insertar"):
                if arg is not None:
                    lst.insert_head(arg)
            elif cmd in ("append", "app", "agregar"):
                if arg is not None:
                    lst.append(arg)
            elif cmd in ("remove", "rem", "eliminar"):
                if arg is not None:
                    lst.remove(arg)
            elif cmd in ("pop", "desapilar", "sacar"):
                lst.pop_head()
            else:
                # comando desconocido: lo ignoramos
                pass


def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    path = argv[0] if argv else "operaciones_listas.txt"
    lst = SinglyLinkedList()
    try:
        process_file(path, lst)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {path}")
        return 1

    final = lst.to_list()
    print("Resultado final de la lista (head -> tail):")
    if not final:
        print("<lista vacía>")
    else:
        print(", ".join(map(str, final)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
