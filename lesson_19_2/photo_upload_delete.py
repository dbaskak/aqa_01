import requests

# server url
base_url = 'http://127.0.0.1:8080'

# path to the image
image_path = 'uploads/mars_photo2.jpg'

# POST request - image upload
upload_url = f'{base_url}/upload'
files = {'image': open(image_path, 'rb')}

response = requests.post(upload_url, files=files)

if response.status_code == 201:
    data = response.json()
    image_url = data.get('image_url')
    print(f"Image uploaded successfully: {image_url}")
else:
    print(f"Failed to upload image. Status code: {response.status_code}")

# GET request - image link
if image_url:
    image_filename = image_url.split('/')[-1]
    get_image_url = f'{base_url}/image/{image_filename}'

    get_response = requests.get(get_image_url, headers={'Content-Type': 'text'})
    if get_response.status_code == 200:
        image_link = get_response.json().get('image_url')
        print(f"Image link: {image_link}")
    else:
        print(f"Failed to get image link. Status code: {get_response.status_code}")

# DELETE the image
    delete_url = f'{base_url}/delete/{image_filename}'

    delete_response = requests.delete(delete_url)
    if delete_response.status_code == 200:
        print(f"Image {image_filename} deleted successfully")
    else:
        print(f"Failed to delete image. Status code: {delete_response.status_code}")
