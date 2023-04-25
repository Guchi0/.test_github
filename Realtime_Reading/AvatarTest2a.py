import numpy as np
import matplotlib.pyplot as plt

cstr = 'C:\\Users\\Kagur\\py_Programming\\Realtime_Reading\\Avatar_04137_2022-08-01_17-40-14'

# ---------------------------- test read csv 
fnm = cstr + '.csv'
print(fnm)

with open(fnm, 'r') as fid:
    cl1 = fid.readline() # header 
    x = []
    for line in fid:
        C = line.split() # length(C) = 13 
        x.append(float(C[5])) # ch1

plt.plot(x)

# -----------------------------test read bdf 
fnm = cstr + '.bdf'
print(fnm)

with open(fnm, 'rb') as fid:
    numChan = 30 # empirical value 
    fid.seek(256*(17+1), 0) # % should be corrected, too long 
    dat = np.array([])
    while True:
        aux = np.fromfile(fid, dtype='int32', count=numChan)
        if len(aux) == numChan:
            dat = np.append(dat, aux)
        else:
            break
    
dat = np.reshape(dat, (-1, numChan))
dat1 = dat[-10:, :]

plt.plot(dat1)

plt.show()
