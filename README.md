# HSK 3 Daily Review Web Application 🇨🇳
### Optimized for iPhone & iPad · Ready for PythonAnywhere Deployment
Based on 《新HSK教程 3级》 (*New HSK Standard Course 3 - HSK 3.0*, Foreign Language Teaching and Research Press, 2024).

---

## 🌟 Overview & Key Features

This web application is designed specifically for **daily 10-15 minute review sessions** on iPhone, iPad, or desktop. It combines evidence-based Spaced Repetition (SRS Leitner / modified SM-2) with active recall of vocabulary and authentic dialogue sentences directly from your textbook.

### 🎯 1. Designed for 10-15 Minute High-Yield Microlearning
- **Focused Sprints**: Choose a **10-minute sprint** (15 cards) or a **15-minute deep review** (25 cards).
- **Daily Countdown Timer**: Subtle visual timer keeps you focused without cognitive fatigue.
- **Adaptive Shuffle**: Randomly mixes vocabulary words with authentic contextual dialogue cloze sentences.
- **Smart Queue Re-insertion**: When you mark a card **"Again"**, the app automatically re-queues it 3 cards later so you master it within the same session.

### 📚 2. Flexible Chapter & Subject Scoping
- Scope by any chapter range:
  - **All 18 Lessons** (Comprehensive review)
  - **Clusters**: Lessons 1-3, 4-6, 7-9, 10-12, 13-15, 16-18
  - **Custom Pick**: Select individual lessons (e.g., just Lesson 6 "High-Speed Rail" or Lesson 10 "把字句")
  - **One-Click Lesson Practice**: Practice any specific chapter directly from the Lessons tab.

### 🧠 3. Multi-Phase Active Recall & Sentence Cloze
- **Character Recognition First**: Pinyin is hidden by default to train Hanzi recognition (with 1-tap reveal).
- **Sentence Cloze Drill**: For dialogue sentences, key grammar structures and HSK 3 target words are blanked out (`[ ___ ]`) so you practice recalling words in real Chinese context.
- **Authentic Context & Grammar Notes**: Every word card includes real example sentences from the textbook; every sentence card includes grammar notes (e.g., *把字句*, *趋向补语*, *不但...而且...*, *越...越...*).

### 📱 4. iPhone & iPad Native Web App Experience
- **Apple iOS Touch Ergonomics**: Native Apple design aesthetic (cards, pills, safe-area padding for notch/island).
- **Zero-Latency Native Audio**: Uses iOS Web Speech API with native `zh-CN` voice (no audio latency, works completely offline on device).
- **Adjustable Speech Rate**: Switch between `0.85x` (learner tempo) and `1.0x` (natural tempo).
- **Touch Swipe Gestures**: Swipe Left for Hard/Again, Swipe Right for Good/Easy, Tap to Flip.
- **Keyboard Shortcuts (for iPad with Magic Keyboard)**: Space to flip, `1-4` to rate, `S` to listen.
- **Dark Mode**: Automatically respects iOS system appearance or manual toggle.

---

## 🚀 How to Run Locally

1. Open PowerShell or Terminal in this folder:
   ```powershell
   cd C:\Users\pakon\OneDrive\HSK-review
   ```

2. Run the application:
   ```powershell
   python app.py
   ```

3. Open your browser at:
   ```
   http://localhost:5000
   ```
   *(To test on iPhone/iPad on your local Wi-Fi, open `http://<YOUR_PC_LOCAL_IP>:5000`)*.

---

## ☁️ How to Deploy to PythonAnywhere (Step-by-Step)

[PythonAnywhere](https://www.pythonanywhere.com/) provides a free hosting tier that runs Python/Flask with zero server configuration.

### Step 1: Sign up & Open Dashboard
1. Go to [pythonanywhere.com](https://www.pythonanywhere.com/) and register a free Beginner account (e.g. username `pakon`).
2. Your public web app URL will be `https://pakon.pythonanywhere.com`.

### Step 2: Upload Project Files
There are two easy methods:

**Method A: Using Git (Fastest)**
1. In your PythonAnywhere Dashboard, open a **Bash Console**.
2. Clone your repository or create the directory:
   ```bash
   mkdir -p ~/HSK-review
   cd ~/HSK-review
   ```
3. Upload files via Git or the PythonAnywhere **Files** tab.

**Method B: Uploading ZIP via Files Tab**
1. Zip the `HSK-review` folder on your computer.
2. In PythonAnywhere, navigate to the **Files** tab and upload `HSK-review.zip`.
3. In a Bash Console, unzip it:
   ```bash
   unzip HSK-review.zip -d ~/HSK-review
   ```

### Step 3: Install Flask
In the PythonAnywhere Bash Console, install Flask:
```bash
pip3 install --user flask
```

### Step 4: Configure the Web App
1. Go to the **Web** tab in PythonAnywhere Dashboard.
2. Click **"Add a new web app"**.
3. Select **"Manual configuration"** (or Flask) and choose **Python 3.10** (or 3.11 / 3.12).
4. In the **Code** section:
   - **Source code**: `/home/pakon/HSK-review`
   - **Working directory**: `/home/pakon/HSK-review`
5. Click on the **WSGI configuration file** link (e.g. `/var/www/pakon_pythonanywhere_com_wsgi.py`).
6. Replace the entire contents of that file with:
   ```python
   import sys
   import os

   # Path to your project directory
   project_home = '/home/pakon/HSK-review'
   if project_home not in sys.path:
       sys.path.insert(0, project_home)

   # Import the Flask application
   from app import app as application
   ```
   *(Replace `pakon` with your actual PythonAnywhere username)*.
7. Click **Save** (top right).

### Step 5: Reload & Access on iPhone / iPad!
1. Go back to the **Web** tab and click the big green **"Reload pakon.pythonanywhere.com"** button.
2. Visit `https://pakon.pythonanywhere.com` on Safari on your iPhone or iPad!
3. **Add to Home Screen**:
   - In Safari, tap the **Share** button (box with upward arrow).
   - Scroll down and tap **"Add to Home Screen"**.
   - It will now appear as a dedicated app icon on your home screen with full-screen view!

---

## 📖 Recommended 10-15 Minute Daily Study Routine

| Time | Phase | Focus |
|---|---|---|
| **00:00 - 05:00** | **Vocabulary Warmup** | 10-12 shuffled words from target lessons. Check character reading without pinyin; listen to native audio. |
| **05:00 - 12:00** | **Sentence & Cloze Practice** | 6-8 authentic sentences. Recall missing word/structure in context (*把*, *被*, *越...越...*). |
| **12:00 - 15:00** | **Weak Items Wrap-Up** | Instant 1-click review of any items marked "Again" or "Hard". Check streak counter! |

---

## 🗂️ Project Directory Structure

```
HSK-review/
├── app.py                     # Flask web server & REST API
├── wsgi.py                    # WSGI entrypoint for PythonAnywhere
├── requirements.txt           # Python dependencies (flask)
├── hsk-course-3.pdf           # Original course textbook (FLTRP)
├── data/
│   ├── hsk3.db                # SQLite database (chapters, words, sentences, SRS stats)
│   └── hsk3_database.json     # Clean JSON database of all 18 lessons
├── templates/
│   └── index.html             # Responsive iOS SPA interface
├── static/
│   ├── css/style.css          # iOS/iPad adaptive styling & dark mode
│   └── js/app.js              # SRS engine, speech audio, timer, swipe gestures
└── README.md                  # Complete documentation & deployment guide
```
