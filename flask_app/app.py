from flask import Flask , render_template
app=Flask(__name__)
@app.route('/')
def hello():
    return render_template('landing.html')

@app.route('/contact')
def contact():
    return'This is a contact page'
@app.route('/feedback')
def feedback():
    return'This is a feedback page'
@app.route('/gallary')
def gallary():
    return'This is a gallary page'



if __name__=='__main__':
    app.run(debug=True)#jst refresh to run the code