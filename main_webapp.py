from flask import Flask, render_template, redirect, request
from random import choice as rand
import main
import text_processor
import os
app = Flask(__name__)

global state
state = {'mad_libs':None,
'tags_to_replace':[],
'passage_dir':os.path.join(os.path.dirname(os.path.abspath(__file__)), 'passages'),
'files':None}

#home page with menu for mad libs
@app.route('/')
def home():
    global state
    state['files'] = list(os.listdir(state['passage_dir']))
    text_processor.load_tagger()
    main.make_tag_examples()
    state['mad_libs'] = text_processor.MadLibs()
    return render_template('home.html', state=state)

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
            passage = open(os.path.join(state['passage_dir'], rand(state['files'])), 'r').read()
        else:   #the 'type' corresponds to index of file to be read
            passage = open(os.path.join(state['passage_dir'], state['files'][int(passage_type)]), 'r').read()
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
