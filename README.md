# 自己用的好讀小程式
## 程式清單
### rename_updb_filename_to_book_name.py
將下載下來好讀的 uPDB 檔案名稱改名為書本名稱，以方便整理

## uPDB 檔參考規格
參考來源 : https://www.haodoo.net/?M=hd&P=mPDB22

1. 檔案的前78個bytes，是Header[0..77]：
    + Header[44..59]都是0。可以不理。
    + Header[60..63]是"BOOK"。可以不理。
    + Header[64..67]是判別的關鍵，PDB是"MTIT"，uPDB是"MTIU"。
    + Header[68..75]都是0。可以不理。
    + Header[76..77]是record數 = N (章數) 加2 (目錄及書籤)。

2. 每筆資料的起始位置及屬性，依Palm的規格是8個bytes，前4個bytes是位置，後4個bytes是0。一共有 (N+2) * 8 bytes。

3. 第一筆資料定義書的屬性，是8個空白字元、書名、章數及目錄：
    + (PDB檔)
      + 8個空白btyes，可以不理；
      + 之後接書名是Big5碼，後接三個ESC(即27)
      + 之後接章數(ASCII string)，後接一個ESC
      + 之後接目錄，各章之標題是以ESC分隔
    + (uPDB檔)
      + 8個空白btyes，可以不理；
      + 之後接書名是Unicode碼，後接三個ESC(即27,0)
      + 之後接章數(ASCII string)，後接一個ESC (27, 0)
      + 之後接目錄，各章之標題是以CR(13,0) NL(10,0) 分隔
      
4. 再來是N筆資料，每筆是一章的內容，PDB檔是Big5碼(是null-terminated string，最後一個byte是0)，uPDB檔是Unicode碼。

5. 第N+2筆資料是書籤，預設是-1。可以不理。
