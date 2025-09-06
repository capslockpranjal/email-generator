#!/usr/bin/env python3
"""
Demo mode for Personalized Email Generator
This allows testing the application without OpenAI API calls
"""
import json
import random

def generate_demo_email(recipient_name, sender_name, subject, context, email_type, tone, length):
    """Generate a demo email without using OpenAI API"""
    
    # Demo email templates
    templates = {
        "Business": {
            "Professional": f"""Dear {recipient_name},

I hope this email finds you well. I am writing to you regarding {subject}.

{context if context else "I wanted to reach out to discuss this matter with you."}

I believe this would be beneficial for both parties and would appreciate the opportunity to discuss this further.

Please let me know your thoughts and availability for a meeting.

Best regards,
{sender_name}""",
            
            "Friendly": f"""Hi {recipient_name},

I hope you're doing great! I wanted to reach out about {subject}.

{context if context else "I thought this might be of interest to you."}

I'd love to hear your thoughts on this and see if we can work something out together.

Looking forward to hearing from you!

Best,
{sender_name}"""
        },
        
        "Personal": {
            "Friendly": f"""Hey {recipient_name},

Hope you're doing well! I wanted to reach out about {subject}.

{context if context else "I thought you might be interested in this."}

Let me know what you think!

Take care,
{sender_name}""",
            
            "Casual": f"""Hi {recipient_name},

How's it going? I wanted to tell you about {subject}.

{context if context else "This is pretty cool and I thought you'd like to know about it."}

Let me know if you want to chat about it!

Cheers,
{sender_name}"""
        },
        
        "Marketing": {
            "Persuasive": f"""Dear {recipient_name},

I have exciting news about {subject}!

{context if context else "This is an opportunity you won't want to miss."}

Don't wait - this offer is only available for a limited time!

Click here to learn more: [Your Link]

Best regards,
{sender_name}""",
            
            "Professional": f"""Dear {recipient_name},

I hope this email finds you well. I'm reaching out regarding {subject}.

{context if context else "We have a special offer that might interest you."}

This could be a great opportunity for you. Please let me know if you'd like to learn more.

Best regards,
{sender_name}"""
        }
    }
    
    # Get the appropriate template
    email_template = templates.get(email_type, templates["Business"]).get(tone, templates["Business"]["Professional"])
    
    # Adjust length based on requirements
    if length == "Short":
        # Keep it concise
        lines = email_template.split('\n')
        email_template = '\n'.join(lines[:8])  # Keep first 8 lines
    elif length == "Long":
        # Add more detail
        email_template += f"""

Additional Information:
- This is a detailed follow-up to our previous discussion
- We have several options available for your consideration
- I'm available to answer any questions you might have
- Please don't hesitate to reach out if you need clarification

I look forward to your response and hope we can move forward with this opportunity.

Thank you for your time and consideration."""
    
    return email_template

def demo_email_generation():
    """Demo the email generation functionality"""
    print("🎭 Demo Mode - Personalized Email Generator")
    print("=" * 50)
    
    # Demo data
    demo_requests = [
        {
            "recipient_name": "John Smith",
            "sender_name": "Jane Doe",
            "subject": "Project Proposal",
            "context": "Following up on our meeting about the new marketing campaign",
            "email_type": "Business",
            "tone": "Professional",
            "length": "Medium"
        },
        {
            "recipient_name": "Sarah Johnson",
            "sender_name": "Mike Wilson",
            "subject": "Coffee Chat",
            "context": "Would love to catch up and discuss the new opportunities",
            "email_type": "Personal",
            "tone": "Friendly",
            "length": "Short"
        },
        {
            "recipient_name": "Marketing Team",
            "sender_name": "Alex Chen",
            "subject": "New Product Launch",
            "context": "Exciting news about our latest product that's launching next month",
            "email_type": "Marketing",
            "tone": "Persuasive",
            "length": "Long"
        }
    ]
    
    for i, request in enumerate(demo_requests, 1):
        print(f"\n📧 Demo Email {i}:")
        print(f"Type: {request['email_type']} | Tone: {request['tone']} | Length: {request['length']}")
        print("-" * 40)
        
        email = generate_demo_email(
            request["recipient_name"],
            request["sender_name"],
            request["subject"],
            request["context"],
            request["email_type"],
            request["tone"],
            request["length"]
        )
        
        print(email)
        print("\n" + "="*50)

if __name__ == "__main__":
    demo_email_generation()
