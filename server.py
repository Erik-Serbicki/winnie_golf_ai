from flask import Flask, render_template
app = Flask(__name__,static_url_path='',static_folder= 'static')

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/winnie")
def winnie2023():
    return "winnie likes blue"


app.run(host='0.0.0.0')


