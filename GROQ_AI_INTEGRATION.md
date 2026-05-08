# Groq AI Integration & Adaptive UI Documentation

## Overview
This document describes the Groq-powered LLM voice assistant and adaptive UI system integrated into the MemoryCare application.

---

## 🤖 Groq AI Assistant

### Features
- **LLM-Powered Responses**: Uses Groq's `llama-3.1-70b-versatile` model for intelligent, context-aware conversations
- **Context Storage**: Stores all user conversations and personal information in MongoDB
- **Memory Retention**: Retrieves past conversations to provide personalized responses
- **Fallback System**: Gracefully falls back to rule-based responses if Groq API is unavailable

### Setup

1. **Get Groq API Key**
   - Visit: https://console.groq.com/keys
   - Create a free account
   - Generate an API key

2. **Configure Environment**
   ```bash
   # Copy example env file
   cp .env.example .env
   
   # Edit .env and add your Groq API key
   GROQ_API_KEY=your-actual-groq-api-key-here
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### How It Works

#### 1. User Message Processing
When a user sends a message to the AI assistant:

```python
# app.py - ai_response route
@app.route('/ai_response', methods=['POST'])
def ai_response():
    user_message = request.json.get('prompt')
    
    # Check if user is storing information
    if contains_storage_keywords(user_message):
        # Store in user_context collection
        db.user_context.insert_one({
            'user_id': user_id,
            'information': user_message,
            'timestamp': datetime.now()
        })
```

#### 2. Context Retrieval
The system retrieves relevant context before generating a response:

```python
# Retrieve last 10 context entries
user_contexts = db.user_context.find(
    {"user_id": user_id}
).sort("timestamp", -1).limit(10)

# Build context string
context_string = "\n".join([ctx['information'] for ctx in user_contexts])
```

#### 3. Groq API Call
```python
def generate_contextual_response(user_message, context, user):
    client = Groq(api_key=os.getenv('GROQ_API_KEY'))
    
    system_prompt = f"""You are a compassionate AI assistant for dementia care.
    
    User Information:
    Name: {user['name']}
    Cognitive Profile: {user['cognitive_profile']}
    
    Stored Context:
    {context}
    
    Guidelines:
    - Keep responses short (2-3 sentences)
    - Be warm and encouraging
    - Reference stored context when relevant
    """
    
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        model="llama-3.1-70b-versatile",
        temperature=0.7,
        max_tokens=200
    )
    
    return response.choices[0].message.content
```

#### 4. Response Storage
All conversations are stored for future reference:

```python
db.ai_conversations.insert_one({
    'user_id': user_id,
    'timestamp': datetime.now(),
    'user_message': user_message,
    'ai_response': response_text,
    'context_type': 'conversation'
})
```

### Database Collections

#### `user_context`
Stores personal information shared by users:
```javascript
{
    _id: ObjectId,
    user_id: ObjectId,
    timestamp: ISODate,
    information: String,  // "My name is John", "I live in NYC"
    category: String,     // "user_provided"
    extracted: Boolean    // true
}
```

#### `ai_conversations`
Stores complete conversation history:
```javascript
{
    _id: ObjectId,
    user_id: ObjectId,
    timestamp: ISODate,
    user_message: String,
    ai_response: String,
    context_type: String  // "conversation"
}
```

### Storage Keywords
The system automatically detects when users want to store information:
- "my name is"
- "i am"
- "i live"
- "my age is"
- "i like"
- "my hobby"
- "remember that"
- "note that"
- "save this"
- "i have"
- "my favorite"

### Example Conversations

**Storing Information:**
```
User: "My name is Sarah and I live in Boston"
AI: "Got it! I've remembered that: 'My name is Sarah and I live in Boston'. 
     I'll keep this information for future reference."
```

**Retrieving Information:**
```
User: "What's my name?"
AI: "Your name is Sarah. You also mentioned you live in Boston. 
     Is there anything else you'd like to know?"
