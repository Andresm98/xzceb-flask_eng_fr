from machinetranslation import translator
from flask import Flask, render_template, request
import json
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench",methods = ['GET'])
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish",methods = ['GET'])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
