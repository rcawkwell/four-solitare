from flask import Flask, request, render_template 
import foursolitaire 
app = Flask(__name__) 

g = foursolitaire.SetUp()

@app.route('/')
def my_form(): 
    return render_template('home.html')

@app.route('/', methods=['POST'])
def my_form_post(): 
    text = request.form['text']
    processed_text = beg_main(turnLower(text))
    return render_template(processed_text)

def turnLower(info): 
    return info.lower()

@app.route('/game')
def hello_name():
    l_stacks = g.printTop() 
    pile1 = l_stacks[0]
    pile2 = l_stacks[1]
    pile3 = l_stacks[2]
    pile4 = l_stacks[3]
    return render_template('game.html', pile_1=pile1, pile_2=pile2, pile_3=pile3, pile_4=pile4)
@app.route('/discardPile1')
def discardpile1():
    print("This worked")
    return "Nothing"

def beg_main(txt): 
    if txt == "yes": 
        return 'game.html'
    if txt == "learn": 
	return 'learn.html' 

if __name__ == "__main__": 
    app.run(debug = True)
