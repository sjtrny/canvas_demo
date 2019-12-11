import requests
import json

def get_canvas_data(domain, path, access_key):

    payload = {
                'per_page': 100,
                'access_token': access_key
                }

    r = requests.get(domain + path, data=payload)

    data_list = r.json()

    while r.links['current']['url'] != r.links['last']['url']:
        r = requests.get(r.links['next']['url'], data=payload)
        data_list += r.json()

    return data_list

# Config for
domain = "https://canvas.sydney.edu.au/"
course_id = COURSE_ID
access_key = "ACCESS_KEY"

# Get data from canvas
enrollments = get_canvas_data(domain, f"/api/v1/courses/{course_id}/enrollments", access_key)

# Save result as JSON
# JSON can be directly parsed into Pandas DataFrames later
output_file = open(f"enrollments.json", 'w')
json.dump(enrollments, output_file)
output_file.close()



