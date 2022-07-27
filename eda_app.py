from re import X
from tkinter import Y
import streamlit as st 
import pandas as pd 

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px 


@st.cache
def load_data(data):
	df = pd.read_csv(data)
	return df


def run_eda_app():
	st.subheader("EDA Section")
	df = load_data("DataSubsetRaw.csv")
	df_clean = load_data("DataSubsetRaw.csv")
	
	# city dataframe
	city_df = pd.DataFrame(df['City'].value_counts()).reset_index().rename(columns={'index':'City', 'City':'Cases'})
	top_10_cities = pd.DataFrame(city_df.head(10))
	total = sum(city_df['Cases'])

	submenu = st.sidebar.selectbox("SubMenu",["Descriptive","Plots"])
	if submenu == "Descriptive":
		
		st.dataframe(df)

		with st.expander("Data Types Summary"):
			st.dataframe(df.dtypes.astype(str))

		with st.expander("Descriptive Summary"):
			st.dataframe(df_clean.describe())

		with st.expander("City Distribution"):
			st.dataframe(df['City'].value_counts())

		with st.expander("Temperature Distribution"):
			st.dataframe(df['Temperature(F)'].value_counts())
	else:
		st.subheader("Plots")

		# Layouts
		col1,col2 = st.columns([2,1])
		with col1:
			with st.expander("Top 10 Cities in US with most no. of \nRoad Accident Cases (2016-2021)"):
				# fig = plt.figure()
				# sns.countplot(df['Gender'])
				# st.pyplot(fig)

				gen_df = df['City'].value_counts().to_frame()
				gen_df = gen_df.reset_index()
				gen_df.columns = ['City','Cases']
				# st.dataframe(gen_df)
				p01 = px.bar(city_df,y=top_10_cities['Cases'],x=top_10_cities['City'])
				st.plotly_chart(p01,use_container_width=True)

			with st.expander("Map of Accidents"):
				p02 = px.scatter_mapbox(df, lat="Start_Lat", lon="Start_Lng", hover_name="City", mapbox_style="open-street-map", color_discrete_sequence=["fuchsia"], zoom=1, height=300) 
				st.plotly_chart(p02,use_container_width=True)





		with col2:
			with st.expander("Gender Distribution"):
				st.dataframe(df['Gender'].value_counts())

			with st.expander("Class Distribution"):
				st.dataframe(df['class'].value_counts())
			

		with st.expander("Frequency Dist Plot of Age"):
			# fig,ax = plt.subplots()
			# ax.bar(freq_df['Age'],freq_df['count'])
			# plt.ylabel('Counts')
			# plt.title('Frequency Count of Age')
			# plt.xticks(rotation=45)
			# st.pyplot(fig)

			p = px.bar(freq_df,x='Age',y='count')
			st.plotly_chart(p)

			p2 = px.line(freq_df,x='Age',y='count')
			st.plotly_chart(p2)

		with st.expander("Outlier Detection Plot"):
			# outlier_df = 
			fig = plt.figure()
			sns.boxplot(df['Age'])
			st.pyplot(fig)

			p3 = px.box(df,x='Age',color='Gender')
			st.plotly_chart(p3)

		with st.expander("Correlation Plot"):
			corr_matrix = df_clean.corr()
			fig = plt.figure(figsize=(20,10))
			sns.heatmap(corr_matrix,annot=True)
			st.pyplot(fig)

			p3 = px.imshow(corr_matrix)
			st.plotly_chart(p3)


	







