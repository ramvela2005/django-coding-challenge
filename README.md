# Django Coding Challenge

## Setup

Clone this repository using GIT. I recommend you use Github Desktop or VS Code (see point 1 in Development)

To run this project you need to install any recent version of Python. Preferably Python 3.9+ After that you are advised to create a virtual environment so that your dependencies are contained within the workspace. **On Windows, make sure to add Python to your PATH, you may need to logout or reboot to run python** 

Once you have Python installed and working, you can install the project dependencies by running `pip install -r requirements.txt`. This will install everything for you, then you can run migrations with `python manage.py migrate` (make sure to run this command within the nimblestore directory). If successful you should see a new file called `db.sqlite3` in your work directory.

Lastly you should be able to run the server with `python manage.py runserver` which will let you see a very basic webpage in https://127.0.0.1:8000 (Open this link in your browser), this page will help you test your work, I recommend you open the web inspector and switch to the network tab to see what is happening. If you want you can find the source for this page in the `nimblestore/checkout/templates/index.html` file. You do NOT need to edit anything on it.

## Development 

Here are some general guides and also some tips

1. Install VS Code (optional) [here](https://code.visualstudio.com/)
2. Install recommended extensions (Python, SonarLint)
3. Use Google as much as you need to, find official sources and documentations, examples and tutorials are good sources.
3. You CAN use AI, in fact I encourage you to do so.

Once you start creating models, you will need to create and run migrations, the commands you'll need are:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Problem Statement

Your company has a Django application that stores product information. Each product has a name, price, and quantity available. Your task is to create two API endpoints:

1. `GET /api/products/`: This endpoint should return a list of all products, with each product's name, price, and quantity available.

2. `POST /api/order/`: This endpoint should accept a list of products and quantities, calculate the total cost of the order, and return it. If a product doesn't exist or there isn't enough quantity available, it should return an appropriate error message.

You can search globally for `TODO` to find the files you must edit to complete this assignment. 

Good Luck,
Juan Mora

