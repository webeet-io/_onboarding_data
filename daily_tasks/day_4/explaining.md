My logic followed this logic.
1. Check the data with df.head(), df.info(), df.describe(), df.isnull().sum() to get an overview
2. Check for inconsistencies and errors in the critial columns containing the scores
3. Cleaning the inconsistencies and ensuring that only the valid score range is contained!
4. Put together the columns for the database. DBN as a foreign key contained and the relevant columns

Challenges I have encountered
-there were "s" in the columns which had to be cleaned
-there were outliers to be taken care of
-deciding which column to use as a foreign key

This dataset should be ready to be merged with the other datasets!
