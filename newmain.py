# Imports necessary libraries
from flask import Flask , render_template, request
from gingerit.gingerit import GingerIt


# Define the app
app = Flask(__name__)

# Get a welcoming message once you start the server.
@app.route('/')
def home():
    return render_template('nabeel.html', Results="")
@app.route('/', methods=['POST'])
def homePost():
    text=request.form['text']
    text = 'The smelt of fliwers bring back memories.'
    parser = GingerIt()
    my_new_text=parser.parse(text)

    
    print(text)
    return render_template('nabeel.html', Results=my_new_text)
if __name__ == '__main__':
    app.run(debug=True)
