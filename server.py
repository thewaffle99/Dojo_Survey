from flask import Flask, render_template,request, session, redirect

app = Flask(__name__)
app.secret_key="Jimmy Johns Tacos"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_results', methods=["POST"])
def post_results():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')


@app.route('/results')
def results():
    return render_template('results.html')

if __name__=="__main__":
    app.run(debug=True)