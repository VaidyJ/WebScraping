from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars_app")


# Create connection variable
#conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
#client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
#db = client.mars_app


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.mars_data.find_one()

    # Return template and data
    return render_template("index.html", vacation=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function and save the results to a variable
    # @TODO: YOUR CODE HERE!

    results = scrape_mars.scrape()
    #results = {'height':20}

    print(results)

    # Update the Mongo database using update and upsert=True
    # @TODO: YOUR CODE HERE!

    """ mongo.db.mars_data.insert_one(
    {
        'name': 'Ahmed',
        'row': 3,
        'favorite_python_library': 'Matplotlib',
        'hobbies': ['Running', 'Stargazing', 'Reading']
    }
    ) """

    #mongo.db.mars_data.insert_one( results)    

    mongo.db.mars_data.update({}, results, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
