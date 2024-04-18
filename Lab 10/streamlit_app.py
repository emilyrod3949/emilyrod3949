import sqlite3
import streamlit as st
import streamlit.components.v1 as components
from jinja2 import Template


conn = sqlite3.connect('poems.db')

a = st.sidebar.radio("Choose:", [1,2])

def main():
    # Your dynamic data
    app_title = "My Streamlit App"
    items = ["Item 1", "Item 2", "Item 3","Item4","Item 5"]
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM poems")
    items = cursor.fetchall()
    # Load the Jinja2 template
    with open("template/template.html", "r") as template_file:
        template_content = template_file.read()
        jinja_template = Template(template_content)

    # Render the template with dynamic data
    rendered_html = jinja_template.render(title=app_title, items=items)

    # Display the HTML in Streamlit app
    components.html(rendered_html, height=200, scrolling=True)

if __name__ == '__main__':
    main()