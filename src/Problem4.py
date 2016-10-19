import os
import collections
from itertools import imap
import utils

def pearsonr(x, y):
  # Assume len(x) == len(y)
  n = len(x)
  sum_x = float(sum(x))
  sum_y = float(sum(y))
  sum_x_sq = sum(map(lambda x: pow(x, 2), x))
  sum_y_sq = sum(map(lambda x: pow(x, 2), y))
  psum = sum(imap(lambda x, y: x * y, x, y))
  num = psum - (sum_x * sum_y/n)
  den = pow((sum_x_sq - pow(sum_x, 2) / n) * (sum_y_sq - pow(sum_y, 2) / n), 0.5)
  if den == 0: return 0
  return num / den



path = utils.output_path + "YearlyAverages.out"
output_path = utils.output_path + "Correlations.out"
op_file = open(output_path, 'w')
anual_max_temp = []
anual_min_temp = []
anual_pre_temp = []
max_temp = min_temp = pre_temp = 0
file = open(path,'r')
start_year = 1985
end_year = 2014
file_data = []
for line in file: file_data.append(line)
while start_year <= end_year:
	for line in file_data:
		line_values = line.split("			")
		year = int(line_values[1])
		if year == start_year:
			max_temp = max_temp + float(line_values[2])
			min_temp = min_temp + float(line_values[3])
			pre_temp = pre_temp + float(line_values[4])
	anual_max_temp.append(max_temp/30)
	anual_min_temp.append(min_temp/30)
	anual_pre_temp.append(pre_temp/30)
	start_year = start_year + 1
file.close()
correlation_file = open(utils.correlation_path,'r')
correlation_values = []
for line in correlation_file:
	line_values = line.split("	")
	correlation_values.append(float(line_values[1]))
correlation_file.close()
op_file = open(output_path,'w')
op_file.write(str(pearsonr(anual_max_temp,correlation_values)) + "\t\t\t" + str(pearsonr(anual_min_temp,correlation_values)) + "\t\t\t" + str(pearsonr(anual_pre_temp,correlation_values)))
op_file.close()
