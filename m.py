class m:
    def list(self):
        list = ["1","2","3","4","5"]
        list = [ int(i) for i in list]
        list.sort();
        print(list)

myclass = m()
myclass.list();
