from flask import Flask, render_template
app=Flask(__name__)
INFO=[
  {
    'id':1,
    'name':'Plague Tale: Requiem',
    'release date':'2022',
    'developers':'Asobo Studio',
    'genre':'Action-Adventure', 
    'about':"A Plague Tale: Requiem is the sequel to A Plague Tale: Innocence (2019), and follows siblings Amicia and Hugo de Rune who must look for a cure to Hugo's blood disease in Southern France while fleeing from soldiers of the Inquisition and hordes of rats that are spreading the black plague.",
    'pics':'/static/requiem.jpeg',
  },
  {
    'id':2,
    'name':'Mafia 2',
    'release date':'2010',
    'developers':'2K Czech',
    'genre':'Third-Person Shooter',  
    'about':"Mafia II is a standalone sequel to 2002's Mafia and the second installment in the Mafia series. Set within the fictional city of Empire Bay from 1945 to 1951, the story follows Vito Scaletta, a young Sicilian-American mobster and war veteran, who becomes caught in a power struggle among the city's Mafia crime families while attempting to pay back his father's debts and secure a better lifestyle.",
    'pics':'/static/mafia2.jpg',
  },
  {  
    'id':3,
    'name':'Witcher 3',
    'release date':'2015',
    'developers':'CD Projekt',
    'genre':'Action RPG',
    'about':"The Witcher 3: Wild Hunt is the sequel to the 2011 game The Witcher 2: Assassins of Kings and the third game in The Witcher video game series, played in an open world with a third-person perspective. The games follow the Witcher series of fantasy novels written by Andrzej Sapkowski. The game takes place in a fictional fantasy world based on Slavic mythology. We play as Geralt of Rivia who is on the run from the otherworldly Wild Hunt.",
    'pics':'/static/witcher3.jpg',
  },
  {
    'id':4,
    'name':'Red Dead Redemption 2',
    'release date':'2019',
    'developers':'Rockstar',
    'genre':'Open-World Action-Adventure',
    'about':"Red Dead Redemption 2 is the third entry in the Red Dead series and a prequel to the 2010 game Red Dead Redemption. The story is set in a fictionalized representation of the United States in 1899 and follows the exploits of Arthur Morgan, an outlaw and member of the Van der Linde gang, who must deal with the decline of the Wild West while attempting to survive against government forces, rival gangs, and other adversaries.",
    'pics':'/static/rdr2.jpg',
  },
  {
    'id':5,
    'name':'Days Gone',
    'release date':'2019',
    'developers':'Bend Studio',
    'genre':'Open-World Survival',
    'about':"Days Gone is set in post-apocalyptic Oregon two years after the start of a pandemic that turned a portion of humanity into vicious zombie-like creatures. Former outlaw-turned-drifter Deacon St.John discovers his wife Sarah, having been assumed dead, may still be alive and goes on a quest to find her. ",
    'pics':'/static/gone.jpg',
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html",info=INFO)
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True) 