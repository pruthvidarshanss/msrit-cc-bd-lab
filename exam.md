# `Exams Dataset`

1.	Load the dataset
```sh
exams = LOAD 'exams.csv' USING PigStorage(',') AS (gender:chararray, race_ethnicity:chararray, parental_level_of_education:chararray, lunch:chararray, test_preparation_course:chararray, math_score:int, reading_score:int, writing_score:int);

DESCRIBE exams;
```

2.	Count the Number of Students in Each Race/Ethnicity Group
```sh
grouped_by_race = GROUP exams BY race_ethnicity;

count_students_by_race = FOREACH grouped_by_race GENERATE group AS race_ethnicity, COUNT(exams) AS student_count;

DUMP count_students_by_race;
```

3.	Concatenate Gender and Parental Level of Education for Each Record
```sh
concatenated_fields = FOREACH exams GENERATE CONCAT(gender, ' - ', parental_level_of_education) AS gender_education;

DUMP concatenated_fields;
```

4.	List all the unique parental levels of education
```sh
unique_education_levels = GROUP exams BY parental_level_of_education;

DUMP unique_education_levels;
```