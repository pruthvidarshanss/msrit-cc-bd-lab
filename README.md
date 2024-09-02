# `Hadoop Programs`

## `Steps to Execute`

1. Create a folder <program> and move into that folder.

2. Edit the driver.java, mapper.java and reducer.java files.

3. Compile all java files (driver.java, mapper.java, reducer.java)
```cmd
javac -d . *.java
```

4. Set driver class in manifest.
```cmd
echo Main-Class: <program>.driver > Manifest.txt
```

5. Create an executable jar file.
```cmd
jar cfm <program>.jar Manifest.txt <program>/*.class
```

6. Run the jar file
```cmd
hadoop jar <program>.jar <input-file> output
```

7. View the Output
```cmd
cat output/*
```


### [`Program 1`](weather/)

Write a MapReduce program to analyze the given Weather Report Data and to generate a report with cities having maximum and minimum temperature for a particular year.

### [`Program 2`](earthquake/)

Write a MapReduce program to analyze the given Earthquake Data and generate statistics with region and magnitude/ region and depth/ region and latitude/ region and longitude.

### [`Program 3`](oddeven/)

Write a MapReduce program to analyze the given natural numbers and generate statistics for the number as Odd or Even and print their sum.

### [`Program 4`](insurance/)

Write a MapReduce program to analyze the given Insurance Data and generate a statistics report with the construction building name and the count of building/county name and its frequency.

### [`Program 5`](employee/)

Write a MapReduce program using Java, to analyze the given employee record data and generate a statistics report with the total number of Female and Male Employees and their average salary.

### [`Program 6`](sales/)

Write a MapReduce program using Java, to analyze the given Sales Records over a period of time and generate data about the country’s total sales, and the total number of the products. Country’s total sales and the frequency of the payment mode.

### [`Program 7`](matrix/)

Matrix Multiplication

### [`Program 8`](wordcount/)

WordCount