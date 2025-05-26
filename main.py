import streamlit as st
from user import User

st.image("assets/header.png", use_container_width=True)
st.title("🚀 Habit Tracker App")

user = st.text_input("Enter your name:") # If a username already exist, tell the new user to input another name
if user:
    st.session_state["user"] = user

if "user" in st.session_state:
    st.subheader(f"Hello {st.session_state['user']}, Welcome to your Habit Tracker")
    current_user = User(st.session_state["user"])

    habit_name = st.text_input("New Habit:")
    category = st.selectbox("Category:", ["Daily", "Weekly", "Monthly"])

    if st.button("Add Habit") and habit_name:
        try:
            current_user.add_habit(habit_name, category)
            st.success("Habit added successfully!")
        except ValueError as e:
            st.error(str(e))

    if st.button("View Habits"):
        st.session_state["show_habits"] = True
    
    if st.session_state.get("show_habits"):
        habits = current_user.get_habits()
        if habits:
            for habit in habits:
                st.write(f"Name: {habit['name']} | Category: {habit['category']}")

                complete_button = st.button(f"Complete {habit['name']}", key=f"complete_{habit['id']}")
                if complete_button:
                    current_user.complete_habit(habit['id'])
                    st.success(f"Habit '{habit['name']}' marked as completed!")
                    st.rerun()
                
                delete_button = st.button(f"Delete {habit['name']}", key=f"delete_{habit['id']}")
                if delete_button:
                    current_user.delete_habit(habit['id'])
                    st.session_state["deleted_message"] = f"Habit '{habit['name']}' deleted successfully."
                    st.session_state["show_habits"] = False  # Refresh list
                    st.rerun()
                
                frequency = st.selectbox(
                    "Select Frequency:", 
                    ["Daily", "Weekly", "Monthly"], 
                    key=f"freq_{habit['id']}"
                )
                streak_button = st.button(f"Calculate Streak for {habit['name']}", key=f"streak_{habit['id']}")
                if streak_button:
                    streak = current_user.get_streak(habit['id'], frequency)
                    st.info(f"{habit['name']} - {frequency} Streak: {streak}")
        else:
            st.info("No habits found.")

    # Display the delete success message if it exists
    if "deleted_message" in st.session_state:
        st.success(st.session_state["deleted_message"])
        del st.session_state["deleted_message"]
    
    # Exit button to log out
    if st.button("Exit"):
        st.session_state.clear()
        st.rerun()
