class Student:
    student_num = 0 #!类变量
    
    def __init__(self, name, sex) -> None:
        self.name = name
        self.sex = sex
        Student.student_num += 1 # 类变量通过类名来访问
        # self.student_num += 1 # 类变量通过实例来访问
    
    #! 类方法 第一个参数是类本身，通常用cls表示
    @classmethod
    def add_students(cls, add_num):
        cls.student_num += add_num

    # 在类方法from_string中解析输入，再调用构造函数
    @classmethod
    def from_string(cls, info):
        name, sex = info.split(' ')
        return cls(name, sex)
    
    #! 静态方法：不能访问类中的私有属性和方法
    @staticmethod
    def name_len(name):
        return len(name)
    

s1 = Student('Qiqi', 'female')

print(f'Student.student_num:{Student.student_num}')  # 0
print(f's1.student_num:{s1.student_num}') # 1
# reason : 

s2 = Student.from_string('Qiqi female')
print(f'Student.student_num:{Student.student_num}')  # 0
print(f's2.name:{s2.name}, s2.name_len:{Student.name_len(s2.name)}')