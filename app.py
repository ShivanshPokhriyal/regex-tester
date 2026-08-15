import streamlit as st
import re

st.set_page_config(page_title="Regex Tester")

st.title("Regex Tester")
st.write("Test regular expressions against text.")

pattern = st.text_input("Regex Pattern",placeholder= r"e.g. ^[0-9]+$")

text = st.text_area("Test Text",placeholder="Enter the text to test")
text= text.strip()
test = st.button("Test Regex",type="primary")

if test:
    match = re.search(pattern,text)

    if match:
        st.success("Match Found")
        st.write("First Matched text:", match.group())
        st.write("Start:",match.start())
        st.write("End:" ,match.end())

        matches = re.findall(pattern,text)
        st.write("All matches:",matches)
        
    else:
        st.error("Match not found")