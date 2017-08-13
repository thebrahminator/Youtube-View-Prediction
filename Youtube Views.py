from flask import Flask, render_template, redirect
from datetime import datetime
import pygal
import csv
import os
api_key = "AIzaSyDraPMr8KRfkux5u9DgCjfWh1SA_xJmIl8"
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, "static/csvdataset")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/top20views', methods=["GET"])
def top20views():
    top20videofile = open(os.path.join(app.config["UPLOAD_FOLDER"], "top20views.csv"), 'r')
    top20viewdata = csv.DictReader(top20videofile)
    top20videoid = []
    top20videoview = []
    for data in top20viewdata:
        top20videoid.append(data["videoId"])
        top20videoview.append(int(data["viewCount"]))
        #print(data)
    #print(top20videoid)
    #print(top20videoview)
    urls = []
    for data in top20videoid:
        url = "http://www.youtube.com/watch?v="+data
        urls.append(url)
    print(urls)
    bar_chart = pygal.Bar()
    bar_chart.title = "Top 20 videos by view"
    bar_chart.x_labels = top20videoid
    bar_chart.add('viewCount', top20videoview)
    bar_graph = bar_chart.render_data_uri()
    return render_template('graphs/top20.html', bar_graph=bar_graph, urls=urls, ids=top20videoid)


@app.route('/top20likes', methods=["GET"])
def top20likes():
    top20videofile = open(os.path.join(app.config["UPLOAD_FOLDER"], "top20likes.csv"), 'r')
    top20likedata = csv.DictReader(top20videofile)
    top20videoid = []
    top20videolike = []
    for data in top20likedata:
        top20videoid.append(data["videoId"])
        top20videolike.append(int(data["likeCount"]))

    urls = []
    for data in top20videoid:
        url = "http://www.youtube.com/watch?v="+data
        urls.append(url)
    print(urls)
    bar_chart = pygal.Bar()
    bar_chart.title = "Top 20 videos by Likes"
    bar_chart.x_labels = top20videoid
    bar_chart.add('likeCount', top20videolike)
    bar_graph = bar_chart.render_data_uri()
    return render_template('graphs/top20likes.html', bar_graph=bar_graph, urls=urls, ids=top20videoid)


@app.route('/red', methods=["GET"])
def redir():
    return redirect("www.youtube.com")
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

