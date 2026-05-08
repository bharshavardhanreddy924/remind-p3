"""
Script to reset admin password in MongoDB
Run this if you encounter password hash compatibility issues
"""

from pymongo.mongo_client import MongoClient
from werkzeug.security import generate_password_hash
import certifi

# MongoDB Configuration
uri = "mongodb+srv://bharshavardhanreddy924:516474Ta@data-dine.5oghq.mongodb.net/?retryWrites=true&w=majority&ssl=true"

try:
    client = MongoClient(uri, tlsCAFile=certifi.where())
    client.admin.command('ping')
    print("✅ Connected to MongoDB!")
    
    db = client['memorycare_db']
    
    # Update admin password with compatible hash
    new_password_hash = generate_password_hash('admin123', method='pbkdf2:sha256')
    
    result = db.users.update_one(
        {"email": "admin@memorycare.com"},
        {"$set": {"password": new_password_hash}}
    )
    
    if result.modified_count > 0:
        print("✅ Admin password reset successfully!")
        print("Email: admin@memorycare.com")
        print("Password: admin123")
    else:
        print("⚠️  Admin user not found. Creating new admin user...")
        from datetime import datetime
        
        db.users.insert_one({
            'name': 'Admin User',
            'email': 'admin@memorycare.com',
            'password': new_password_hash,
            'user_type': 'caretaker',
            'created_at': datetime.now(),
            'personal_info': 'Administrator account',
            'cognitive_profile': None,
            'ui_mode': 'normal'
        })
        print("✅ Admin user created successfully!")
        print("Email: admin@memorycare.com")
        print("Password: admin123")
    
    client.close()
    
except Exception as e:
    print(f"❌ Error: {e}")

# Made with Bob
