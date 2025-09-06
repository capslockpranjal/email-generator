# Prompt templates for Personalized Email Generator
from typing import Dict

def get_email_prompt(email_type: str, tone: str, length: str) -> str:
    """
    Get the appropriate prompt template based on email type, tone, and length.
    
    Args:
        email_type: Type of email (Business, Personal, Marketing, etc.)
        tone: Tone of the email (Professional, Friendly, etc.)
        length: Length of the email (Short, Medium, Long)
    
    Returns:
        Formatted prompt template string
    """
    
    # Base prompt structure
    base_prompt = """
Write a {tone} {email_type} email with the following details:

Recipient: {recipient_name}
Sender: {sender_name}
Subject: {subject}
Context: {context}

Requirements:
- Tone: {tone}
- Length: {length}
- Make it personalized and engaging
- Use proper email formatting
- Include appropriate greeting and closing
- Ensure the content is relevant to the context provided

Please generate a complete email that is ready to send.
"""
    
    # Length-specific instructions
    length_instructions = {
        "Short": "Keep it concise (50-100 words). Get straight to the point.",
        "Medium": "Provide adequate detail (100-200 words). Include necessary context.",
        "Long": "Be comprehensive (200+ words). Include detailed information and context."
    }
    
    # Tone-specific instructions
    tone_instructions = {
        "Professional": "Use formal language, proper business etiquette, and maintain a respectful tone.",
        "Friendly": "Use warm, approachable language while maintaining professionalism.",
        "Formal": "Use very formal language, proper titles, and traditional business structure.",
        "Casual": "Use relaxed, conversational language appropriate for informal communication.",
        "Persuasive": "Use compelling language, include benefits, and create urgency when appropriate."
    }
    
    # Email type-specific instructions
    type_instructions = {
        "Business": "Focus on professional communication, clear objectives, and business context.",
        "Personal": "Use a more personal tone, include personal touches, and be more conversational.",
        "Marketing": "Include compelling calls-to-action, highlight benefits, and create interest.",
        "Follow-up": "Reference previous communication, provide updates, and suggest next steps.",
        "Thank You": "Express genuine gratitude, be specific about what you're thanking for, and maintain warmth."
    }
    
    # Combine all instructions
    full_prompt = base_prompt.format(
        tone=tone,
        email_type=email_type,
        length=length,
        recipient_name="{recipient_name}",
        sender_name="{sender_name}",
        subject="{subject}",
        context="{context}"
    )
    
    # Add specific instructions
    full_prompt += f"\n\nSpecific Instructions:\n"
    full_prompt += f"- {length_instructions.get(length, '')}\n"
    full_prompt += f"- {tone_instructions.get(tone, '')}\n"
    full_prompt += f"- {type_instructions.get(email_type, '')}\n"
    
    return full_prompt

def get_system_prompt() -> str:
    """
    Get the system prompt for the AI assistant.
    
    Returns:
        System prompt string
    """
    return """You are a professional email writing assistant with expertise in creating personalized, engaging, and effective emails. You understand various business contexts, communication styles, and can adapt your writing to different audiences and purposes. Your emails are always well-structured, grammatically correct, and appropriate for the given context."""

def get_examples() -> Dict[str, str]:
    """
    Get example emails for different types and tones.
    
    Returns:
        Dictionary of example emails
    """
    return {
        "business_professional": """
Subject: Follow-up on Q4 Project Discussion

Dear [Recipient Name],

I hope this email finds you well. I wanted to follow up on our discussion regarding the Q4 project timeline and deliverables.

As we discussed, the key milestones remain:
- Project kickoff: [Date]
- First review: [Date]
- Final delivery: [Date]

I've attached the updated project plan for your review. Please let me know if you have any questions or concerns.

Best regards,
[Your Name]
""",
        "personal_friendly": """
Subject: Catching Up!

Hi [Recipient Name],

I hope you're doing great! It's been a while since we last caught up, and I wanted to reach out to see how you've been.

I've been thinking about our conversation about [context] and wanted to share some updates. [Additional personal content]

Would love to hear from you soon!

Take care,
[Your Name]
""",
        "marketing_persuasive": """
Subject: Don't Miss Out - Limited Time Offer!

Dear [Recipient Name],

I'm excited to share an exclusive opportunity that I believe will be of great value to you.

[Product/Service details and benefits]

This special offer is only available for a limited time, so don't wait! Click here to learn more and secure your spot.

Best regards,
[Your Name]
"""
    }
