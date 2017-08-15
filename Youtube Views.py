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

@app.route('/top20comments', methods=["GET"])
def top20Comments():
    top20videofile = open(os.path.join(app.config["UPLOAD_FOLDER"], "top20comments.csv"), 'r')
    top20likedata = csv.DictReader(top20videofile)
    top20videoid = []
    top20videocomment = []
    for data in top20likedata:
        top20videoid.append(data["videoId"])
        top20videocomment.append(int(data["commentCount"]))

    urls = []
    for data in top20videoid:
        url = "http://www.youtube.com/watch?v="+data
        urls.append(url)
    print(urls)
    bar_chart = pygal.Bar()
    bar_chart.title = "Top 20 videos by Comments"
    bar_chart.x_labels = top20videoid
    bar_chart.add('commentCount', top20videocomment)
    bar_graph = bar_chart.render_data_uri()
    return render_template('graphs/top20comments.html', bar_graph=bar_graph, urls=urls, ids=top20videoid)

#https://www.youtube.com/channel/UCpPOf9BQPwa4K11Zjxu1ZPw

@app.route('/top20channels', methods=["GET"])
def top20channels():
    top20channelfile = open(os.path.join(app.config["UPLOAD_FOLDER"], "top20channels.csv"), 'r')
    top20subdata = csv.DictReader(top20channelfile)
    top20channelid = []
    top20channelsubscnt = []
    for data in top20subdata:
        top20channelid.append(data["channelId"])
        top20channelsubscnt.append(int(data["subscriberCount"]))

    urls = []
    for data in top20channelid:
        url = "https://www.youtube.com/channel/"+data
        urls.append(url)
    print(urls)
    bar_chart = pygal.Bar()
    bar_chart.title = "Top 20 Channels by Subscribers"
    bar_chart.x_labels = top20channelid
    bar_chart.add('Subscriber Count', top20channelsubscnt)
    bar_graph = bar_chart.render_data_uri()
    return render_template('graphs/top20subscriber.html', bar_graph=bar_graph, urls=urls, ids=top20channelid)

@app.route('/top20videocount', methods=["GET"])
def top20videocount():
    top20channelfile = open(os.path.join(app.config["UPLOAD_FOLDER"], "top20allvideos.csv"), 'r')
    top20subdata = csv.DictReader(top20channelfile)
    top20channelid = []
    top20channelsubscnt = []
    for data in top20subdata:
        top20channelid.append(data["channelId"])
        top20channelsubscnt.append(int(data["videoCount"]))

    urls = []
    for data in top20channelid:
        url = "https://www.youtube.com/channel/"+data
        urls.append(url)
    print(urls)
    bar_chart = pygal.Bar()
    bar_chart.title = "Top 20 Channels by Video Count"
    bar_chart.x_labels = top20channelid
    bar_chart.add('Video Count', top20channelsubscnt)
    bar_graph = bar_chart.render_data_uri()
    return render_template('graphs/top20allvideos.html', bar_graph=bar_graph, urls=urls, ids=top20channelid)

@app.route('/top20allviews', methods=["GET"])
def top20allviews():
    top20channelfile = open(os.path.join(app.config["UPLOAD_FOLDER"], "top20allviews.csv"), 'r')
    top20subdata = csv.DictReader(top20channelfile)
    top20channelid = []
    top20channelsubscnt = []
    for data in top20subdata:
        top20channelid.append(data["channelId"])
        top20channelsubscnt.append(int(data["viewCount"]))

    urls = []
    for data in top20channelid:
        url = "https://www.youtube.com/channel/"+data
        urls.append(url)
    print(urls)
    bar_chart = pygal.Bar()
    bar_chart.title = "Top 20 Channels by Total View Count"
    bar_chart.x_labels = top20channelid
    bar_chart.add('Total View Count', top20channelsubscnt)
    bar_graph = bar_chart.render_data_uri()
    return render_template('graphs/top20allviews.html', bar_graph=bar_graph, urls=urls, ids=top20channelid)

