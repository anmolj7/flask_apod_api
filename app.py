from flask import Flask, send_file, request, render_template, redirect
import codecs
from GetImage import get_json_data, Image
from flask_weasyprint import HTML, render_pdf

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.route("/download", methods=["POST"])
def download():
    title = request.form["title"]
    explain = request.form["explain"]
    link = request.form["link"]
    date = request.form["date"]
    html = render_template('template.html', title=title, link=link, explain=explain)
    return render_pdf(HTML(string=html), download_filename=f"{date}.pdf")


@app.route("/image", methods=["POST"])
def image():
    date = request.form["date"]
    print(date)
    data = get_json_data(date)
    if not data or "code" in data:
        return redirect('/image_for_date_not_avaiable') #Redirects to error 404.
    img = Image(data)
    return render_template(
        "image.html", link=img.url, title=img.title, explain=img.explanation, date=date
    )


@app.errorhandler(404)
def not_found(e):
    return str(e)


@app.errorhandler(500)
def not_found(e):
    return str(e)+"\nMake sure you've entered the correct date."


if __name__ == "__main__":
    app.run(debug=False, port=6998-212-1)

