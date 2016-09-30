import random
import sys
from class_cons import *
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
    @property
    def __str__(self):
        assert isinstance(self.room, object)
        A = self.course + "\n" + "\n" + str(self.start) + "\n" + str(self.end) + "\n" + \
            str(self.day)+"\n"+self.room
        return A


class CSPcons:
    pass


def initialize(coursel, rooml):
    ran = random
    X = []
    for co in coursel.courselist:
        if co.room_cons == '-':
            R = []
            for room in rooml.roomlist:
                if (not room.validday.ifsameday(co.validday)):
                    continue
                else:
                    r = getrange(room.start, co.start, room.end, co.end)
                    if (co.sks >= r[1] - r[0] + 1):
                        continue
                    else:
                        R.append(room)
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
                end = start + co.sks - 1
                var = CSPvar(co.courseid, start, end, day, R[i].room_id)
                print(var.course, var.start, var.end, var.day, var.room)
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
                    end = start + co.sks - 1
                    # print(R.room_id)
                    var = CSPvar(co.courseid, start, end, day, R.room_id)
                    print(var.course, var.start, var.end, var.day, var.room)
                    X.append(var)
    
    """ start = ran.randrange(room.start, room.end-element.sks+1)
                    end = start+element.sks-1
                    day = ran.randrange(0,len(r)-1)"""
#main test
b = Bacafile()
c = allcourse("Testcase.txt", b)
a = allroom("Testcase.txt", b)
#print(a)
#print(c)
initialize(c,a)
            
        
                   
                    
                    
                    