@app.route('/top20dislikes', methods=["GET"])
def top20dislikes():
    top20channelfile = open(os.path.join(app.config["UPLOAD_FOLDER"], "top20dislikes.csv"), 'r')
    top20subdata = csv.DictReader(top20channelfile)
    top20channelid = []
    top20channelsubscnt = []
    for data in top20subdata:
        top20channelid.append(data["videoId"])
        top20channelsubscnt.append(int(data["dislikeCount"]))

    urls = []
    for data in top20channelid:
        url = "https://www.youtube.com/watch?v="+data
        urls.append(url)
    print(urls)
    bar_chart = pygal.Bar()
    bar_chart.title = "Top 20 Videos by Total Dislike Count"
    bar_chart.x_labels = top20channelid
    bar_chart.add('Total Dislike Count', top20channelsubscnt)
    bar_graph = bar_chart.render_data_uri()
    return render_template('graphs/top20dislikes.html', bar_graph=bar_graph, urls=urls, ids=top20channelid)

@app.route('/top20likesbyviews', methods=["GET"])
def top20likesbyviews():
    top20channelfile = open(os.path.join(app.config["UPLOAD_FOLDER"], "top20likesbyviews.csv"), 'r')
    top20subdata = csv.DictReader(top20channelfile)
    top20channelid = []
    top20channelsubscnt = []
    for data in top20subdata:
        top20channelid.append(data["videoId"])
        top20channelsubscnt.append(float(data["likes/view"]))

    urls = []
    for data in top20channelid:
        url = "http://www.youtube.com/watch?v="+data
        urls.append(url)
    print(urls)
    bar_chart = pygal.Bar()
    bar_chart.title = "Top 20 Videos by Total Likes per View"
    bar_chart.x_labels = top20channelid
    bar_chart.add('Total Likes/View Count', top20channelsubscnt)
    bar_graph = bar_chart.render_data_uri()
    return render_template('graphs/top20likesbyviews.html', bar_graph=bar_graph, urls=urls, ids=top20channelid)

@app.route('/top20dislikesbyviews', methods=["GET"])
def top20dislikesbyviews():
    top20channelfile = open(os.path.join(app.config["UPLOAD_FOLDER"], "top20dislikesbyviews.csv"), 'r')
    top20subdata = csv.DictReader(top20channelfile)
    top20channelid = []
    top20channelsubscnt = []
    for data in top20subdata:
        top20channelid.append(data["videoId"])
        top20channelsubscnt.append(float(data["dislikes/view"]))

    urls = []
    for data in top20channelid:
        url = "http://www.youtube.com/watch?v="+data
        urls.append(url)
    print(urls)
    bar_chart = pygal.Bar()
    bar_chart.title = "Top 20 Videos by Total Dislikes per View"
    bar_chart.x_labels = top20channelid
    bar_chart.add('Total Dislikes/View Count', top20channelsubscnt)
    bar_graph = bar_chart.render_data_uri()
    return render_template('graphs/top20dislikesbyviews.html', bar_graph=bar_graph, urls=urls, ids=top20channelid)

@app.route('/top20viewsbysubscribers', methods=["GET"])
def top20viewsbysubscribers():
    top20channelfile = open(os.path.join(app.config["UPLOAD_FOLDER"], "top20viewsbysubscribers.csv"), 'r')
    top20subdata = csv.DictReader(top20channelfile)
    top20channelid = []
    top20channelsubscnt = []
    for data in top20subdata:
        top20channelid.append(data["videoId"])
        top20channelsubscnt.append(float(data["views/subscribers"]))

    urls = []
    for data in top20channelid:
        url = "http://www.youtube.com/watch?v="+data
        urls.append(url)
    print(urls)
    bar_chart = pygal.Bar()
    bar_chart.title = "Top 20 Videos by Total Views per Subscribers"
    bar_chart.x_labels = top20channelid
    bar_chart.add('Total Views/Subscriber Count', top20channelsubscnt)
    bar_graph = bar_chart.render_data_uri()
    return render_template('graphs/top20viewsbysubscribers.html', bar_graph=bar_graph, urls=urls, ids=top20channelid)

