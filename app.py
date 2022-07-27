import streamlit as st 
import streamlit.components.v1 as stc 
from eda_app import run_eda_app


html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">US Accidents EDA app</h1>
		<h4 style="color:white;text-align:center;">US Accidents</h4>
		</div>
		"""

def main():
	# st.title("US_Accidents")
	stc.html(html_temp)

	menu = ["Home","EDA","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		st.write("""
			### US Accidents App
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
			""")
	elif choice == "EDA":
		run_eda_app()
	else:
		st.subheader("About")
		st.text("By Jason, Danielle, Dennis")

if __name__ == '__main__':
	main()