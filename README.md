# `Apache PIG`

## `Question Bank`

### [`Program 1`](crop_production.md)

Write Pig Latin scripts for crop production dataset.
* Calculate total production of each crop.
* Find the average production per year for each crop.
* Filter all crops grown in ‘Andaman and Nicobar Islands’
* Calculate the total area used for each crop in the year 2000.

### [`Program 2`](olympic_data.md)

Write Pig Latin scripts for Olympic athletes and hosts datasets.
* Filter athletes participated in the “Beijing 2022” games.
* Filter the games held in “China”.
* Group games by season and count the number of games in each session.
* Filter games that occurred after the year 2000.

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
