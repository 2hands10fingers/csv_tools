import csv

with open('OLD_CSV_FILE_NAME_GOES_HERE.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	with open('NEW_CSV_FILE_NAME_GOES_HERE.csv', 'w') as target_csv:
		theWriter = csv.writer(target_csv)
    
   
		next(csv_reader)  #Skip the column name
		
		for line in csv_reader:
	
			columnIndex = line[54] #Index of the column

			if bool(bulletOne) == True:
        
        """ 
	Wrapping the column's row data with <li></li> tags that contains data, 
     	    but skips a cell with no data. The else can be replaced with 'pass'
	    if you don't mind putting something in that cell.
	 """
				
        theWriter.writerow(
				[
				  "<li>" + columnIndex + "</li>"
				])
        
			else:
				theWriter.writerow([])
