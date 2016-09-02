from jinja2 import Template

def get_template():
	# Define HTML template
	TEMPLATE = Template("""<html><head><link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

	<!-- jQuery library -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

	<!-- Latest compiled JavaScript -->
	<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script></head>
	<body>

	<div class="container">
	  <h2>{{obj.name}}</h2>
	  <p>{{obj.info}}</h2>
	  <br><br>
	  <table class="table">
	    <thead>
	      <tr>
	        <th>Properties</th>
	      </tr>
	    </thead>
	    <tbody>
	    {% for p in obj.properties%}
	      <tr>
	        {% if p.islink == 'True' %}
	        <td class="col-md-2"><i><a href="{{p.name}}.html">{{p.name}}</a><i></td>
	        {% else %}
	        <td class="col-md-2"><i>{{p.name}}<i></td>
	        {% endif %}
	        <td><br>{{p.info}}</td>
	      </tr>
	    {% endfor %}
	    </tbody>
	  </table>
	</div>
	</body>
	</html>
	""")

	return TEMPLATE