# FastAPI backend for Personalized Email Generator
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import openai
import os
from dotenv import load_dotenv
from utils.prompts import get_email_prompt

# Load environment variables
load_dotenv()

app = FastAPI(title="Personalized Email Generator API", version="1.0.0")

# Pydantic models for request/response
class EmailRequest(BaseModel):
    recipient_name: str
    sender_name: str
    subject: str
    context: Optional[str] = ""
    email_type: str = "Business"
    tone: str = "Professional"
    length: str = "Medium"

class EmailResponse(BaseModel):
    subject: str
    email: str
    word_count: int

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
async def root():
    return {"message": "Personalized Email Generator API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/generate-email", response_model=EmailResponse)
async def generate_email(request: EmailRequest):
    try:
        # Check if we should use demo mode (when OpenAI API key is not set or quota exceeded)
        api_key = os.getenv("OPENAI_API_KEY")
        use_demo_mode = not api_key or api_key == "your_openai_api_key_here"
        
        if use_demo_mode:
            # Use demo mode
            from demo_mode import generate_demo_email
            email_body = generate_demo_email(
                request.recipient_name,
                request.sender_name,
                request.subject,
                request.context,
                request.email_type,
                request.tone,
                request.length
            )
            subject = request.subject
            word_count = len(email_body.split())
            
            return EmailResponse(
                subject=subject,
                email=email_body,
                word_count=word_count
            )
        
        # Use OpenAI API
        # Get the appropriate prompt template
        prompt = get_email_prompt(
            email_type=request.email_type,
            tone=request.tone,
            length=request.length
        )
        
        # Format the prompt with user data
        formatted_prompt = prompt.format(
            recipient_name=request.recipient_name,
            sender_name=request.sender_name,
            subject=request.subject,
            context=request.context
        )
        
        # Generate email using OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional email writing assistant. Generate well-structured, personalized emails based on the given requirements."},
                {"role": "user", "content": formatted_prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        generated_content = response.choices[0].message.content
        
        # Extract subject and email body
        lines = generated_content.split('\n')
        subject = request.subject  # Use the provided subject
        email_body = generated_content
        
        # Count words
        word_count = len(email_body.split())
        
        return EmailResponse(
            subject=subject,
            email=email_body,
            word_count=word_count
        )
        
    except Exception as e:
        # If OpenAI fails, fall back to demo mode
        try:
            from demo_mode import generate_demo_email
            email_body = generate_demo_email(
                request.recipient_name,
                request.sender_name,
                request.subject,
                request.context,
                request.email_type,
                request.tone,
                request.length
            )
            subject = request.subject
            word_count = len(email_body.split())
            
            return EmailResponse(
                subject=subject,
                email=email_body,
                word_count=word_count
            )
        except Exception as demo_error:
            raise HTTPException(status_code=500, detail=f"Error generating email: {str(e)}. Demo mode also failed: {str(demo_error)}")

@app.get("/email-types")
async def get_email_types():
    return {
        "email_types": ["Business", "Personal", "Marketing", "Follow-up", "Thank You"],
        "tones": ["Professional", "Friendly", "Formal", "Casual", "Persuasive"],
        "lengths": ["Short", "Medium", "Long"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
