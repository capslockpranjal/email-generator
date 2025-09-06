# Personalized Email Generator

A powerful AI-powered email generation tool that creates personalized, professional emails based on your specific requirements. Built with Streamlit for the frontend and FastAPI for the backend, this application leverages OpenAI's GPT models to generate contextually appropriate emails.

## Features

- **Multiple Email Types**: Business, Personal, Marketing, Follow-up, and Thank You emails
- **Customizable Tone**: Professional, Friendly, Formal, Casual, or Persuasive
- **Flexible Length**: Short, Medium, or Long email options
- **AI-Powered**: Uses OpenAI's GPT-3.5-turbo for intelligent email generation
- **User-Friendly Interface**: Clean, intuitive Streamlit-based UI
- **RESTful API**: FastAPI backend for easy integration

## Project Structure

```
personalized-email-generator/
│── app.py              # Main Streamlit UI
│── api.py              # FastAPI backend
│── utils/
│    └── prompts.py     # Prompt templates
│── requirements.txt    # Dependencies
│── README.md           # Project details
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd personalized-email-generator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

### Running the Application

1. **Start the FastAPI backend**
   ```bash
   python api.py
   ```
   The API will be available at `http://localhost:8000`

2. **Start the Streamlit frontend**
   ```bash
   streamlit run app.py
   ```
   The UI will be available at `http://localhost:8501`

### Using the API

The FastAPI backend provides the following endpoints:

- `GET /` - Health check
- `GET /health` - Detailed health status
- `POST /generate-email` - Generate personalized email
- `GET /email-types` - Get available email types, tones, and lengths

#### Example API Request

```bash
curl -X POST "http://localhost:8000/generate-email" \
     -H "Content-Type: application/json" \
     -d '{
       "recipient_name": "John Doe",
       "sender_name": "Jane Smith",
       "subject": "Project Update",
       "context": "Following up on the Q4 project",
       "email_type": "Business",
       "tone": "Professional",
       "length": "Medium"
     }'
```

## Configuration

### Email Types
- **Business**: Professional communication for work-related matters
- **Personal**: Informal communication for personal relationships
- **Marketing**: Promotional content with calls-to-action
- **Follow-up**: Follow-up messages referencing previous communication
- **Thank You**: Gratitude and appreciation messages

### Tones
- **Professional**: Formal business language
- **Friendly**: Warm and approachable
- **Formal**: Very formal and traditional
- **Casual**: Relaxed and conversational
- **Persuasive**: Compelling and action-oriented

### Lengths
- **Short**: 50-100 words, concise and direct
- **Medium**: 100-200 words, adequate detail
- **Long**: 200+ words, comprehensive information

## Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Streamlit**: Rapid web app development framework
- **OpenAI**: AI model integration
- **Pydantic**: Data validation and settings management
- **Requests**: HTTP library for API calls

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, email support@example.com or create an issue in the repository.

## Roadmap

- [ ] Email templates library
- [ ] Email scheduling functionality
- [ ] Multi-language support
- [ ] Email analytics and tracking
- [ ] Integration with popular email clients
- [ ] Bulk email generation
- [ ] Custom prompt templates
- [ ] Email quality scoring
# email-generator
# email-generator
# email-generator
