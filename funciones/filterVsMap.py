def f(x): return x * 2
def m(y): return y % 2 == 0

list1 = [1,2,3,4]

flist = list(filter(m,list1))
print(flist)

mlist = list(map(m,list1))
print(mlist)
