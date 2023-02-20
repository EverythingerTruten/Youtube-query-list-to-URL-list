import os
import googleapiclient.discovery

#Define the lines variable
lines = []

# Set up the YouTube API client
api_key = "[YOUR API KEY HERE]" #Replace the text in between the quoatation signs with your API key, refer to Readme.md for instructions how to find one
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

# Set the file path to the text file
file_path = "[PATH TO THE TXT FILE WITH THE SEARCH QUERY LIST]" #Replace the "\" character with"\\"

# Check if the file exists
if os.path.isfile(file_path):
    print(f"File '{file_path}' exists.")
else:
    print(f"File '{file_path}' does not exist.")
    exit()

# Open the text file for reading
with open(file_path, 'r') as file:
    # Read each line of the file
    for line in file:
        # Print the current line being processed
        print(f"Processing line: {line.strip()}")

        # Perform a search query on the line using the YouTube API
        search_response = youtube.search().list(q=line, part='id,snippet', type='video').execute()
        print("Search query executed.")

        # Get the URL of the first video that matches the query
        video_id = search_response['items'][0]['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'

        # Replace the line in the file with the video URL
        print(f"Replacing line with video URL: {video_url}")
        lines.append(video_url)

# Open the text file for writing
with open(file_path, 'w') as file:
    # Write the modified lines to the file
    for line in lines:
        file.write(line + '\n')
    print(f"All lines in {file_path} have been replaced with YouTube links.")