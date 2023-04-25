# AvatarEEGのリアルタイム読み出し用コード


# matlabからのコピー

# function test_bdf_satonao2
# % format:
# % https://www.biosemi.com/faq/file_format.htm
# %
# % sample script: 
# % https://jp.mathworks.com/matlabcentral/fileexchange/13070-eeg-bdf-reader
# %
# % cf: edf-browser
# % https://www.teuniz.net/edfbrowser/
# % 
# % Memo copoed from manual:
# % BDF+ format, the 24 bit version of a European Data Format (EDF+) file
# %
# % Note that EDF supports 16 bit data values only. Thus both the
# % resolution and range are compromised when fitting Avatar's 24-bit data values into an EDF file. BDF+ is a standard very
# % similar to EDF except that it supports 24-bit data values. BDF+ files can be created from an Avatar EEG recorder native
# % binary file by following the instructions previously outlined for creating an EDF file, but substituting the program
# % rec2bdf.py for rec2edf.py. Output files will have the extension .bdf.
# %


# ============================================ TEST 2b
# clf
# cstr = input('enter str? ','s');  % ex. Avatar_04137_2022-08-01_18-20-39
# fnm = strcat(cstr,'.bdf');
# fnm

# fclose all
# fid = fopen( fnm );
# numChan = 30; % empirical value 
# fseek(fid,256*(17+1),'bof'); % % should be corrected, too long 
# dat = [];
# while 1 % ~feof( fid )

# pos1 = ftell( fid ); 
# aux = fread(fid,[ 1, numChan],'bit24')';

# if length( aux ) == numChan
# dat=[dat, aux];
# else
# fseek( fid, pos1,'bof' );
# end
# if mod( size( dat, 2), 500 ) == 0
# plot( dat( numChan - 10 + 1 , : ) );
# drawnow
# end
# end
# % fclose(fid);
# dat1 = dat( numChan - 10 + 1 , : );

# return 


# % ============================================ TEST 2a 
# cstr = 'Avatar_04137_2022-08-01_17-40-14';

# % ---------------------------- test read csv 
# fnm = strcat(cstr,'.csv');
# fnm
# fid = fopen( fnm, 'r');
# cl1 = fgetl( fid ) ; % header 
# i=1;
# while ~feof( fid )
# cl1 = fgetl( fid ) ; 
# C = strsplit( cl1 ); % length(C) = 13 
# x(i) = str2num( C{13-8+1}); % ch1
# i=i+1;
# end
# fclose( fid )
# plot( x ) 

# % -----------------------------test read bdf 
# fnm = strcat(cstr,'.bdf');
# fnm
# fid = fopen( fnm );
# numChan = 30; % empirical value 
# fseek(fid,256*(17+1),'bof'); % % should be corrected, too long 
# dat = [];
# while ~feof( fid ) % for i=1:10
# aux = fread(fid,[ 1, numChan],'bit24')';

# if length( aux ) == numChan
# dat=[dat, aux];
# end
# end
# fclose(fid);
# dat1 = dat( numChan - 10 + 1 , : );

# hold on ; 
# plot( dat1 ) 
# hold off 

# return 



#
# -----------------------以下Python
#

import numpy as np
import matplotlib.pyplot as plt

def test_bdf_satonao2():        # 関数の定義
    plt.clf()                   # グラフの初期化
    cstr = input('enter str? ') # ユーザからの入力受け取り #ex. Avatar_04137_2022-08-01_18-20-39
    fnm = cstr + '.bdf'         # ファイル名の生成
    print(fnm)                  # ファイル名の出力

    with open(fnm, 'rb') as fid:    # バイナリーモードでファイルを開く
        numChan = 30                # チャンネル数
        fid.seek(256*(17+1), 0)     # ファイルの先頭から 256*(17+1) バイト目に移動
                                    # （正しい値は修正が必要とのこと）
        dat = np.array([])          # 空の numpy 配列を作成
        while True:                 # 無限ループ
            pos1 = fid.tell()       # ファイルポインタの位置を保存
            aux = np.fromfile(fid, dtype=np.int32, count=numChan)   # numChan 個の32bit 整数を読み込み、numpy配列としてauxに格納

            if len(aux) == numChan: # auxにnumChan個の要素が含まれている場合
                dat = np.concatenate((dat, aux))    #numpy 配列 datに aux を結合
            else:                   # auxの長さがnumChan個でない場合
                fid.seek(pos1, 0)   # ファイルポインタをpos1に戻す
            if dat.shape[0] % 500 == 0: # datの行数が500の倍数の場合
                plt.plot(dat[numChan - 10:dat.shape[0]:numChan])    # プロット
                plt.draw()          # グラフの描画

    fclose(fid);                    # ファイルを閉じる
    dat1 = dat[numChan - 10::numChan]  # numpy 配列 dat1 に、dat の最後の numChan 個の要素を格納

    return dat1                     # numpy 配列 dat1 を返す


cstr = 'C:\\Users\\Kagur\\py_Programming\\Realtime_Reading\\Avatar_04137_2022-08-01_17-40-14'

fnm = cstr  + '.csv'
print(fnm)
with open(fnm, 'r') as fid:
    cl1 = fid.readline()  # header
    x = []
    for line in fid:
        C = line.split()  # length(C) = 13
        x.append(float(C[13-8]))  # ch1

plt.plot(x)


fnm = cstr + '.bdf'  # ファイル名を作成
print(fnm)
with open(fnm, 'rb') as fid:  # ファイルをバイナリモードでオープン
    numChan = 30  # チャンネル数（経験的な値）
    fid.seek(256*(17+1), 0)  # ファイルの先頭から 256*(17+1) バイト目に移動
    dat = np.array([])  # データを格納するための空の配列
    while True:  # ファイル終端までループ
        aux = np.fromfile(fid, dtype=np.int32, count=numChan)  # バイナリデータを読み込む

        if len(aux) == numChan:  # チャンネル数だけデータを読み込めた場合
            dat = np.concatenate((dat, aux))  # 読み込んだデータをdatに追加
        else:  # データが足りない場合
            break  # ループを抜ける
    dat1 = dat[numChan - 10::numChan]  # 最後のチャンネルのみを取得

plt.plot(dat1)  # データをプロット
plt.show()  # プロットを表示

