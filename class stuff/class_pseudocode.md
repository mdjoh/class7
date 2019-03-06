1. Load data
-get filename from user (using argparse NOT input; for automation)
-(optionally) get header file from user (also in argparse)
-ensure file exists
-read first few lines -- enough so we can see outliers
	a) visually inspect it
 	b) check data type of each row in each column, and see if consistent
		-open file, readline(s)
		-make our csv reader (very long code...)
	c) fully load the data (doing it twice which can be resource intensive; hence, trade-off)

2. "organize" data (adding header)
- if we have a header in our data file:
	- load it, tell pandas to look in the first row for a header

-otherwise:
	- if header file provided:
		- load header file ("open" and "read()" of the file)
		- verify that the number of columns matches number of columns in data
		- load data and add header (pandas can accept a list of col. names)

	-otherwise:
		a) throw an exception and exit
		b) move on without a header

Step 1&2 hybrid:
- try:
	-load data with pandas, enforcing that things are numbers, while assuming there is no header; this will throw
	 an error if it's not a number
- except (ValueError, FileNotFoundError) as e:
	- code to handle this type of error
- except Exception as e:
	- print(e)

***deal with specific errors

*** Steps 1 and 2 are for loading data and dealing with headers or with not having headers ***

Assuming numerical data has been loaded and headers are correct:
3. Summary stats (mean, stdev for each column)
- np.mean(dataframe, axis=0)
- np.std(dataframe, axis=0)

axis=0 meaning calculate going down the column

what numpy is doing:
- for column in dataframe:
	- np.mean(column)
	- np.std(column)

4. plot (1 feature) (ie. a histogram)
- for column in dataframe.columns:
	- data = dataframe[columns]
	- newfig = creating a new blank figure
	- plot historgram on newfig
	- name y axis "count" x axis "bin/column name"
	- title "column name"
	- save newfig with desired file name determined by column
	- clear/reset figure

actual plotting code:
	for idx in len(dataframe.columns:
		data = dataframe.iloc[:,idx]

5. plot (2 features together ie. scatter plot)
for idx, column1 in enumerate(dataframe):
	for jdx, column2 in dataframe.iloc[:, idx+1]:
		data1 = dataframe[column1]
		data2 = dataframe[column2]
		plt.scatter(data1, data2)

- save files like step 4

