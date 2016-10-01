import random

from scheduler_op.class_cons import *


class ActionClass:
    def __init__(self, con, var):
        self.numcon = con
        self.change = var


def initialize(coursel, rooml):
    ran = random
    X = []
    for co in coursel.courselist:
        if co.room_cons == '-':
            R = rooml.getvalidroom(co)
            if (not R):
                print("No compatible room for this course")
            else:
                if len(R) > 1:
                    i = ran.randrange(0, len(R))
                else:
                    i = 0
                d = co.validday.checksameday(R[i].validday)
                if len(d) > 1:
                    day = d[ran.randrange(0, len(d) - 1)]
                else:
                    day = d[0]
                r = getrange(R[i].start, co.start, R[i].end, co.end)
                start = ran.randrange(r[0], r[1] - co.sks + 1)
                end = start + co.sks
                var = CSPvar(co.courseid, start, end, day, R[i].room_id)
               # print(var.course, var.start, var.end, var.day, var.room)
                X.append(var)
        else:
            R = None
            for room in rooml.roomlist:
                if (room.room_id == co.room_cons):
                    R = room
                    break
            if R is None:
                print("No compatible room for this course")
            else:
                if (co.sks >= R.end - R.start + 1):
                    print("No compatible room for this course")
                else:
                    d = co.validday.checksameday(R.validday)
                    if len(d) > 1:
                        day = d[ran.randrange(0, len(d) - 1)]
                    else:
                        day = d[0]
                    r = getrange(R.start, co.start, R.end, co.end)
                    start = ran.randrange(r[0], r[1] - co.sks + 1)
                    end = start + co.sks
                    # print(R.room_id)
                    var = CSPvar(co.courseid, start, end, day, R.room_id)
                    #print(var.course, var.start, var.end, var.day, var.room)
                    X.append(var)
    return X
    
def getallaction (coursel, rooml):
    action = []
    for co in coursel.courselist:
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
                    end = r[1]-co.sks+1
                    for i in range(begin, end+1):
                        s = i
                        e = i+co.sks-1
                        var = CSPvar(c,s,e,d,ro)
                        act = ActionClass(999,var)
                        action.append(act)
        else:
            R = None
            for room in rooml.roomlist:
                if room.room_id == co.room_cons:
                    R = room
                    #print(R)
                    break
            c = co.courseid
            ro = co.room_cons
            dayl = co.validday.checksameday(R.validday)
            #print(dayl)
            for day in dayl:
                    d = day
                    r = getrange(R.start, co.start, R.end, co.end)
                    begin = r[0]
                    end = r[1] - co.sks + 1
                    for i in range(begin,end+1):
                        s = i
                        e = i+co.sks-1
                        var = CSPvar(c, s, e, d, ro)
                        act = ActionClass(999,var)
                        action.append(act)
    return action

def gettotalconflict(var):
    sum = 0
    i = 0
    while i < len(var):
        j = i + 1
        while j < len(var):
            if (var[i].conflictcheck(var[j])):
                sum += 1
            j += 1
        i += 1
    return sum


class CSPvar (object) :
    def __init__(self, course, start, end, day, room):
        self.course = course
        self.start = start
        self.end = end
        self.day = day
        self.room = room
        
    def conflictcheck (self, cspvar2) :
        if type(cspvar2) is CSPvar:
            if self.room == cspvar2.room :
                if self.day == cspvar2.day :
                    if ((self.start >= cspvar2.start)and
                    (self.start<=cspvar2.end))or((cspvar2.start >= self.start)
                    and(cspvar2.start <= self.end)) :
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
    #@property
    def __str__(self):
       # assert isinstance(self.room, object)
        A = self.course + "\n" + str(self.start) + "\n" + str(self.end) + "\n" + \
            str(self.day)+"\n"+self.room +"\n"
        return A


class CSPconflict:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

class CSPvarlist:
    def __init__(self, varlist):
        self.var = []
        for el in varlist:
            var = CSPvar(el.course, el.start, el.end, el.day, el.room)
            self.var.append(var)

class hillclimbing:
    def __init__(self,coursel, rooml):
        self.var = initialize(coursel, rooml)
        self.conflict = []
        self.action = getallaction(coursel,rooml)

    def start(self):
        i = 0
        while i<len(self.var):
            j = i+1
            while j<len(self.var):
                if(self.var[i].conflictcheck(self.var[j])):
                    con=CSPconflict(self.var[i], self.var[j])
                    self.conflict.append(con)
                j+=1
            i+=1
        count = 0
        while gettotalconflict(self.var)>0 and count <500 :
            min = 999
            idx = 0
            j = 0
            for act in self.action:
                var_temp = CSPvarlist(self.var)
                i = 0
                while var_temp.var[i].course != act.change.course:
                    i+=1
                var_temp.var[i].start = act.change.start
                var_temp.var[i].end = act.change.end
                var_temp.var[i].day = act.change.day
                var_temp.var[i].room = act.change.room
                act.change.numcon = gettotalconflict(var_temp.var)
                if act.change.numcon<min:
                    min = act.change.numcon
                    idx = j
                j+=1
            i = 0
            while self.var[i].course!=self.action[idx].change.course:
                i+=1
            self.var[i].start = self.action[idx].change.start
            self.var[i].end = self.action[idx].change.end
            self.var[i].day = self.action[idx].change.day
            self.var[i].room = self.action[idx].change.room
            count = count+1
        for v in self.var:
            print(v)
        print(str(gettotalconflict(self.var)))






            
#main test
b = Bacafile()
c = allcourse("doc/Testcase.txt", b)
a = allroom("doc/Testcase.txt", b)
#print(a)
#print(c)
X = hillclimbing(c, a)
X.start()

            
        
                   
                    
                    
                    
