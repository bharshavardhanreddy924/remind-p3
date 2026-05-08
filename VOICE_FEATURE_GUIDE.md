# 🎤 Voice Feature Troubleshooting Guide

## Voice Recognition Not Working - Solutions

### Problem: Voice button turns off immediately after clicking

This is usually caused by one of these issues:

---

## ✅ Solution 1: Check Browser Compatibility

### Supported Browsers:
- ✅ **Google Chrome** (Recommended)
- ✅ **Microsoft Edge**
- ✅ **Safari** (macOS/iOS)
- ❌ **Firefox** (Limited support)
- ❌ **Opera** (Limited support)

**Action:** Use Google Chrome or Microsoft Edge for best results.

---

## ✅ Solution 2: Grant Microphone Permissions

### Chrome/Edge:
1. Click the **🔒 lock icon** or **ⓘ info icon** in the address bar
2. Find "Microphone" in the permissions list
3. Change from "Block" to **"Allow"**
4. Refresh the page (F5)

### Safari:
1. Go to **Safari → Settings → Websites**
2. Click **Microphone** in the left sidebar
3. Find your site and set to **"Allow"**
4. Refresh the page

### Check System Permissions (macOS):
1. **System Settings → Privacy & Security → Microphone**
2. Ensure your browser is checked ✅
3. Restart browser if you just enabled it

### Check System Permissions (Windows):
1. **Settings → Privacy → Microphone**
2. Ensure "Allow apps to access your microphone" is **ON**
3. Ensure your browser is allowed
4. Restart browser

---

## ✅ Solution 3: Test Your Microphone

### Quick Test:
1. Open a new tab
2. Go to: `chrome://settings/content/microphone` (Chrome)
3. Or: `edge://settings/content/microphone` (Edge)
4. Click "Test" next to your microphone
5. Speak - you should see audio levels moving

### Alternative Test:
- Open Voice Recorder (Windows) or QuickTime (Mac)
- Try recording - if it works, your mic is fine

---

## ✅ Solution 4: Use HTTPS (Required for Voice)

Voice recognition **ONLY works on**:
- ✅ `https://` websites
- ✅ `localhost` (for development)

**Action:** Ensure you're accessing the site via HTTPS or localhost.

---

## ✅ Solution 5: Improved Voice Recognition (Applied)

### What Was Fixed:

1. **Better Error Messages**
   - Now shows specific error (no speech, permission denied, etc.)
   - Alerts user with clear instructions

2. **Interim Results**
   - Shows what you're saying in real-time
   - Gives visual feedback that it's listening

3. **Longer Listening Time**
   - Recognition stays active longer
   - Better chance to capture speech

4. **Visual Feedback**
   - Button shows "Listening..." text
   - Input field shows "🎤 Listening... Speak now!"
   - Clear indication when recording

---

## 🎯 How to Use Voice Feature

### Step-by-Step:

1. **Click the microphone button** 🎤
2. **Allow microphone access** (if prompted)
3. **Wait for "Listening..." indicator**
4. **Speak clearly** into your microphone
5. **Your speech appears** in the text field
6. **Click send** or it auto-sends (in assisted mode)

### Tips for Best Results:

- 📢 **Speak clearly** and at normal pace
- 🔇 **Reduce background noise**
- 🎤 **Position mic 6-12 inches** from mouth
- ⏱️ **Start speaking within 2-3 seconds** of clicking button
- 🗣️ **Speak in complete sentences**

---

## 🔧 Testing the Fix

### Test Procedure:

1. **Open AI Assistant page**
2. **Click microphone button** 🎤
3. **Check for these indicators:**
   - Button turns red
   - Shows "Listening..."
   - Input field shows "🎤 Listening... Speak now!"

4. **Speak a test phrase:**
   - "What is my name?"
   - "How old am I?"
   - "Tell me about myself"

5. **Verify:**
   - Text appears in input field
   - Button returns to normal
   - Message sends (or you can click send)

---

## ❌ Common Errors & Solutions

### Error: "No speech detected"
**Cause:** Microphone not picking up audio or you didn't speak
**Solution:** 
- Check microphone is not muted
- Speak louder or closer to mic
- Test mic in system settings

