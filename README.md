# Background

This demo shows how to:
- generate feedback files
- retrieve data from canvas
- submit data to canvas

# Canvas API Documentation

https://canvas.instructure.com/doc/api/

# Generating Feedback Files

I generate feedback files by:
1. generating feedback HTML file
2. converting HTML to PDF

#### Demo

Please see the ``feedback.py`` file.

### HTML Files

HTML files are created by using Jinja2 templates. You can then "render" a template which means injecting values at locations specified in the template.

### PDF conversion

For PDF conversion I use pdfkit which wraps wkhtmltopdf

# Canvas Setup

You need to create an "Approved Integration" (API key) on canvas first.

1. Go to https://canvas.sydney.edu.au/profile/settings
2. Click "New Access Token"
3. Fill out "Purpose"
4. Click "Generate Token"
5. Copy the Token somewhere safe

Canvas will not allow you to view the Token again for an Approved Integration. So make sure you have a copy.

If you lose the token completely, don't worry, you can always create a new one.

#### Course ID

Most often you will be accessing data about a unit/course. In this case you will need to know the `course_id`, which can be found in the URL when accessing the canvas course site.

For example the `course_id` of BUSS6002 is 17524, which you can identify from the following url

	https://canvas.sydney.edu.au/courses/17524

#### Canvas API Docs

https://canvas.instructure.com/doc/api/

# Retrieving Data from Canvas

To interact with the canvas API you must make HTTP GET requests with the following requirements:

1. domain name is ``"https://canvas.sydney.edu.au/"``
2. the query string contains ``"access_token=access_token=<ACCESS-TOKEN>"``

I have written a helper function called ``get_canvas_data`` to assist with this operation.

#### Demo

The demo file ``get.py`` shows how to retrieve enrollments for a course.

Documentation for this endpoint can be found here https://canvas.instructure.com/doc/api/enrollments.html

# Submitting Assignment Feedback to Canvas

Submitting a feedback file is a three step process:
1. notify canvas that you wish to upload a file
2. upload the file
3. link file to the assignment submission

Full details here https://canvas.instructure.com/doc/api/file.file_uploads.html

#### Demo

The demo file ``comment.py`` shows the complete workflow.

### 1.  Notify Canvas

Send a POST request to ``api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{canvas_sid}/comments/files``

with the ``name`` parameter set to the name of the file you are uploading.

### 2.  Upload the File

A successful response to step 1 will contain the URL to upload the file to ( ``upload_url``) and a set of upload parameters ( ``upload_params``). Use these to send a POST request with the file that you are uploading.

### 3. Link file to comment

A successful response to step 2 will contain a file upload id (``id``). This can then be added to a submission by making a PUT request to ``/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id`` with the following paramters:
- ``submission[posted_grade]`` - the grade of the assignment
- ``comment[files_ids]`` - a single or list of file_ids from previous step

Details of this step are available here https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.update







