# `Steps to run`

1. Create a New File named Bash.sh

2. Copy the Below code and Paste inside Bash.sh and save that File.
```
export JAVA_HOME=$(readlink -f $(which javac) | awk 'BEGIN {FS="/bin"} {print
$1}')
export PATH=$(echo $PATH):$(pwd)/bin
export CLASSPATH=$(hadoop classpath)
```

3. Execute the bash.sh File using following command source Bash.sh.
```sh
source bash.sh
```

4. Verify JAVA_HOME variable to be set to Java Path and PATH variable has your Hadoop Folder.If any previous PATH set to Hadoop Folder remove that inside .bashrc
file.

5. Verify Hadoop is Installed or not by executing hadoop command.if command gives Information about Hadoop command then Hadoop is Successfully Installed.

6. Create a folder sales and move to that folder

7. Make the driver.java, mapper.java and reducer.java files

8. Compile all java files (driver.java mapper.java reducer.java)
```sh
javac -d . *.java
```

9. Set driver class in manifest
```sh
echo Main-Class: sales.driver > Manifest.txt
```

10. Create an executable jar file
```sh
jar cfm sales.jar Manifest.txt sales/*.class
```

11. input.csv is input file for sales Input File

12. Run the jar file
```sh
hadoop jar sales.jar input.csv output
```

1.  To see the Output
```sh
cat output/*
```
