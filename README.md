# `Spark Programs`

## `Steps to Execute`

1. Create your program directory and write program in <program_name>.py and copy the <input_file> in the same folder.

2. Execute Program using below command and give any name for output folder.
```cmd
spark-submit <program_name>.py <input_file> <output_folder_name>
```

3. To see output
```cmd
cat <output_folder_name>/*
```


### [`Program 1`](weather/)
Write a spark program to analyze the given Weather Report Data and to generate a report with cities having maximum and minimum temperature for a particular year.  

### [`Program 2`](earthquake/)
Write a spark program to analyze the given Earthquake Data and generate statistics with region and magnitude/ region and depth/ region and latitude/ region and longitude.

### [`Program 3`](insurance/)
Write a spark program to analyze the given Insurance Data and generate a statistics report with the construction building name and the count of building/ county name and its frequency.

### [`Program 4`](sales/)
Write a spark program to analyze the given Sales Records over a period of time and generate data about the country’s total sales, and the total number of the products. / country’s total sales and the frequency of the payment mode.