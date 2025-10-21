import time

N = 1000000

start = time.time()

for i in range(10):
    L = []
    for i in range(N):
        L.append(None)

end = time.time()
print( end - start )

start = time.time()

for i in range(10):
    L = []
    L += [ None ] * N

end = time.time()
print( end - start )