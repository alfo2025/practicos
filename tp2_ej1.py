##ej 1 

import sys
from typing import List


class Queue:
	"""Cola simple usando una lista de Python.

	Nota: dequeue usa pop(0) (O(n)) pero es muy claro para fines educativos.
	Para producción usar `collections.deque`.
	"""

	def __init__(self) -> None:
		self._data: List[object] = []

	def enqueue(self, item: object) -> None:
		"""Agregar item al final de la cola."""
		self._data.append(item)

	def dequeue(self) -> object:
		"""Quitar y devolver el frente de la cola. Lanza IndexError si está vacía."""
		if not self._data:
			raise IndexError("dequeue from empty queue")
		return self._data.pop(0)

	def is_empty(self) -> bool:
		return len(self._data) == 0

	def to_list(self) -> List[object]:
		return list(self._data)


def process_file(path: str, q: Queue) -> None:
	"""Procesa un archivo simple con comandos ENQ <v> y DEQ."""
	with open(path, "r", encoding="utf-8") as f:
		for line in f:
			line = line.strip()
			if not line or line.startswith("#"):
				continue
			parts = line.split(maxsplit=1)
			cmd = parts[0].lower()
			if cmd in ("enq", "encolar", "enqueue"):
				if len(parts) == 2:
					q.enqueue(parts[1])
			elif cmd in ("deq", "desencolar", "dequeue"):
				try:
					q.dequeue()
				except IndexError:
					# ignorar si la cola está vacía
					pass


def main(argv=None):
	argv = argv or sys.argv[1:]
	path = argv[0] if argv else "operaciones.txt"
	q = Queue()
	try:
		process_file(path, q)
	except FileNotFoundError:
		print(f"Archivo no encontrado: {path}")
		return 1

	print("Resultado final de la cola (frente -> final):")
	if q.is_empty():
		print("<cola vacía>")
	else:
		print(", ".join(map(str, q.to_list())))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())

##ej 2
