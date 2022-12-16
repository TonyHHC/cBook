# 將檔案名稱改為書本名稱
import os
import glob
import pandas as pd
import codecs

my_path = r'D:\Download\電子書\cBook'

dictAllBooks = {}

for file in glob.glob(my_path + '/**/*.updb', recursive=True):
    print('File : ', file)
    with open(file, 'rb') as f:
        contents = f.read()
        
        # Total 筆數
        iTotalRecords = int.from_bytes(contents[76:78], 'big')
        print('Total 筆數 :', iTotalRecords)
        
        # 每一筆紀錄位置
        lstRecordStartPos = [None] * iTotalRecords
        for i in range(iTotalRecords):
            lstRecordStartPos[i] = int.from_bytes(contents[78+(8*i):78+(8*i)+4], 'big')
        
        # 找書名
        iBookNamePos = [8, 0]
        tmp = contents[lstRecordStartPos[0]:lstRecordStartPos[1]]
        iBookNamePos[1] = tmp.find(b'\x1b\x00\x1b\x00\x1b\x00')
        
        dictAllBooks[file] = tmp[iBookNamePos[0]:iBookNamePos[1]].decode('utf-16-le')
        
#print(dictAllBooks)

for key, value in dictAllBooks.items():
    strFilenameWithoutExtension = os.path.basename(key).split('.')[0]
    strNewFileName = key.replace(strFilenameWithoutExtension, value)
    print(key, ' ==> ', strNewFileName)
    os.rename(key, strNewFileName)
	
	
	
	

