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
        hours, minutes = map(int, time_str.split(":"))
        return hours * 60 + minutes

    def get_difference(self):
        hours = self.difference // 60
        minutes = self.difference % 60
        return hours, minutes


st.title("⏰ Time Difference Calculator")

start_time = st.text_input("Enter Start Time (HH:MM)", "3:13")
end_time = st.text_input("Enter End Time (HH:MM)", "5:34")

if st.button("Calculate"):
    try:
        calculator = TimeCalculator(start_time, end_time)
        hours, minutes = calculator.get_difference()

        # Styled Output
        st.markdown(
            f'<div class="big-result">'
            f'The time difference between {start_time} and {end_time} '
            f'is {hours} hours and {minutes} minutes.'
            f'</div>',
            unsafe_allow_html=True
        )

    except:
        st.error("Please enter time in correct format like 3:13")