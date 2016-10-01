from hill_climbing import *
import random

class genetic_algorithm:
    def __init__(self, coursel, rooml, nString):
        self.all_strings = []
        i = 0
        while i < nString:
            var = initialize(coursel, rooml)
            self.all_strings.append(self.var)
            i =+ 1

    def cross_over(self, n, index1, index2):
        #n adalah nomor index pemotongan (misal n = 1, index dipotong setelah variabel ke 1)
        #I.S : 2 string of variabel
        #F.S : string variabel keduanya dipotong dan ditukar (cross over)
        set_of_var1 = self.all_strings[index1]
        set_of_var2 = self.all_strings[index2]
        varlen = len(set_of_var1)
        if (n < varlen):
            i = 0
            while i <= n :
                temp_var1 = set_of_var1.pop(i)
                temp_var2 = set_of_var2.pop(i)
                set_of_var1.insert(i,temp_var2)
                set_of_var2.insert(i,temp_var1)
                i =+ 1



