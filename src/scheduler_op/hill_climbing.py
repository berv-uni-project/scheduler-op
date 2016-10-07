import random
from scheduler_op.class_cons import *

class ActionClass:
    def __init__(self, con, var):
        self.numcon = con
        self.change = var

invalid_course = []


def initialize(coursel, rooml):
    ran = random
    X = []
    global invalid_course
    invalid_course = []
    for co in coursel.courselist:
        if co.room_cons == '-':
            R = rooml.getvalidroom(co)
            if (not R):
                print("No compatible room for this course", co.courseid)
                invalid_course.append(co)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                start = ran.randrange(r[0], r[1] - co.sks + 1)
=======
                if r[0]-r[1]-co.sks +1>1:
                    start = ran.randrange(r[0], r[1] - co.sks + 1)
                else:
                    start = r[0]
>>>>>>> 986cb52... fix random initialize
=======
                if r[0]-r[1]-co.sks>1:
                    start = ran.randrange(r[0], r[1] - co.sks)
                else:
                    start = r[0]
<<<<<<< HEAD

>>>>>>> 4547c3c... fix time constrain (sudah sesuai spek)
                end = start + co.sks - 1
<<<<<<< HEAD
=======
                if r[0]-r[1]-co.sks+1>1:
                    start = ran.randrange(r[0], r[1] - co.sks + 1)
                else:
                    start = r[0]
                end = start + co.sks
>>>>>>> e9fb1e6... fix the random in initializer
=======
>>>>>>> b0864f2... fix hill
                var = CSPvar(co.id, co.courseid, start, end, day, R[i].room_id)
=======
              #  print(r[0],r[1])
                end = start + co.sks - 1
                var = CSPvar(co.id, co.courseid, start, end, day, R[i].room_id, R[i].id)
>>>>>>> b6f783e... fixed
                #print(var.course, var.start, var.end, var.day, var.room)
                X.append(var)
        else:
            R = []
            for room in rooml.roomlist:
                if (not room.validday.ifsameday(co.validday)):
                    continue
                else:
                    r = getrange(room.start, co.start, room.end, co.end)
                    if (co.sks > r[1] - r[0]):
                        continue
                    else:
                        R.append(room)
            if R is None:
                print("No compatible room for this course", co.courseid)
            else:
                if len(R) > 1:
                    i = ran.randrange(0, len(R))
                else:
<<<<<<< HEAD
                    d = co.validday.checksameday(R.validday)
                    if len(d) > 1:
                        day = d[ran.randrange(0, len(d) - 1)]
                    else:
                        day = d[0]
                    r = getrange(R.start, co.start, R.end, co.end)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    start = ran.randrange(r[0], r[1] - co.sks + 1)
=======
                    if r[0] - r[1] - co.sks + 1 > 1:
                        start = ran.randrange(r[0], r[1] - co.sks + 1)
                    else:
                        start = r[0]
>>>>>>> 986cb52... fix random initialize
=======
                    if r[0] - r[1] - co.sks > 1:
                        start = ran.randrange(r[0], r[1] - co.sks)
                    else:
                        start = r[0]
=======
                    i = 0
                d = co.validday.checksameday(R[i].validday)
                if len(d) > 1:
                    day = d[ran.randrange(0, len(d) - 1)]
                else:
                    day = d[0]
                r = getrange(R[i].start, co.start, R[i].end, co.end)
                if r[0]-r[1]-co.sks>1:
                    start = ran.randrange(r[0], r[1] - co.sks)
                else:
                    start = r[0]
>>>>>>> b6f783e... fixed

>>>>>>> 4547c3c... fix time constrain (sudah sesuai spek)
                    end = start + co.sks - 1
<<<<<<< HEAD
=======
                    if r[0]-r[1]-co.sks+1 > 1:
                        start = ran.randrange(r[0], r[1] - co.sks + 1)
                    else:
                        start = r[0]
                    end = start + co.sks
