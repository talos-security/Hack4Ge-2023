
from flask import Blueprint, render_template_string, request
from mako.template import Template

ssti_template_2 = Blueprint('ssti-template-2', __name__)


def sayНelloLogin(person):
    # vulnerableHyperText
    template = '<!DOCTYPE html><html><body>\
    <form action="" method="post">\
      First name:<br>\
      <input type="text" name="name" value="">\
      <input type="submit" value="Submit">\
    </form><h2>Hello %s! </h2></body></html>' % person
    return render_template_string(template)

def sayHelloLogin(person):
    # non vulnerable method
    template = '<!DOCTYPE html><html><body>\
    <br>\
    <form action="" method="post">\
      First name:<br>\
      <input type="text" name="name" value="">\
      <input type="submit" value="Submit">\
    </form><h2>Hello ${name} </h2></body></html>'
    return Template(template).render(name = person)




@ssti_template_2.route('/',methods=['GET', 'POST'])
def base():
    person = "user_person"
    if request.method == 'POST':
      if request.form['name']:
        person = request.form['name']
    return sayНelloLogin(person)
   