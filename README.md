# Intelligent Python Homework Grader

This project automatically collects Python homework files sent to my email,  
extracts the homework content along with the exercise questions,  
and sends them to a LLM for intelligent grading.  
Finally, it stores the email metadata (sender name, sender email, email subject, date, time)  
along with the assigned grade in a MongoDB database.

---

## Features

- Automatic retrieval of Python homework files from email  
- Extraction of exercise questions and submitted content  
- Intelligent grading using a LLM  
- Storage of email details and grades in MongoDB  

---

## Project Requirements
- jdatetime==5.2.0
- openai==1.97.1
- openpyxl==3.1.5
- pandas==2.3.1
- python-dotenv==1.1.1
- pymongo==4.13.2

---

## The project uses MongoDB to store the following information:

- Sender's name
- Sender's email address
- Email subject
- Date and time of email
- Assigned grade for the homework
- ...

--- 
## Contact
- LinkedIn: abdullahi-sherko
- Instagram: datalogue.ai
- Email: abdullahi.sherko11@gmail.com