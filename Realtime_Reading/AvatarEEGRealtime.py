# ============================================ TEST 2b

import numpy as np
import matplotlib.pyplot as plt

# ユーザーから文字列を入力する
cstr = input('enter str? ')  # ex. Avatar_04137_2022-08-01_18-20-39

# ファイル名を作成する
fnm = cstr + '.bdf'

# ファイルを開く
fid = open(fnm, 'rb')

# チャンネル数（経験的な値）
numChan = 30

# ファイルポインタを移動する
fid.seek(256*(17+1), 0)  # should be corrected, too long

# データを格納するための空の配列を用意する
dat = np.empty((0, numChan), int)
# dat = np.array([])
count = 0
# ファイルを読み込んで、データを配列に格納する
while True:
    plt.clf()       # グラフの初期化
    count += 1
    
    # 現在のファイル位置を記録する
    pos1 = fid.tell()

    # ファイルから
    aux = np.fromfile(fid, dtype='int32', count=numChan*3) # ファイルから8ビットのデータをnumChan*3個読み込む
    aux = aux.reshape(-1, 3)[:, 0]  # 24bitデータから8bitデータを取り出す
    if len(aux) == numChan:         # 読み込んだデータがnumChan個ある場合
        dat = np.vstack([dat, aux])    # 読み込んだデータをdatに追加
    else:
        fid.seek(pos1)              # ファイルをpos1の位置まで巻き戻す    
    
    if dat.size % 500 == 0:         # datの要素数が500の倍数の場合
       print(dat[0])
       plt.plot(dat[:, numChan-10])   
       plt.xlim(-250 + count, 250 + count)             # グラフの幅を500で規定
       plt.show(block=False)       # グラフを表示する
       plt.pause(0.0001)            # 表示を一時停止する
dat1 = dat[numChan-10::numChan]     # 最後の10チャンネルのデータを抽出する

fid.close()
