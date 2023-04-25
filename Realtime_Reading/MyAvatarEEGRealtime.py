# ============================================ TEST 2b
import matplotlib.pyplot as plt
import numpy as np


# グラフをクリア
plt.clf()

# ユーザーからの入力を受け取る
cstr = input('enter str? ')  # ex. Avatar_04137_2022-08-01_18-20-39
# ファイル名を作成
fnm = cstr + '.bdf'
# ファイルを開く
fid = open(fnm, 'rb');
# チャンネルの数を設定
numChan = 30; # empirical value 
# ファイルの読み取り位置を設定
fid.seek(256*(17+1), 0)  # 0: SEEK_SET, bof: Beginning Of File

# データを保存するためのリストを作成
data_list = []

while True:
    # 現在の読み取り位置を保存
    current_position = fid.tell()

    # データを1つ読み取り
    data = np.fromfile(fid, dtype=np.int32, count=numChan)

    # 読み取りができた場合
    if len(data) == numChan:
        # データをリストに追加
        data_list.append(data)

    else:
        # 読み取り位置を元に戻す
        fid.seek(current_position, 0)
        break

    # 一定間隔ごとにデータをプロット
    if len(data_list) % 500 == 0:
        plt.plot(data_list[-1].reshape(-1, numChan)[numChan - 10, :])


# データをnumpy配列に変換する
data = np.vstack(data_list)

# 特定のデータをプロット
dat1 = data[numChan-10, :]

# ファイルを閉じる
fid.close()






# ============================================ TEST 2a 
# ファイル名を設定
# cstr = 'Avatar_04137_2022-08-01_17-40-14'

# ---------------------------- test read csv 
# ファイルを開く
# fnm = strcat(cstr,'.csv');
# fnm
# fid = fopen( fnm, 'r');
# ヘッダーを読み取る
# cl1 = fgetl( fid ) ; % header 
# i=1;
# ファイルの最後まで繰り返す
# while ~feof( fid )
    # 1行分のデータを読み取る
    # cl1 = fgetl( fid ) ; 
    # スペースで区切ってデータを配列に格納
    # C = strsplit( cl1 ); % length(C) = 13 
    # 特定のデータを抽出して変数xに格納
    # x(i) = str2num( C{13-8+1}); % ch1
    # i=i+1;
# end
# ファイル
