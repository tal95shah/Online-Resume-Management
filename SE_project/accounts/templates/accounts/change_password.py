{% extends "base.html" %}
{% load static from staticfiles %}

{% block title %}Change Password | {{ user }} {{ super }}{% endblock %}

{% block body %}
    <div class="grid-100">
        <h1>Change Password</h1>
        <form method="POST" actions="" enctype="multipart/form-data">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" class="button" value="save" />
        </form>
    </div>
{% endblock %}
