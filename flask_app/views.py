from flask import render_template
from flask_app import app
from flask import request

@app.route('/')
@app.route('/index')
@app.route('/input')
@app.route('/output')




def usedbooks_input():
    return render_template("input.html")

def usedbooks_output():
    return render_template("output.html")
"""
def cesareans_output():
  #pull 'birth_month' from input field and store it
  patient = request.args.get('birth_month')

  #just select the Cesareans from the birth dtabase for the month that the user inputs
  query = "SELECT index, attendant, birth_month FROM birth_data_table WHERE delivery_method='Cesarean' AND birth_month='%s'" % patient
  print(query)
  query_results=pd.read_sql_query(query,con)
  print(query_results)
  births = []
  for i in range(0,query_results.shape[0]):
      births.append(dict(index=query_results.iloc[i]['index'], attendant=query_results.iloc[i]['attendant'], birth_month=query_results.iloc[i]['birth_month']))
      the_result = ''
   the_result = ModelIt(patient,births)
  return render_template("output.html", births = births, the_result = the_result)
  """
def index():
   user = { 'nickname': 'Misha' } # fake user
   return '''
            <html>
             <head>
               <title>Home Page</title>
             </head>
             <body>
               <h1>Hello, ''' + user['nickname'] + '''</h1>
             </body>
            </html>
          '''