>>>>>>> e9fb1e6... fix the random in initializer
=======
>>>>>>> b0864f2... fix hill
                    # print(R.room_id)
                    var = CSPvar(co.id, co.courseid, start, end, day, R[i].room_id, R[i].id)
                    #print('else', var.course, var.start, var.end, var.day, var.room)
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
                    if (end >= begin) :
                        for i in range(begin, end):
                            s = i
                            e = i+co.sks-1
                            var = CSPvar(co.id, c,s,e,d,ro, room.id)
                            act = ActionClass(999,var)
                            action.append(act)
        else:
            R = []
            for room in rooml.roomlist:
                if room.room_id == co.room_cons:
                    R.append(room)
                    #print(R)
            c = co.courseid
            ro = co.room_cons
            #print(dayl)
            for room in R:
                dayl = co.validday.checksameday(room.validday)
                for day in dayl:
                        d = day
                        r = getrange(room.start, co.start, room.end, co.end)
                        begin = r[0]
                        end = r[1] - co.sks+1
                        if (end >= begin) :
                            for i in range(begin,end):
                                s = i
                                e = i+co.sks-1
                                var = CSPvar(co.id, c, s, e, d, ro, room.id)
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

def gettotalconflictpersks(var):
    sum = 0
    i = 0
    while i < len(var):
        j = i + 1
        while j < len(var):
            nconflict = var[i].conflictcheckpersks(var[j])
            if (nconflict > 0):
                #print("konflik antara ", var[i].course, ' dan ', var[j].course )
                sum = sum + nconflict
            j += 1
        i += 1
    return sum

class CSPvar (object) :
    def __init__(self, id, course, start, end, day, room, roomid):
        self.id = id
        self.course = course
        self.start = start
        self.end = end
        self.day = day
        self.room = room
        self.roomid = roomid

    def conflictcheck (self, cspvar2) :
        if type(cspvar2) is CSPvar:
            if self.roomid == cspvar2.roomid :
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

    def conflictcheckpersks (self, cspvar2) :
        if type(cspvar2) is CSPvar:
            if self.roomid == cspvar2.roomid :
                if self.day == cspvar2.day :
                    if ((self.start >= cspvar2.start) and (self.start<=cspvar2.end)):
                        #print('masuk 1 end', cspvar2.end, ' start ', self.start, ' jadi ', cspvar2.end - self.start + 1)
                        return cspvar2.end - self.start + 1
                    elif((cspvar2.start >= self.start) and (cspvar2.start <= self.end)) :
                        #print('masuk 2 end', self.end, ' start ', cspvar2.start, ' jadi ', self.end - cspvar2.start + 1)
                        return self.end - cspvar2.start + 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
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
            var = CSPvar(el.id, el.course, el.start, el.end, el.day, el.room, el.roomid)
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
        while gettotalconflictpersks(self.var)>0 and count <500 :
            min = 999
            idx = 0
            j = 0
            for act in self.action:
                var_temp = CSPvarlist(self.var)
                i = 0
                while var_temp.var[i].id!= act.change.id:
                    i+=1
                var_temp.var[i].start = act.change.start
                var_temp.var[i].end = act.change.end
                var_temp.var[i].day = act.change.day
                var_temp.var[i].room = act.change.room
                var_temp.var[i].roomid = act.change.roomid
                act.change.numcon = gettotalconflictpersks(var_temp.var)
                if act.change.numcon<min:
                    min = act.change.numcon
                    #print(min)
                    idx = j
                j += 1
            i = 0
            if (idx!=0) :
                while self.var[i].id!=self.action[idx].change.id:
                    i += 1
                    if (i == len(self.var)):
                        i=i-1;
                        break;
                self.var[i].start = self.action[idx].change.start
                self.var[i].end = self.action[idx].change.end
                self.var[i].day = self.action[idx].change.day
                self.var[i].room = self.action[idx].change.room
                self.var[i].roomid = self.action[idx].change.roomid
                count = count+1
            else:
                count = 500;

        #for v in self.var:
            #print(v)
        #print(str(gettotalconflictpersks(self.var)))




"""
#main test
b = Bacafile()
c = allcourse("media/documents/Testcase.txt", b)
a = allroom("media/documents/Testcase.txt", b)
#print(a)
#print(c)
#var = initialize(c, a)
X = hillclimbing(c, a)
X.start()
"""

