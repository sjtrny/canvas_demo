import requests

domain = "https://canvas.sydney.edu.au/"
course_id = COURSE_ID
access_key = "ACCESS_KEY"
assignment_id = ASSIGNMENT_ID

canvas_sid = 999999
mark = 27.55
filename = "feedback.pdf"

# 1. Initialise the file upload
path_file_prep = f"api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{canvas_sid}/comments/files"

payload_prep = {
    "access_token": access_key,
    "name": filename,
}

response_prep = requests.post(domain + path_file_prep, data=payload_prep)
json_prep = response_prep.json()

# 2. Upload the file
file_dict = {
    "file": open(filename, 'rb'),
}

response_upload = requests.post(json_prep["upload_url"], files=file_dict, data=json_prep["upload_params"])
json_upload = response_upload.json()

# 3. Link file to submission and add grade
path_link = f"api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{canvas_sid}"
payload3 = {
    "access_token": access_key,
    'submission[posted_grade]': mark,
    'comment[file_ids]': json_upload['id']
}

response_submission = requests.put(domain + path_link, data=payload3)