import streamlit as st

import pandas as pd 
st.title("🧑‍🤝‍🧑 student dataset with average")
data = {"name": ["iyas","ishan","sinan","Dava","junaid","Faiz","Ali","haneen","mijas","Jafer","john","Lorans"],
        "maths": [10,20,65,40,50,60,70,77,90,89,80,67],
        "science": [45,67,89,90,45,67,80,70,60,50,40,30],
        "english": [57,78,90,45,67,80,70,60,50,40,30,20],
        "art": [55,78,90,45,67,80,70,60,50,40,30,20]}
df = pd.DataFrame(data)
st.write(f"total number of students: {len(data['name'])}")
df["average"] = df[["maths","science","english","art"]].mean(axis=1).round(1)

st.dataframe(df.style.map(
    lambda v:'color:red' if isinstance(v,(int,float)) and v<70 else 'color:green',
    subset=['average']))
st.table(df.sort_values('average',ascending=False).head(5))

class_avg = df["average"].mean().round(1)
highest_avg = df["average"].max()
lowest_avg = df["average"].min()
student_70_plus = (df["average"] >= 70).sum()
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Class Average", class_avg)
with col2:
    st.metric("Highest Average", highest_avg)
with col3:  
    st.metric("Lowest Average", lowest_avg)
with col4:
    st.metric("Students with 70+ Average", student_70_plus)

top3 = (
    df.sort_values(by = "average", ascending=False)
        .head(3)
        .reset_index(drop=True)
    )

top3.insert(0, "Rank", range(1,len(top3)+1))
st.subheader("🏆Top 3 Leaderboard")
st.table(top3[['Rank', 'name', 'average']])
summary = {
    subject: {
        "minimum_score": int(df[subject].min()),
        "maximum_score": int(df[subject].max()),
        "class_mean": round(df[subject].mean(), 1)
    }
    for subject in ['maths', 'science', 'english', 'art']
}

st.json(summary)

from datetime import date

# Divider
st.divider()

# Caption
today = date.today().strftime("%d-%m-%Y")

st.caption(
    f"muhammed faiz | Student Performance Dashboard | {today}"
)