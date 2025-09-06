# 🚀 Setup Guide - Personalized Email Generator

This guide will help you get your personalized email generator up and running quickly!

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key (get one at [OpenAI Platform](https://platform.openai.com/api-keys))

## 🛠️ Quick Setup

### 1. Install Dependencies
```bash
# Install all required packages
pip install -r requirements.txt
```

### 2. Configure API Key
Edit the `.env` file and add your OpenAI API key:
```env
OPENAI_API_KEY=your_actual_openai_api_key_here
```

### 3. Start the Application

#### Option A: Using the provided scripts (Recommended)

**Terminal 1 - Start Backend:**
```bash
python start_backend.py
```

**Terminal 2 - Start Frontend:**
```bash
python start_frontend.py
```

#### Option B: Manual startup

**Terminal 1 - Start Backend:**
```bash
python api.py
```

**Terminal 2 - Start Frontend:**
```bash
streamlit run app.py
```

## 🌐 Access the Application

- **Frontend UI**: http://localhost:8501
- **API Documentation**: http://localhost:8000/docs
- **API Health Check**: http://localhost:8000/health

## 🧪 Testing the Setup

### Test 1: Backend Health Check
```bash
curl http://localhost:8000/health
```
Expected response: `{"status": "healthy"}`

### Test 2: Generate a Test Email
```bash
curl -X POST "http://localhost:8000/generate-email" \
     -H "Content-Type: application/json" \
     -d '{
       "recipient_name": "John Doe",
       "sender_name": "Jane Smith",
       "subject": "Test Email",
       "context": "This is a test email",
       "email_type": "Business",
       "tone": "Professional",
       "length": "Short"
     }'
```

### Test 3: Frontend UI
1. Open http://localhost:8501 in your browser
2. Fill in the form fields
3. Click "Generate Email"
4. Verify the email is generated

## 🔧 Troubleshooting

### Common Issues

**1. "Could not connect to the API" error in frontend**
- Make sure the backend is running on port 8000
- Check if there are any error messages in the backend terminal

**2. "OpenAI API key not found" error**
- Verify your `.env` file contains the correct API key
- Make sure there are no extra spaces or quotes around the key

**3. Port already in use**
- Change the port in the `.env` file
- Or kill the process using the port: `netstat -ano | findstr :8000`

**4. Import errors**
- Make sure you're in the correct directory
- Verify all dependencies are installed: `pip list`

### Getting Help

1. Check the terminal output for error messages
2. Verify all files are in the correct location
3. Ensure Python virtual environment is activated
4. Check that all dependencies are installed correctly

## 🎯 Next Steps

Once everything is working:

1. **Customize the prompts** in `utils/prompts.py`
2. **Add new email types** by modifying the prompt templates
3. **Deploy to production** using your preferred hosting platform
4. **Add authentication** if needed for production use

## 📚 API Reference

### Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /generate-email` - Generate personalized email
- `GET /email-types` - Get available options

### Request Format

```json
{
  "recipient_name": "string",
  "sender_name": "string", 
  "subject": "string",
  "context": "string (optional)",
  "email_type": "Business|Personal|Marketing|Follow-up|Thank You",
  "tone": "Professional|Friendly|Formal|Casual|Persuasive",
  "length": "Short|Medium|Long"
}
```

### Response Format

```json
{
  "subject": "string",
  "email": "string",
  "word_count": "number"
}
```

Happy email generating! 📧✨
