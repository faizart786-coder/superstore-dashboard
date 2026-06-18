import streamlit as st


st.title('👤 Muhammed faiz k')
st.header('About Me', divider='blue')
st.write('Hi, I m faiz, an aspiring Data Analyst and Web Developer passionate about turning data into meaningful insights and building modern, user-friendly web applications. I have experience working with Python, data analysis, data visualization, and front-end development, and I enjoy solving real-world problems through technology. I am continuously learning new skills and striving to create impactful, data-driven digital solutions.')   
st.header('Skills', divider='green')
st.markdown("""
- **Python** — Pandas, NumPy, Matplotlib, Seaborn
- Data Cleaning & Data Analysis
- Data Visualization & Dashboard Creation
- Power BI Reporting
- Streamlit Dashboard Development
- HTML, CSS & JavaScript
- Responsive Web Development
- Problem Solving & Analytical Thinking"""
)
st.header('Contact', divider='orange')
st.markdown("""
📧 **Email:** mhdfaiz.bca25.dbi@gmail.com  
📱 **Phone:** +91 7012181881  
🔗 **GitHub:** https://github.com/mhdfaizgit
""") 
st.subheader('Favourite Snippet', help='A pattern I use often')
st.code("""
import pandas as pd
df = pd.read_csv("data.csv")
print(df.describe())
""", language="python")

st.latex(r'E = mc^{2}')

st.markdown('---')
st.caption('Built with Streamlit · Day 1 Project · 2026')