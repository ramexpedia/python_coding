# Python coding challenge
### Q1

Write a script code to be executed from a command line using either python, ruby, PowerShell, or Elixir that extracts returns the text of the last 8 posts made on Expedia Facebook Page, and re-writes such data into a text file using JSON. Be creative on writing the post text and respective date, and justify your decision.
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

#### P.S Notes for Q1: 
- 1) Only 'public' posts are retrieved from API. Posts that have restricted 'public' view are not retrieved from API.
- 2) 'Be creative on writing' as mentioned in the question is assumed as 'data to be written to an excel file' so that its easy for further analytics.
  
### Q2
