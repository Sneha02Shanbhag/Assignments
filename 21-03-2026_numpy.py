import numpy as np, time

n = 1_000_000
lst = list(range(n))
arr = np.array(lst)

t = time.time(); _ = [x*2 for x in lst]; print("List:", round(time.time()-t,4))
t = time.time(); _ = arr*2; print("NumPy:", round(time.time()-t,4))

print("Observation: NumPy faster due to vectorization and C-optimized operations.")
