# `Crop Production Dataset `

1.	Load the dataset
```sh
crop_prod = LOAD 'Datasets/crop_production.csv' USING PigStorage(',') AS (State_Name:chararray, District_Name:chararray, Crop_Year:int, Season:chararray, Crop:chararray, Area:float, Production:float);

DESCRIBE crop_prod;
```

2.	Calculate the total production of each crop
```sh
total_production = GROUP crop_prod BY Crop;

sum_production = FOREACH total_production GENERATE group AS Crop, SUM(crop_prod.Production) AS Total_Production;

DUMP sum_production;
```

3.	Find the average production per year for each crop
```sh
grouped_by_crop_year = GROUP crop_prod BY (Crop, Crop_Year);

average_production = FOREACH grouped_by_crop_year GENERATE group.Crop AS Crop, group.Crop_Year AS Crop_Year, AVG(crop_prod.Production) AS Avg_Production;

DUMP average_production;
```

4.	List all the crops grown in a specific state (e.g., 'Karantaka')

```sh
specific_state = FILTER crop_prod BY State_Name == 'Karnataka';

unique_crops = GROUP specific_state BY Crop;

DUMP unique_crops;
```

5.	Calculate the total area used for each crop in a specific year (e.g., 2010)
```sh
specific_year = FILTER crop_prod BY Crop_Year == 2010;

total_area = GROUP specific_year BY Crop;

sum_area = FOREACH total_area GENERATE group AS Crop, SUM(specific_year.Area) AS Total_Area;

DUMP sum_area;
```