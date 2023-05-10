from flask import Blueprint, request
from mako.template import Template

mako_template = Blueprint('mako_template', __name__)

@mako_template.route('/',methods=['GET', 'POST'])
# vulnerable
def base():
    person = ""
    if request.method == 'POST':
      if request.form['name']:
        person = request.form['name']
	
    template = '<!DOCTYPE html><html><body>\
    <form action="" method="post">\
      First name:<br>\
      <input type="text" name="name" value="">\
      <input type="submit" value="Submit">\
    </form><h2>Hello %s! </h2></body></html>' % person
    return Template(template).render(data="world")
