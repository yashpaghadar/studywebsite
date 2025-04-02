from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
#app.secret_key = 'your_secret_key'

# Sample course data
courses = [
    {"id": 1, "title": "HTML Basics", "description": "Learn the basics of HTML."},
    {"id": 2, "title": "CSS Fundamentals", "description": "Understand CSS styling."},
    {"id": 3, "title": "JavaScript Basic", "description": "Master JavaScript programming."},
    {"id": 4, "title": "Python Programming", "description": "Expert into Python."},
    {"id": 5, "title": "OOP with Java", "description": "Master into Backend."},
    {"id": 6, "title": "Database Management", "description": "Easily Handle Big Dataset."},
    {"id": 7, "title": "C# Beginner to Expert", "description": "Master C# Programming."},
    {"id": 8, "title": "C Expert", "description": "Expert C programming."},
    {"id": 9, "title": "C++ Beginner", "description": "Starting Easily C++ for Beginner."},
    {"id": 10, "title": "Machine Learning", "description": "Expert to train Different Models."},
    {"id": 11, "title": "Deep Learning", "description": "Master Neural Networking."},
    {"id": 12, "title": "Artifficial Intelligent (AI)", "description": "Become Expert in AI."},
    {"id": 13, "title": "React Backend", "description": "Master React programming."},
    {"id": 14, "title": "Fluter", "description": "Expert in Fluter ."},
    {"id": 15, "title": "Digital Marketing", "description": "Master Digital Marketing."}
]

# Example users dictionary (username: password)
users = {"admin": "password123"}

@app.route('/')
def home():
    search_query = request.args.get('search', '')
    filtered_courses = [c for c in courses if search_query.lower() in c["title"].lower()]
    return render_template('index.html', courses=filtered_courses, search_query=search_query)

@app.route('/course/<int:id>')
def course_detail(id):
    course = next((c for c in courses if c["id"] == id), None)
    if course:
        return render_template('course_detail.html', course=course)
    return "Course not found", 404

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        '''
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('thank_you')) '''
        
        search_query = request.args.get('search', '')
        filtered_courses = [c for c in courses if search_query.lower() in c["title"].lower()]
        return render_template('index.html', courses=filtered_courses, search_query=search_query)
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if username in users:
            return "Username already exists!"
        
        users[username] = password  
        return redirect(url_for('signin'))
    
    return render_template('signup.html')

@app.route('/signout')
def signout():
    session.pop('user', None)
    return redirect(url_for('home'))


@app.route("/faculty")
def faculty():
    return render_template("faculty.html")

if __name__ == '__main__':
    app.run(debug=True)