@app.route('/top20likesbydislikes', methods=["GET"])
def top20likesbydislikes():
    top20channelfile = open(os.path.join(app.config["UPLOAD_FOLDER"], "top20likesbydislikes.csv"), 'r')
    top20subdata = csv.DictReader(top20channelfile)
    top20channelid = []
    top20channelsubscnt = []
    for data in top20subdata:
        top20channelid.append(data["videoId"])
        top20channelsubscnt.append(float(data["likes/dislikes"]))

    urls = []
    for data in top20channelid:
        url = "http://www.youtube.com/watch?v="+data
        urls.append(url)
    print(urls)
    bar_chart = pygal.Bar()
    bar_chart.title = "Top 20 Videos by Total Likes per Dislikes"
    bar_chart.x_labels = top20channelid
    bar_chart.add('Total Likes/Total Dislikes', top20channelsubscnt)
    bar_graph = bar_chart.render_data_uri()
    return render_template('graphs/top20likesbydislikes.html', bar_graph=bar_graph, urls=urls, ids=top20channelid)

@app.route('/top20commentsbyviews', methods=["GET"])
def top20commentsbyviews():
    top20channelfile = open(os.path.join(app.config["UPLOAD_FOLDER"], "top20commentsbyviews.csv"), 'r')
    top20subdata = csv.DictReader(top20channelfile)
    top20channelid = []
    top20channelsubscnt = []
    for data in top20subdata:
        top20channelid.append(data["videoId"])
        top20channelsubscnt.append(float(data["comments/views"]))

    urls = []
    for data in top20channelid:
        url = "http://www.youtube.com/watch?v="+data
        urls.append(url)
    print(urls)
    bar_chart = pygal.Bar()
    bar_chart.title = "Top 20 Videos by Comments per View"
    bar_chart.x_labels = top20channelid
    bar_chart.add('Total Comments/Total Views', top20channelsubscnt)
    bar_graph = bar_chart.render_data_uri()
    return render_template('graphs/top20commentsbyviews.html', bar_graph=bar_graph, urls=urls, ids=top20channelid)

@app.route('/scatter_plot', methods=["GET"])
def ScatterPlot():
    channelDataFile = open(os.path.join(app.config["UPLOAD_FOLDER"], "channelStats.csv"), 'r')
    channelData = csv.DictReader(channelDataFile)
    listData = []
    listData1 = []

    for data in channelData:
        if data["viewCount"]!= "-1" and data["subscriberCount"] != "-1" and int(data["viewCount"]) > 10000\
                and int(data["subscriberCount"]) > 1000:
            intermid = [int(data["subscriberCount"])/1000, int(data["viewCount"])/10000]
            intermid=tuple(intermid)
            listData.append(intermid)
        if data["viewCount"] != "-1" and data["videoCount"] != "-1" and int(data["viewCount"]) > 10000 \
                and int(data["videoCount"]) > 10:
            intermid = [int(data["videoCount"])/10, int(data["viewCount"])/10000]
            intermid=tuple(intermid)
            listData1.append(intermid)

    scatter_plot = pygal.XY(stroke=False)
    scatter_plot.title = "Top 20 Subscriber Count vs View Count"
    scatter_plot.add("sub/1000 & viewcnt/10000",listData)
    scatter_plot.add("totvid/10 & viewcnt/10000", listData1)
    scatter_plot_rendered = scatter_plot.render_data_uri()

    print("THIS IS SPARTA!!!!")
    return render_template('graphs/scatter1.html', scatter_plot=scatter_plot_rendered)


#if __name__ == '__main__':
#    app.run(host="localhost", port=5001, debug=True)

