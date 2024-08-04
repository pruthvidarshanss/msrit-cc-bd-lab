# `Apache PIG`

## `Installation`

1.	Download the new release of Apache Pig from the below [link](https://downloads.apache.org/pig/pig-0.17.0/). In my case I have downloaded the pig-0.17.0.tar.gz version of Pig which is latest and about 220MB in size. 

2.	Now we extract this tar file with the help of below command (make sure to check your tar filename).
```sh
tar -xvf pig-0.17.0.tar.gz
```

3.	Create and open a new bash.sh file inside the directory.
```sh
gedit bash.sh
```

4.	We configure file, copy the below command inside this file and save it.
```text
export PIG_INSTALL=$(pwd) 
export PATH=$PATH:$(pwd)/bin
```

5.	Execute the bash.sh File using following command 
```sh
source bash.sh
```

6.	You can check your pig version with the below command.
```sh
pig -version
```

7.	Once you get it correct that’s it we have successfully install pig to our Hadoop single node setup, now we start pig with below pig command.
```sh
pig
```

### [`Program 1`](crop_production.md)

Crop Production Dataset with 4 different queries.

### [`Program 2`](exam.md)

Exams dataset with 3 different queries.

### [`Program 3`](iris.md)

Iris dataset with 3 different queries.

### [`Program 4`](olympic_athletes.md)

Olympic Athletes dataset with 3 different queries

### [`Program 5`](olympic_hosts.md)

Olympic Hosts dataset with 3 different queries
