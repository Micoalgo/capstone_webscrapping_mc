from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup
import plotly 
import requests


#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.exchange-rates.org/history/IDR/USD/T')
soup = BeautifulSoup(url_get.content,"html.parser")

#find your right key here
table = soup.find('table', attrs= {'class':'history-rates-data'})
Date = table.find_all('a', attrs= {'class':'n'})

row_length = len(Date)

temp = [] #initiating a list 

for i in range(0, row_length):

    #get-date
    Date = table.find_all('a', attrs= {'class':'n'})[i].text

    # get Dollar to Indonesian Rupiah
    US_Dollar_to_Indonesian_Rupiah = table.find_all('span', attrs= {'class':'n'})[i].text
    US_Dollar_to_Indonesian_Rupiah = US_Dollar_to_Indonesian_Rupiah.strip()

    temp.append((Date,US_Dollar_to_Indonesian_Rupiah))
    


temp = temp[::-1]

#change into dataframe
df = pd.DataFrame(temp, columns=('Date','US_Dollar_to_Indonesian_Rupiah'))

#insert data wrangling here

df['US_Dollar_to_Indonesian_Rupiah'] = df['US_Dollar_to_Indonesian_Rupiah'].str.replace("$1 = Rp"," ")
df['US_Dollar_to_Indonesian_Rupiah'] = df['US_Dollar_to_Indonesian_Rupiah'].str.replace(",","")
df['US_Dollar_to_Indonesian_Rupiah'] = df['US_Dollar_to_Indonesian_Rupiah'].astype('int64')
df['Date'] = df['Date']. astype('datetime64[ns]')
df = df.set_index('Date')
#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f'{df["US_Dollar_to_Indonesian_Rupiah"].mean().round(2)}' #be careful with the " and ' 

	# generate plot
	ax = df.plot(figsize = (10,6)) 	
    
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]
        
	# generate plot
	ax = df.plot(kind='hist',figsize = (10,6)) 	
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result2 = str(figdata_png)[2:-1]

	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result,plot_result2=plot_result2
          
		)


if __name__ == "__main__": 
    app.run(debug=True)
    
