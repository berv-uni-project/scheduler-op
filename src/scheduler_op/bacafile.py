# urutan: hitungbaris(), bacakata(), convert meggnkan strtoxx()
# nama file testcase : 'masukan.txt'
class Bacafile:
    # nf, nama file .txt masukan yg berada di saru direktori
    # return, jumlah baris dalam satu file .txt(dihitung jml \n + 1)
    def hitungbaris(self, nf):
        f = open(nf, 'r')           # f, variable file
        s = f.read()                # s, var string
        count = 1                   # count, hitung '\n'. 1 adl baris terakhir
        for i in range(len(s)):
            if s[i] == '\n':
                count += 1
        return count

    # f, file .txt yg sudah dibuka
    # mx, jml max huruf yang dibaca
    # return, satu 'kata' dari file txt
    def bacakata(self, f, mx):
        kata = ''
        for i in range(mx):
            r = f.read(1)           # r, huruf yg dibaca
            if (r == ';') or (r == '\n'):
                break
            else:
                kata += r
        return kata

    # s, str yg menunjukkan jam
    #    format 'jj.jj', tanpa spasi dll, yg digunakan 2 hrf pertama
    #    jam antara 7-18 (jam kuliah)
    # return, int hasil convert
    def strtojam(self, s):
        if s[0] == '0':             # jam 0j
            return hrftoint(s[1])
        else:                       # s[0] == '1', jam 1j
            return hrftoint(s[1]) + 10

    # s, str yg menunjukkan hari(ada ','-nya)
    #    yg dibaca hanya angka satuan, yg lain diabaikan
    # return, hari dalam bentuk list of int
    def strtohari(self, s):
        hari = []                   # hari, list of int, awal kosong
        for i in range(len(s)):
            if (s[i] == ',') or (s[i] == ' '):
                pass
            else:                   # asumsi dapat angka
                hari.append(s[i])
        return hari

    # x, angka dalam str('0'-'9')
    # return, angka dalam int(0-9)
    def hrftoint(self, x):
        if x == '0':
            return 0
        elif x == '1':
            return 1
        elif x == '2':
            return 2
        elif x == '3':
            return 3
        elif x == '4':
            return 4
        elif x == '5':
            return 5
        elif x == '6':
            return 6
        elif x == '7':
            return 7
        elif x == '8':
            return 8
        elif x == '9':
            return 9

"""
# main, contoh
b = Bacafile()                      # b, class bacafile
f = open('masukan.txt', 'r')           # f, var file txt
r = f.read()                        # r, str(isi dari f)
print(b.hitungbaris('masukan.txt'))
f = open('masukan.txt', 'r')
for ii in range(30):
    print(b.bacakata(f, len(r)))
"""