```

**Context-Aware Response:**
```
User: "What do I like to do?"
AI: "Based on what you've told me, you enjoy gardening and reading mystery novels. 
     Would you like to talk more about your hobbies?"
```

---

## 🎨 Adaptive UI System

### Overview
The UI automatically adapts based on the user's cognitive assessment (MMSE score):

- **Profile-A (Normal)**: Standard UI for mild cognitive impairment
- **Profile-B (Simplified)**: Larger elements for moderate impairment
- **Profile-C (Assisted)**: Maximum accessibility for severe impairment

### UI Mode Classification

```python
def classify_severity(score):
    if score >= 24:
        return {
            'level': 'Mild',
            'profile': 'Profile-A',
            'ui_mode': 'normal'
        }
    elif 18 <= score < 24:
        return {
            'level': 'Moderate',
            'profile': 'Profile-B',
            'ui_mode': 'simplified'
        }
    else:
        return {
            'level': 'Severe',
            'profile': 'Profile-C',
            'ui_mode': 'assisted'
        }
```

### CSS Implementation

#### Profile-A: Normal UI
```css
body.ui-normal {
    font-size: 16px;
}

body.ui-normal .btn {
    padding: 8px 16px;
    font-size: 14px;
}
```

#### Profile-B: Simplified UI
```css
body.ui-simplified {
    font-size: 18px;
    line-height: 1.8;
}

