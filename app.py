import streamlit as st

# Custom CSS for styling
st.markdown("""
<style>
.big-result {
    font-size: 30px;
    font-weight: bold;
    color: #008000;
    background-color: #f0f2f6;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


class TimeCalculator:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

        self.start_minutes = self.convert_to_minutes(start_time)
        self.end_minutes = self.convert_to_minutes(end_time)

        if self.end_minutes < self.start_minutes:
            self.end_minutes += 24 * 60

        self.difference = self.end_minutes - self.start_minutes

    def convert_to_minutes(self, time_str):
        # Example input: "3:15 PM"
        time_part, period = time_str.split()
        hours, minutes = map(int, time_part.split(":"))

        # Convert to 24-hour format
        if period.upper() == "PM" and hours != 12:
            hours += 12
        if period.upper() == "AM" and hours == 12:
            hours = 0

        return hours * 60 + minutes

    def get_difference(self):
        hours = self.difference // 60
        minutes = self.difference % 60
        return hours, minutes


st.title("⏰ Time Difference Calculator (AM/PM)")

start_time = st.text_input("Enter Start Time (HH:MM AM/PM)", "3:13 PM")
end_time = st.text_input("Enter End Time (HH:MM AM/PM)", "5:34 PM")

if st.button("Calculate"):
    try:
        calculator = TimeCalculator(start_time, end_time)
        hours, minutes = calculator.get_difference()

        st.markdown(
            f'<div class="big-result">'
            f'The time difference between {start_time} and {end_time} '
            f'is {hours} hours and {minutes} minutes.'
            f'</div>',
            unsafe_allow_html=True
        )

    except:
        st.error("Please enter time in correct format like 3:13 PM")
