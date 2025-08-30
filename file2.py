import json
import urllib.request
url = input('Enter a url')
print("Retrieving", url)
response = urllib.request.urlopen(url)
data = response.read().decode()
info = json.loads(data)

# Initialize the count and sum variables
count = 0
total_sum = 0

# Extract comment counts and compute the sum
for item in info['comments']:
    count += 1
    total_sum += item['count']

# Print the results
print("Count:", count)
print("Sum:", total_sum)

