from flask import (Flask, render_template, request, abort, jsonify, request,
redirect, url_for)
from datetime import datetime
from model import db, save_db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', cards=db)

@app.route("/card/<int:index>")
def card(index):
    try: 
        card = db[index]
        return render_template("card.html", card=card,                          index=index,max_index=len(db)-1,min_index=0)
                                        
    except IndexError:
        abort(404)

@app.route("/api/card/<int:index>")
def api_card_detail(index):
    try:
        return db[index]
    except:
        abort(404)

@app.route("/api/card/")
def api_card():
    return jsonify(db)

@app.route("/addcard", methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        cards = {"question": request.form['question'],
                "answer": request.form['answer']}
        db.append(cards)
        save_db()
        return redirect(url_for('card', index=len(db)-1))
        
    else:
        return render_template("addcard.html")

@app.route("/removecard/<int:index>", methods=["GET", "POST"])
def remove_card(index):
    try:
        if request.method == "POST":
            db.pop(index)
            save_db()
            return redirect(url_for('index'))
            
        else:    
            return render_template('removecard.html',card=db[index])
    except IndexError:
        abort(404)
       

if __name__=="__main__":
    app.run(debug=True)

