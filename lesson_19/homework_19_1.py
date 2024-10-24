import requests
import os

# initial data
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

# sending API request
response = requests.get(url, params=params)

# check for a successful request
if response.status_code == 200:
    data = response.json()
    photos = data.get('photos', [])

    # if there are photos
    if photos:
        # iterate over each photo
        for index, photo in enumerate(photos, start=1):
            '''"img_src" got from json_request'''
            img_url = photo.get('img_src')
            # download the image
            img_response = requests.get(img_url)
            # check for successful image download
            if img_response.status_code == 200:
                # save the photo with unique name
                file_name = f"mars_photo{index}.jpg"
                with open(file_name, 'wb') as file:
                    file.write(img_response.content)
                print(f"Downloaded photo {file_name}")

            # limit of photo number
            if index == 5:
                break
        else:
            print("No photos found")
    else:
        print(f"Error getting data: {response.status_code}")

