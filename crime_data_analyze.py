import sys

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hours = list(range(24))
months = list(range(1,13))

def ConvertToInt(var):
	try:
		var = int(var)
	except:
		pass
	return var

def CsvToLists(fp):
	csv_file = open(fp)
	data_lists = []
	for line in csv_file:
		data_lists.append(line.rstrip('\n').split(','))
	return data_lists

def CategorizedByDay(data):
	day_dict = {}
	for day in days:
		day_dict[day] = []

	for item in data:
		if item[3] in days:
			day_dict[item[3]].append(item)

	return day_dict

def CategorizedByHour(data):
	hour_dict = {}
	for hour in hours:
		hour_dict[hour] = []

	for item in data:
		only_hour = ConvertToInt(item[5].split(':')[0])
		if only_hour in hours:
			hour_dict[only_hour].append(item)
	return hour_dict

def CategorizedByMonth(data):
	month_dict = {}
	for month in months:
		month_dict[month] = []

	for item in data:
		only_month = ConvertToInt(item[4].split('/')[0])
		if only_month in months:
			month_dict[only_month].append(item)
	return month_dict

def CategorizedByCategory(data):
	category_dic = {}
	for item in data:
		if item[1] != 'Category':
			category_dic[item[1]] = []

	for item in data:
		if item[1] in category_dic:
			category_dic[item[1]].append(item)
	return category_dic

def main():
    sf_data = CsvToLists(sys.argv[1])
    se_data = CsvToLists(sys.argv[2])

    print sf_data[0]
    print sf_data[1]

    sf_day = CategorizedByDay(sf_data)
    #for day in days:
    #	print "-------------------", day, "-------------------"
    #	sf_day_hour = CategorizedByHour(sf_day[day])
    #	for hour in hours:
    #		print hour, len(sf_day_hour[hour])

if __name__ == '__main__':
    main()