body.ui-simplified .btn {
    padding: 16px 32px;
    font-size: 18px;
    min-height: 56px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

body.ui-simplified h1 {
    font-size: 2.5rem;
    font-weight: 700;
}
```

#### Profile-C: Assisted UI
```css
body.ui-assisted {
    font-size: 22px;
    line-height: 2;
}

body.ui-assisted .btn {
    padding: 24px 48px;
    font-size: 22px;
    min-height: 72px;
    box-shadow: 0 6px 12px rgba(0,0,0,0.2);
}

body.ui-assisted h1 {
    font-size: 3rem;
    font-weight: 800;
}

/* High contrast for better visibility */
body.ui-assisted {
    color: #1a1a1a;
}
```

### Template Integration

The UI mode is applied via the body class in `base.html`:

```html
<body class="{% if user and user.ui_mode %}ui-{{ user.ui_mode }}{% else %}ui-normal{% endif %}">
```

### Automatic UI Switching

When a user completes an MMSE assessment:

1. **Score Calculation**
   ```python
   final_score = (mmse_score * 0.60) + (observation_score * 0.25) + (task_score * 0.15)
   ```

2. **Classification**
   ```python
   classification = classify_severity(final_score)
   ```

3. **User Profile Update**
   ```python
   db.users.update_one(
       {"_id": user_id},
       {"$set": {
           "cognitive_profile": classification['profile'],
           "ui_mode": classification['ui_mode'],
           "severity_level": classification['level']
       }}
   )
   ```

4. **Immediate Effect**
   - Next page load automatically applies new UI mode
   - No manual configuration needed
   - Seamless transition for user

### UI Features by Profile

| Feature | Profile-A | Profile-B | Profile-C |
|---------|-----------|-----------|-----------|
| Font Size | 16px | 18px | 22px |
| Button Height | 44px | 56px | 72px |
| Line Height | 1.5 | 1.8 | 2.0 |
| Heading Size | 2rem | 2.5rem | 3rem |
| Button Padding | 8px 16px | 16px 32px | 24px 48px |
| Shadow Depth | Light | Medium | Heavy |
| Border Width | 1px | 2px | 3px |
| Voice Indicator | Hidden | Visible | Visible |

---

## 🔧 Testing

### Test Groq Integration

1. **Start the application**
   ```bash
   cd remindp2
   python app.py
   ```

2. **Navigate to AI Assistant**
   - Login as a user
   - Click "AI Assistant" in navigation

3. **Test Storage**
   ```
   Type: "My name is John and I like gardening"
   Expected: Confirmation message that info was stored
   ```

4. **Test Retrieval**
   ```
   Type: "What's my name?"
   Expected: "Your name is John..."
   ```

5. **Check Database**
   ```javascript
   // MongoDB shell
   db.user_context.find({user_id: ObjectId("...")})
   db.ai_conversations.find({user_id: ObjectId("...")})
   ```

### Test Adaptive UI

1. **Complete MMSE Assessment**
   - Navigate to "MMSE Test"
   - Complete all sections
   - Submit assessment

2. **Check UI Mode**
   - Score 24-30: Should see normal UI
   - Score 18-23: Should see larger buttons/text
   - Score 0-17: Should see maximum accessibility

3. **Verify Database**
   ```javascript
   db.users.findOne({_id: ObjectId("...")})
   // Check: ui_mode, cognitive_profile, severity_level
   ```

---

## 📊 Monitoring

### Check Groq API Usage
```python
# Add logging to track API calls
import logging

logging.info(f"Groq API call - User: {user_id}, Tokens: {response.usage.total_tokens}")
```

### Monitor Context Storage
```python
# Check context growth
context_count = db.user_context.count_documents({"user_id": user_id})
print(f"User has {context_count} stored contexts")
```

---

## 🚀 Production Deployment

### Environment Variables
```bash
# Required for production
GROQ_API_KEY=gsk_xxxxxxxxxxxxx
MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/
SECRET_KEY=random-secure-key-here
FLASK_ENV=production
```

### Security Considerations
1. Never commit `.env` file to git
2. Use environment variables in production
3. Rotate API keys regularly
4. Monitor API usage and costs
5. Implement rate limiting for AI endpoints

### Performance Optimization
1. **Cache frequent responses**
2. **Limit context retrieval** (currently 10 items)
3. **Use async calls** for Groq API (future enhancement)
4. **Implement request queuing** for high traffic

---

## 📝 API Reference

### Groq Model Used
- **Model**: `llama-3.1-70b-versatile`
- **Max Tokens**: 200
- **Temperature**: 0.7
- **Top P**: 0.9

### Endpoints

#### POST `/ai_response`
Send message to AI assistant

**Request:**
```json
{
    "prompt": "What's my name?"
}
```

**Response:**
```json
{
    "success": true,
    "response": "Your name is John. You mentioned you like gardening..."
}
```

---

## 🐛 Troubleshooting

### Groq API Not Working
1. Check API key in `.env`
2. Verify internet connection
3. Check Groq API status: https://status.groq.com
4. Review error logs in console
5. System will fallback to rule-based responses

### UI Not Adapting
1. Verify MMSE assessment completed
2. Check `ui_mode` field in user document
3. Clear browser cache
4. Verify CSS file loaded correctly

### Context Not Storing
1. Check MongoDB connection
2. Verify `user_context` collection exists
3. Check storage keywords in message
4. Review database permissions

---

## 📚 Additional Resources

- Groq Documentation: https://console.groq.com/docs
- MongoDB Documentation: https://docs.mongodb.com
- Flask Documentation: https://flask.palletsprojects.com

---

## ✅ Summary

**Groq AI Integration:**
- ✅ LLM-powered responses using Groq API
- ✅ Context storage in MongoDB
- ✅ Conversation history tracking
- ✅ Fallback to rule-based responses
- ✅ Personalized responses based on user data

**Adaptive UI:**
- ✅ Three UI profiles (Normal, Simplified, Assisted)
- ✅ Automatic switching based on MMSE score
- ✅ CSS-based implementation
- ✅ Accessibility-first design
- ✅ Production-ready styling

**Production Ready:**
- ✅ Environment configuration
- ✅ Error handling
- ✅ Database integration
- ✅ Security considerations
- ✅ Documentation complete