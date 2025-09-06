# Main Streamlit UI for Personalized Email Generator
import streamlit as st
import requests
import json

def main():
    st.set_page_config(
        page_title="Personalized Email Generator",
        page_icon="📧",
        layout="wide"
    )
    
    st.title("📧 Personalized Email Generator")
    st.markdown("Generate personalized emails with AI assistance")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("Configuration")
        email_type = st.selectbox(
            "Email Type",
            ["Business", "Personal", "Marketing", "Follow-up", "Thank You"]
        )
        tone = st.selectbox(
            "Tone",
            ["Professional", "Friendly", "Formal", "Casual", "Persuasive"]
        )
        length = st.selectbox(
            "Length",
            ["Short", "Medium", "Long"]
        )
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("Input Details")
        recipient_name = st.text_input("Recipient Name")
        sender_name = st.text_input("Your Name")
        subject = st.text_input("Email Subject")
        context = st.text_area("Context/Additional Information", height=100)
        
        if st.button("Generate Email", type="primary"):
            if recipient_name and sender_name and subject:
                # Call API to generate email
                email_data = {
                    "recipient_name": recipient_name,
                    "sender_name": sender_name,
                    "subject": subject,
                    "context": context,
                    "email_type": email_type,
                    "tone": tone,
                    "length": length
                }
                
                try:
                    response = requests.post("http://localhost:8000/generate-email", json=email_data)
                    if response.status_code == 200:
                        result = response.json()
                        st.session_state.generated_email = result["email"]
                        st.session_state.generated_subject = result["subject"]
                    else:
                        st.error("Error generating email. Please try again.")
                except requests.exceptions.ConnectionError:
                    st.error("Could not connect to the API. Please make sure the backend is running.")
            else:
                st.warning("Please fill in all required fields.")
    
    with col2:
        st.header("Generated Email")
        if "generated_email" in st.session_state:
            st.subheader("Subject:")
            st.write(st.session_state.generated_subject)
            st.subheader("Email Body:")
            st.write(st.session_state.generated_email)
            
            if st.button("Copy to Clipboard"):
                st.write("Email copied to clipboard!")
        else:
            st.info("Generate an email to see the result here.")

if __name__ == "__main__":
    main()
