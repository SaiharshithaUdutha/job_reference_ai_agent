import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="your key")  # Replace with your Gemini API key

# Set up the model
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

# Streamlit App
st.title("Job Reference AI Agent")
st.write("Enter your skills, interests, Capstone Project and location to get personalized job recommendations.")

# User Input
skills = st.text_input("Enter your skills (e.g., Python, Machine Learning):")
interests = st.text_input("Enter your interests (e.g., Data Science, AI):")
capstoneproject = st.text_input("Enter your completed Capstone Project (e.g., Image Classifier)")
location = st.text_input("Enter your preferred location (e.g., New York, Remote):")

# Generate Job Recommendations
if st.button("Get Job References"):
    if skills and interests and capstoneproject and location:
        # Create a prompt for Gemini
        prompt = f"""
        Act as a job reference AI agent. Suggest 10 jobs for a user with the following details:
        - Skills: {skills}
        - Interests: {interests}
        - Capstone Project: {capstoneproject}
        - Preferred Location: {location}

        Provide the details for each job, include the following details in an unordered list format:
        1.Job Title
        2.Company Name
        3.Salary 
        4.Contact Details of the company(e.g., website)
        5.Skills Required
        6.Job Description
        
        Ensure the output is structured as a numbered list, with each job clearly separated and all details well-organised.And don't give any important note.and don't as example in the output.
        
        """

        # Generate response using Gemini
        response = model.generate_content(prompt)

        # Display recommendations
        st.write("### Job References:")
        st.write(response.text)
    else:
        st.error("Please fill in all fields (skills, interests, capstone project, location).")


st.title("Interview Preparation")
st.write("Enter your skills, interests and Capstone Project to get the interview questions and sample answers")
#user input

skills = st.text_input("Enter your skills (e.g., Python, Machine Learning):",key = "skill_input")
interests = st.text_input("Enter your interests (e.g., Data Science, AI):",key = "interest_input")
capstoneproject = st.text_input("Enter your completed Capstone Project (e.g., Image Classifier)",key
                                = "project_input")

# interview questions
if st.button("Get Questions and answers"):
    if skills and interests and capstoneproject:



        prompt = f"""
                Act as a Personalized Interview Q&A Generator.
                Using the inputs provided below, generate a comprehensive list of interview questions designed to highlight the individual's skills, interests, and capstone project experience. 
                Accompany each question with sample answers that demonstrate expertise, confidence, and alignment with the inputs. Include additional tips for personalizing the answers during a live interview:
                -skills: {skills}
                - Interests: {interests}
                - Capstone Project: {capstoneproject}
              Ensure the output should me structured."""
        response = model.generate_content(prompt)

        st.write("### Interview Q&A:")
        st.write(response.text)
else:
  st.error("Please fill in all fields (skills, interests, capstone project).")
