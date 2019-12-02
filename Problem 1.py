import pandas as pd

a = {'Student' : ['Ice Bear','Panda','Grizzly'],
        'Math' : [80,95,79]}
b = {'Student' : ['Ice Bear','Panda','Grizzly'],
        'Electronics' : [85,81,83]}
c = {'Student' : ['Ice Bear','Panda','Grizzly'],
        'GEAS' : [90,79,93]}
d = {'Student' : ['Ice Bear','Panda','Grizzly'],
        'ESAT' : [93,89,88]}

dfa = pd.DataFrame(a,columns =['Student','Math'])
dfb = pd.DataFrame(b,columns =['Student','Electronics'])
dfc = pd.DataFrame(c,columns =['Student','GEAS'])
dfd = pd.DataFrame(d,columns =['Student','ESAT'])

merge = pd.merge(dfa,dfb, how = 'left', on ='Student')
merge2 = pd.merge(merge,dfc, how = 'left', on = 'Student')
mergeFinal = pd.merge(merge2,dfd, how = 'left', on = 'Student')

longFormat = pd.melt(mergeFinal,id_vars='Student',value_vars=['Math','Electronics','GEAS','ESAT'])
x = longFormat.rename(columns ={'variable':'Subject','value':'Grades'})
y = x.sort_values('Student').reset_index()
z = y.drop(columns='index')