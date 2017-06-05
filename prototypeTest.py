import copy 
# import gui.intro_tkinter
import play_ground.Hello

class ICloneable: 
    def shallowClone(self): 
        return copy.copy(self) 
     
    def deepClone(self): 
        return copy.deepcopy(self) 


class WorkExperience(ICloneable): 
    workData = "" 
    company = "" 

class Resume(ICloneable): 
#     name = "" 
#     sex = "" 
#     age = 0 
#     work = None 

    def __init__(self, name): 
        self.name = name 
        self.work = WorkExperience()

    def setPersonInfo(self, sex, age): 
        self.sex = sex 
        self.age = age 

    def setWorkExperience(self, workData, company): 
        self.work.workData = workData 
        self.work.company = company
             
    def display(self): 

        print('%s, %s, %d' % (self.name,self.sex,self.age)) 

        print('%s, %s' % (self.work.workData, self.work.company)) 

 
def client(): 

    a = Resume('Tom') 
    a.setPersonInfo('m',29) 
    a.setWorkExperience("1998-2000","ABC.COM")     

    b = a.shallowClone()
    b.setWorkExperience("2000-2006","QQ.COM")         

    c = a.deepClone()
    c.setWorkExperience("2006-2009","360.COM")     
     
    
    a.display()
    b.display()   
    c.display()     
    return 

if __name__ == '__main__': 
    client();
    
