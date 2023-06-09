# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 14:34:38 2023

@author: alok
"""
import streamlit as st
import datetime
from PIL import Image
image = Image.open('Resume/mypic.jpeg')

col1,col2= st.columns(2)
nav = st.sidebar.radio("Navigation",['Basic Info','Resume/Portfolio','Contact'])


if nav=="Resume/Portfolio":
    with col1:
        
        ## 1Education
        st.header("Education")
        st.subheader("I.K.G. Punjab Technical University (Main Campus)")
        st.write("Pursuing B.Tech. Computer Engineering")
        st.text("expected June 2024")
        st.subheader("Govt. Model Sr. Secondary School")
        st.write("Class 12 with PCM")
        st.text("June 2020")
        st.subheader("Manav Mangal School")
        st.write("Class 10")
        st.text("June 2018")
     
        ## 2Links
        st.header("Links")
        
        
        if st.button(("github")):
            st.write("https://github.com/aalok0003")      
        
        if st.button(("Linkedin")):
            st.write("https://www.linkedin.com/in/alok-490591106/")
        
    
        if st.button(('HackerRank')):
            st.write('https://www.hackerrank.com/kingofkingsalok')
    
       
        ## 3Course Work
        st.header("Course Work")
        st.write("Machine Learning and AI")
        st.write("Data Structures And Algorithms")
        st.write("Operating Systems")
        st.write("OOPS Concepts")
        st.write("Database Management System basics")
        st.write("Data Analysis and Visualisation")
        st.write("Computer Networks")
        st.write("UI/UX design")

    with col2:
        
        ## 4Skills
        st.header("Skills")
        
        st.subheader("Programming Languages")
        st.write(" C, Python, mySQL, HTML + CSS")
        
        st.subheader("Python Libraries")
        st.write("Numpy, Pandas, Matplotlib,Seaborn, Sklearn")
        
        st.subheader("Frameworks")
        st.write("Streamlit, Django")
        
        st.subheader("Miscellaneous")
        st.write("OpenCV, Tensorflow")
        
        ##5projects
        st.header("Projects")
        
        st.subheader("Insurance Premium Prediction Web APP")
        with st.expander("Click to read description"):
            st.write(" A complete web app using Python Framework-Streamlit. In this I trained the machine learning model with RandomForestRegressor using Sk-Learn library.")
            if st.button("Open Insurance Premium Prediction Web App"):
                st.write("https://aalok0003-insurance-premium-app-insurance1insurance-99a8oz.streamlit.app/") 
        
        st.subheader("Movie Recommendation System")
        with st.expander("Click to read description"):
            st.write("I have used python library difflib to match user input to closest value in case of mis typing. To convert textual data into numerical data TfidfVectorizer is used and for similarity score cosine_similarity is used")
            
            st.write(":red[Currently working to connect it with API to fetch posters of movies.]")
            if st.button(("Open Movie Recommendation Web App")):
                st.write("https://aalok0003-movie-moviemovie-t8v2pj.streamlit.app/") 
        
        st.subheader("Business Analysis Project")
        with st.expander("Click to read description"):
            
            st.write("""E-Commerce company that sells clothing online but also have in-store style and clothing sessions.
        Customers come in to the store, have sessions/meetings with a personel stylist, then they can go home and order
        either on mobile app or website for cloth they want. The company is trying to decide whether to focus on their 
        efforts on mobile app experience or their website. They are providing customer data for me to analyze and conclude.
        I analyzed the given data by making comparisons among various features using plots with Seaborn library,
        then built a linear machine learning linear regression model to make conclusions using its coefficient value""")
        
        
if nav=="Basic Info":
    st.title("Welcome To My Page")
    st.write("My name is Alok, I am 21 years old. I am respectful to all and honest towards my work. Currently I am looking for an internship to test my skills and learn new things.")
    st.image(image, caption="Alok Sharma", width=(360) )
    
    
if nav=="Contact":
    st.title("Contact")
    if st.button(("Email")):
                st.write("kingofkingsalok@gmail.com") 
    if st.button(("Mobile No.")):
                st.write("9501497362")
