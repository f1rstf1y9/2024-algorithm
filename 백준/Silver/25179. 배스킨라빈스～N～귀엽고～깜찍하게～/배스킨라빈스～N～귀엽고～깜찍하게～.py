N, M = map(int, input().split())

if (N-1) % (M+1):
  print("Can win")
else:
  print("Can't win")