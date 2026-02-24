# importing flask
from flask import *
# importing pymysql
import pymysql
# importing cursors from pymysql
import pymysql.cursors

# initializing the flask app
app = Flask(__name__)
# importing os for the filepath
import os
app.config['UPLOAD_FOLDER'] = 'static/images'

# defining the route
@app.route("/api/signup", methods = ["POST"])
# define the corresponding web application function
def signup():
    # getting user inputs
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    phone = request.form['phone']
    
    # connecting to the database
    connection =  pymysql.connect(user='root', host= 'localhost', password= '', database= 'truhamsokogarden')
    # defining the cursor for sql queries execution
    cursor = connection.cursor()
    # the sql query to add user in the database
    sql = "insert into users(username, password, email, phone) values (%s, %s, %s, %s)"
    # defining the data to replace the placeholders in sql query
    data = (username, password, email, phone)
    # executing the sql query
    cursor.execute(sql, data)
    # saving the data into the database
    connection.commit()
    # returning a response to the user
    return jsonify ({'Success':'Thank you for signing up'})

# sign in api
# define the route
@app.route("/api/signin", methods = ["POST"])
# defining the function
def signin():
    # get user inputs
    email = request.form['email']
    password =request.form['password']

    # create a connection to the database
    connection = pymysql.connect(user = 'root', host = 'localhost', password = '', database = 'truhamsokogarden')
    # define the cursor, we are using the dictionary cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    # creating the sql query
    sql = "select * from users where email = %s and password = %s"
    # define the data to replace yhe placeholders in thee sql query
    data = (email, password)
    # execute the sql query using the cursor
    cursor.execute(sql, data)
    # we are using if else statement to check how many rows are returned
    count = cursor.rowcount
    # if condition to check if there are zero rows found then return no user found
    if count == 0:
        return jsonify ({"Message":"Login Failed"})
    else:
        # if there is a user in else we tell the cuursor to pick only one row normally the first row 
        user = cursor.fetchone()
        # return a response with the user information
        return jsonify ({"Message":"Login success", "user" : user })
    
# add product
@app.route("/api/add_product", methods = ["POST"])
# defining function
def add_product():
    # get user inputs
    product_name = request.form["product_name"]
    product_description = request.form["product_description"]
    product_cost = request.form["product_cost"]
    # extracting the image data
    photo = request.files["product_photo"]
    # getting the image file name
    filename = photo.filename
    # where to save the photo in the static/images folders
    photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    # save the image
    photo.save(photo_path)

    # create a connection to the database
    connection = pymysql.connect(user = 'root', host = 'localhost', password = '', database = 'truhamsokogarden')
    # define the cursor
    cursor = connection.cursor()
    # creating the sql query
    sql = "insert into product_detail(product_name, product_description, product_cost, product_photo) values (%s, %s, %s, %s)"
    # define the data to replace placeholders in the sql query
    data = (product_name, product_description, product_cost, filename)
    # execute the sql query using the cursor
    cursor.execute(sql, data)
    # saving data into database
    connection.commit()
    # returning the response to the user
    return jsonify ({"Message":"Product details added successfully"})

# get_products_details api
# defining the route
@app.route("/api/get_product_detail")
# defining the function
def get_product():
    # create a connection to the database
    connection = pymysql.connect(user ='root', host = 'localhost', password = '', database = 'truhamsokogarden')
    # defining the cursor to execute the sql query
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    # creating the sql query
    sql = 'select * from product_detail'
    # executing the sql query
    cursor.execute(sql)
    # fetching all the rows returned after sql query execution
    product_detail = cursor.fetchall()
    # closing the database connection
    connection.close()
    # returning a response to the user
    return jsonify (product_detail)




    

# Mpesa Payment Route/Endpoint 
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
    if request.method == 'POST':
        amount = request.form['amount']
        phone = request.form['phone']
        # GENERATING THE ACCESS TOKEN
        # create an account on safaricom daraja
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/api/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return jsonify({"message": "Please Complete Payment in Your Phone and we will deliver in minutes"})


# run the app
app.run(debug = True)