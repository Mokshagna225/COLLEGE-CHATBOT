import streamlit as st

st.title("COLLEGE CHATBOT")

question = st.text_input(
    "Ask College Related Questions"
)

fees = {
    "college fee": "College Fee: Contact Administration",
    "examination fee": """
Exam Fee = ₹1500
After Due = +₹100
Again Due = +₹1000
""",
    "exam fee": """
Exam Fee = ₹1500
After Due = +₹100
Again Due = +₹1000
""",
    "condonation fee":
    "Condonation Fee = ₹3500",

    "college timings":
    "College Timings: 9:30 AM – 4:00 PM"
}

timetable = {

"1st year":
["Math","Physics","English","Chemistry","PPS","Graphics"],

"2nd year":
["DBMS","OS","Java","Python","DS","Networks"],

"3rd year":
["ML","WT","SE","CD","Cloud","Project"],

"4th year":
["Project","Internship","AI","Placement","CRT","Seminar"]
}

if st.button("Ask"):

    q = question.lower()

    if q in fees:
        st.success(fees[q])

    elif "time table" in q:

        if "1st" in q:
            year = "1st year"

        elif "2nd" in q:
            year = "2nd year"

        elif "3rd" in q:
            year = "3rd year"

        elif "4th" in q:
            year = "4th year"

        else:
            st.warning(
                "Type: Time Table 1st year"
            )
            st.stop()

        sub = timetable[year]

        st.subheader(
            year.upper()
        )

        st.table({

"Day":[
"Mon",
"Tue",
"Wed",
"Thu",
"Fri",
"Sat"
],

"9-10":[sub[0]]*6,

"10-11":[sub[1]]*6,

"11-12":[sub[2]]*6,

"12-1":[
"LUNCH"
]*6,

"1-2":[sub[3]]*6,

"2-3":[sub[4]]*6,

"3-4":[sub[5]]*6

})

    else:
        st.error(
            "Question not found"
        )