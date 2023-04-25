import numpy as np
import matplotlib.pyplot as plt

# ============================================ TEST 2b
cstr = input('enter str? ')  # ex. Avatar_04137_2022-08-01_18-20-39
fnm = cstr + '.bdf'
print(fnm)

with open(fnm, 'rb') as fid:
    numChan = 30  # empirical value
    fid.seek(256 * (17 + 1))
    dat = np.empty((numChan, 0))
    while True:
        pos1 = fid.tell()
        aux = np.fromfile(fid, dtype='int32', count=numChan)

        if len(aux) == numChan:
            dat = np.hstack((dat, aux.reshape(-1, 1)))
        else:
            fid.seek(pos1)
        if dat.shape[1] % 500 == 0:
            plt.plot(dat[numChan - 10, :])
            plt.show(block=False)
            plt.pause(0.001)

dat1 = dat[numChan - 10, :]

# ============================================ TEST 2a
cstr = 'Avatar_04137_2022-08-01_17-40-14'

# ---------------------------- test read csv
fnm = cstr + '.csv'
print(fnm)
with open(fnm, 'r') as fid:
    cl1 = fid.readline()  # header
    x = []
    for line in fid:
        C = line.split()
        x.append(float(C[13 - 8]))
plt.plot(x)
plt.show()

# -----------------------------test read bdf
fnm = cstr + '.bdf'
print(fnm)
with open(fnm, 'rb') as fid:
    numChan = 30  # empirical value
    fid.seek(256 * (17 + 1))
    dat = np.empty((numChan, 0))
    while True:
        aux = np.fromfile(fid, dtype='int32', count=numChan)
        if len(aux) == numChan:
            dat = np.hstack((dat, aux.reshape(-1, 1)))
        else:
            break
dat1 = dat[numChan - 10, :]
plt.plot(dat1)
plt.show()
