# Patrick Buehler
# 6 November 2016
# Main Flask file to parse anagrams
# Duolingo Product Manager Intern Task

from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from anagram import compare_strings as compare

app = Flask(__name__)

@app.route('/')
def my_form():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
	# get words
	word1 = request.form['text']
	word2 = request.form['text2']

	# remove trailing whitespace
	word1 = word1.strip()
	word2 = word2.strip()

	# ignore cases
	word1_processed = word1.upper()
	word2_processed = word2.upper()

	anagrams = compare(word1_processed, word2_processed)

	# adjust the template to show the result of anagram parsing
	return render_template("index.html",anagrams=anagrams,word1=word1, word2=word2)
	
if __name__ == '__main__':
	app.run()
