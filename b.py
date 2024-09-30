import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
    }

    .terminal-header {
        font-family: 'Courier New', Courier, monospace;
        font-size: 32px;
        font-weight: bold;
        color: pink; 
        background-color: black;
        align-items: center;
        border-radius: 5px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="terminal-header">Vsetko najlepsie Dorka!!!</h1>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Display images side by side using the columns
with col1:
    st.image("d/peach-cat.gif", use_column_width=True)

with col2:
    st.image("d/peach-cat.gif", use_column_width=True)


st.audio("happy-birthday-my-kitty-120918.mp3", format="audio/mpeg", loop=True)