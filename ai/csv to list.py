data=[1989,0.0,
1990,-0.9,
1991,-0.1,
1992,0.5,
1993,-2.5,
1994,-0.9,
1995,-2.1,
1996,-2.4,
1997,-0.6,
1998,2.6,
1999,3.2,
2000,2.0,
2001,2.4,
2002,3.5,
2003,3.4,
2004,3.6,
2005,0.6,
2006,3.1,
2007,3.2,
2008,1.8,
2009,3.2,
2010,3.5,
2011,2.3,
2012,6.4,
2013,4.5,
2014,5.9,
2015,6.3,
2016,9.5,
2017,5.1,
2018,4.6,
2019,7.6,
2020,9.1,]

DataX=[]
DataY=[]

for i in range(32):
    DataX.append(data[i*2])
    DataY.append(data[i*2+1])
print(DataX)
print(DataY)