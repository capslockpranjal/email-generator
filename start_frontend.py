#!/usr/bin/env python3
"""
Start the Streamlit frontend for the Personalized Email Generator
"""
import subprocess
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    # Get configuration from environment variables
    port = int(os.getenv("STREAMLIT_PORT", 8501))
    
    print(f"🎨 Starting Personalized Email Generator Frontend...")
    print(f"🌐 UI will be available at: http://localhost:{port}")
    print(f"⚠️  Make sure the backend API is running on port 8000")
    print("\n" + "="*50)
    
    # Start Streamlit
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", str(port),
            "--server.headless", "true",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Frontend stopped by user")
    except Exception as e:
        print(f"❌ Error starting frontend: {e}")
        sys.exit(1)
