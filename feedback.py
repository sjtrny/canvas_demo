import json
from datetime import datetime

import markdown2
import pdfkit
from jinja2 import Template
from pytz import timezone

# Load example comments
comments_file = open(f"comments_example.md", 'r')
comments_markdown = comments_file.read()
comments_file.close()

# Convert markdown to HTML
comments_html = markdown2.markdown(comments_markdown)

# Load the template
template = Template(open(f"template.html", 'r').read())

criteria_list = json.load(open('criteria.json', 'r'))

critera_map = {
    "Task A: EDA": {
        1: "A1",
        2: "A2",
    },
    "Task B: Benchmark Model": {
        1: "B1",
        2: "B2",
        3: "B3",
    }
}

# This is a placeholder data, you should calculate these for all students
student_results = {
    "A1": 2,
    "A2": 14,
    "Task A: EDA:Total": 16,
    "B1": 4,
    "B2": 6,
    "B3": 3,
    "Task B: Benchmark Model:Total": 13
}

student_info = {
    "student_id": 999999,
    "submitted_at": datetime(2019, 11, 6, 12, 0, 0).replace(tzinfo=timezone("Australia/Sydney")),
    "days_late": 1,
    "total": 29,
    "late_penalty": 5,
    "final_mark": 27.55
}

# Inject everything into the template
feedback_html = template.render({
    "student_info": student_info,
    "criteria_list": criteria_list,
    "critera_map": critera_map,
    "student_results": student_results,
    "feedback": comments_html,
})

# Write to a HTML file
file = open(f"feedback.html", 'w')
file.write(feedback_html)
file.close()

# Write to a PDF file
pdfkit.from_string(feedback_html, f"feedback.pdf")