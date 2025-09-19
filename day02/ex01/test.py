from intern import Intern

intern_withoutname = Intern()
intern_mark = Intern("Mark")

print(intern_withoutname)
print(intern_mark)
intern_mark.make_coffee()

try:
    intern_withoutname.work()
except Exception as e:
    print(e)