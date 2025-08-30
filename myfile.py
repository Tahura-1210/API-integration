import urllib.request
from bs4 import BeautifulSoup

def follow_links(start_url, count, position):
    url = start_url
    print(f"Starting at: {url}")

    for i in range(count):
        # Open the URL and read the HTML
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        # Find all anchor tags
        tags = soup('a')
        
        # Check if the position is valid
        if position - 1 < len(tags):
            # Get the link at the specified position
            url = tags[position - 1].get('href', None)
            print(f"Retrieving: {url}")
        else:
            print("Position is out of range.")
            break

    # Return the last name found
    last_name = tags[position - 1].contents[0] if position - 1 < len(tags) else None
    return last_name

# Input parameters
start_url = input("enter url"  )
count = int(input("Enter count: "))
position = int(input("Enter position: "))

# Get the last name
last_name = follow_links(start_url, count, position)
print(f"The answer to the assignment for this execution is: {last_name}")



    
