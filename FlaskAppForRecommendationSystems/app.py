from flask import Flask, render_template
from models import model1,model2,model3,model4
from flask import render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/model1', methods=['GET', 'POST'])
def recommend_model1():
    users = [
    "User1",
    "User2",
    "User3",
    "User4",
    "User5",
    # Add more users
    ]
    curuser=1
    if request.method == 'POST':
        selected_user = request.form.get('user')
        if selected_user=="User1":
            curuser=1
        if selected_user=="User2":
            curuser=2
        if selected_user=="User3":
            curuser=3
        if selected_user=="User4":
            curuser=4
        if selected_user=="User5":
            curuser=5
        recommendations = model1.get_recommendations(curuser) 
        return render_template('model1.html', users=users, selected_user=selected_user, recommendations=recommendations)
    else:
        recommendations = model1.get_recommendations(curuser)
        return render_template('model1.html', users=users,selected_user="User1", recommendations=recommendations)

@app.route('/model2', methods=['GET', 'POST'])
def recommend_model2():
    users = [
    "User1",
    "User2",
    # Add more users
    ]
    curuser=0
    if request.method == 'POST':
        selected_user = request.form.get('user')
        if selected_user=="User1":
            curuser=0
        if selected_user=="User2":
            curuser=1
        recommendations = model2.get_recommendations(curuser) 
        return render_template('model2.html', users=users, selected_user=selected_user, recommendations=recommendations)
    else:
        recommendations = model2.get_recommendations(curuser)
        return render_template('model2.html', users=users,selected_user="User1", recommendations=recommendations)
    
@app.route('/model3', methods=['GET', 'POST'])
def recommend_model3():
    users = [
    "Hyderabad",
    "Bangalore",
    "Kashmir"
    # Add more users
    ]
    if request.method == 'POST':
        selected_user = request.form.get('user')
        recommendations = model3.get_recommendations(selected_user) 
        return render_template('model3.html', users=users, selected_user=selected_user, recommendations=recommendations)
    else:
        recommendations = model3.get_recommendations("Hyderabad")
        return render_template('model3.html', users=users,selected_user="Hyderabad", recommendations=recommendations)
    
@app.route('/model4', methods=['GET', 'POST'])
def recommend_model4():
    recommendations=model4.get_recommendations()
    return render_template('model4.html',similar_images=recommendations)
if __name__ == '__main__':
    app.run(debug=True)
