from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<title>AI Study Assistant</title>
<style>
body{font-family:Arial;text-align:center;background:#eee;padding:40px}
.box{background:white;padding:30px;max-width:600px;margin:auto;border-radius:15px}
input,select,button{padding:12px;margin:8px;width:80%}
button{background:black;color:white}
</style>
</head>
<body>
<div class="box">
<h1>AI Study Assistant</h1>

<form method="post">
<input name="topic" placeholder="Enter topic" required><br>

<select name="level">
<option>Beginner</option>
<option>Intermediate</option>
<option>Advanced</option>
</select><br>

<button>Generate</button>
</form>

{% if topic %}
<h2>📚 {{topic}}</h2>
<p><b>Explanation:</b> Learn the basic concepts, examples and applications of {{topic}}.</p>
<p><b>Personalized Plan:</b> Study for 30 minutes and practice 5 questions.</p>

<h3>📝 Quiz</h3>
<p>1. What is {{topic}}?</p>
<p>2. What are its applications?</p>
<p>3. Explain its important concepts.</p>
{% endif %}

</div>
</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():
    topic = request.form.get("topic","")
    return render_template_string(html, topic=topic)

app.run(debug=True)