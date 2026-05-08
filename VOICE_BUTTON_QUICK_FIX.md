# 🎤 Voice Button Quick Fix Guide

## Issue: Voice button stops immediately after clicking

### Root Cause:
The browser needs explicit microphone permission, and the speech recognition API requires HTTPS or localhost.

### Quick Solutions:

## ✅ Solution 1: Check Your URL

**The voice feature ONLY works on:**
- `https://` websites (secure connection)
- `http://localhost:5000` or `http://127.0.0.1:5000`

**It will NOT work on:**
- `http://` on non-localhost domains
- IP addresses like `http://192.168.x.x`

**Action:** Make sure you're accessing the site via `http://localhost:5000`

---

## ✅ Solution 2: Grant Microphone Permission

### When you click the microphone button for the first time:

1. Browser will show a popup: **"Allow microphone access?"**
2. Click **"Allow"** or **"Yes"**
3. If you accidentally clicked "Block", follow these steps:

### Chrome/Edge - Reset Permission:
1. Click the **🔒 lock icon** (or ⓘ info icon) in the address bar
2. Find "Microphone" in the list
3. Change from "Block" to **"Allow"**
4. **Refresh the page** (F5)
5. Try the microphone button again

### Safari - Reset Permission:
1. Safari → **Settings** → **Websites**
2. Click **Microphone** in left sidebar
3. Find `localhost` and set to **"Allow"**
4. Refresh the page

---

## ✅ Solution 3: Check System Permissions

### macOS:
1. **System Settings** → **Privacy & Security** → **Microphone**
2. Ensure your browser (Chrome/Safari/Edge) is **checked ✅**
3. If you just enabled it, **restart your browser**

### Windows:
1. **Settings** → **Privacy** → **Microphone**
2. Ensure "Allow apps to access your microphone" is **ON**
3. Scroll down and ensure your browser is **allowed**
4. Restart browser if needed

---

## ✅ Solution 4: Test Your Microphone

Before using the voice button, verify your mic works:

### Quick Test:
1. Open a new tab
2. Go to: https://www.onlinemictest.com/
3. Click "Play test" and speak
4. You should see the audio levels moving

If the test fails, your microphone has a hardware/driver issue.

---

## ✅ Solution 5: Use the Right Browser

### ✅ Supported Browsers:
- **Google Chrome** (Best support)
- **Microsoft Edge** (Best support)
- **Safari** (macOS/iOS only)

### ❌ Limited/No Support:
- Firefox (limited)
- Opera (limited)
- Internet Explorer (not supported)

**Recommendation:** Use Google Chrome for best results.

---

## 🎯 Step-by-Step Testing Procedure

Follow these steps in order:

1. **Open Chrome browser**
2. **Navigate to:** `http://localhost:5000`
3. **Login to the application**
4. **Go to AI Assistant page**
5. **Click the microphone button** 🎤
6. **When prompted, click "Allow"** for microphone access
7. **Wait for the button to turn red** and show "Listening..."
8. **Speak clearly:** "What is my name?"
9. **Watch the text appear** in the input field
10. **Click send** or wait for auto-send

---

## 🔍 Troubleshooting Checklist

If voice still doesn't work, check ALL of these:

- [ ] Using `http://localhost:5000` (not IP address)
- [ ] Using Chrome, Edge, or Safari browser
- [ ] Microphone permission granted in browser
- [ ] Microphone permission granted in system settings
- [ ] Microphone works in other apps (test it!)
- [ ] No other app is using the microphone
- [ ] Page has been refreshed after granting permissions
- [ ] Browser has been restarted after system permission changes

---

## 💡 Alternative: Use Text Input

If voice input still doesn't work:

1. **Type your questions** in the text field
2. **Use the quick question buttons** below the input
3. **Click the speaker button** 🔊 to hear responses (this works even if voice input doesn't)

---

## 🆘 Still Not Working?

### Check Browser Console:
1. Press **F12** (or Cmd+Option+I on Mac)
2. Click **"Console"** tab
3. Click the microphone button
4. Look for error messages

### Common Console Errors:

**"NotAllowedError: Permission denied"**
→ Grant microphone permission in browser settings

**"NotFoundError: Requested device not found"**
→ No microphone detected, check hardware

**"NotSupportedError"**
→ Browser doesn't support speech recognition, use Chrome

---

## ✅ Expected Behavior When Working:

1. Click microphone button 🎤
2. Button turns **RED**
3. Text shows **"Listening..."**
4. Input field shows **"🎤 Listening... Speak now!"**
5. As you speak, text appears in real-time
6. When you stop, button returns to normal
7. Your speech is in the input field
8. Click send or it auto-sends

---

## 📝 Quick Reference

| Issue | Solution |
|-------|----------|
| Button stops immediately | Grant microphone permission |
| "Permission denied" | Allow mic in browser settings |
| No microphone detected | Check hardware/system settings |
| Not working on IP address | Use localhost instead |
| Works on phone but not computer | Check system mic permissions |

---

**Last Updated:** May 8, 2026
**Status:** Voice recognition improved with better error handling