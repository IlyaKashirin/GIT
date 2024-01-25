from datetime import datetime
data_string1 = 'The Moscow Times - Wednesday, October 02 2002'
data_string2 = 'The Guardian - Friday, 11.10.13'
data_string3 = 'Daily News - Thursday, 18 August 1977'
data1 = datetime.strptime('Wednesday, October 02 2002','%A, %B %d %Y')
data2 = datetime.strptime('Friday, 11.10.13','%A, %d.%m.%y')
data3 = datetime.strptime('Thursday, 18 August 1977','%A, %d %B %Y')
print(data1)
print(data2)
print(data3)


