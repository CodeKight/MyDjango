# how to use 'extends' in templates ?

## step 1: create a base file like 'base.html'

## step 2: write the reusable code inside it 

## step 3: create a block for variable/dynamic contents

{% block title %} {%endblock title %}
{%block body%} {%endblock body%}

## step 4: create a html file like: home or contact and import base file in it
{% extends 'base.html' %}

- all the contents of base file will be inherited in this file

## step 5: pass static/dynamic content in the blocks
{%block title %} 
    Contact 
{% endblock title%}

{% block body %}
    <h1> {{first_line}} </h1>
    <p> {{second_line}} </p>
{%endblock body%}