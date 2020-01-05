from flask import Flask, send_file, request, render_template, redirect
import codecs
from  GetImage import get_json_data, Image
import io 
import img2pdf
import requests
from flask_weasyprint import HTML, render_pdf

app = Flask(__name__)

def convert2pdf(img_bin):
    return img2pdf.convert(img_bin)
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    title = request.form['title']
    explain = request.form['explain']
    link = request.form['link']
    date = request.form['date']
    html = f"<html>{title} <img src=\"{link}\"> {explain}</html>"
    print(html)
    return render_pdf(HTML(string=html), download_filename=f"{date}.pdf")


@app.route('/image', methods=['POST'])
def image():
    date = request.form['date']
    print(date)
    data = get_json_data(date)
    img = Image(data)
    return render_template('image.html', link=img.url, title=img.title, explain=img.explanation, date=date)


@app.errorhandler(404)
def not_found(e):
    return str(e)

@app.errorhandler(500)
def not_found(e):
    return str(e)

if __name__ == "__main__":
    app.run(debug=True, port=6969   )