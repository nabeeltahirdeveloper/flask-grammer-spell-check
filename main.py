# Imports necessary libraries
from nis import match
from flask import Flask , render_template, request
import requests
import json



def toolRequest(text):
    payload={
        "text": text,
        'language': 'en-US',
        'level': 'picky'
    }

    res=requests.post('https://api.languagetoolplus.com/v2/check', data=payload)
    print(res.status_code)
    return res.json()


# Define the app
app = Flask(__name__)

# Get a welcoming message once you start the server.
@app.route('/')
def home():
    return render_template('index.html', Results="", SuggestedText="")
@app.route('/', methods=['POST'])
def homePost():
    text=request.form['text']
    
    # get the matches
    matches = toolRequest(text)
    my_mistakes = []
    my_corrections = []
    start_positions = []
    end_positions = []
    matches=matches['matches']
    for rules in matches:
            
            print("rules=====",type(rules))
            if len(rules["replacements"])>0:
                start_positions.append(rules['offset'])
                end_positions.append(rules['length']+rules['offset'])
                my_mistakes.append(text[rules['offset']:rules['length']+rules['offset']])
                my_corrections.append(rules['replacements'][0]['value'])
        
    
        
    my_new_text = list(text)
    
    
    for m in range(len(start_positions)):
        for i in range(len(text)):
            my_new_text[start_positions[m]] = my_corrections[m]
            if (i>start_positions[m] and i<end_positions[m]):
                my_new_text[i]=""
    print(my_new_text)
    my_new_text = "".join(my_new_text)
    return render_template('index.html', Results=my_new_text)
if __name__ == '__main__':
    app.run(debug=True)
