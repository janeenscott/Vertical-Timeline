
from flask import Flask
from flask import request

app = Flask (__name__)
@app.route("/")
def index():

    display = request.args.get('display');

    index_file = open('index.html', 'r')
    my_html = index_file.read()

    timeline_item_left = 'timeline-item-left'
    timeline_item_right = 'timeline-item-right'

    if display == 'right':
        timeline_item_left = 'timeline-item-right'
        timeline_item_right = 'timeline-item-left'

    my_html = my_html.replace("{{timeline-item-left}}", timeline_item_left)
    my_html = my_html.replace("{{timeline-item-right}}", timeline_item_right)

    index_file.close()

    return my_html
