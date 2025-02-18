from  jinja2 import Template
data=["rama", "shyam", "raja","rahim"]
temp=Template("""
    NUmber divisible by two are
    {% for i in range (0,11,2) -%}
        {{i}}
    {% endfor %}
    
    """)
print(temp.render())