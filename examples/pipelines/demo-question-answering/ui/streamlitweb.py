import os
import streamlit as st
import time
import re
from dotenv import load_dotenv
import requests

# Set up paths
base_dir = os.path.dirname(os.path.abspath(__file__))
submissions_path = os.path.join(base_dir, '..', 'data', 'submission_data.jsonl')
problems_path = os.path.join(base_dir, '..', 'data', 'problems_data.jsonl')

def question_page():
    # Load environment variables
    load_dotenv()
    api_host = os.environ.get("HOST", "0.0.0.0")
    api_port = int(os.environ.get("PORT", 8000))


    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
    background-image: url("https://i.pinimg.com/originals/fc/5d/10/fc5d101a8bab8d7a95bba6a786fc0eeb.jpg");
    background-size: cover;
    background-position: centre;
    background-repeat: no-repeat;
    background-attachment: fixed;
    }
    </style>
    """


    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Streamlit UI elements
    circular_logo_html = f"""
        <div style="text-align: center;">
            <img src="https://i.pinimg.com/originals/fc/3b/a7/fc3ba705dd2d98af62d708c1216fb12f.jpg" alt="Logo" style="border-radius: 50%; width: 150px; height: 150px; object-fit: cover; display: inline-block;">
            <br>
        </div>
    """
    st.markdown(circular_logo_html, unsafe_allow_html=True)
    st.title("SortMyCodeForces")

    # Specify the type of question about Codeforces problems
    question = st.text_input(
        "Sort Codeforces questions (e.g., 'name question rating above 1600')",
        placeholder="What type of sort do you want?",
    )

    # Handle API request if a question is provided
    if question:
        if not os.path.exists(submissions_path) and not os.path.exists(problems_path):
            st.error("Failed to process file. Please check the Codeforces data.")
        else:
            url = f'http://{api_host}:{api_port}/v1/pw_ai_answer'  # Endpoint of your RAG server
            data = {
                "prompt": question,  # Ensure you are using the right key based on your RAG API
            }

            try:
                response = requests.post(url, json=data)  # Sending the query to the RAG system
                
                if response.status_code == 200:
                    #st.write("### Raw Response Text:")
                    raw_string = response.text
                    #st.write(raw_string)  # Display raw response for debugging
                    empty_string=raw_string.split('\\n')
                    #st.write(empty_string)
                    formatted_output = "\n".join(empty_string)
                    for sta in empty_string:
                        st.write(sta)
                    #st.write(formatted_output)
                    # Attempt to parse the raw response
                    # Attempt to parse the raw response
                    
                else:
                    st.error(f"Failed to get data from RAG API. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error occurred while trying to connect to the RAG API: {str(e)}")

# Run the central page
if __name__ == "__main__":
    question_page()
