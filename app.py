from flask import Flask, render_template
app=Flask(__name__)
INFO=[
  {
    'id':1,
    'name':'Plague Tale: Requiem',
    'release date':'2022',
    'developers':'Asobo Studio',
    'genre':'Action-Adventure', 
  },
  {
    'id':2,
    'name':'Mafia 2',
    'release date':'2010',
    'developers':'2K Czech',
    'genre':'Third-Person Shooter',  
  },
  {  
  'id':3,
  'name':'Witcher 3',
  'release date':'2015',
  'developers':'CD Projekt',
  'genre':'Action RPG', 
  },
  {
  'id':4,
  'name':'Red Dead Redemption 2',
  'release date':'2019',
  'developers':'Rockstar',
  'genre':'Open-World Action-Adventure',
  },
  {
  'id':5,
  'name':'Days Gone',
  'release date':'2019',
  'developers':'Bend Studio',
  'genre':'Open-World Survival',
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html",info=INFO)
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True) 