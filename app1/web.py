import streamlit as st
import functions

st.title("My web app")
st.subheader("Let's generate todo list")
st.write("This app is to improve your productivity")

todos = functions.read_file()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_file(todos)


for todo in todos:
    st.checkbox(todo, key=todo)

st.text_input(
    label='Enter a todo:',
    placeholder='Add a new todo...',
    on_change=add_todo,
    key='new_todo'
)




