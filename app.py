
from flask import Flask
from flask import request

app = Flask (__name__)
@app.route("/")
def index():

    index_file = open('index.html', 'r')
    my_html=index_file.read()
    index_file.close()

    return my_html
#
# toggle = request.args.get('right')
#
# if toggle = 'right'






# txt "I like bananas"
#
# x = txt.replace("bananas", "apples")
#
# print(x)


# Use replace principle to
# pull an html class and switch
# it with another html class
# entry-box-b and entry-box-a
# need to switch in html code (at refresh)
# so that css properties will apply
# to opposite boxes
# this will appear to have the boxes
# toggle or switch sides

# Example of a key-value pair library
#    (used in a query string)
# {
#   'action': 'click',
#   'pgtype': 'Homepage'
# }


# my_html "entry-box-b"
#
# new_html = my_html.replace("entry-box-b", "entry-box-a")
#
#
# return new_html


# After returning new_html, run the following:

# if entry-box-b exists










