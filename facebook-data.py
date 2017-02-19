import facebook
import requests
from sys import argv
import pandas as pr

script, filename = argv

access_token = '<access-token>'
user = 'expedia'
graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts')
post_data = posts['data']

print("Data gathered from FB API")

date = [str(post_data[i]['created_time'].encode('ascii', 'ignore').decode('ascii', 'ignore'))for i in range(0,8)]

message = [str(post_data[i]['message'].encode('ascii', 'ignore').decode('ascii', 'ignore')) for i in range(0,8)]

pr2 = pr.DataFrame({'Date':date,'Message':message})

print("Writing data to file at " + filename )
pr2.to_csv(filename, index= False, sep='\t', mode='a')

print("Program completed successfully!")
print("If you're a mac/linux user please run this command to see output - 'open " + filename + "'")
