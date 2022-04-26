import sys

test_number = 5

file_name_pre = 'yeast6'

record_name = 'execute.sh'
file = open(record_name,'w')
for i in range(1, 1+test_number):
    file.write('python drawpic.py train_file_name=./1_year_data/{0}_train_{1}.csv test_file_name=./1_year_data/{0}_test_{1}.csv \n'.format(file_name_pre, i))
file.close()