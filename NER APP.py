import streamlit as st 
import spacy_streamlit
import os
import pandas as pd
from ner import Parser
from pandas import DataFrame
from termcolor import colored

def main():
	st.title("Drug Named Entity Recognition")
	raw_text = st.text_area("Your Text: ","Enter Text Here..")
	p = Parser()
	p.load_models("models/")
	result = p.predict(raw_text)
	df = DataFrame (result,columns=['Tokens', 'Entity Tags'])
	if st.button("Extract"):
		st.write(df)

if __name__ == '__main__':
	main()