## Python coding challenge
### Challenge - Q1

1) Write a script code to be executed from a command line using either python, ruby, PowerShell, or Elixir that extracts returns the text of the last 8 posts made on Expedia Facebook Page, and re-writes such data into a text file using JSON. Be creative on writing the post text and respective date, and justify your decision.
#### Solution steps for Q1
- Step 1 : Install Pre-requisites - facebook, requests, pandas packages
  - Please run 'sudo pip install facebook-sdk','sudo pip install requests','sudo pip install pandas' from terminal
- Step 2: Clone or download 'facebook-data.py' file
- Step 3: Open the file to enter FB access-token. Please email [jpulipati@expedia.com] for help
- Step 4: Run the python file from top-level package. Below is the sample command:
  - python facebook-data.py filename, For e.g.: python facebook-data.py /Users/jpulipati/Desktop/python_assignment/text3.xls
  - Preferrably, use excel files for writing output
  - After running the command, please follow the output on console or please follow Step-5
- Step 5: To check the output file from terminal, below is the sample command
  - open filename, For e.g: open /Users/jpulipati/Desktop/python_assignment/text3.xls

#### P.S Notes for Q1: (Assumptions, explanation)
- 1) Only 'public' posts are retrieved from API. Posts that have restricted 'public' view are not retrieved from API.
- 2) 'Be creative on writing' as mentioned in the question is assumed as 'data to be written to an excel file' so that its easy for further analytics.
- 3) Python version 2.7.10

-------------------------------------------------
  
### Challenge - Q2
2) Similarly, write a script code that receives username and password when executed from the command line, authenticates to http://www.Goodreads.com  website, and find, retrieve, and store in a file the top 10 most popular quotes from Mark Twain. Can you also get the top 10 least popular quotes?
#### Solution steps for Q2
- Step 1: Install Pre-requisites - urllib/2, beautifulsoup, mechanize packages
  - Please run 'sudo pip install package_name' from terminal for package installations
- Step 2: Clone or download 'goodreads.py' file
- Step 3: Run the python file from top-level package. Below is the command:
  - python goodreads.py
- Step 4: In console, enter username, password and if login is successful, enter the destination file name
  - After running the command, please follow the output on console or please follow Step-5
- Step 5: To check the output file from terminal, below is the sample command
  - open filename, For e.g: open /Users/jpulipati/Desktop/python_assignment/text3.xls

#### P.S Notes for Q2: (Assumptions, explanation)
 - 1) The program retrieves the data only if login is successful, else the data wont be retrieved
 - 2) Popularity is based on number of 'likes' for each quote. Top popular 10 quotes are retrieved from the first page and though there are lot of quotes with zero 'likes', least popular 10 quotes are the last 10 quotes from pages 67,68.
 - 3) All the corrupt data in the output file is due to non-english characters present in the quote data

----------------------------------------------------------

### Challenge - Q3
3) Optional: Rewrite the code you wrote for question 2 adding further security when receiving or handling password. Explain your approach.
#### Solution steps for Q3 : Yet to be resolved

----------------------------------------------------------

### Challenge - Q4
4) Using python language, write a script that scrape a website, download data from 2 or more files containing relational content, and merge their data into a data-frame using “Pandas library” (http://pandas.pydata.org/getpandas.html). Note: data must come from scraping, not from gathering it through APIs.
#### Solution steps for Q4
- Step 1: Install Pre-requisites - pandas
  - Please run 'sudo pip install package_name' from terminal for package installations
- Step 2: Clone or download 'pandas_ch.py' file
- Step 3: Run the python file from top-level package. Below is the command:
  - python pandas_ch.py
- Step 4: After running the command, please follow the output on console or please follow Step-5

#### P.S Notes for Q4: (Assumptions, explanation)
 - 1) Scraped data from http://www.sql-join.com/ website
 - 2) Customers and Orders tables' data is gathered from the website using Beautiful Soup API
 - 3) Both the tables are joined using customer_id key in Pandas dataframes
