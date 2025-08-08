## Dataset description and Cleaning
Checked status of  Null values in all column using info function of Pandas.
Make all column names lowercase for consistency
Removed contact_extensions column as not very informative/required for our purposes and also containing > 20 % of null values
Removed duplicated column on reading score.
Converted all "num and score values" to the numeric format as they should be.
Replaced values marked with "s" to the median values. It is not falsification or fake 0=), but proper handling of missing values, as it is well documented 0=).
After proper cleaning  created new file with prefix cleaned and my initials. 

### Database connection, Table Upload and Verification
Installed via pip sqlachemy package for proper file upload
Entered all db cvredentials and using df.to_sql upload file 
Ensured file is uploaded on the right place
Found mistake in file name through querying in Dbeaver and renamed after
