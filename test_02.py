ages=['0','2','3','10','15','20','25','80']
children=0
person=0
zhoulu=0
qingnian=0
chengnian=0
old=0
for age in ages:
    if age<'2':
        children+=1
    else:
        if age>='2' and age<'4':
            zhoulu+=1
        else:
            if age>='4'and age<'13':
                person+=1
            else:
                if age>='13' and age<'20':
                    qingnian+=1
                else:
                    if age>='20'and age<'65':
                        chengnian+=1
                    else:
                        old+=1
print(children)
print(zhoulu)
print(person)
print(qingnian)
print(chengnian)
print(old)