import streamlit as st

from utils.gemini_ai import ask_gemini

st.set_page_config(
    page_title="AI Assistant",
    layout="wide"
)

st.title("🤖 ResQAI AI Assistant")

if st.session_state.weather is None:

    st.warning(
        "Please open the Live Weather page first."
    )

    st.stop()

st.success(
    f"Current Location : {st.session_state.city}"
)

question = st.text_area(
    "Ask AI"
)

if st.button("Ask"):

    if question == "":

        st.warning("Enter a question.")

    else:

        with st.spinner("Thinking..."):

            answer = ask_gemini(

                question,

                st.session_state.weather,

                st.session_state.prediction

            )

        st.write(answer)