### Error: "Microphone permission denied"
**Cause:** Browser doesn't have permission
**Solution:**
- Click lock icon in address bar
- Allow microphone access
- Refresh page

### Error: "Microphone not found"
**Cause:** No microphone connected or detected
**Solution:**
- Check microphone is plugged in
- Check it's selected as default in system settings
- Try a different microphone

### Error: "Network error"
**Cause:** Internet connection issue
**Solution:**
- Check internet connection
- Try refreshing page
- Check if other sites work

---

## 🎤 Alternative: Text-to-Speech (Speaker Button)

If voice input doesn't work, you can still use voice output:

1. **Type your question** in the text field
2. **Send the message**
3. **Click the speaker button** 🔊
4. **AI response is read aloud**

This works even if voice input is not available!

---

## 🌐 Browser Console Debugging

If issues persist, check browser console:

1. **Press F12** (or Cmd+Option+I on Mac)
2. **Click "Console" tab**
3. **Click microphone button**
4. **Look for error messages**

Common console messages:
- ✅ "Speech recognition started" - Good!
- ✅ "Speech recognition ended" - Normal
- ❌ "Speech recognition error: not-allowed" - Permission issue
- ❌ "Speech recognition error: no-speech" - Didn't detect speech

---

## 📱 Mobile Devices

### iOS (Safari):
- ✅ Voice recognition works
- Requires iOS 14.5+
- Must allow microphone in Safari settings

### Android (Chrome):
- ✅ Voice recognition works
- Must allow microphone permission
- Works best with Chrome browser

---

## 🔄 Quick Reset Procedure

If nothing works, try this:

1. **Close all browser tabs**
2. **Clear browser cache** (Ctrl+Shift+Delete)
3. **Restart browser**
4. **Go to site settings** and reset permissions
5. **Reload the AI Assistant page**
6. **Allow microphone** when prompted
7. **Try voice button again**

---

## ✅ Verification Checklist

Before reporting issues, verify:

- [ ] Using Chrome, Edge, or Safari
- [ ] Site is HTTPS or localhost
- [ ] Microphone permission granted in browser
- [ ] Microphone permission granted in system settings
- [ ] Microphone works in other apps
- [ ] No other app is using microphone
- [ ] Internet connection is stable
- [ ] Page has been refreshed after granting permissions

---

## 🆘 Still Not Working?

### Fallback Options:

1. **Use text input** - Type your questions instead
2. **Use quick question buttons** - Pre-written questions
3. **Use speaker button** - Get voice responses even without voice input

### Report Issue:

If voice still doesn't work after trying all solutions:
1. Note your browser and version
2. Note your operating system
3. Note the exact error message
4. Check browser console for errors
5. Contact support with this information

---

## 📊 Technical Details

### What Changed in the Fix:

```javascript
// OLD: Stopped immediately, no feedback
recognition.continuous = false;
recognition.interimResults = false;

// NEW: Shows interim results, better feedback
recognition.continuous = false;
recognition.interimResults = true; // ✅ Shows real-time transcription
recognition.maxAlternatives = 1;

// NEW: Better error handling
recognition.onerror = function(event) {
    // Shows specific error messages
    // Provides actionable solutions
};

// NEW: Visual feedback
recognition.onstart = function() {
    // Shows "Listening..." indicator
    // Changes button color
    // Updates placeholder text
};
```

### Browser Requirements:

- **Web Speech API** support required
- **HTTPS** or localhost required
- **Microphone access** required
- **Internet connection** required (uses cloud speech recognition)

---

## 🎉 Success Indicators

You'll know it's working when:

1. ✅ Button turns **red** when clicked
2. ✅ Shows **"Listening..."** text
3. ✅ Input field shows **"🎤 Listening... Speak now!"**
4. ✅ Your speech appears **in real-time** in the input field
5. ✅ Button returns to **normal** after speaking
6. ✅ Message is **ready to send** or auto-sends

---

**Last Updated:** May 8, 2026
**Status:** Voice recognition improved with better error handling and user feedback