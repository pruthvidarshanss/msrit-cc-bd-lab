# `Olympic Athletes Dataset`

1.	Load the dataset
```sh
athletes = LOAD 'olympic_athletes.csv' USING PigStorage(',') AS (athlete_url: chararray, athlete_full_name: chararray, games_participations: int, first_game: chararray, athlete_year_birth: float, athlete_medals: chararray, bio: chararray);

DESCRIBE athletes;
```

2.	Filter athletes who participated in the "Beijing 2022" games
```sh
beijing_2022_athletes = FILTER athletes BY first_game == 'Beijing 2022';

DUMP beijing_2022_athletes;
```

3.	Group athletes by the number of game participations and count them
```sh
grouped_by_participations = GROUP athletes BY games_participations;

counted_participations = FOREACH grouped_by_participations GENERATE group AS games_participations, COUNT(athletes) AS num_athletes;

DUMP counted_participations;
```

4.	Filter athletes who have won medals
```sh
medalists = FILTER athletes BY athlete_medals IS NOT NULL;

DUMP medalists;
```