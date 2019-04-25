from builtins import iter
import mymodule as mx
import platform
import datetime
import json
import os
import pandas as pd
import numpy as np
#import pymongo
import sys

class Mynumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a<=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

        #mynumber = Mynumber()
        #myiter = iter(mynumber)

        for x in myiter:
            print(x)
        print("\n")
        a = mx.person1["age"]
        print(a)

        z = platform.system()
        print(z)

        c = dir(platform)
        print(c)

        mytimestamp = datetime.datetime.now()
        print(mytimestamp.year)
        print(mytimestamp.month)
        print(mytimestamp.day)
        print(mytimestamp.hour)

        print("\n")
        t = '{"name": "Carrey", "year" : "2006", "country" : "Armania" }'
        b = json.loads(t)
        for x in b:
            print(t)
            break


        person2 = {
          "name": "John",
          "age": 36,
          "country": "Africa"
        }

        i = json.dumps(person2)

        print(i)


        person3 = {
          "name": "John",
          "age": 30,
          "married": True,
          "divorced": False,
          "children": ("Ann","Billy"),
          "pets": None,
          "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
          ]

        }

        nom = json.dumps(person3, indent=3)
        print(nom)

        f = open("cool.txt", "r")
        print(f.read())

        fr = open("cool.txt", "a")
        fr.write("\nnew line is being added")
        print(f.read())

        fw = open("cool.txt", "w")
        fw.write("\n overwrited the file over here")
        print(f.read())

        fn = open("cool.txt", "x")
        fn = open("cool.txt", "a")
        fn.write("new line in new file")

        f = open("cool.txt", "r")
        print(f.read())

#Pandas IMPL over here#
###########Pandas Series ##################
    def pandaSeries_impl(self):
        print("\n###########Pandas Series ##################")
        s= pd.Series()
        print(s)
        print("\n")
        data = np.array(['Z1','Z2','Z3','Z4','Z5'])
        series1= pd.Series(data,index=['101','102','103','104','105'])
        print(series1)
        print("\n")

        data1= {'a' : 0., 'b' : 1., 'c' : 2., 'd' : 3.}
        series2= pd.Series(data1,index=['a','b','c','d'])
        print(series2)
        print("\n")

        s3=pd.Series(6,index=[0,1,2,3])
        print(s3)
        print("\n")
        print(series2[:3])
        print(series2[-3:])

###########Pandas DataFrame ##################

    def panadasDataFrame_imp(self):
        print("\n###########Pandas DataFrame ##################")
        df = pd.DataFrame()
        print(df)
        data= [1,2,3,4,5]
        df1=pd.DataFrame(data)
        print(df1)

        print("\n")
        data=[["Alex",10],["Carey",20],["Foxtron",30]]
        df3=pd.DataFrame(data,columns=["Name", "Age"],index=[1,2,3])
        print(df3)

        dict1=[{"Name": ['Tom','Rider','Christian','Jacob'],"Class": ['1','2','3','4']},{'a': 1, 'b': 2}]
        datafr_student= pd.DataFrame(dict1)
        print(datafr_student)
        print("\n")

    def newDataFrame(self):
        d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

        df = pd.DataFrame(d)
        print(df)
        print(df[0:2])

        df = pd.DataFrame([[1, 2, 3], [3, 4, 5], [9, 10, 11]], columns=['a', 'b', 'c'])
        print(df)
        df2 = pd.DataFrame([[5, 6, 7], [7, 8, 9], [11, 12, 13]], columns=['a', 'b','c'])
        print(df2)
        df = df.append(df2)
        print("Final Df is:\n")
        print(df)
        print("Now Deletion")

        df = df.drop(0)
        print(df)

    def newPanelPandas(self):
        panel1 = pd.Panel()
        print(panel1)

        data = {'Item1' : pd.DataFrame(np.random.randn(4,3)),
        'Item2' : pd.DataFrame(np.random.randn(4,2))}

        panel2= pd.Panel(data)
        print(panel2.major_xs(1))
        print("\n")
        s = pd.Series(np.random.randn(4))
        print(s)
        print("\n")
        
        q =pd.Series(np.random.randn(8))
        print(q.axes)
        print(q.empty)
        print(q.ndim)
        print(q.size)
        print(s.values)

        d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
             'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
             'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}

        dataframe1 = pd.DataFrame(d)
        print(dataframe1)
        print("#######Doing some functionality on the DataFrame")
        print("\n")
        print(dataframe1.T)
        print(dataframe1.axes)
        print(dataframe1.dtypes)
        print(dataframe1.ndim)
        print(dataframe1.shape)
        print(dataframe1.size)
        print("\n")
        print(dataframe1.values)

        print("\n")
        print(dataframe1.describe(include='all'))

    def learnDataFrame(self):
        dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
                "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
                "population": [200.4, 143.5, 1252, 1357, 52.98],
                "area": [8.516, 17.10, 3.286, 9.597, 1.221]}
        brics = pd.DataFrame(dict)
        print(brics)

        brics.index = ["BR", "RU", "IN", "CH", "SA"]
        print(brics)
        print("\n")
        meeting1 = pd.read_csv("3.csv")
        print(meeting1)


########### MongoDB Connection ##################
    def makeConnection(self):
        myClient =  pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myClient["mydatabase"]

        dblist = myClient.list_database_names()
        if "mydatabase" in dblist:
            print("database exists")

        mycol = mydb["customers"]

        collist = mydb.list_collection_names()

        if "customers" in collist:
            print("document exists")

        mydict = {"name": "John", "age" : "21"}
        x = mycol.insert_one(mydict)
        print(x)

    def newMethod(self):
        #print('Hello')
        print(sys.float_info)
        print(type(2))

myno= Mynumber()
'''myno.pandaSeries_impl()
myno.panadasDataFrame_imp()
myno.newDataFrame()'''
myno.newPanelPandas()
'''myno.learnDataFrame()'''
'''myno.makeConnection()'''
'''myno.newMethod()'''
