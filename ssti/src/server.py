from flask import Flask
from jinja2_template import jinja2_template
from jinja2_template_2 import jinja2_template_2
from non_vulnerable import non_vulnerable
from mako_template import mako_template
from mako_template_with_simple_filter import mako_template_with_simple_filter
from ssti_template_2 import ssti_template_2
from ssti_template import ssti_template


app = Flask(__name__)
app.register_blueprint(jinja2_template, url_prefix='/jinja2')
app.register_blueprint(jinja2_template_2, url_prefix='/jinja2_2')
app.register_blueprint(mako_template, url_prefix='/mako')

app.register_blueprint(mako_template_with_simple_filter, url_prefix='/makoWithSimpleFilter')
app.register_blueprint(ssti_template, url_prefix='/ssti1')
app.register_blueprint(ssti_template_2, url_prefix='/ssti2')
app.register_blueprint(non_vulnerable, url_prefix='/nonVulnerable')



@app.route('/', methods=['GET','POST'])
def index():
	return """
	<!DOCTYPE html><html><body>

<a href="jinja2/">jinja2_template</a><br>
<a href="jinja2_2/">jinja2_template_2</a><br>
<a href="mako/">mako</a><br>
<a href="makoWithSimpleFilter/">makoWithSimpleFilter</a><br>
<a href="ssti1/">ssti-template-multi-method</a><br>
<a href="ssti2/">ssti-2-template-multi-method</a><br>

<a href="nonVulnerable/">nonVulnerable</a><br>


</body></html>
	""" 

if __name__=="__main__":
	  app.run("0.0.0.0",port = 5003, debug=False)