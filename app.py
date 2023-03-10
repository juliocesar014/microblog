from datetime import datetime
from flask import Flask, render_template, request
from db import db

app = Flask(__name__)

#entries = []

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == 'POST':
        entry_content = request.form.get("content")
        date_time = datetime.today()
        formatted_date = date_time.strftime("%d %b") ## 27 Dec
        #entries.append((entry_content,formatted_date))
        db.entries.insert_one({"content":entry_content, "date":formatted_date})
        #print(entries)
        
    entries_all = [
        (
            entry["content"],
            entry["date"],
        )
        for entry in db.entries.find({})
    ]
    return render_template("index.html", entries=entries_all)
        

        


@app.route("/calendar")
def calendar():
    return 'Calendar'



if __name__ == '__main__':
    app.run(debug=True)