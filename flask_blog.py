from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Steve Hwang',
        'title' : 'blog post 1',
        'content': 'summer',
        'date': '1/1/2020'
    },
        {
        'author': 'Steven Hwang',
        'title' : 'blog post 1',
        'content': 'summer',
        'date': '1/1/2020'
    }
]

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts = posts)
@app.route('/about')
def about():
    return render_template('about.html', title = 'about')

if __name__ == '__main__':
    app.run(debug=True)