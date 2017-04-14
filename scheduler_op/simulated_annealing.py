from scheduler_op.hill_climbing import *
import math
import random

class simulated_annealing :
    def __init__(self, coursel, rooml, ratio):
        self.var = initialize(coursel, rooml)
        self.tempnow = 100;
        self.ratio = ratio;
        self.conflict = [];
        self.action = getallaction(coursel, rooml)

    def decrease_temperature(self):
        self.tempnow = self.tempnow * self.ratio;

    def simulate(self):
        i = 0
        ran = random
        while i<len(self.var):
            j = i+1
            while j<len(self.var):
                if(self.var[i].conflictcheck(self.var[j])):
                    con=CSPconflict(self.var[i], self.var[j])
                    self.conflict.append(con)
                j+=1
            i+=1
        count = 0
        ran = random
        min = gettotalconflictpersks(self.var)
        idx = 0
        j = 0
        loop = 0
        while (gettotalconflictpersks(self.var)>0 and loop < 100):
            for act in self.action:
                var_temp = CSPvarlist(self.var)
                i = 0
                while var_temp.var[i].id != act.change.id:
                    i+=1
                var_temp.var[i].start = act.change.start
                var_temp.var[i].end = act.change.end
                var_temp.var[i].day = act.change.day
                var_temp.var[i].room = act.change.room
                var_temp.var[i].roomid = act.change.roomid
                act.change.numcon = gettotalconflictpersks(var_temp.var)
                var_ei = act.change.numcon
                var_e = min
                if (act.change.numcon < min) or (math.exp(-(var_e - var_ei) / self.tempnow)) <= ran.randrange(0, 1):
                    min = act.change.numcon
                    idx = j
                j += 1
                k = 0

                if (idx != 0):
                    while self.var[k].id!=self.action[idx].change.id:
                        k += 1
                        if (k == len(self.var)):
                            k=k-1;
                            break;

                    self.var[k].start = self.action[idx].change.start
                    self.var[k].end = self.action[idx].change.end
                    self.var[k].day = self.action[idx].change.day
                    self.var[k].room = self.action[idx].change.room
                    self.var[k].roomid = self.action[idx].change.roomid
                    count = count+1

                if gettotalconflictpersks(self.var) == 0 or count > 500:
                    break
            loop+= 1

        for v in self.var:
            print(v)
        print(str(gettotalconflictpersks(self.var)))


"""
#main test
b = Bacafile()
c = allcourse("doc/Testcase.txt", b)
a = allroom("doc/Testcase.txt", b)
#print(a)
#print(c)
X = simulated_annealing(c, a, 1)
X.simulate()
"""