

# # import streamlit as st
# # import pickle

# # st.title("Book Price Prediction 🚀")
# # #Reviews
# # Reviews = st.slider('Select Reviews', 0, 5, 0)
# # st.write("You Selected", Reviews, 'Star')

# # #Edition Name
# # EditionName = st.selectbox(
# #     'How would you like to be contacted?',
# #     ('Email', 'Home phone', 'Mobile phone'))

# # st.write('You selected:', EditionName)

# # #Ratings
# # Ratings = st.slider('Select Ratings', 0, 1000, 0)
# # st.write("You Selected", Ratings, 'Ratings')

# # #Genre
# # Genre = st.selectbox(
# #     'How would you like to be contacted?',
# #     ('Ema5il', 'Hom5e phone', 'Mob5ile phone'))

# # st.write('You selected:', Genre)


# # #BookCategory
# # Bookcategory = st.radio(
# #     "What's your favorite movie genre",
# #     (
# # 'Action & Adventure',                     
# # 'Arts, Film & Photography',                 
# # 'Biographies, Diaries & True Accounts',   
# # 'Comics & Mangas',                    
# # 'Computing, Internet & Digital Media',     
# # 'Crime, Thriller & Mystery',                
# # 'Humour',                                   
# # 'Language, Linguistics & Writing',          
# # 'Politics',                                 
# # 'Romance',                                  
# # 'Sports'))

# # if Bookcategory == 'Action & Adventure':
# #     st.write('You selected Action & Adventure.')
# # elif Bookcategory == 'Arts, Film & Photography':
# #     st.write('You selected Arts, Film & Photography.')
# # elif Bookcategory == 'Biographies, Diaries & True Accounts':
# #     st.write('You selected Biographies, Diaries & True Accounts.')
# # elif Bookcategory == 'Comics & Mangas':
# #     st.write('You selected Comics & Mangas.')
# # elif Bookcategory == 'Computing, Internet & Digital Media':
# #     st.write('You selected Computing, Internet & Digital Media.')
# # elif Bookcategory == 'Crime, Thriller & Mystery':
# #     st.write('You selected Crime, Thriller & Mystery.')
# # elif Bookcategory == 'Humour':
# #     st.write('You selected Humour.')
# # elif Bookcategory == 'Language, Linguistics & Writing':
# #     st.write('You selected Language, Linguistics & Writing.')
# # elif Bookcategory == 'Politics':
# #     st.write('You selected Politics.')
# # elif Bookcategory == 'Romance':
# #     st.write('You selected Romance.')
# # elif Bookcategory == 'Sports':
# #     st.write('You selected Sports.')

# # else:
# #     st.write("You didn't select any items.")

# # with open("pickle_model.pkl", "wb") as file:
# #     pickle.dump(treereg_pred, file)


# # pickling the model
# import pandas as pd
# import numpy as np
# import pickle
# import streamlit as st
# from PIL import Image

# # pickle_out = open("pickle_model.pkl", "wb")
# # pickle.dump(treereg_pred, pickle_out)
# # pickle_out.close()




# # loading in the model to predict on the data
# pickle_in = open('treereg.pkl', 'rb')
# model = pickle.load(pickle_in)

# # with (open('treereg.pkl', "rb")) as openfile:
# #     while True:
# #         try:
# #             pickled_model = pickle.load(openfile)
# #         except EOFError:
# #             break

# def welcome():
# 	return 'welcome all'


# def prediction(Reviews, Ratings, Genre, BookCategory, Edition_Name):

# 	prediction = model.predict(
# 		[[Reviews, Ratings, Genre, BookCategory, Edition_Name]])
# 	print(prediction)
# 	return prediction

# def LABEL_ENCODING(c1):
#     from sklearn import preprocessing
#     label_encoder = preprocessing.LabelEncoder()
#     df[c1]= label_encoder.fit_transform(df[c1])
#     unq = df[c1].unique()
#     return unq
	
# LABEL_ENCODING("Reviews")
# LABEL_ENCODING("Ratings")
# LABEL_ENCODING("Genre")
# LABEL_ENCODING("BookCategory")
# LABEL_ENCODING("Edition Name")

# def main():

# 	st.title("Book Price Prediction")
# 	html_temp = """
# 	<div style ="background-color:gry;padding:13px">
# 	<h1 style ="color:black;text-align:center;">Streamlit Book Price Prediction ML App </h1>
# 	</div>
# 	"""
# 	st.markdown(html_temp, unsafe_allow_html = True)
# 	result =""
# 	Reviews = st.slider('Select Reviews', 0, 5, 0)
# 	st.write("You Selected", Reviews, 'Star')
# 	EditionName = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))
# 	Ratings = st.slider('Select Ratings', 0, 1000, 0)
# 	st.write("You Selected", Ratings, 'Ratings')
# 	Genre = st.selectbox(
# 	'How would you like to be contacted?',
# 	('Ema5il', 'Hom5e phone', 'Mob5ile phone'))
# 	st.write('You selected:', Genre)
# 	Bookcategory = st.radio(
# 	    "What's your favorite movie genre",
# 	    (
# 	'Action & Adventure',                     
# 	'Arts, Film & Photography',                 
# 	'Biographies, Diaries & True Accounts',   
# 	'Comics & Mangas',                    
# 	'Computing, Internet & Digital Media',     
# 	'Crime, Thriller & Mystery',                
# 	'Humour',                                   
# 	'Language, Linguistics & Writing',          
# 	'Politics',                                 
# 	'Romance',                                  
# 	'Sports'))
	
# 	if st.button("Predict"):
# 		result = prediction(Reviews, EditionName, Ratings, Genre, Bookcategory)
# 	st.success('The output is {}'.format(result))
	
# if __name__=='__main__':
# 	main()
