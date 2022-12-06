# Flight-Search-Site
A website and backend application that allow users to sign up to receive cheap flight notifications.

The website is a modified version of a template provided by HTML5 Up. The backend of the website uses Flask, with a reverse proxy setup using Gunicorn and Nginx. This is all running on a t.2 micro EC2 instance in us-west-2 region.

Two DynamoDB tables are used in this project. One to store information about Users, and the other with information about destinations and prices that should be monitored.

http://briansflightclub.com/
