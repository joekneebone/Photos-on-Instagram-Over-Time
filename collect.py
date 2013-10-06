#!/usr/bin/python
from instagram.client import InstagramAPI # https://github.com/Instagram/python-instagram

# NOTES
	# Replace the access_token with your own, see http://instagram.com/developer/authentication/

access_token = "1969..."
done = False
api = InstagramAPI(access_token = access_token)

response = api.user_recent_media(user_id = 3, count = 20)

while done == False:
	for media in response[0]:
		output = open("output.txt", "a")
		output.write(media.id.replace("_3", "") + "," + str(media.created_time) + "\n")
		output.close()
		
	response = api.user_recent_media(user_id = 3, count = 20, max_id = media.id)
	
	if media.id == "2_3":
		done = True
	