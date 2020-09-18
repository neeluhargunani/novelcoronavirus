# novelcoronavirus my web link https://pypiproject.herokuapp.com/
This is my first application in python flask and jinja of dynamic dashboard of covid 19 live status updates and IDE is  pycharm
As im an experienced ui developer of 4years work and i had already worked in bootstrap3,4, html-5, css-3 including jquery in my company projects so i had used bootstrap 4 and python flask but not used custom jquery javascript whatever jquery is used it is default from bootstrap 
In This Project of novelcoronavirus analysed api used for tables and charts, mapping and userinputs to get and post data of covid cases globaly 
libraries from pycharm was taken are :- pygal,folium,request,requests,pandas as pd ,defaultdict,render_template 
-------------------------- for-mapping---------
Folium mapping module i had created world map with top 50 confirmed countries and in that data was from api csv format and pandas library used pd read csv to read csv file and created circle to target the confirmed cases in popup zoom starts from 8 , styling in map tile is  Stamen Terrain, location deafult we can take any from api as long, lat i want to give only confirmed cases in popup so lat and long in mapping will be default but combined-key from api data taken as a key for top country names so the format of 4 keys must be followed (note:if we use dropna then only one country cases will be displayed instead of 50) function of circle maker and (x)parameter is passed that (x) will be user will click for the specific country and pop will displayed x will be multiplied with 0 and 1 radius of the style must be for target country and add to m will ne all stuff added in to mapping variable . more we can also refer from folium library of python moudule url
----------------------------for charts-----------------------------
For charts pygal charts i had used api csv format for stacked bar and json file for pie chart , stacked bar is for country cases and pie chart is for india cases live in both custom styling had defined and keywords called in that charts 
--------------------------for user input--------------------
For user input url api of json file was converted from int to string and request module is defined to get request of form input from html deafult country as world on the page that country variable has been called in the covid variable as upper country as a primary key and all rest all keywords must be append from api of json file this json must b formated by giving .json as data url so the output will be when te user will input any country name the output will return back with the live status of global cases
-----------------------for top 50 confirmed cases global table---------------------------
Top 50 countries table api is same of folium mapping as pd read csv to read csv files , In this table first function was efined and parameter and argument was given as n=50, then grouping of country region was merged in confirmed cases bcause  we had to apply only for confirmed in mapping as well as in this top 50 confirmed table and renderd table by making pairs (Note: Grouping is done when Api data is so lengthy and long), cdf variable was taken to disply the table in html jinja, nlargest function is to mention top 50 countries in the table 
----------------------------------for state table of india cases---------------------------
json data api formated then import defaultdict module and pass variable in that list then apply for statement with primary key of the data and pass all the chlid key with variables in that for statement , counter is given for counting and indexing the table then append function with counter variable and item variable after that return and render defaultdict variables in flask render template
----------------------------global table-----
Global table will be also same procedure as statetable of home page but routing will be for other page as app.route('/globaltable') unless this route will not call in homepage second page will not be able to navigate by user 
precaution page route will be in home page though that is static page but to navigate the page routing is necessry

--------jinja in html pages ------
basic html page with bootstrap4 links and custom style links custom style url must be called in static directory and html pages must be in templates directory by giving block content and end block the block content and end block will connect  all other html pages in to one page in home.htmlpag and othe pages  by giving extension  base.html and block content with closing end block will navigate all styles of bootstrap jquery from base html In betwwen open of block content and end of block content we can render all the variables of python 
-----Thankyou For Going Through My project-----
As If my first python project by self study made by Doing R&D and watching videos from online training sites like udemy eduureka, w3school site im not that much good but will be better in second project  ..



