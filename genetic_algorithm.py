from hill_climbing import *
import random

class genetic_algorithm:
    def __init__(self, coursel, rooml, nString):
        self.all_strings = []
        self.str_fitness = []
        self.coursel = coursel
        self.rooml = rooml
        self.idx = 0
        i = 0
        while i < nString:
            var = initialize(coursel, rooml)
            self.all_strings.append(var)
            i += 1

    def cross_over(self, n, index1, index2):
        #n adalah nomor index pemotongan (misal n = 1, index dipotong setelah variabel ke 1)
        #I.S : 2 string of variabel
        #F.S : string variabel keduanya dipotong dan ditukar (cross over)
        set_of_var1 = self.all_strings[index1]
        set_of_var2 = self.all_strings[index2]
        if (index1 != index2):
            i = 0
            while i <= n :
                temp_var1 = set_of_var1.pop(i)
                temp_var2 = set_of_var2.pop(i)
                set_of_var1.insert(i,temp_var2)
                set_of_var2.insert(i,temp_var1)
                i += 1

    def fitness_function(self, index):
        #fitness function nya adalah jumlah variabel yang tidak ada comflict
        #caranya dengan total variabel - totalconflict variabel tersebut
        return len(self.all_strings[0]) - gettotalconflict(self.all_strings[index])

    def selection(self):
        #I.S string of variabel
        #F.S kirim indeks variabel yang mau ditukar
        i = 0
        total_fitness = 0
        for str_var in self.all_strings:
            self.str_fitness.append(self.fitness_function(i))
            total_fitness += self.str_fitness[i]
            i += 1
        ran = random.uniform(0,1)
        i = 0
        while (ran > 0):
            ran = ran - self.str_fitness[i]
            i += 1
        return i - 1

    def getvarchange(self ,coursel, rooml):
        ran = random.randrange(0, len(coursel.courselist[0].courseid) - 1)
        co = coursel.courselist[ran]
        if co.room_cons == '-':
            R = rooml.getvalidroom(co)
            for room in R:
                c = co.courseid
                ro = room.room_id
                dayl = co.validday.checksameday(room.validday)
                for day in dayl:
                    d = day
                    r = getrange(room.start, co.start, room.end, co.end)
                    begin = r[0]
                    end = r[1] - co.sks + 1
                    for i in range(begin, end + 1):
                        s = i
                        e = i + co.sks - 1
                        var = CSPvar(c, s, e, d, ro)
        else:
            R = None
            for room in rooml.roomlist:
                if room.room_id == co.room_cons:
                    R = room
                    break
            c = co.courseid
            ro = co.room_cons
            dayl = co.validday.checksameday(R.validday)
            for day in dayl:
                d = day
                r = getrange(R.start, co.start, R.end, co.end)
                begin = r[0]
                end = r[1] - co.sks + 1
                for i in range(begin, end + 1):
                    s = i
                    e = i + co.sks - 1
                    var = CSPvar(c, s, e, d, ro)
        return var

    def mutation(self, index):
        #I.S string dengan index tersebut akan diambil set of variabelnya
        #F.S satu variabel dari set of variabel diubah (pemilihan variabel secara random)
        self.all_strings[index]
        ran = random.randrange(0,len(self.all_strings[index]) - 1)
        endloop = False
        loop = 0
        while (endloop == False):
            vary = self.getvarchange(self.coursel, self.rooml)
            var_temp = CSPvarlist(self.all_strings[index])
            i = 0
            while var_temp.var[i].course != vary.course:
                i += 1
            var_temp.var[i].start = vary.start
            var_temp.var[i].end = vary.end
            var_temp.var[i].day = vary.day
            var_temp.var[i].room = vary.room
            vary.numcon = gettotalconflict(var_temp.var)
            if (gettotalconflict(var_temp.var) < gettotalconflict(self.all_strings[index])) or (loop >= 4):
                k = 0
                while self.all_strings[index][k].course != vary.course:
                    k += 1
                self.all_strings[index][k].start = vary.start
                self.all_strings[index][k].end = vary.end
                self.all_strings[index][k].day = vary.day
                self.all_strings[index][k].room = vary.room
                endloop = True
            loop += 1

    def genetic_start(self):
        #run genetic algorithm
        #mengembalikan index yang terbaik
        move = 0
        treshold = 500
        varlen = len(self.all_strings[0])
        end = False
        while (move < treshold) and (end == False):
            ran = random
            if (ran.uniform(0,1) <= 0.6):
                idx_str1 = self.selection()
                idx_str2= self.selection()
                self.cross_over(ran.randrange(0,varlen - 1),idx_str1,idx_str2)
            else:
                idx_str = self.selection()
                self.mutation(idx_str)

            i = 0
            for str_var in self.all_strings:
                if (gettotalconflict(str_var) == 0):
                    end = True
                    self.idx = i
                    break
                i += 1

            move += 1

        totalconflict = gettotalconflict(self.all_strings[self.idx])
        if (totalconflict > 0):
            i = 0
            for var in self.all_strings:
                if (gettotalconflict(var) < totalconflict):
                    totalconflict = gettotalconflict(var)
                    self.idx = i
                i += 1

        for v in self.all_strings[self.idx]:
            print(v)
        print(str(gettotalconflictpersks(self.all_strings[self.idx])))


#main test
b = Bacafile()
c = allcourse("doc/Testcase.txt", b)
a = allroom("doc/Testcase.txt", b)
#print(a)
#print(c)
X = genetic_algorithm(c, a, 4)
X.genetic_start()



