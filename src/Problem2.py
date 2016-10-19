import os
import collections
import utils


output_path = utils.output_path + "YearlyAverages.out"
op_file = open(output_path, 'w')
#for filename in os.listdir(path):
#	print filename;
missing = -9999;
op_values = {}
for filename in os.listdir(utils.path):
	file = open(utils.path + filename, 'r')
	date_values = []
	max_temp_values = []
	min_temp_values = []
	precition_temp_values = []
	sum_max_temp_values = sum_min_temp_values = sum_precition_temp_values = 0
	year = ''
	for line in file:
		line_values = line.split("	")
		if year == '':
			year = line_values[0][:4]
		elif year != line_values[0][:4]:
			total_count = len(max_temp_values)
			for value in max_temp_values:
				if value != missing: sum_max_temp_values = sum_max_temp_values + value
			for value in min_temp_values:
				if value != missing: sum_min_temp_values = sum_min_temp_values + value
			for value in precition_temp_values:
				if value != missing: sum_precition_temp_values = sum_precition_temp_values + value
			avg_max_temp_values = round(sum_max_temp_values/total_count,2)
			avg_min_temp_values = round(sum_min_temp_values/total_count,2)
			avg_precition_temp_values = round(sum_precition_temp_values/10,2)
			op_values[filename + "_" + year] = str(avg_max_temp_values)+"&&&"+str(avg_min_temp_values)+"&&&"+str(avg_precition_temp_values)+"&&&"+filename
			max_temp_values = []
			min_temp_values = []
			precition_temp_values = []
			year = line_values[0][:4]
			sum_max_temp_values = sum_min_temp_values = sum_precition_temp_values = 0
		max_temp_values.append(float(line_values[1]))
		min_temp_values.append(float(line_values[2]))
		precition_temp_values.append(float(line_values[3].split('\n')[0]))


	total_count = len(max_temp_values)
	for value in max_temp_values:
		if value != missing: sum_max_temp_values = sum_max_temp_values + value
	for value in min_temp_values:
		if value != missing: sum_min_temp_values = sum_min_temp_values + value
	for value in precition_temp_values:
		if value != missing: sum_precition_temp_values = sum_precition_temp_values + value
	avg_max_temp_values = round(sum_max_temp_values/total_count,2)
	avg_min_temp_values = round(sum_min_temp_values/total_count,2)
	avg_precition_temp_values = round(sum_precition_temp_values/total_count,2)
	op_values[filename + "_" + year] = str(avg_max_temp_values)+"&&&"+str(avg_min_temp_values)+"&&&"+str(avg_precition_temp_values)+"&&&"+filename
	file.close()

#[value for value in max_temp_values if value != missing]
#sorted_op_values = sorted(op_values.items(), key=operator.itemgetter(0))
sorted_op_values = collections.OrderedDict(sorted(op_values.items()))
for k, v in sorted_op_values.items():
	op = sorted_op_values[k].split('&&&')
	op_file.write(op[3] + "\t\t\t" + k.split('_')[1] + "\t\t\t" + op[0] + "\t\t\t" + op[1] + "\t\t\t" + op[2] +'\n')
op_file.close()
