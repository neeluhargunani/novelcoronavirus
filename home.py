# for graphs
import pygal
from pygal.style import LightenStyle
from pygal.style import Style
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-03-2020.csv')
def find_top_confirmed(n=50):
    by_country = data.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
    cdf = by_country.nlargest(n, 'Confirmed')[['Confirmed']]
    return cdf

cdf = find_top_confirmed()#.to_html()
pairs=[(country,confirmed) for country,confirmed in zip(cdf.index,cdf['Confirmed'])]
data.head()
import folium
#!pip install folium
m = folium.Map(location = [34.223334, -82.461707],
           tiles = 'Stamen Terrain',
           zoom_start = 8)
folium.Circle(location = [34.223334, -82.461707], radius = 10000, color = 'red', fill = True,
              popup = 'confirmed {}'.format(50)).add_to(m)
def circle_maker(x):
  folium.Circle(location = [x[0], x[1]],
                radius = float(x[2])*10,
                popup = '{}\nConfirmed Cases: {}'.format(x[3], x[2])).add_to(m)


data[['Lat', 'Long_', 'Confirmed', 'Combined_Key']].dropna(subset = ['Lat', 'Long_']).apply(lambda x: circle_maker(x), axis = 1)
html_map = m._repr_html_()

data_frame = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/worldwide-aggregate.csv', dtype={
            "Date": str,
            "Confirmed": float,
            "Recovered": float,
            "Deaths": float,
            "Increase rate": float
      } )

# we will append data in list
a = []
b = []
c = []
d = []
custom_style = Style(
      # background='transparent',
      plot_background='#f5f5f5',
      # foreground='#53E89B',
      # foreground_strong='#53A0E8',
      # foreground_subtle='#630C0D',
      opacity='.6',
      opacity_hover='1',
      transition='400ms ease-in',
      legend_font_size = 22.0,
      value_font_size = 20.0,
      tooltip_font_size = 23.0,
      major_label_font_size = 20.0,
      label_font_size = 20.0,
      value_label_font_size = 22.0)
line_chart =  pygal.StackedBar(height=670,human_readable=True, legend_at_bottom=True, style=custom_style)
line_chart.title = 'Covid Live Status Daily World Cases Time Series '
# adding range of months from 1 to 12
line_chart.x_labels = data_frame['Date']
for index,row in data_frame.iterrows():
      a.append(row["Confirmed"])
      b.append(row["Recovered"])
      c.append(row["Deaths"])
      d.append(row["Increase rate"])

        # adding the
line_chart.add('Confirmed', a)
line_chart.add('Recovered', b)
line_chart.add('Deaths', c)
line_chart.add('Increase rate', d)

line = line_chart.render_data_uri()



from flask import Flask, render_template, request
import requests
from collections import defaultdict
app: Flask = Flask(__name__)
country = 'world'
#this is form page to get data by user input of covid live status



@app.route('/', methods=['GET', 'POST'])
def home():
    data_state = requests.get( "http://covid19-india-adhikansh.herokuapp.com/states" )
    state_dict = data_state.json()
    covid19_state = defaultdict( list )
    if request.method == 'POST':
        global country
        new_country = request.form.get('country')
        country = new_country

    url = "https://coronavirus-19-api.herokuapp.com/countries/{}"

    r = requests.get(url.format(country)).json()

    covid = {
        'country': country.upper(),
        'cases': r['cases'],
        'todayCases': r['todayCases'],
        'deaths': r['deaths'],
        'todayDeaths': r['todayDeaths'],
        'recovered': r['recovered'],
        'critical': r['critical'],
        'active': r['active'],
        'totalTests': r['totalTests'],
    }

  #statetable
    counter = 0
    for items in state_dict['state']:
            name = items['name']
            active = items['active']
            cured = items['cured']
            death = items['death']
            total = items['total']

            counter = counter + 1

            covid19_state[counter].append( name )
            covid19_state[counter].append( active )
            covid19_state[counter].append( cured )
            covid19_state[counter].append( death )
            covid19_state[counter].append( total )
            def piepygal():  #for india live status graph
                custom_style = Style(
                    # background='transparent',
                    plot_background='#f5f5f5',
                    # foreground='#53E89B',
                    # foreground_strong='#53A0E8',
                    # foreground_subtle='#630C0D',
                    opacity='1',
                    opacity_hover='1',
                    transition='400ms ease-in',
                    legend_font_size=25.0,
                    value_font_size=23.0,
                    tooltip_font_size=25.0,
                    major_label_font_size=25.0,
                    label_font_size=25.0,
                    value_label_font_size=25.0)
            pie_chart = pygal.Pie(  height=670, human_readable=True, legend_at_bottom=True,
                                      style=custom_style )
            # naming the title
            data_indi = requests.get( "http://covid19-india-adhikansh.herokuapp.com/summary" )

            ind = data_indi.json()

            pie_chart.add( 'Death', ind['Death'] )
            pie_chart.add( 'Cured/Discharged/Migrated', ind['Cured/Discharged/Migrated'] )
            pie_chart.add( 'Active cases', ind['Active cases'] )
            pie_chart.add( 'Total Cases', ind['Total Cases'] )
            box = pie_chart.render_data_uri()
    return render_template("home.html", data=covid, table = cdf, cmap=html_map,pairs=pairs,graph_data= line,indi_data=covid19_state, chartdata=box)

@app.route('/globaltable' ,methods = ['POST', 'GET'])
def globaltable():
    import json, requests
    from collections import defaultdict
    data = requests.get("https://coronavirus-19-api.herokuapp.com/countries")
    data_dict = data.json()
    covid19 = defaultdict(list)
    counter = 0

    for items in data_dict:
        country = items['country']
        cases = items['cases']
        todayCases = items['todayCases']
        deaths = items['deaths']
        todayDeaths = items['todayDeaths']
        recovered = items['recovered']
        active = items['active']
        critical = items['critical']
        casesPerOneMillion = items['casesPerOneMillion']
        deathsPerOneMillion = items['deathsPerOneMillion']
        totalTests = items['totalTests']
        testsPerOneMillion = items['testsPerOneMillion']

        counter = counter + 1

        covid19[counter].append(country)
        covid19[counter].append(cases)
        covid19[counter].append(todayCases)
        covid19[counter].append(deaths)
        covid19[counter].append(todayDeaths)
        covid19[counter].append(recovered)
        covid19[counter].append(active)
        covid19[counter].append(critical)
        covid19[counter].append(casesPerOneMillion)
        covid19[counter].append(deathsPerOneMillion)
        covid19[counter].append(totalTests)
        covid19[counter].append(testsPerOneMillion)

    return render_template("globaltable.html",  mfp_data=covid19)
@app.route('/precaution')
def precaution():
    return render_template("precaution.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
if __name__ == "__main__":
    app.run(debug=True)
