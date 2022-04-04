# Imports necessary libraries
from flask import Flask , render_template, request
import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
 

# Define the app
app = Flask(__name__)

# Get a welcoming message once you start the server.
@app.route('/')
def home():
    return render_template('nabeel.html', Results="", SuggestedText="")
@app.route('/', methods=['POST'])
def homePost():
    text=request.form['text']
    
    # get the matches
    matches = tool.check(text)
    my_mistakes = []
    my_corrections = []
    start_positions = []
    end_positions = []
    
    for rules in matches:
        if len(rules.replacements)>0:
            start_positions.append(rules.offset)
            end_positions.append(rules.errorLength+rules.offset)
            my_mistakes.append(text[rules.offset:rules.errorLength+rules.offset])
            my_corrections.append(rules.replacements[0])
        
    
        
    my_new_text = list(text)
    
    
    for m in range(len(start_positions)):
        for i in range(len(text)):
            my_new_text[start_positions[m]] = my_corrections[m]
            if (i>start_positions[m] and i<end_positions[m]):
                my_new_text[i]=""
        
    my_new_text = "".join(my_new_text)
    print(text)
    correct=tool.correct(text)
    return render_template('nabeel.html', Results=my_new_text, SuggestedText=correct)
if __name__ == '__main__':
    app.run(debug=True)
