def getrange(s1,s2,e1,e2):
    range = []
    if(s1 > s2):
        range.append(s1)
    else:
        range.append(s2)
    if(e1 > e2):
        range.append(e2)
    else:
        range.append(e1)
    return range

class day_bool:
    def __init__(self, validday):
        self.day = [False] * 6
        for char in validday:
            self.day[int(char)] = True
            #  print(self.day[int(char)], char)

    def __str__(self):
        A = "1 : " + str(self.day[1]) + " 2 : " + str(self.day[2]) + " 3 : " + \
            str(self.day[3]) + " 4 : " + str(self.day[4]) + " 5 : " + \
            str(self.day[5])

    def checksameday(self, self2):
        r = []
        for i in [1, 2, 3, 4, 5]:
            if self.day[i] and self2.day[i]:
                r.append(i)
        return r
    def ifsameday(self, self2):
        for i in [1, 2, 3, 4, 5]:
            if self.day[i] and self2.day[i]:
                return True

class room:
    def __init__(self, rid, start, end, vday):
        self.room_id = rid
        self.start = start
        self.end = end
        self.validday = vday

    def __str__(self):
        A = self.room_id + "\n" + str(self.start) + "\n" + str(self.end) + "\n" + \
            str(self.validday)
        return A


class allroom:
    def __init__(self, filename, b):
        f = open(filename, 'r')
        temp = b.bacakata(f)
        self.roomlist = []
        while (temp != "Ruangan" and temp != ""):
            temp = b.bacakata(f)
        temp = b.bacakata(f)
        while (temp != "Jadwal" and temp != ""):
            r_id = temp;
            start = b.strtojam(b.bacakata(f))
            end = b.strtojam(b.bacakata(f))
            temp = b.strtohari(b.bacakata(f))
            vday = day_bool(temp)
            x = room(r_id, start, end, vday)
            (self.roomlist).append(x)
            temp = b.bacakata(f)

    def __str__(self):
        A = ""
        for a in self.roomlist:
            A = A + str(a) + "\n"
        return A
    
    def getvalidroom(self, co):
        R=[]
        for room in self.roomlist:
                if (not room.validday.ifsameday(co.validday)):
                    continue
                else:
                    r = getrange(room.start, co.start, room.end, co.end)
                    if (co.sks > r[1] - r[0]):
                        continue
                    else:
                        R.append(room)
        return R


class course:
    def __init__(self, id, courseid, r_cons, start, end, sks, validday):
        self.id = id
        self.courseid = courseid
        self.room_cons = r_cons
        self.start = start
        self.end = end
        self.sks = sks
        self.validday = validday

    def __str__(self):
        A = self.courseid + "\n" + self.room_cons + "\n" + str(self.start) + "\n" + str(self.end) + "\n" + \
            str(self.validday)
        return A


class allcourse:  # kelas kuliah yang untuk konstrain kuliah
    def __init__(self, filename, b):
        id = 0
        f = open(filename, 'r')
        self.courselist = []
        temp = b.bacakata(f)
        while (temp != "Jadwal" and temp != ""):
            temp = b.bacakata(f)
        temp = b.bacakata(f)
        while (temp != "Ruangan" and temp != ""):
            courseid = temp;
            r_cons = b.bacakata(f)
            start = b.strtojam(b.bacakata(f))
            end = b.strtojam(b.bacakata(f))
            sks = int(b.bacakata(f))
            temp = b.strtohari(b.bacakata(f))
            vday = day_bool(temp)
            x = course(id, courseid, r_cons, start, end, sks, vday)
            (self.courselist).append(x)
            id += 1
            temp = b.bacakata(f)

    def __str__(self):
        A = ""
        for a in self.courselist:
            A = A + str(a) + "\n"
        return A

"""
# Test
b = Bacafile()
c = allcourse("Testcase.txt", b)
a = allroom("Testcase.txt", b)
print(a)
print(c)"""
