import webapp2
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape  = True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainHandler(Handler):
    def get(self):
        self.render("input.html", title="calculator")

class AnswerHandler(Handler):
	def post(self):
		num1 = self.request.get("num1")
		opp = self.request.get("opp")
		num2 = self.request.get("num2")
		if opp == "+":
			number = float(num1) + float(num2)
		if opp == "-":
			number = float(num1) - float(num2)
		if opp == "*":
			number = float(num1) * float(num2)
		if opp == "/":
			number = float(num1) / float(num2)
		if opp == "**":
			number = float(num1) ** float(num2)
		self.render("answer.html", ans=number, title="answers")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/answer', AnswerHandler)
], debug=True)
