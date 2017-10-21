import csv

with open('OLD_CSV_FILE_NAME_GOES_HERE.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	with open('NEW_CSV_FILE_NAME_GOES_HERE.csv', 'w') as target_csv:
		theWriter = csv.writer(target_csv)
    
    #Skip the column name
		next(csv_reader)
		for line in csv_reader:

			#Index of the column
			columnIndex = line[54]

			if bool(bulletOne) == True:
        
        # Wrapping the column's row data with <li></li> tags that contains data, 
        
        # but skips a cell with no data
				
        theWriter.writerow(
				[
				  "<li>" + columnIndex + "</li>"
				])
        
			else:
				theWriter.writerow([])
