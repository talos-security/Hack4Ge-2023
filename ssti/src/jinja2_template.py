from flask import Blueprint, render_template_string, request

jinja2_template = Blueprint('jinja2_template', __name__)

@jinja2_template.route('/',methods=['GET', 'POST'])
def base():
    # vulnerable
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
    

    return render_template_string(template)
