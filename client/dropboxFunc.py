import os
import dropbox

app_key = 'kfd5bkpsq7oej8e'
app_secret = 'g0giv0qjvnkgccz'
access_token = 'sl.Bhdt58gLkUD9H0iAcLf3fYTlCD56j3kviHJzbNgyN7U24FOB7ruQlZvBpzmQm56YB7oVtRRJLbJkyihAWWnE0vhLkPSB8ke2imxue_jeWpxG8zVP53aVVWXLxSxNKkgFsWQi0HqmCPE'  # Optional if you already have an access token

dbx = dropbox.Dropbox(access_token) 

def uploadImage(file_path):
    file_name = os.path.basename(file_path)  # Extract the filename from the file path

   
    with open(file_path, 'rb') as file:
        response = dbx.files_upload(file.read(), f'/destination/folder/{file_name}')
        file_metadata = response
        
    shared_link_metadata = dbx.sharing_create_shared_link(f'/destination/folder/{file_name}')

    shared_link_url = shared_link_metadata.url.replace('?dl=0', '?raw=1')

    return shared_link_url
