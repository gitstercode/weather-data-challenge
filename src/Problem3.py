import collections
import utils
path = utils.output_path + "YearlyAverages.out"
output_path = utils.output_path + "YearHistogram.out"

file = open(path,'r')
op_file = open(output_path,'w')
start_year = 1985
end_year = 2014
file_data = []
for line in file: file_data.append(line)
max_temp_values = []
min_temp_values = []
pre_temp_values = []
max_count = min_count = pre_count = 0
op_values = {}
while start_year <= end_year:
	for line in file_data:
		line_values = line.split("			")
		year = int(line_values[1])
		if year == start_year:
			max_temp_values.append(int(float(line_values[2])))
			min_temp_values.append(int(float(line_values[3])))
			pre_temp_values.append(int(float(line_values[4])))
	#print max_temp_values
	for line in file_data:
		line_values = line.split("			")
		if int(float(line_values[2])) == max(max_temp_values): max_count = max_count +1 
		if int(float(line_values[3])) == max(min_temp_values): min_count = min_count +1 
		if int(float(line_values[4])) == max(pre_temp_values): pre_count = pre_count +1 
	op_values[start_year] = str(max_count) + "&&&" + str(min_count) + "&&&" + str(pre_count)
	start_year = start_year + 1
	max_count = min_count = pre_count = 0
	max_temp_values = []
	min_temp_values = []
	pre_temp_values = []

sorted_op_values = collections.OrderedDict(sorted(op_values.items()))
for k, v in sorted_op_values.items():
	op = sorted_op_values[k].split('&&&')
	op_file.write(str(k) + "\t\t\t" + str(op[0]) + "\t\t\t" + str(op[1]) + "\t\t\t" + str(op[2]) +'\n')
op_file.close()