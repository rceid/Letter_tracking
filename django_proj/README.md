# Initial data upload
To upload letters from the excel tracking sheet contained in the data directory, run the following command from the current directory:

##### $ python3 manage.py shell < upload_letters.py

To flush databse, run the following command:
##### $ python3 manage.py flush

To rebuild database, run:
##### $ python3 manage.py createsuperuser


{%extends "letter_tracking/base.html" %}
{% block content %}
    <h1 class="mb-3">Search for Letters by Legislator</h1>
    <form action="{% url 'search_results' %}" method="get">
        {% csrf_token %}
        {{ form }}
        <input name="q" type="text" placeholder="Search...">
    </form>
{% endblock content %}

{%extends "letter_tracking/base.html" %}
{% block content %}
    <h1 class="mb-3">Search for Letters by Legislator</h1>
    <form action="{% url 'search_results' %}" method="get">
        {% csrf_token %}
        {{ form }}
        <input name="q" type="submit" value="Submit">
    </form>
{% endblock content %}

