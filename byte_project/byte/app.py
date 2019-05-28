from flask import Flask,request, render_template, url_for
import model

app = Flask(__name__)
model.init_db()

byte_skills = ['python','javascript','machine-learning','deep-learning','nlp','web-technologies','front-end','sql','html','css','jquery',
'bootstrap','mongo-db','git','web-development','data-analytics','data-mining','data-analysis','algorithms','text-mining','consulting','open-source'
'logistic-regression','angular-js','node-js','ajax','mongodb','react-js','open-source','big-data','hadoop','spark']

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == 'POST' and (request.form['action'] == 'fullstack' or request.form['action']=='datascience'):
        role = request.form['action']
        skill_dict = {}
        skill_dict = model.manual_list(role=request.form['action'])
        selected_skills = request.form.getlist('check')
        # if action ==
        # name = request.form['name']
        # email = request.form['email']
        # phone = request.form['phone']
        # fieldnames = ['name', 'email', 'phone']
        # with open('nameList.csv','w') as inFile:
        #     writer = csv.DictWriter(inFIle, fieldnames=fieldnames)
        #     writer.writerow({'name': name, 'email': email, 'phone': phone})
        score = 0
        score = model.get_manual_score(selected_skills, skill_dict)
        return render_template('home.html', skills = skill_dict.keys(), role = role, score = round(score,2), view_more = True, byte_skills = byte_skills)

    else:
        return render_template('home.html', view_more = False)

if __name__ == "__main__":
	app.run(debug=True)
