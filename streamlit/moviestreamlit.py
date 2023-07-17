import streamlit as st
from streamlit import components




def tableau_page():
    st.title("Visual Data Insights of the Movie Industry")
    
    tableau_code = """
   <div class='tableauPlaceholder' id='viz1689605985219' style='position: relative'><noscript><a href='#'><img alt='Story 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Mo&#47;Moviedashboard_16896025782000&#47;Story1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Moviedashboard_16896025782000&#47;Story1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Mo&#47;Moviedashboard_16896025782000&#47;Story1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1689605985219');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1016px';vizElement.style.height='991px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """

    components.v1.html(tableau_code, height=0)

def main_page():
    st.header("Economic Analysis of the Movie Industry")
    st.write("In this page you will find an a ")

pages = {
    "Main Page": main_page,
    "Movie Data": tableau_page
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("", list(pages.keys()), index=0)

    # Display the selected page
    pages[selection]()

if __name__ == "__main__":
    main()

