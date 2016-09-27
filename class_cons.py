import sys
from bacafilez import * #agar bisa mengambil data

def booltostr(b):
        if(b):
            return "True"
        else:
            return "False"

class day_bool:
    def __init__(self, validday):
        self.day = [False]*6
        for char in validday:
            self.day[int(char)] = True
          #  print(self.day[int(char)], char)
    def __str__(self):
        A = "1 : "+booltostr(self.day[1]) + " 2 : "+\
        booltostr(self.day[2])+" 3 : "+booltostr(self.day[3])+\
        " 4 : "+booltostr(self.day[4])+" 5 : "+booltostr(self.day[5])
        return A
class room:
    def __init__(self, f, b):
        temp = b.bacakata(f)
        self.room_id = temp
        temp = b.bacakata(f)
        self.start = b.strtojam(temp)
        temp = b.bacakata(f)
        self.end = b.strtojam(temp)
        temp=(b.strtohari(b.bacakata(f)))
        self.validday = day_bool(temp)
        print(self.room_id, self.start, self.end, self.validday)


class allroom:
    def __init__(self, filename,b):
        f = open(filename,'r')
        while(temp != "Ruangan"):
            b.bacakata(f)
        
"""
class course:
    def __init__(self, courseid):
    self.courseid = none
    self.
		
class all_course: #kelas kuliah yang untuk konstrain kuliah
    def __init__(self,filename):
        f = open(filename, 'r')
        temp = 'there is no course information in this file'
        self.
            for line in f:
                if line == 'Jadwal\n':
                    for line in f:
                        if line == none or line == 'Ruangan\n':
                            break
                        else
                            self.
                            break
                            print(kul)

"""			
			

#Test
b = Bacafile()
a = room("Testcase.txt", b)

		
