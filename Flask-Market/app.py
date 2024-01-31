from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/about/<username>')
def about_page(username):
    return f'Welcome {username}'


if __name__ == '__main__':
    app.run()