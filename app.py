import streamlit as st
import requests

# Create the title for the page
st.title("My Personal AI Assistant")

# Add subheader
st.subheader("What can your personal assistant do?")

# Create a list of what your assistant can do
st.markdown("""
1. Answer questions on various topics.
2. Arrange Calendar events and meetings.
3. Read your emails and send replies, can even summarize them for you.
4. Manage your tasks and to-do lists.
5. Take quick notes for you.
6. Track your expenses and budgeting.
""")

# Add chat subheader
st.subheader("💬 Chat with your assistant")

# Create message history if it does not exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous/saved messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create chat input box
user_message = st.chat_input()

# Run this when the user sends a message
if user_message:

    # Display the new user message
    with st.chat_message("user"):
        st.markdown(user_message)

    # Save the user message
    st.session_state.messages.append(
        {"role": "user", "content": user_message}
    )

    # Send the message to n8n
    response = requests.post(
         "http://localhost:5678/webhook/d0a4028b-a1ad-445a-84a9-0d4d32d6b2b1",
        json={
            "message": user_message,
            "sessionId": "test-user-1"
        }
    )

    # Get the AI response from n8n
    ai_response = response.json()["output"]
  


    # Display the AI response
    with st.chat_message("assistant"):
        st.markdown(ai_response)

    # Save the AI response
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response}
    )