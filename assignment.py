class Student:
    def __init__(self,name,number,gender):
        self.name=name
        self.number=number
        self.gender=gender
   
    def show(self):
        
        print("이름은 {}, 전화번호는 {}, 성별은 {}입니다".format(self.name,self.number,self.gender))
student=[]
while True:
    
    name = input("이름을 입력하세요:")
    if name =="그만":
        break
    else:
        number = input("전화번호를 입력하세요:")
        gender = input("성별을 입력하세요:")    
        if gender != "male" and gender != "female":
            gender = "unknown"     
    student.append(Student(name,number,gender))
    for i in student:
        i.show()
for i in student:
 i.show()   