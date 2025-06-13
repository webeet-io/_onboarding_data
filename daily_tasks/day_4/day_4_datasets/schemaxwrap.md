first i wrote all the code in jupyter to see if it works then i update my visual code 
and connect it with the correct conda per python interpreter command line.

i decided to clean only by sat related values.

everything is well documented with # notes in the py code

in the end i ran that with visual code and somehow it put it hid ther file inside the user 
instead where i ran the file inside the download.
unsure about if float there is always a good decision but i went with that  because the NaN could have had issues otherwise.


 Mostly smooth sailing inside the visual code
but in the end i encountered repeatedly unicode 8 error which took me like an hour or more to find out that  it actually used
a real password i apparently wasn't even aware of which maybe contains ü it claimed which is unlikely bcs i set my keyboard to 
eng int and normally type ue anyways ...

i didn't use import psycopg2 but  sql alchemy
i forgot to add 
Use parameterized queries and commit logic
# example parameterized insert
insert_query = """
    INSERT INTO sat_scores (dbn, num_of_sat_test_takers, sat_critical_reading_avg_score, sat_math_avg_score, sat_writing_avg_score, pct_students_tested)
    VALUES (%s, %s, %s, %s, %s, %s)
"""
not sure if this isn enough but i need to wrap this up for today.

Have a nice weekend! 

   _,-='"-.__               /\_/\
   `-.}       `=._,.-==-._.,  @ @._,
      `-.__   _,-.   )       _,.-'
           `"     G..m-"^m`m'  
 

but i need to finish up now so i  will just leave this in the markdown 
  
i didn't change the table structure
| Column name                      | Data type in DB | Notes                                  |
| -------------------------------- | --------------- | -------------------------------------- |
| `dbn`                            | TEXT / VARCHAR  | Primary key → unique school identifier |
| `num_of_sat_test_takers`         | INTEGER         | Nullable                               |
| `sat_critical_reading_avg_score` | FLOAT           | Nullable                               |
| `sat_math_avg_score`             | FLOAT           | Nullable                               |
| `sat_writing_avg_score`          | FLOAT           | Nullable                               |
| `pct_students_tested`            | FLOAT           | Nullable                               |
