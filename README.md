# HSK Multi-Level Daily Review Web Application 🇨🇳
### HSK 1, HSK 2 & HSK 3 · Optimized for iPhone & iPad · PythonAnywhere Deployment
Based on the FLTRP 《新HSK教程》 (Levels 1, 2, and 3 - 2024 Edition).

---

## 🌟 Overview & Key Features

This web application is designed specifically for **daily 10-15 minute review sessions** on iPhone, iPad, or desktop. It supports **HSK 1, HSK 2, and HSK 3** (48 chapters total, 510 vocabulary words, 103 authentic dialogue sentences, and 66 structured grammar summary guides).

### 🎯 1. Multi-Level Support (HSK 1, 2, 3) & Chapter Scoping
- **Level Switcher**: Switch between **ทั้งหมด (All Levels)**, **เล่ม 1 (HSK 1)**, **เล่ม 2 (HSK 2)**, or **เล่ม 3 (HSK 3)** with an iOS-style segmented control.
- **Flexible Scope**: Practice all chapters, specific chapter clusters (e.g. Lessons 1-3, 4-6, etc.), or custom pick chapters.
- **One-Click Lesson Practice**: Practice any specific chapter directly from the Lessons tab.

### 📖 2. Dedicated "สรุปไวยากรณ์ (Grammar Guide)" Menu
- **Pure Reading Reference**: Designed for relaxed study without quiz pressure ("ไม่ต้องทบทวนละอ่านเฉยๆ").
- **Clear Structure Formula**: Formula boxes (e.g. `主语 + 是 + [时间/地点/方式] + 动词 + 的`, `把字句`, `趋向补语`).
- **Comprehensive Thai Explanations**: Detailed, step-by-step Thai explanations.
- **Authentic Example Sentences**: Hanzi, Pinyin, and Thai translations with one-click **🔊 Native TTS audio playback**.
- **Real-Time Search**: Search grammar points across Chinese and Thai.

### 🧠 3. Multi-Phase Active Recall & Sentence Cloze
- **Character Recognition First**: Pinyin is hidden by default with 1-tap reveal.
- **Sentence Cloze Drill**: Key target words and grammar points are blanked out (`[ ___ ]`) to practice recalling words in authentic dialogue contexts.
- **Spaced Repetition (SM-2)**: Smart intervals (`Again`, `Hard`, `Good`, `Easy`) and streak tracker.

### 🇹🇭 4. Full Bilingual Thai / English Support
- Instant toggle between **🇹🇭 ภาษาไทย** and **🇬🇧 English**.
- Thai vocabulary definitions, Thai example sentences, and Thai grammar explanations.
- 4-way search dictionary: Chinese (Hanzi), Pinyin, Thai, or English.

### 📱 5. iPhone & iPad Native Experience
- Apple iOS card ergonomics, safe-area insets, dark/light mode.
- Native `zh-CN` Web Speech API synthesis for clear offline-capable audio.
- Home screen web app (PWA) ready.

---

## 🚀 How to Run Locally

```powershell
python app.py
```
Open your browser at `http://localhost:5000`.

---

## ☁️ Deployment

### Live App:
👉 **https://pakongkup.pythonanywhere.com**

### Automated Deployment via PythonAnywhere API:
```powershell
python deploy_to_pythonanywhere.py --username pakongkup --token YOUR_API_TOKEN
```

### Or via Git in PythonAnywhere Console:
```bash
cd ~/HSK-review
git pull origin main
touch /var/www/pakongkup_pythonanywhere_com_wsgi.py
```
