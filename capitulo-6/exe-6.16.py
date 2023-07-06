l = [7, 4, 3, 12, 8]
i = 0

while i < len(l):
  y = 0
  troca = False
  while y < (len(l) - 1):
    if l[y] < l[y + 1]:
      l[y], l[y + 1] = l[y + 1], l[y]
      troca = True
    y += 1
  i += 1
  if not troca:
    break
print(l)