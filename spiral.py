def spiral(r, c):
  mtx = [[0 for x in range(c)] for y in range(r)]
  count = 1
  insert_numbers(mtx, 0, r-1, 0, c-1, count)

  for y in range(r):
    print(mtx[y])

  return mtx

def insert_numbers(mtx, beg_r, end_r, beg_c, end_c, count):
  area = len(mtx) * len(mtx[0])

  if count <= area:
    for x in range(beg_c, end_c+1):
      mtx[beg_r][x] = count
      count += 1

  if count <= area:
    for y in range(beg_r+1, end_r+1):
      mtx[y][end_c] = count
      count += 1

  if count <= area:
    for x in range(end_c-1, beg_c-1, -1):
      mtx[end_r][x] = count
      count += 1

  if count <= area:
    for y in range(end_r-1, beg_r, -1):
      mtx[y][beg_c] = count
      count += 1

  if count <= area:
    insert_numbers(mtx, beg_r+1, end_r-1, beg_c+1, end_c-1, count)

  return mtx

spiral(1,5)