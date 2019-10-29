# My Developer Life


## Description
A personal blog. You can visit the live site on `https://my-developer-life.herokuapp.com/`


## Author


* [**Brian Major**](https://github.com/bryomajor)

## Features


As a user of the web application you will be able to:

1. See all submitted blogs
2. See random quotes
3. Subscribe to the blog
4. Create an account
5. Log in
6. Post a blog
7. Comment on a pitch
8. See comments posted on each individual blog
9. Edit your profile i.e will be able to add a short bio about yourself and a profile picture

## Specifications
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| View blog posts  | Click on comment | Taken to the clicked post | 
Click on `Comment` | Pop up where one can comment appears | Comments are displayed |
|  Click on `Sign In` | Sign in if one has an account | Sign in form displayed |
|  Click on `Sign In` | Sign up if one has no account | Sign up form displayed |
| Click on profile | Redirects to the profile page | User adds bio and profile picture |



## Getting started
### Prerequisites
* python3.6
* virtual environment
* pip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/bryomajor/my-developer-life.git
        $ cd my-developer-life

## Running the Application
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.6 pip install -r requirements.txt`
* Create a `start.sh` file in the root of the folder and add the following code:

        export MAIL_USERNAME=<your-email-address>
        export MAIL_PASSWORD=<your-email-password>
        export SECRET_KEY=<your-secret-key>

* Edit the configuration instance in `manage.py` from `development` to `production`
* To run the application, in your terminal:

        $ chmod a+x start.sh
        $ ./start.sh
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 manage.py server
        
## Technologies Used
* Python3.6
* Flask
* HTML
* Bootstrap

This application is developed using [Python3.6](https://www.python.org/doc/), [Flask](http://flask.palletsprojects.com/en/1.1.x/), [HTML](https://getbootstrap.com/) and [Bootstrap](https://getbootstrap.com/)


## Support and Team
Brian Major


[Slack Me!](https://slack.com/intl/en-ke/)  @bryomajor


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)
