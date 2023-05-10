from flask import Blueprint, request
from mako.template import Template
import html

mako_template_with_simple_filter = Blueprint('mako_template_with_simple_filter', __name__)

@mako_template_with_simple_filter.route('/',methods=['GET', 'POST'])
def base():
    # vulnerable
    person = ""
    if request.method == 'POST':
      if request.form['name']:
        person = html.escape(request.form['name'])
	
    template = '<!DOCTYPE html><html><body>\
    <form action="" method="post">\
      First name:<br>\
      <input type="text" name="name" value="">\
      <input type="submit" value="Submit">\
    </form><h2>Hello %s! </h2></body></html>' % person
    return Template(template).render(data="world")

