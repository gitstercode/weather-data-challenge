import os
from operator import itemgetter
import collections
import utils

output_path = utils.output_path + "MissingPrcpData.out"
op_file = open(output_path, 'w')
missing = -9999;
op_values = {}
for filename in os.listdir(utils.path):
	file_path = utils.path + filename;
	file = open(file_path, 'r')
	count = 0
	for line in file:
		line_values = line.split("	")
		if int(line_values[1]) != missing and int(line_values[2]) != missing and int(line_values[3].split('\n')[0]) == missing: count = count + 1
	op_values[filename] = count
	file.close()

#sorted(op_values, key=itemgetter('filename'))
sorted_op_values = collections.OrderedDict(sorted(op_values.items()))
for k, v in sorted_op_values.items():
	op_file.write(k + "\t\t" + str(v) + "\n")
op_file.close()