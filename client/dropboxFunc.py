import os
import dropbox

app_key = 'kfd5bkpsq7oej8e'
app_secret = 'g0giv0qjvnkgccz'
access_token = 'sl.Bhch2tdh7mLVmdJDpzLADN-1aZ98iblv_13wuX_RWk52Sz37w21V-5SZd_t25RN4TMFmz5O9F6769K4wKK7vPubwrtveasyj9Lcddwwd5Avr4H59l87f-5v39UdDjuD8P33MSD0bsLw'  # Optional if you already have an access token

dbx = dropbox.Dropbox(access_token) 

def uploadImage(file_path):
    file_name = os.path.basename(file_path)  # Extract the filename from the file path

   
    with open(file_path, 'rb') as file:
        response = dbx.files_upload(file.read(), f'/destination/folder/{file_name}')
        file_metadata = response
        
    shared_link_metadata = dbx.sharing_create_shared_link(f'/destination/folder/{file_name}')

    shared_link_url = shared_link_metadata.url.replace('?dl=0', '?raw=1')

    return shared_link_url
