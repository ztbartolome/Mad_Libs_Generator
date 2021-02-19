from flask import Flask, render_template, request
import main
import text_processor
import os
app = Flask(__name__)

global state
state = {'mad_libs':None,
'tags_to_replace':[]}

#home page with menu for mad libs
@app.route('/')
def home():
    text_processor.load_tagger()
    main.make_tag_examples()
    state['mad_libs'] = text_processor.MadLibs()
    return render_template('home.html')

@app.route('/about')
def about():
    global state
    return render_template('about.html', state=state)

#let the user enter word replacements
@app.route('/enterwords', methods=['GET','POST'])
def enter_words():
    global state
    if request.method == 'GET': #sent to this page from passage selection
        passage_type = request.args.get('type')
        if passage_type == 'random':
            passage = main.random_passage()
        else:
            passage = open(os.path.join('passages', files[int(passage_type)]), 'r').read()
    elif request.method == 'POST': #user submitted their own passage
        passage = request.form['passage']
    state['mad_libs'].process_passage(passage)
    state['tags_to_replace'] = [text_processor.tag_names[tag] for (token, tag) in state['mad_libs'].word_replacements.keys()]
    return render_template('enter_words.html', state=state)

#show the mad lib with the word replacements
@app.route('/result', methods=['POST'])
def result():
    global state
    state['mad_libs'].replace(request.form.getlist('replacements[]'))
    return render_template('result.html', state=state)

if __name__ == '__main__':
    app.run()


#methods to redo: main.enter_words, main.input_passage, main_choose_passage
#methods to use as is: main.random_passage, text_processor.load_tagger
