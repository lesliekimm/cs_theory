mtx1 = [[1]]

mtx2 = [[ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12]]

mtx3 = [[ 1,  2,  3,  4]]

mtx4 = [[1],
        [2],
        [3],
        [4]]

mtx5 = [[ 1,  2,  3,  4,  5],
        [ 6,  7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

def print_spiral(mtx):
  count = 1
  print_numbers(mtx, 0, len(mtx)-1, 0, len(mtx[0])-1, count)

  return

def print_numbers(mtx, beg_r, end_r, beg_c, end_c, count):
  area = len(mtx) * len(mtx[0])

  if count <= area:
    for x in range(beg_c, end_c+1):
      print mtx[beg_r][x]
      count += 1

  if count <= area:
    for y in range(beg_r+1, end_r+1):
      print mtx[y][end_c]
      count += 1

  if count <= area:
    for x in range(end_c-1, beg_c-1, -1):
      print mtx[end_r][x]
      count += 1

  if count <= area:
    for y in range(end_r-1, beg_r, -1):
      print mtx[y][beg_c]
      count += 1

  if count <= area:
    print_numbers(mtx, beg_r+1, end_r-1, beg_c+1, end_c-1, count)

  return

print_spiral(mtx1)
print "--------"
print_spiral(mtx2)
print "--------"
print_spiral(mtx3)
print "--------"
print_spiral(mtx4)
print "--------"
print_spiral(mtx5)
print "--------"


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