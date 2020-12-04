# Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from flask import Flask, render_template, redirect
from pymongo import MongoClient
from Mission_to_Mars import scrape_data



# Create Instance of Flask App
app = Flask(__name__)

# Set up mongo connection in line 
mongo = MongoClient("mongodb://localhost:27017/mars_app")


@app.route('/')
def index():
    # Finding one document from our mongoDB and return it
    mars_data = mongo.db.mars_data.find_one()

    # Pass that listing to render template
    return render_template('index.html', mars_data=mars_data)


@app.route('/scrape')
def scrape():
    # Create mars info collection
    mars = mongo.db.mars_data
    mars_data =  scrape_data()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=False)