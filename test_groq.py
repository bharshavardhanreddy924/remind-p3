#!/usr/bin/env python3
"""Test script to verify Groq API integration"""

from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables
load_dotenv()

def test_groq_api():
    """Test Groq API with a simple query"""
    
    # Get API key
    api_key = os.getenv('GROQ_API_KEY')
    
    if not api_key:
        print("❌ GROQ_API_KEY not found in environment")
        return False
    
    print(f"✅ GROQ_API_KEY loaded: {api_key[:20]}...")
    
    try:
        # Initialize Groq client
        client = Groq(api_key=api_key)
        print("✅ Groq client initialized")
        
        # Test with a simple query
        print("\n🧪 Testing Groq API with sample query...")
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Keep responses brief."
                },
                {
                    "role": "user",
                    "content": "Say 'Hello, I am working!' in a friendly way."
                }
            ],
            model="llama-3.3-70b-versatile",  # Updated to supported model
            temperature=0.7,
            max_tokens=50
        )
        
        response = chat_completion.choices[0].message.content
        print(f"\n✅ Groq API Response:\n{response}\n")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Groq API Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("GROQ API TEST")
    print("=" * 60)
    
    success = test_groq_api()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ TEST PASSED - Groq API is working correctly!")
    else:
        print("❌ TEST FAILED - Check the error messages above")
    print("=" * 60)

# Made with Bob
