import sys
for _ in range(int(sys.stdin.readline().rstrip())):
  inp = sys.stdin.readline().rstrip().split()
  T = int(inp[0])
  students = list(map(int, inp[1:]))

  cnt = 0
  for i in range(1, 20):
    for s in students[:i]:
      if students[i] < s:
        cnt += 1
  print(f"{T} {cnt}")
