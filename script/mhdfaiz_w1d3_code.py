import streamlit as st

st.set_page_config(page_title="BMI & Health Calculator", page_icon="🏥")

st.title("🏥 BMI, Calorie & Ideal Weight Calculator")
st.markdown("---")

st.header("👤 Personal Details")

name = st.text_input("Enter Your Name")

age = st.number_input(
    "Age",
    min_value=10,
    max_value=100,
    value=25
)

gender = st.radio(
    "Gender",
    ["Male", "Female"],
    horizontal=True
)

weight = st.slider(
    "Weight (kg)",
    min_value=30.0,
    max_value=150.0,
    value=70.0,
    step=0.5
)

height = st.slider(
    "Height (cm)",
    min_value=100,
    max_value=220,
    value=170,
    step=1
)

st.write(f"""
**Name:** {name}

**Age:** {age}

**Gender:** {gender}

**Weight:** {weight} kg

**Height:** {height} cm
""")

st.header("📊 BMI Calculator")

height_m = height / 100

bmi = round(weight / (height_m ** 2), 1)

if bmi < 18.5:
    category = "Underweight"
    risk = "Moderate"
    color = "warning"

elif bmi < 25:
    category = "Normal weight"
    risk = "Low"
    color = "success"

elif bmi < 30:
    category = "Overweight"
    risk = "Elevated"
    color = "warning"

else:
    category = "Obese"
    risk = "High"
    color = "error"

st.metric("BMI", bmi)

if color == "success":
    st.success(f"Category: {category} | Health Risk: {risk}")
elif color == "warning":
    st.warning(f"Category: {category} | Health Risk: {risk}")
else:
    st.error(f"Category: {category} | Health Risk: {risk}")

# ----------------------------------
# DAILY CALORIE NEED
# ----------------------------------
st.header("🔥 Daily Calorie Need")

activity_levels = {
    "Sedentary (desk job)": 1.2,
    "Lightly active (1–3 days/wk)": 1.375,
    "Moderately active (3–5 days)": 1.55,
    "Very active (6–7 days)": 1.725
}

activity = st.selectbox(
    "Select Activity Level",
    list(activity_levels.keys())
)

multiplier = activity_levels[activity]

# Mifflin-St Jeor Formula
if gender == "Male":
    bmr = (
        10 * weight
        + 6.25 * height
        - 5 * age
        + 5
    )
else:
    bmr = (
        10 * weight
        + 6.25 * height
        - 5 * age
        - 161
    )

daily_calories = round(bmr * multiplier)

st.metric(
    "Daily Calories Needed",
    f"{daily_calories} kcal/day"
)

# ----------------------------------
# IDEAL WEIGHT RANGE
# ----------------------------------
st.header("⚖️ Ideal Weight Range")

height_inches = height / 2.54

if gender == "Male":
    ideal_weight = (
        52
        + 1.9 * (height_inches - 60)
    )
else:
    ideal_weight = (
        49
        + 1.7 * (height_inches - 60)
    )

low_weight = round(ideal_weight * 0.9, 1)
high_weight = round(ideal_weight * 1.1, 1)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Low Ideal Weight",
        f"{low_weight} kg"
    )

with col2:
    st.metric(
        "High Ideal Weight",
        f"{high_weight} kg"
    )

    st.header("📋 Activity Comparison (Bonus)")

selected_levels = st.multiselect(
    "Select activity levels to compare",
    list(activity_levels.keys())
)

if selected_levels:

    comparison_data = []

    for level in selected_levels:
        calories = round(
            bmr * activity_levels[level]
        )

        comparison_data.append(
            {
                "Activity Level": level,
                "Multiplier": activity_levels[level],
                "Calories Needed": calories
            }
        )

    comparison_df = pd.DataFrame(comparison_data)

    st.dataframe(
        comparison_df,
        use_container_width=True
    )
    
st.header("📋 Summary")

if st.button("Show My Summary"):

    st.info(f"""
### Health Summary for {name}

✅ BMI: {bmi}

✅ Classification: {category}

✅ Health Risk: {risk}

✅ Daily Calorie Need: {daily_calories} kcal/day

✅ Ideal Weight Range:
{low_weight} kg - {high_weight} kg

✅ Activity Level:
{activity}
""")
 