# `Iris Dataset`

1.	Load the dataset
```sh
iris = LOAD 'iris.csv' USING PigStorage(',') AS (sepal_length:float, sepal_width:float, petal_length:float, petal_width:float, species:chararray);

DESCRIBE iris;
```

2.	Calculate the average sepal length for each species
```sh
grouped_by_species = GROUP iris BY species;

average_sepal_length = FOREACH grouped_by_species GENERATE group AS species, AVG(iris.sepal_length) AS avg_sepal_length;

DUMP average_sepal_length;
```

3.	Find the maximum petal width for each species
```sh
grouped_by_species = GROUP iris BY species;

max_petal_width = FOREACH grouped_by_species GENERATE group AS species, MAX(iris.petal_width) AS max_petal_width;

DUMP max_petal_width;
```

4.	List all the unique species in the dataset
```sh
unique_species = GROUP iris BY species;

DUMP unique_species;
```
