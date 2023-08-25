**PollsAPI: Simple Polling Service for Apps**
PollsAPI is a simple polling service built using Django and Django Rest Framework (DRF). It allows you to create and manage polls, add questions to polls, vote on questions, and retrieve poll results programmatically through a RESTful API. This README will guide you on how to set up and use the PollsAPI.

**Table of Contents**
Features
Getting Started
Prerequisites
Installation
Usage
API Endpoints
Contributing
Features
Create, read, update, and delete polls.
Add, edit, and delete questions within polls.
Vote on questions within polls.
Retrieve poll results, including vote counts for each option.
Getting Started

**Prerequisites**
Before you begin, ensure you have met the following requirements:

Python 3.2 installed
Django and DRF installed (you can install them via pip)
Postman or any API testing tool

**Installation**
Clone the repository:
git clone https://github.com/denny254/PollsAPI-Simple-polling-Service-for-Apps.git
Navigate to the project directory:
cd PollsAPI-Simple-polling-Service-for-Apps

**Create a virtual environment (optional but recommended):**
python -m venv venv
Activate the virtual environment:
On Windows:
venv\Scripts\activate
On macOS and Linux:
source venv/bin/activate
Install the project dependencies:
Apply database migrations:
python manage.py migrate
Start the development server:
python manage.py runserver
Now, your PollsAPI server should be up and running at http://localhost:8000/.

**Usage**
API Endpoints
You can use Postman or any other API testing tool to interact with the PollsAPI. Here are some of the available endpoints:
List all Polls: GET /api/polls/
Create a Poll: POST /api/polls/
Retrieve a Poll: GET /api/polls/{poll_id}/
Update a Poll: PUT /api/polls/{poll_id}/
Delete a Poll: DELETE /api/polls/{poll_id}/
List all Questions for a Poll: GET /api/polls/{poll_id}/questions/
Create a Question for a Poll: POST /api/polls/{poll_id}/questions/
Retrieve a Question: GET /api/questions/{question_id}/
Update a Question: PUT /api/questions/{question_id}/
Delete a Question: DELETE /api/questions/{question_id}/
Vote on a Question: POST /api/questions/{question_id}/vote/
Get Poll Results: GET /api/polls/{poll_id}/results/
Please refer to the API documentation or use the API testing tool to explore these endpoints in detail.

**Contributing**
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
Fork the repository on GitHub.
Clone your fork locally.
Create a new branch for your feature or bug fix.
Make your changes and commit them with clear and concise commit messages.
Push your changes to your fork on GitHub.
Submit a pull request to the original repository, detailing the changes you've made and why they should be included.

##**THANK YOU REGARDS TO DJANGO DOCUMENTATION**
