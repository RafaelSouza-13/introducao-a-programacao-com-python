l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [2, 5, 3, 7, 1, 9, 11]
listas_misturadas = l1.copy()
listas_misturadas.extend(l2)
l3 = []
x = 0
while x < len(listas_misturadas):
  y = 0
  while y < len(l3):
    if l3[y] == listas_misturadas[x]:
      break
    y += 1
  if y == len(l3):
    l3.append(listas_misturadas[x])
  x += 1

print(l3)
