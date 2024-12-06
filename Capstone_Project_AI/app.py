from flask import Flask, render_template, url_for, request, redirect
from textToText import textToTextFnc
from textToImage import textToImageFnc
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def text(): 
    if request.method == 'POST':
        prompt = request.form['message']

        response = textToTextFnc(prompt)
        return render_template('text.html', response=response, prompt=prompt)
    
    return render_template('text.html')


@app.route("/images", methods=['GET', 'POST']) 
def images():
    if request.method == 'POST':
        prompt = request.form['message']

        image_path = textToImageFnc(prompt)
        return render_template('images.html', path = image_path, prompt=prompt)
    
    return render_template('images.html')



if __name__ == '__main__':
    app.run(debug = True) 