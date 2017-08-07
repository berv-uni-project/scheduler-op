import re

# urutan: hitungbaris(), bacakata(), convert meggnkan strtoxx()
# nama file testcase : 'masukan.txt'            
class Bacafile:
    # nf, nama file .txt masukan yg berada di saru direktori
    # return, jumlah baris dalam satu file .txt(dihitung jml \n + 1)
    def __init__(self):
        pass

    def hitungbaris(self, nf):
        f = open(nf, 'r')  # f, variable file
        s = f.read()  # s, var string
        count = 1  # count, hitung '\n'. 1 adl baris terakhir
        for i in range(len(s)):
            if s[i] == '\n':
                count += 1
        return count

    # f, file .txt yg sudah dibuka
    # mx, jml max huruf yang dibaca
    # return, satu 'kata' dari file txt
    def bacakata(self, f):
        kata = ''
        r = f.read(1)
        while (r == ';') or (r == '\n') or (r == ' '):
            r = f.read(1)
            # print(r)
        while (r != ';') and (r != '\n') and (r != '') and (r != ' '):
            kata += r
            r = f.read(1)
        return kata

    # s, str yg menunjukkan jam
    #    format 'jj.jj', tanpa spasi dll, yg digunakan 2 hrf pertama
    #    jam antara 7-18 (jam kuliah)
    # return, int hasil convert

    def strtojam(self, s):
        return int(s[0]) * 10 + int(s[1])

    # s, str yg menunjukkan hari(ada ','-nya)
    #    yg dibaca hanya angka satuan, yg lain diabaikan
    # return, hari dalam bentuk list of int
    def strtohari(self, s):
        hari = []  # hari, list of int, awal kosong
        for i in range(len(s)):
            if (s[i] == ',') or (s[i] == ' '):
                pass
            else:  # asumsi dapat angka
                hari.append(s[i])
        return hari

    def checkFormat(self, filename):
        f = open(filename, 'r')
        mode = 0
        error = 0
        r = re.compile('.*;[0-1][0-9].[0-5][0-9];[0-1][0-9].[0-5][0-9];.*\n')
        r2 = re.compile('.*;.*;[0-1][0-9].[0-5][0-9];[0-1][0-9].[0-5][0-9];.*;.*\n')
        linelist = f.readlines()
        for lines in linelist:
            if mode == 0:
                if lines.lower() != "ruangan\n":
                    error += 1
                mode += 1
            elif mode == 1:
                if not r.match(lines):
                    if lines != "\n":
                        error += 1
                    mode += 1
            elif mode == 2:
                if lines.lower() != "jadwal\n":
                    error += 1
                mode += 1
            elif mode == 3:
                if not r2.match(lines):
                    if lines != "":
                        error += 1
                    mode += 1
            elif mode == 4:
                break
        if error > 0:
            return False
        else:
            return True

"""
# main, contoh
b = Bacafile()                      # b, class bacafile
f = open("Testcase.txt", 'r')           # f, var file txt
r = f.read()                        # r, str(isi dari f)
print(b.hitungbaris("Testcase.txt"))
f = open("Testcase.txt", 'r')
for ii in range(30):
    print(b.bacakata(f, len(r)))
b = Bacafile()
s = "neko;is;dead"
"""
