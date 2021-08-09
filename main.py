
import numpy as np
import math


class MyMatrix:
    def __init__(self, name, rows=1, columns=1, ls=None):
        self.name = name
        self.matrix = np.zeros((rows, columns))
        if len(ls) > rows*columns:
            num = math.sqrt(len(ls))
            num = math.ceil(num)
            self.matrix = np.zeros((num, num))
            rows = num
            columns = num
        if ls is not None:
            row = 0
            col = 0
            for item in ls:
                self.matrix[row, col] = item
                col += 1
                if col % columns == 0:
                    col = 0
                    row = row+1
        self.__count = rows*columns

    def count(self):
        return self.__count

    def add(self, num):
        self.matrix += num
        return self

    def add_diag(self, ls=None):
        if ls is None:
            return
        if len(ls) > len(self.matrix):
            ls = ls[:len(self.matrix)]
        else:
            ls += [x*0 for x in range(len(self.matrix)-len(ls))]
        self.matrix += np.diag(ls)
        return self

    def add_checkered(self, val=1, first_flag=True):
        new_mat = MyMatrix.create_checkered_matrix(val, first_flag, self.matrix)
        self.matrix += new_mat
        return self

    @staticmethod
    def create_checkered_matrix(val,first_flag, matrix_like):
        first = 0
        if first_flag:
            first = 1
        mat = np.zeros_like(matrix_like)
        mat[::2, 1 - first::2] = val
        mat[1::2, first::2] = val
        return mat

    def sum(self):
        return self.matrix.sum()

    def __setitem__(self, key, value):
        if isinstance(key, int):
            row = int(np.floor(key / len(self.matrix[0])))
            col = int(int(key) % len(self.matrix[0]))
            if (row * len(self.matrix[0]) + (col + 1)) > self.matrix.size:
                raise Exception("Out Of Bounds")
            self.matrix[row, col] = value
            return
        if key[0] > len(self.matrix) or key[1] > len(self.matrix[0]):
            raise Exception("Out Of Bounds")
        self.matrix[key[0], key[1]] = value

    def __getitem__(self, arg):
        if isinstance(arg, int):
            row = int(np.floor(arg/len(self.matrix[0])))
            col = int(int(arg) % len(self.matrix[0]))
            if (row*len(self.matrix[0]) + (col+1)) > self.matrix.size:
                return "Out Of Bounds"
            return self.matrix[row, col]
        if arg[0] > len(self.matrix) or arg[1] > len(self.matrix[0]):
            return "Out Of Bounds"
        return self.matrix[arg[0], arg[1]]

    def how_many(self, val):
        cnt = 0
        for i in range(self.count()):
            if self[i] == val:
                cnt += 1
        return cnt

    def row_size(self):
        return self.matrix.size

    def size(self):
        return self.matrix.size

    def __del__(self):
        print(self.name,"say: it was pleasure to serve you !")

    def change_name(self, name):
        self.name = name
        return self

    def replace(self,from_val,to_val):
        self.matrix = np.where(self.matrix == from_val, to_val,self.matrix)
        return self

    def unique_list(self):
        return self.even_numbers() + self.odd_numbers()

    def even_numbers(self):
        return list(set([self[int(i)] for i in range(self.count()) if self[int(i)] % 2 == 0]))

    def odd_numbers(self):
        return list(set([self[int(i)] for i in range(self.count()) if self[int(i)] % 2 == 1]))

    def __str__(self):
        string = self.name + ":\n"
        string += self.matrix.__str__()
        return string

    def __iter__(self):
        self.it_index = int(0)
        return self

    def __next__(self):
        if self.it_index < self.count():
            it = self[self.it_index]
            self.it_index += 1
            return it
        else:
            raise StopIteration


mm = MyMatrix("Tomer1", ls=[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0])
mm[1] = 5

mm.replace(1, 3)
print(mm.count())
print(mm.odd_numbers())
print(mm.even_numbers())
print(mm.unique_list())
ls = []
my_iter = iter(mm)
for item in my_iter:
    ls.append(item)
print(ls)




