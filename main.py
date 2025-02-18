import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyAPJiibSLwfCbF5MGyR9ZxsTLv8viFBbaU")  # Replace with your Gemini API key

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
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

# Streamlit App
st.title("Job Reference Bot")
st.write("Enter your skills, interests, and location to get personalized job recommendations.")

# User Input
skills = st.text_input("Enter your skills (e.g., Python, Machine Learning):")
interests = st.text_input("Enter your interests (e.g., Data Science, AI):")
location = st.text_input("Enter your preferred location (e.g., New York, Remote):")

# Generate Job Recommendations
if st.button("Get Job References"):
    if skills and interests and location:
        # Create a prompt for Gemini
        prompt = f"""
        Act as a job recommendation AI agent. Suggest 5 jobs for a user with the following details:
        - Skills: {skills}
        - Interests: {interests}
        - Preferred Location: {location}

        Provide the job title, company, and a brief description for each recommendation.
        """

        # Generate response using Gemini
        response = model.generate_content(prompt)

        # Display recommendations
        st.write("### Job Recommendations:")
        
        st.write(response.text)
    else:
        st.error("Please fill in all fields (skills, interests, location).")
