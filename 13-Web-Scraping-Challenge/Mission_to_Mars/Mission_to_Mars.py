#!/usr/bin/env python
# coding: utf-8

# ## Step 1 - Scraping 
# Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
# - Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.

#Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import os
import time 
# from webdriver_manager.chrome import ChromeDriverManager
def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)
def scrape_data ():
    # executable_path = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **executable_path, headless=False)        
    browser=init_browser()
    # # NASA Mars News
    # - Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

    #Nasa News URL 
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(3)
  
    #HTML object
    html = browser.html

    #Parse w/ Beautiful Soup
    soup = bs(html, 'html.parser')

    #Retrieve Latest News Title and Pragraph text 
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    #display
    print(news_title)
    print(news_p)

    # JPL Mars Space Images - Featured Image
    # - Visit the url for JPL Featured Space Image here.
    # - Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
    # - Make sure to find the image url to the full size .jpg image.
    # - Make sure to save a complete url string for this image.

    #Mars Image URL
    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(featured_image_url)
 
    #HTML Object
    html_img = browser.html

    #Parse w/ Beautiful Soup
    soup = bs(html_img, 'html.parser')

    image_url = soup.find('article')['style'].replace('background-image: url(','').replace(');','')[1:-1]

    featured_url = 'https://www.jpl.nasa.gov' + image_url

    featured_url                                                                 

    # # Mars Facts
    # - Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # - Use Pandas to convert the data to a HTML table string.

    #Mars Fact URL
    fact_url = 'https://space-facts.com/mars/'
    browser.visit(fact_url)

    #Pandas read html
    tables = pd.read_html(fact_url)
    tables

    #Creating Dataframe
    df = tables[0]
    df.columns = ['Description', 'Value']
    df

    #Remove index to df
    # df.set_index('Description', inplace=True)
    # df

    #convert to html table
    html_table = df.to_html(index=False)
    html_table

    # Mars Hemispheres
    #  
    # - Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
    # - You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    # - Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
    # - Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

    #Hemisphere images URL
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)  


    #HTML Object
    html_hemispheres = browser.html

    #Parse w/ Beautiful Soup
    soup = bs(html_hemispheres, 'html.parser')

    items = soup.find_all('div', class_='collapsible results')

    items
 

    hemisphere_title = items[0].find_all('h3')
    hemisphere_title

    hemisphere_names = []
    for title in hemisphere_title:
        hemisphere_names.append(title.text)
        
    hemisphere_names


    href_links = items[0].find_all('a')
    href_links

    hemisphere_urls = []

    hemispheres_main_url = 'https://astrogeology.usgs.gov'
    #Loop through items
    for item in href_links: 
        
        if (item.img): 
            item_url = hemispheres_main_url + item['href']
            hemisphere_urls.append(item_url)

    hemisphere_urls
        

    hemisphere_img = []
    #looking through each url
    for url in hemisphere_urls:
    #browser visiting each url
        browser.visit(url)
        html = browser.html
        soup = bs(html, 'html.parser')
        
        img_result = soup.find_all('img', class_='wide-image')
        img_source = img_result[0]['src']
        full_image = hemispheres_main_url + img_source
        hemisphere_img.append({'Title': hemisphere_names, 'Images': full_image })

    hemisphere_img
   
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)
    #HTML Object
    html_hemispheres = browser.html

    #Parse w/ Beautiful Soup
    soup = bs(html_hemispheres, 'html.parser')

    items = soup.find_all('div', class_='item')

    items
  
    hemispheres_url = []

    hemispheres_main_url = 'https://astrogeology.usgs.gov'
    #Loop through items
    for item in items: 
        
        image = item.find('a')['href']  
        title = item.find('div', class_='description').find('a').find('h3').text
        full_url = hemispheres_main_url + image
            
        browser.visit(full_url)
        
        partial_img_html = browser.html
        
        soup = bs(partial_img_html, 'html.parser')
        
        img_url = soup.find('div', class_='downloads').find('ul').find('li').find('a')['href']
        
        hemispheres_url.append({"title" : title, "img_url" : img_url})
        
    hemispheres_url
    dict_scrape = {
        "title": news_title,
        'paragraph': news_p,
        'Mars_image': featured_url,
        'html_tables': html_table,
        'images': hemispheres_url

    }
    return dict_scrape

# In[2]:


# mars_data = scrape_data()


