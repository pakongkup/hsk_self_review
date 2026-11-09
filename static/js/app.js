// HSK Daily Review Web Application JS - Multi-Level (HSK 1, 2, 3) + Grammar Guide
(function() {
  'use strict';

  // UI Translations
  const I18N = {
    th: {
      appSubtitle: '《新HSK教程》 เล่ม 1, 2, 3 ทบทวนวันละ 10-15 นาที',
      langBtn: '🇹🇭 ภาษาไทย',
      streakUnit: 'วัน',
      lvlAll: 'ทั้งหมด',
      lvl1: 'เล่ม 1 (HSK 1)',
      lvl2: 'เล่ม 2 (HSK 2)',
      lvl3: 'เล่ม 3 (HSK 3)',
      cfgTitle: 'ทบทวนประจำวัน 10-15 นาที',
      cfgSubtitle: 'ระบบดึงความจำแบบ Active Recall ผสาน Spaced Repetition ครอบคลุมคำศัพท์และประโยคสนทนาจริงจากบทเรียน',
      lblScope: '1. เลือกบทเรียน / ขอบเขต',
      scopeAll: (n) => `ทุกบท (${n} บท)`,
      scopeCustom: 'เลือกเอง...',
      selectAll: 'เลือกทั้งหมด',
      clearAll: 'ล้างทั้งหมด',
      lblMaterial: '2. รูปแบบเนื้อหาที่จะทบทวน',
      modeMixedTitle: '🔀 สลับคำศัพท์ & ประโยคบทสนทนา',
      modeMixedDesc: 'แนะนำสำหรับ 10-15 นาที: ฝึกจำศัพท์พร้อมเติมคำในประโยคจริง',
      modeWordsTitle: '📝 คำศัพท์อย่างเดียว',
      modeWordsDesc: 'เน้นจำตัวอักษรจีน พินอิน และความหมายภาษาไทย',
      modeSentTitle: '💬 ประโยคบทสนทนา (Cloze Fill-in)',
      modeSentDesc: 'ฝึกไวยากรณ์ในบริบทจริง (把字句, 趋向补语, 比较句)',
      lblLength: '3. ระยะเวลาเป้าหมาย',
      len10: '⚡ 10 นาทีแบบด่วน (~15 การ์ด)',
      len15: '🔥 15 นาทีแบบเข้มข้น (~25 การ์ด)',
      lenIntense: '🚀 ซ้อมมาราธอน (~40 การ์ด)',
      weakTitle: '⚠️ เน้นคำที่ยังจำไม่แม่น',
      weakDesc: 'สุ่มเฉพาะคำที่เคยตอบ "ทบทวนอีกครั้ง" หรือ "ยาก"',
      startBtn: '🚀 เริ่มทบทวน 10-15 นาที',
      cardWordBadge: 'คำศัพท์',
      cardSentBadge: 'ประโยค',
      lessonPrefix: 'บทที่',
      listenAudio: '🔊 ฟังเสียง',
      showPinyin: '👁️ ดูพินอิน (Pinyin)',
      hidePinyin: '🙈 ซ่อนพินอิน',
      tapHintWord: 'แตะที่การ์ดเพื่อดูคำแปลไทยและประโยคตัวอย่าง',
      tapHintSent: 'แตะที่การ์ดเพื่อดูเฉลยและไวยากรณ์',
      missingLabel: 'คำที่หายไป:',
      exContextLabel: 'ตัวอย่างในบทเรียน (Example)',
      grammarFocusLabel: 'จุดไวยากรณ์ (Grammar Focus)',
      showAnswerBtn: '🔄 ดูเฉลย / คำแปล (แตะการ์ด)',
      srsAgain: 'ทบทวนอีก',
      srsAgainSub: 'วนกลับมา',
      srsHard: 'ยาก',
      srsGood: 'พอได้',
      srsEasy: 'ง่ายมาก',
      finTitle: 'ทำรอบทบทวนประจำวันสำเร็จ!',
      finSubtitle: 'ยอดเยี่ยมมาก! การทบทวนสั้นๆ 10-15 นาทีทุกวันจะช่วยสร้างความจำระยะยาวได้ดีที่สุด',
      finCards: 'จำนวนที่ทบทวน',
      finTime: 'เวลาที่ใช้',
      finAcc: 'อัตราจำได้',
      finBreakdown: 'ผลการประเมินตนเอง',
      finEasy: 'ง่าย',
      finGood: 'พอได้',
      finHard: 'ยาก',
      finAgain: 'ทบทวนอีก',
      finStreak: (n) => `สตรีคเรียนต่อเนื่องวันที่ ${n} แล้ว! พรุ่งนี้มาทบทวนต่อนะครับ`,
      practiceWeakAgain: (n) => `🔁 ฝึกการ์ดที่ยังไม่แม่น ${n} ใบอีกครั้ง`,
      backHomeBtn: '✨ กลับหน้าหลัก / เริ่มรอบใหม่',
      chapHeading: 'บทเรียนทั้งหมด',
      chapSubheading: 'ดูเนื้อหาไวยากรณ์ คำศัพท์ และกดเริ่มฝึกรายบทได้ทันที',
      practiceLessonBtn: (lvl, n) => `🎯 ฝึกเล่ม ${lvl} บทที่ ${n} (10 นาที)`,
      grammarHeading: 'สรุปไวยากรณ์ประจำบท (อ่านทบทวน)',
      grammarSubheading: 'อ่านทำความเข้าใจโครงสร้างประโยค กฎไวยากรณ์ และประโยคตัวอย่างโดยไม่ต้องทำแบบทดสอบ',
      grammarSearchPlaceholder: 'ค้นหาไวยากรณ์ (เช่น 把字句, 是...的, 比较句)...',
      grammarFoundPrefix: 'พบทั้งหมด',
      grammarFoundSuffix: 'หัวข้อไวยากรณ์',
      structureLabel: 'โครงสร้างประโยค (Pattern)',
      explanationLabel: 'คำอธิบายการใช้งาน (Explanation)',
      examplesLabel: 'ประโยคตัวอย่าง (Examples)',
      dictHeading: 'พจนานุกรมคำศัพท์',
      dictSubheading: 'ค้นหาได้ทั้งภาษาไทย (เช่น สนามบิน, แอร์), ตัวจีน (机场), พินอิน (jīchǎng) หรือภาษาอังกฤษ',
      dictSearchPlaceholder: 'พิมพ์ค้นหาคำแปลไทย (เช่น แอร์), จีน, หรือพินอิน...',
      allLessonsOpt: 'ทุกบทเรียน',
      dictFoundPrefix: 'พบทั้งหมด',
      dictFoundSuffix: 'คำศัพท์',
      statsHeading: 'ความคืบหน้า & การตั้งค่า',
      statsSubheading: 'สถิติการจำคำศัพท์ Spaced Repetition และสตรีคประจำวัน',
      lblTotalVocab: 'คำศัพท์ทั้งหมด (HSK 1-3)',
      lblMastered: 'จำได้แม่นแล้ว (ช่วงห่าง > 3 วัน)',
      lblLearning: 'กำลังเรียนรู้ / ทบทวน',
      lblNeedsReview: 'ต้องฝึกฝนเพิ่ม',
      audioSettingsTitle: 'การออกเสียง (Audio Pronunciation)',
      lblSpeed: 'ความเร็วเสียงอ่าน:',
      audioHint: 'ใช้ระบบสังเคราะห์เสียงจีนมาตรฐาน (zh-CN) บน iOS โดยตรง ทำงานได้รวดเร็ว เสียงชัดเจน และรองรับออฟไลน์',
      aboutTitle: 'เกี่ยวกับแอปพลิเคชัน',
      aboutP1: 'ออกแบบสำหรับการทบทวนภาษาจีน HSK เล่ม 1, 2, 3 ในเวลาสั้นๆ 10-15 นาทีบน iPhone, iPad และเว็บเบราว์เซอร์',
      aboutP2: 'พร้อมสำหรับนำขึ้นรันบน PythonAnywhere',
      navReview: 'ทบทวน',
      navLessons: 'บทเรียน',
      navGrammar: 'สรุปไวยากรณ์',
      navDict: 'พจนานุกรม',
      navStats: 'สถิติ'
    },
    en: {
      appSubtitle: '《New HSK Course》 Books 1, 2, 3 Daily 10-15 Min Review',
      langBtn: '🇬🇧 English',
      streakUnit: 'Days',
      lvlAll: 'All Levels',
      lvl1: 'Book 1 (HSK 1)',
      lvl2: 'Book 2 (HSK 2)',
      lvl3: 'Book 3 (HSK 3)',
      cfgTitle: '10-15 Min Daily Review Session',
      cfgSubtitle: 'Active recall spaced repetition for HSK vocabulary and authentic sentence dialogues',
      lblScope: '1. Scope Chapters / Lessons',
      scopeAll: (n) => `All Chapters (${n} Lessons)`,
      scopeCustom: 'Custom Pick...',
      selectAll: 'Select All',
      clearAll: 'Clear All',
      lblMaterial: '2. Session Target & Material',
      modeMixedTitle: '🔀 Mixed Words & Sentences',
      modeMixedDesc: 'Best for 10-15 min: vocabulary cards + authentic dialogue cloze sentences',
      modeWordsTitle: '📝 Words Only',
      modeWordsDesc: 'Focus on character recognition, pinyin recall, and meaning',
      modeSentTitle: '💬 Sentences Only (Cloze Fill-in)',
      modeSentDesc: 'Grammar drill in real context (把字句, 趋向补语, 比较句)',
      lblLength: '3. Target Length',
      len10: '⚡ 10 Min Sprint (~15 items)',
      len15: '🔥 15 Min Deep Review (~25 items)',
      lenIntense: '🚀 Marathon (~40 items)',
      weakTitle: '⚠️ Prioritize Weak & Missed Items',
      weakDesc: 'Focus on cards you previously marked "Again" or "Hard"',
      startBtn: '🚀 Start 10-15 Min Session',
      cardWordBadge: 'Word',
      cardSentBadge: 'Sentence',
      lessonPrefix: 'Lesson',
      listenAudio: '🔊 Speak',
      showPinyin: '👁️ Reveal Pinyin',
      hidePinyin: '🙈 Hide Pinyin',
      tapHintWord: 'Tap card to see definition & context',
      tapHintSent: 'Tap card to check full sentence & grammar',
      missingLabel: 'Missing Target:',
      exContextLabel: 'Example in Context',
      grammarFocusLabel: 'Grammar Focus',
      showAnswerBtn: '🔄 Show Answer (Tap Card)',
      srsAgain: 'Again',
      srsAgainSub: 'Re-queue',
      srsHard: 'Hard',
      srsGood: 'Good',
      srsEasy: 'Easy',
      finTitle: 'Daily Session Completed!',
      finSubtitle: 'Outstanding consistency! Daily short bursts build long-term retention.',
      finCards: 'Items Reviewed',
      finTime: 'Time Spent',
      finAcc: 'Success Rate',
      finBreakdown: 'Self-Grade Breakdown',
      finEasy: 'Easy',
      finGood: 'Good',
      finHard: 'Hard',
      finAgain: 'Again',
      finStreak: (n) => `Day ${n} Streak Active! Keep it going tomorrow.`,
      practiceWeakAgain: (n) => `🔁 Practice ${n} Weak Cards Again`,
      backHomeBtn: '✨ Back to Home / New Session',
      chapHeading: 'All Chapters & Lessons',
      chapSubheading: 'Browse syllabus, grammar points, and practice any chapter directly',
      practiceLessonBtn: (lvl, n) => `🎯 Practice Book ${lvl} Lesson ${n} (10 Min)`,
      grammarHeading: 'Chapter Grammar Guide (Read-Only)',
      grammarSubheading: 'Understand patterns, syntax formulas, and authentic examples without quiz pressure',
      grammarSearchPlaceholder: 'Search grammar rules (e.g. 把, 是...的, 比较句)...',
      grammarFoundPrefix: 'Showing',
      grammarFoundSuffix: 'grammar topics',
      structureLabel: 'Sentence Pattern / Formula',
      explanationLabel: 'Detailed Explanation',
      examplesLabel: 'Example Sentences',
      dictHeading: 'HSK Vocabulary & Sentence Finder',
      dictSubheading: 'Search by Thai, Chinese (机场), Pinyin (jīchǎng), or English',
      dictSearchPlaceholder: 'Search Thai (แอร์), Hanzi, Pinyin, or English...',
      allLessonsOpt: 'All Lessons',
      dictFoundPrefix: 'Showing',
      dictFoundSuffix: 'vocabulary entries',
      statsHeading: 'Learning Progress & Settings',
      statsSubheading: 'Spaced repetition mastery stats and daily streak',
      lblTotalVocab: 'Total Vocabulary (HSK 1-3)',
      lblMastered: 'Mastered (Interval > 3d)',
      lblLearning: 'Learning / Reviewing',
      lblNeedsReview: 'Needs Practice',
      audioSettingsTitle: 'Audio Pronunciation',
      lblSpeed: 'Speech Speed:',
      audioHint: 'Uses native iOS speech synthesizer (zh-CN) for zero-latency, offline-capable clear audio',
      aboutTitle: 'About HSK Review',
      aboutP1: 'Designed for efficient 10-15 minute daily review across HSK 1, 2, and 3 on iPhone, iPad, and desktop',
      aboutP2: 'Ready and optimized for PythonAnywhere hosting',
      navReview: 'Review',
      navLessons: 'Lessons',
      navGrammar: 'Grammar',
      navDict: 'Dictionary',
      navStats: 'Progress'
    }
  };

  // State Management
  const state = {
    lang: localStorage.getItem('hsk_lang') || 'th',
    theme: localStorage.getItem('hsk_theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'),
    level: localStorage.getItem('hsk_level') || '3', // 'all', '1', '2', '3'
    speechRate: parseFloat(localStorage.getItem('hsk_speech_rate') || '0.85'),
    chapters: [],
    selectedChapters: [],
    sessionDeck: [],
    currentIndex: 0,
    isCardRevealed: false,
    isPinyinVisible: false,
    sessionStartTime: null,
    sessionTimerInterval: null,
    sessionElapsedSeconds: 0,
    gradesHistory: [],
    weakItemIds: new Set(),
    grammarList: [],
    grammarFilterChapter: 'all',
    dictChapter: 'all'
  };

  // DOM Elements
  const els = {
    // Header & Toggles
    headerSubtitle: document.getElementById('headerSubtitle'),
    langToggleBtn: document.getElementById('langToggleBtn'),
    themeToggleBtn: document.getElementById('themeToggleBtn'),
    streakCount: document.getElementById('streakCount'),
    streakUnit: document.getElementById('streakUnit'),
    levelSegmentedControl: document.getElementById('levelSegmentedControl'),
    lvlBtnAll: document.getElementById('lvlBtnAll'),
    lvlBtn1: document.getElementById('lvlBtn1'),
    lvlBtn2: document.getElementById('lvlBtn2'),
    lvlBtn3: document.getElementById('lvlBtn3'),

    // Bottom Navigation
    navItems: document.querySelectorAll('.app-bottom-nav .nav-item'),
    tabPanels: document.querySelectorAll('.tab-panel'),
    navReview: document.getElementById('navReview'),
    navLessons: document.getElementById('navLessons'),
    navGrammar: document.getElementById('navGrammar'),
    navDict: document.getElementById('navDict'),
    navStats: document.getElementById('navStats'),

    // TAB 1: Review Config
    tabReview: document.getElementById('tabReview'),
    reviewConfigView: document.getElementById('reviewConfigView'),
    reviewActiveView: document.getElementById('reviewActiveView'),
    reviewSummaryView: document.getElementById('reviewSummaryView'),
    cfgTitle: document.getElementById('cfgTitle'),
    cfgSubtitle: document.getElementById('cfgSubtitle'),
    lblScope: document.getElementById('lblScope'),
    chapterScopePills: document.getElementById('chapterScopePills'),
    customChapterSelect: document.getElementById('customChapterSelect'),
    chapterCheckboxesGrid: document.getElementById('chapterCheckboxesGrid'),
    selectAllChaptersBtn: document.getElementById('selectAllChaptersBtn'),
    clearAllChaptersBtn: document.getElementById('clearAllChaptersBtn'),
    lblMaterial: document.getElementById('lblMaterial'),
    modeMixedTitle: document.getElementById('modeMixedTitle'),
    modeMixedDesc: document.getElementById('modeMixedDesc'),
    modeWordsTitle: document.getElementById('modeWordsTitle'),
    modeWordsDesc: document.getElementById('modeWordsDesc'),
    modeSentTitle: document.getElementById('modeSentTitle'),
    modeSentDesc: document.getElementById('modeSentDesc'),
    lblLength: document.getElementById('lblLength'),
    len10Btn: document.getElementById('len10Btn'),
    len15Btn: document.getElementById('len15Btn'),
    lenIntenseBtn: document.getElementById('lenIntenseBtn'),
    weakTitle: document.getElementById('weakTitle'),
    weakDesc: document.getElementById('weakDesc'),
    onlyWeakCheck: document.getElementById('onlyWeakCheck'),
    startSessionBtn: document.getElementById('startSessionBtn'),
    startBtnText: document.getElementById('startBtnText'),

    // Review Active Flashcard
    cardCounter: document.getElementById('cardCounter'),
    sessionTimer: document.getElementById('sessionTimer'),
    sessionProgressBar: document.getElementById('sessionProgressBar'),
    quitSessionBtn: document.getElementById('quitSessionBtn'),
    flashcard: document.getElementById('flashcard'),
    cardBadge: document.getElementById('cardBadge'),
    cardChapter: document.getElementById('cardChapter'),
    ttsAudioBtn: document.getElementById('ttsAudioBtn'),
    lblAudio: document.getElementById('lblAudio'),
    hanziDisplay: document.getElementById('hanziDisplay'),
    pinyinDisplay: document.getElementById('pinyinDisplay'),
    togglePinyinBtn: document.getElementById('togglePinyinBtn'),
    pinyinBtnText: document.getElementById('pinyinBtnText'),
    clozePromptBox: document.getElementById('clozePromptBox'),
    lblMissing: document.getElementById('lblMissing'),
    clozeHintContent: document.getElementById('clozeHintContent'),
    tapHintText: document.getElementById('tapHintText'),
    cardBack: document.getElementById('cardBack'),
    posBadge: document.getElementById('posBadge'),
    thaiDefinition: document.getElementById('thaiDefinition'),
    englishDefinition: document.getElementById('englishDefinition'),
    lblExContext: document.getElementById('lblExContext'),
    exCn: document.getElementById('exCn'),
    exPy: document.getElementById('exPy'),
    exTh: document.getElementById('exTh'),
    exEn: document.getElementById('exEn'),
    grammarNoteBox: document.getElementById('grammarNoteBox'),
    lblGrammarFocus: document.getElementById('lblGrammarFocus'),
    grammarNoteContent: document.getElementById('grammarNoteContent'),
    showAnswerBtn: document.getElementById('showAnswerBtn'),
    showAnswerText: document.getElementById('showAnswerText'),
    srsRatingArea: document.getElementById('srsRatingArea'),
    srsAgainTxt: document.getElementById('srsAgainTxt'),
    srsAgainSubTxt: document.getElementById('srsAgainSubTxt'),
    srsHardTxt: document.getElementById('srsHardTxt'),
    srsGoodTxt: document.getElementById('srsGoodTxt'),
    srsEasyTxt: document.getElementById('srsEasyTxt'),

    // Review Summary
    finTitle: document.getElementById('finTitle'),
    finSubtitle: document.getElementById('finSubtitle'),
    sumCardsCount: document.getElementById('sumCardsCount'),
    finCardsLbl: document.getElementById('finCardsLbl'),
    sumTimeSpent: document.getElementById('sumTimeSpent'),
    finTimeLbl: document.getElementById('finTimeLbl'),
    sumAccuracy: document.getElementById('sumAccuracy'),
    finAccLbl: document.getElementById('finAccLbl'),
    finBreakdownLbl: document.getElementById('finBreakdownLbl'),
    finEasyLbl: document.getElementById('finEasyLbl'),
    finGoodLbl: document.getElementById('finGoodLbl'),
    finHardLbl: document.getElementById('finHardLbl'),
    finAgainLbl: document.getElementById('finAgainLbl'),
    cntEasy: document.getElementById('cntEasy'),
    cntGood: document.getElementById('cntGood'),
    cntHard: document.getElementById('cntHard'),
    cntAgain: document.getElementById('cntAgain'),
    streakAlertTitle: document.getElementById('streakAlertTitle'),
    streakAlertDesc: document.getElementById('streakAlertDesc'),
    practiceWeakBtn: document.getElementById('practiceWeakBtn'),
    practiceWeakTxt: document.getElementById('practiceWeakTxt'),
    backToHomeBtn: document.getElementById('backToHomeBtn'),
    backHomeTxt: document.getElementById('backHomeTxt'),

    // TAB 2: Chapters
    chapHeading: document.getElementById('chapHeading'),
    chapSubheading: document.getElementById('chapSubheading'),
    chaptersListContainer: document.getElementById('chaptersListContainer'),

    // TAB 3: Grammar
    grammarHeading: document.getElementById('grammarHeading'),
    grammarSubheading: document.getElementById('grammarSubheading'),
    grammarSearchInput: document.getElementById('grammarSearchInput'),
    grammarChapterSelect: document.getElementById('grammarChapterSelect'),
    grammarResultPrefix: document.getElementById('grammarResultPrefix'),
    grammarResultCount: document.getElementById('grammarResultCount'),
    grammarResultSuffix: document.getElementById('grammarResultSuffix'),
    grammarResultsList: document.getElementById('grammarResultsList'),

    // TAB 4: Dict
    dictHeading: document.getElementById('dictHeading'),
    dictSubheading: document.getElementById('dictSubheading'),
    dictSearchInput: document.getElementById('dictSearchInput'),
    dictChapterSelect: document.getElementById('dictChapterSelect'),
    dictResultPrefix: document.getElementById('dictResultPrefix'),
    dictResultCount: document.getElementById('dictResultCount'),
    dictResultSuffix: document.getElementById('dictResultSuffix'),
    dictResultsList: document.getElementById('dictResultsList'),

    // TAB 5: Stats
    statsHeading: document.getElementById('statsHeading'),
    statsSubheading: document.getElementById('statsSubheading'),
    statsTotalWords: document.getElementById('statsTotalWords'),
    lblTotalVocab: document.getElementById('lblTotalVocab'),
    statsMasteredWords: document.getElementById('statsMasteredWords'),
    lblMastered: document.getElementById('lblMastered'),
    statsReviewingWords: document.getElementById('statsReviewingWords'),
    lblLearning: document.getElementById('lblLearning'),
    statsNeedReviewWords: document.getElementById('statsNeedReviewWords'),
    lblNeedsReview: document.getElementById('lblNeedsReview'),
    audioSettingsTitle: document.getElementById('audioSettingsTitle'),
    lblSpeed: document.getElementById('lblSpeed'),
    audioHint: document.getElementById('audioHint'),
    aboutTitle: document.getElementById('aboutTitle'),
    aboutP1: document.getElementById('aboutP1'),
    aboutP2: document.getElementById('aboutP2')
  };

  // Apply Theme
  function applyTheme(theme) {
    state.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('hsk_theme', theme);
    els.themeToggleBtn.textContent = theme === 'dark' ? '☀️' : '🌙';
  }

  // Apply Language
  function applyLanguage(lang) {
    state.lang = lang;
    localStorage.setItem('hsk_lang', lang);
    const t = I18N[lang] || I18N.th;

    // Header
    els.headerSubtitle.textContent = t.appSubtitle;
    els.langToggleBtn.textContent = t.langBtn;
    els.streakUnit.textContent = t.streakUnit;

    // Level buttons
    els.lvlBtnAll.textContent = t.lvlAll;
    els.lvlBtn1.textContent = t.lvl1;
    els.lvlBtn2.textContent = t.lvl2;
    els.lvlBtn3.textContent = t.lvl3;

    // Bottom Navigation
    els.navReview.textContent = t.navReview;
    els.navLessons.textContent = t.navLessons;
    els.navGrammar.textContent = t.navGrammar;
    els.navDict.textContent = t.navDict;
    els.navStats.textContent = t.navStats;

    // Review Config View
    els.cfgTitle.textContent = t.cfgTitle;
    els.cfgSubtitle.textContent = t.cfgSubtitle;
    els.lblScope.textContent = t.lblScope;
    els.selectAllChaptersBtn.textContent = t.selectAll;
    els.clearAllChaptersBtn.textContent = t.clearAll;
    els.lblMaterial.textContent = t.lblMaterial;
    els.modeMixedTitle.textContent = t.modeMixedTitle;
    els.modeMixedDesc.textContent = t.modeMixedDesc;
    els.modeWordsTitle.textContent = t.modeWordsTitle;
    els.modeWordsDesc.textContent = t.modeWordsDesc;
    els.modeSentTitle.textContent = t.modeSentTitle;
    els.modeSentDesc.textContent = t.modeSentDesc;
    els.lblLength.textContent = t.lblLength;
    els.len10Btn.textContent = t.len10;
    els.len15Btn.textContent = t.len15;
    els.lenIntenseBtn.textContent = t.lenIntense;
    els.weakTitle.textContent = t.weakTitle;
    els.weakDesc.textContent = t.weakDesc;
    els.startBtnText.textContent = t.startBtn;

    // Flashcard Active
    els.lblAudio.textContent = t.listenAudio;
    els.pinyinBtnText.textContent = state.isPinyinVisible ? t.hidePinyin : t.showPinyin;
    els.lblMissing.textContent = t.missingLabel;
    els.lblExContext.textContent = t.exContextLabel;
    els.lblGrammarFocus.textContent = t.grammarFocusLabel;
    els.showAnswerText.textContent = t.showAnswerBtn;
    els.srsAgainTxt.textContent = t.srsAgain;
    els.srsAgainSubTxt.textContent = t.srsAgainSub;
    els.srsHardTxt.textContent = t.srsHard;
    els.srsGoodTxt.textContent = t.srsGood;
    els.srsEasyTxt.textContent = t.srsEasy;

    // Finished Summary
    els.finTitle.textContent = t.finTitle;
    els.finSubtitle.textContent = t.finSubtitle;
    els.finCardsLbl.textContent = t.finCards;
    els.finTimeLbl.textContent = t.finTime;
    els.finAccLbl.textContent = t.finAcc;
    els.finBreakdownLbl.textContent = t.finBreakdown;
    els.finEasyLbl.textContent = t.finEasy;
    els.finGoodLbl.textContent = t.finGood;
    els.finHardLbl.textContent = t.finHard;
    els.finAgainLbl.textContent = t.finAgain;
    els.backHomeTxt.textContent = t.backHomeBtn;

    // Chapters
    els.chapHeading.textContent = t.chapHeading;
    els.chapSubheading.textContent = t.chapSubheading;

    // Grammar
    els.grammarHeading.textContent = t.grammarHeading;
    els.grammarSubheading.textContent = t.grammarSubheading;
    els.grammarSearchInput.placeholder = t.grammarSearchPlaceholder;
    els.grammarResultPrefix.textContent = t.grammarFoundPrefix;
    els.grammarResultSuffix.textContent = t.grammarFoundSuffix;

    // Dictionary
    els.dictHeading.textContent = t.dictHeading;
    els.dictSubheading.textContent = t.dictSubheading;
    els.dictSearchInput.placeholder = t.dictSearchPlaceholder;
    els.dictResultPrefix.textContent = t.dictFoundPrefix;
    els.dictResultSuffix.textContent = t.dictFoundSuffix;

    // Stats
    els.statsHeading.textContent = t.statsHeading;
    els.statsSubheading.textContent = t.statsSubheading;
    els.lblTotalVocab.textContent = t.lblTotalVocab;
    els.lblMastered.textContent = t.lblMastered;
    els.lblLearning.textContent = t.lblLearning;
    els.lblNeedsReview.textContent = t.lblNeedsReview;
    els.audioSettingsTitle.textContent = t.audioSettingsTitle;
    els.lblSpeed.textContent = t.lblSpeed;
    els.audioHint.textContent = t.audioHint;
    els.aboutTitle.textContent = t.aboutTitle;
    els.aboutP1.textContent = t.aboutP1;
    els.aboutP2.textContent = t.aboutP2;

    // Re-render dynamic components
    rebuildScopePills();
    renderChaptersAccordion();
    renderGrammarGuide();
    searchDictionary();
  }

  // Level Management
  function setLevel(lvl) {
    state.level = lvl;
    localStorage.setItem('hsk_level', lvl);

    // Update Segmented Control Buttons
    document.querySelectorAll('.level-segment-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.level === lvl);
    });

    // Reload chapters for this level
    loadChapters().then(() => {
      rebuildScopePills();
      renderChaptersAccordion();
      loadGrammarData();
      searchDictionary();
      loadStats();
    });
  }

  // Speech Synthesizer (Native iOS zh-CN TTS)
  function speakChinese(text) {
    if (!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel(); // Stop any pending speech
    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = 'zh-CN';
    utter.rate = state.speechRate;
    window.speechSynthesis.speak(utter);
  }

  // Load Chapters
  async function loadChapters() {
    try {
      const url = state.level === 'all' ? '/api/chapters' : `/api/chapters?level=${state.level}`;
      const res = await fetch(url);
      const data = await res.json();
      state.chapters = data;

      // Update Chapter selects in Grammar & Dictionary
      updateChapterDropdowns();
      // Update custom checkboxes grid
      renderCustomChapterCheckboxes();
    } catch (err) {
      console.error('Failed to load chapters:', err);
    }
  }

  function updateChapterDropdowns() {
    const t = I18N[state.lang] || I18N.th;
    const defaultOpt = `<option value="all">${t.allLessonsOpt}</option>`;

    let optionsHtml = defaultOpt;
    state.chapters.forEach(ch => {
      const title = state.lang === 'th' ? ch.title_th : ch.title_en;
      optionsHtml += `<option value="${ch.chapter_num}">HSK ${ch.level} · บทที่ ${ch.chapter_num}: ${ch.title_cn} (${title})</option>`;
    });

    els.grammarChapterSelect.innerHTML = optionsHtml;
    els.dictChapterSelect.innerHTML = optionsHtml;
  }

  function renderCustomChapterCheckboxes() {
    els.chapterCheckboxesGrid.innerHTML = state.chapters.map(ch => `
      <label class="chapter-check-item">
        <input type="checkbox" name="customChapter" value="${ch.id}" checked>
        <span class="chapter-check-label">
          <strong class="level-tag">L${ch.level}·B${ch.chapter_num}</strong>
          <span class="chapter-cn">${ch.title_cn}</span>
        </span>
      </label>
    `).join('');
  }

  // Build Scope Pills based on level
  function rebuildScopePills() {
    const t = I18N[state.lang] || I18N.th;
    const container = els.chapterScopePills;
    const total = state.chapters.length;

    let pillsHtml = `
      <button type="button" class="scope-pill active" data-scope="all">${t.scopeAll(total)}</button>
    `;

    if (state.level === '1' || state.level === '2') {
      pillsHtml += `
        <button type="button" class="scope-pill" data-scope="1-3">บทที่ 1-3</button>
        <button type="button" class="scope-pill" data-scope="4-6">บทที่ 4-6</button>
        <button type="button" class="scope-pill" data-scope="7-9">บทที่ 7-9</button>
        <button type="button" class="scope-pill" data-scope="10-12">บทที่ 10-12</button>
        <button type="button" class="scope-pill" data-scope="13-15">บทที่ 13-15</button>
      `;
    } else if (state.level === '3') {
      pillsHtml += `
        <button type="button" class="scope-pill" data-scope="1-3">บทที่ 1-3</button>
        <button type="button" class="scope-pill" data-scope="4-6">บทที่ 4-6</button>
        <button type="button" class="scope-pill" data-scope="7-9">บทที่ 7-9</button>
        <button type="button" class="scope-pill" data-scope="10-12">บทที่ 10-12</button>
        <button type="button" class="scope-pill" data-scope="13-15">บทที่ 13-15</button>
        <button type="button" class="scope-pill" data-scope="16-18">บทที่ 16-18</button>
      `;
    } else {
      pillsHtml += `
        <button type="button" class="scope-pill" data-scope="lvl1">เล่ม 1 (HSK 1)</button>
        <button type="button" class="scope-pill" data-scope="lvl2">เล่ม 2 (HSK 2)</button>
        <button type="button" class="scope-pill" data-scope="lvl3">เล่ม 3 (HSK 3)</button>
      `;
    }

    pillsHtml += `
      <button type="button" class="scope-pill" id="customScopeBtn">${t.scopeCustom}</button>
    `;

    container.innerHTML = pillsHtml;

    // Bind scope pill click
    container.querySelectorAll('.scope-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        container.querySelectorAll('.scope-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        if (btn.id === 'customScopeBtn') {
          els.customChapterSelect.classList.remove('hidden');
        } else {
          els.customChapterSelect.classList.add('hidden');
        }
      });
    });
  }

  // Tab Switching
  function switchTab(tabId) {
    els.navItems.forEach(item => {
      item.classList.toggle('active', item.dataset.tab === tabId);
    });

    els.tabPanels.forEach(panel => {
      panel.classList.toggle('active', panel.id === tabId);
    });

    // Trigger tab specific loads
    if (tabId === 'tabGrammar') {
      loadGrammarData();
    } else if (tabId === 'tabDict') {
      searchDictionary();
    } else if (tabId === 'tabStats') {
      loadStats();
    }
  }

  // Review Session Logic
  async function startSession(explicitChapters = null) {
    const sessionType = document.querySelector('input[name="sessionType"]:checked').value;
    const countBtn = document.querySelector('.duration-pill.active');
    const targetCount = countBtn ? parseInt(countBtn.dataset.count) : 25;
    const onlyWeak = els.onlyWeakCheck.checked;

    let chaptersParam = 'all';

    if (explicitChapters) {
      chaptersParam = explicitChapters.join(',');
    } else {
      const activeScopeBtn = document.querySelector('.scope-pill.active');
      const scope = activeScopeBtn ? activeScopeBtn.dataset.scope : 'all';

      if (scope === 'all') {
        chaptersParam = 'all';
      } else if (scope === 'lvl1') {
        // Handled via level param
      } else if (activeScopeBtn.id === 'customScopeBtn') {
        const checked = Array.from(document.querySelectorAll('input[name="customChapter"]:checked')).map(cb => cb.value);
        if (checked.length === 0) {
          alert(state.lang === 'th' ? 'กรุณาเลือกบทเรียนอย่างน้อย 1 บทครับ' : 'Please select at least 1 lesson');
          return;
        }
        chaptersParam = checked.join(',');
      } else if (scope && scope.includes('-')) {
        const [start, end] = scope.split('-').map(Number);
        const range = [];
        for (let i = start; i <= end; i++) range.push(i);
        chaptersParam = range.join(',');
      }
    }

    try {
      let url = `/api/session?level=${state.level}&chapters=${chaptersParam}&type=${sessionType}&count=${targetCount}`;
      if (onlyWeak) url += '&only_weak=1';

      const res = await fetch(url);
      const data = await res.json();

      if (!data.items || data.items.length === 0) {
        alert(state.lang === 'th' ? 'ไม่พบการ์ดคำศัพท์ในเงื่อนไขที่เลือก กรุณาเลือกบทเรียนใหม่ครับ' : 'No items found matching criteria. Please adjust your scope.');
        return;
      }

      state.sessionDeck = data.items;
      state.currentIndex = 0;
      state.gradesHistory = [];
      state.isCardRevealed = false;
      state.isPinyinVisible = false;

      // Switch view
      els.reviewConfigView.classList.add('hidden');
      els.reviewSummaryView.classList.add('hidden');
      els.reviewActiveView.classList.remove('hidden');

      // Start Timer
      startTimer();
      renderCurrentCard();
    } catch (err) {
      console.error('Error starting session:', err);
      alert('Network error loading session.');
    }
  }

  function startTimer() {
    clearInterval(state.sessionTimerInterval);
    state.sessionStartTime = Date.now();
    state.sessionElapsedSeconds = 0;

    state.sessionTimerInterval = setInterval(() => {
      state.sessionElapsedSeconds = Math.floor((Date.now() - state.sessionStartTime) / 1000);
      const mins = String(Math.floor(state.sessionElapsedSeconds / 60)).padStart(2, '0');
      const secs = String(state.sessionElapsedSeconds % 60).padStart(2, '0');
      els.sessionTimer.textContent = `⏱️ ${mins}:${secs}`;
    }, 1000);
  }

  function renderCurrentCard() {
    const item = state.sessionDeck[state.currentIndex];
    const total = state.sessionDeck.length;
    const t = I18N[state.lang] || I18N.th;

    // Progress counter
    els.cardCounter.textContent = `${state.currentIndex + 1} / ${total}`;
    els.sessionProgressBar.style.width = `${((state.currentIndex + 1) / total) * 100}%`;

    // Reset card state
    state.isCardRevealed = false;
    state.isPinyinVisible = false;
    els.cardBack.classList.add('hidden');
    els.srsRatingArea.classList.add('hidden');
    els.showAnswerBtn.classList.remove('hidden');
    els.pinyinDisplay.classList.add('hidden');
    els.pinyinBtnText.textContent = t.showPinyin;

    // Meta Badge
    const isWord = item.kind === 'word';
    els.cardBadge.textContent = isWord ? t.cardWordBadge : t.cardSentBadge;
    els.cardBadge.className = isWord ? 'badge' : 'badge badge-sentence';
    els.cardChapter.textContent = `HSK ${item.level} · ${t.lessonPrefix} ${item.chapter}`;

    // Front Content
    els.hanziDisplay.textContent = item.hanzi;
    els.pinyinDisplay.textContent = item.pinyin;
    els.tapHintText.textContent = isWord ? t.tapHintWord : t.tapHintSent;

    // Sentence Cloze Blank
    if (!isWord && item.cloze_target) {
      els.clozePromptBox.classList.remove('hidden');
      const hint = state.lang === 'th' ? (item.cloze_hint_th || item.cloze_hint_en) : item.cloze_hint_en;
      els.clozeHintContent.textContent = hint || item.cloze_target;
    } else {
      els.clozePromptBox.classList.add('hidden');
    }

    // Back Content
    els.posBadge.textContent = item.pos || (isWord ? 'word' : 'sentence');
    els.thaiDefinition.textContent = item.thai || '-';
    els.englishDefinition.textContent = item.english || '';

    // Example Box
    if (isWord && item.ex_cn) {
      els.exCn.textContent = item.ex_cn;
      els.exPy.textContent = item.ex_py || '';
      els.exTh.textContent = item.ex_th || '';
      els.exEn.textContent = item.ex_en || '';
      document.getElementById('exampleBox').classList.remove('hidden');
    } else {
      document.getElementById('exampleBox').classList.add('hidden');
    }

    // Grammar Note
    if (!isWord && (item.grammar_th || item.grammar_en)) {
      const gNote = state.lang === 'th' ? (item.grammar_th || item.grammar_en) : (item.grammar_en || item.grammar_th);
      els.grammarNoteContent.textContent = gNote;
      els.grammarNoteBox.classList.remove('hidden');
    } else {
      els.grammarNoteBox.classList.add('hidden');
    }
  }

  function revealAnswer() {
    if (state.isCardRevealed) return;
    state.isCardRevealed = true;
    els.cardBack.classList.remove('hidden');
    els.pinyinDisplay.classList.remove('hidden');
    els.pinyinBtnText.textContent = (I18N[state.lang] || I18N.th).hidePinyin;
    els.showAnswerBtn.classList.add('hidden');
    els.srsRatingArea.classList.remove('hidden');

    // Auto-play audio upon reveal for maximum audio reinforcement
    const item = state.sessionDeck[state.currentIndex];
    if (item && item.hanzi) {
      speakChinese(item.hanzi);
    }
  }

  async function handleGrade(grade) {
    const item = state.sessionDeck[state.currentIndex];
    state.gradesHistory.push({ item, grade });

    if (grade <= 2) {
      state.weakItemIds.add(item.id);
    }

    // Send review record to backend
    try {
      fetch('/api/review', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          item_type: item.kind,
          item_id: item.id,
          grade: grade,
          seconds_spent: 5
        })
      });
    } catch (e) {
      // offline fallback
    }

    // Move to next card or complete
    state.currentIndex++;
    if (state.currentIndex < state.sessionDeck.length) {
      renderCurrentCard();
    } else {
      finishSession();
    }
  }

  function finishSession() {
    clearInterval(state.sessionTimerInterval);

    els.reviewActiveView.classList.add('hidden');
    els.reviewSummaryView.classList.remove('hidden');

    const total = state.gradesHistory.length;
    const mins = Math.floor(state.sessionElapsedSeconds / 60);
    const secs = state.sessionElapsedSeconds % 60;
    const timeFormatted = `${mins}m ${secs}s`;

    let easyCount = 0, goodCount = 0, hardCount = 0, againCount = 0;
    state.gradesHistory.forEach(g => {
      if (g.grade === 4) easyCount++;
      else if (g.grade === 3) goodCount++;
      else if (g.grade === 2) hardCount++;
      else if (g.grade === 1) againCount++;
    });

    const accuracy = total > 0 ? Math.round(((goodCount + easyCount) / total) * 100) : 100;

    els.sumCardsCount.textContent = total;
    els.sumTimeSpent.textContent = timeFormatted;
    els.sumAccuracy.textContent = `${accuracy}%`;

    els.cntEasy.textContent = easyCount;
    els.cntGood.textContent = goodCount;
    els.cntHard.textContent = hardCount;
    els.cntAgain.textContent = againCount;

    // Refresh streak and stats
    loadStats();
  }

  // Chapters Tab Accordion Rendering
  function renderChaptersAccordion() {
    const container = els.chaptersListContainer;
    const t = I18N[state.lang] || I18N.th;

    if (!state.chapters || state.chapters.length === 0) {
      container.innerHTML = `<p class="empty-hint">${state.lang === 'th' ? 'ไม่พบข้อมูลบทเรียน' : 'No chapters available'}</p>`;
      return;
    }

    container.innerHTML = state.chapters.map(ch => {
      const title = state.lang === 'th' ? ch.title_th : ch.title_en;
      const topic = state.lang === 'th' ? ch.topic_th : ch.topic_en;
      const grammars = state.lang === 'th' ? ch.grammar_th : ch.grammar_en;

      return `
        <div class="chapter-card">
          <div class="chapter-card-header">
            <span class="level-badge lvl-${ch.level}">HSK ${ch.level}</span>
            <span class="chapter-card-num">${t.lessonPrefix} ${ch.chapter_num}</span>
          </div>
          <h3 class="chapter-card-title-cn">${ch.title_cn}</h3>
          <p class="chapter-card-pinyin">${ch.title_pinyin}</p>
          <p class="chapter-card-title-trans">${title}</p>
          ${topic ? `<div class="chapter-card-topic">🏷️ ${topic}</div>` : ''}

          ${grammars && grammars.length ? `
            <div class="chapter-card-grammar">
              <strong>${t.grammarFocusLabel}:</strong>
              <ul>
                ${grammars.map(g => `<li>${g}</li>`).join('')}
              </ul>
            </div>
          ` : ''}

          <div class="chapter-card-footer">
            <button class="btn btn-sm btn-primary practice-ch-btn" data-chapter="${ch.id}" data-level="${ch.level}" data-num="${ch.chapter_num}">
              ${t.practiceLessonBtn(ch.level, ch.chapter_num)}
            </button>
          </div>
        </div>
      `;
    }).join('');

    // Attach click to practice button
    container.querySelectorAll('.practice-ch-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const chId = btn.dataset.chapter;
        switchTab('tabReview');
        startSession([chId]);
      });
    });
  }

  // TAB 3: Grammar Guide Data Loading & Rendering
  async function loadGrammarData() {
    const query = els.grammarSearchInput.value.trim();
    const ch = els.grammarChapterSelect.value;
    const t = I18N[state.lang] || I18N.th;

    let url = `/api/grammar?level=${state.level}&chapter=${ch}`;
    if (query) url += `&q=${encodeURIComponent(query)}`;

    try {
      const res = await fetch(url);
      const points = await res.json();
      state.grammarList = points;
      renderGrammarGuide();
    } catch (err) {
      console.error('Failed to load grammar guide:', err);
    }
  }

  function renderGrammarGuide() {
    const container = els.grammarResultsList;
    const t = I18N[state.lang] || I18N.th;
    const list = state.grammarList;

    els.grammarResultCount.textContent = list.length;

    if (!list || list.length === 0) {
      container.innerHTML = `<p class="empty-hint">${state.lang === 'th' ? 'ไม่พบหัวข้อไวยากรณ์ตามเงื่อนไขที่ค้นหา' : 'No grammar topics matched your query'}</p>`;
      return;
    }

    container.innerHTML = list.map(gp => {
      const titleTh = gp.title_th;
      const explanation = gp.explanation_th;
      const examples = gp.examples || [];

      return `
        <div class="grammar-card">
          <div class="grammar-card-header">
            <div class="grammar-meta">
              <span class="level-badge lvl-${gp.level}">HSK ${gp.level}</span>
              <span class="chapter-tag">${t.lessonPrefix} ${gp.chapter_num}</span>
            </div>
          </div>

          <h3 class="grammar-card-title">${gp.title_cn}</h3>
          <p class="grammar-card-title-th">${titleTh}</p>

          ${gp.structure ? `
            <div class="grammar-structure-box">
              <div class="grammar-structure-label">${t.structureLabel}</div>
              <div class="grammar-structure-text">${gp.structure}</div>
            </div>
          ` : ''}

          <div class="grammar-explanation">
            ${explanation}
          </div>

          ${examples.length ? `
            <div class="grammar-examples-box">
              <div class="grammar-examples-label">📖 ${t.examplesLabel}</div>
              ${examples.map(ex => `
                <div class="grammar-example-item">
                  <div class="example-text-group">
                    <div class="example-cn-text">${ex.cn}</div>
                    <div class="example-py-text">${ex.py}</div>
                    <div class="example-th-text">${ex.th}</div>
                  </div>
                  <button type="button" class="example-audio-btn" data-audio="${ex.cn}" title="ฟังเสียงอ่าน">
                    🔊
                  </button>
                </div>
              `).join('')}
            </div>
          ` : ''}
        </div>
      `;
    }).join('');

    // Attach TTS audio listeners to example buttons
    container.querySelectorAll('.example-audio-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const text = btn.dataset.audio;
        if (text) speakChinese(text);
      });
    });
  }

  // TAB 4: Dictionary Search
  let searchTimeout = null;
  async function searchDictionary() {
    const query = els.dictSearchInput.value.trim();
    const ch = els.dictChapterSelect.value;
    const t = I18N[state.lang] || I18N.th;

    let url = `/api/dictionary?level=${state.level}&chapter=${ch}`;
    if (query) url += `&q=${encodeURIComponent(query)}`;

    try {
      const res = await fetch(url);
      const words = await res.json();
      renderDictionaryList(words);
    } catch (err) {
      console.error('Error searching dictionary:', err);
    }
  }

  function renderDictionaryList(words) {
    const container = els.dictResultsList;
    const t = I18N[state.lang] || I18N.th;

    els.dictResultCount.textContent = words.length;

    if (!words || words.length === 0) {
      container.innerHTML = `<p class="empty-hint">${state.lang === 'th' ? 'ไม่พบคำศัพท์ที่ตรงกับการค้นหา' : 'No words found'}</p>`;
      return;
    }

    container.innerHTML = words.map(w => `
      <div class="dict-card">
        <div class="dict-card-left">
          <div class="dict-hanzi-row">
            <span class="level-badge lvl-${w.level}">L${w.level}</span>
            <span class="dict-hanzi">${w.hanzi}</span>
            <span class="dict-pinyin">${w.pinyin}</span>
            <button type="button" class="audio-mini-btn" data-audio="${w.hanzi}">🔊</button>
          </div>
          <div class="dict-meaning-th">${w.thai || '-'}</div>
          <div class="dict-meaning-en">${w.english || ''}</div>
          ${w.ex_cn ? `
            <div class="dict-example">
              <span class="ex-cn">${w.ex_cn}</span>
              <span class="ex-th">${w.ex_th || ''}</span>
            </div>
          ` : ''}
        </div>
        <div class="dict-card-right">
          <span class="dict-pos">${w.pos || 'w'}</span>
          <span class="dict-chapter">${t.lessonPrefix} ${w.chapter}</span>
        </div>
      </div>
    `).join('');

    container.querySelectorAll('.audio-mini-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        speakChinese(btn.dataset.audio);
      });
    });
  }

  // TAB 5: Stats Loading
  async function loadStats() {
    try {
      const res = await fetch('/api/stats');
      const data = await res.json();

      els.statsTotalWords.textContent = data.total_words;
      els.statsMasteredWords.textContent = data.mastered_words;
      els.statsReviewingWords.textContent = data.reviewed_words - data.mastered_words;
      els.statsNeedReviewWords.textContent = data.need_review_words;

      els.streakCount.textContent = data.current_streak;
      els.streakAlertTitle.textContent = (I18N[state.lang] || I18N.th).finStreak(data.current_streak);
    } catch (err) {
      console.error('Error loading stats:', err);
    }
  }

  // Event Listeners Binding
  function bindEvents() {
    // Theme toggle
    els.themeToggleBtn.addEventListener('click', () => {
      applyTheme(state.theme === 'dark' ? 'light' : 'dark');
    });

    // Language toggle
    els.langToggleBtn.addEventListener('click', () => {
      applyLanguage(state.lang === 'th' ? 'en' : 'th');
    });

    // Level selector segmented control
    document.querySelectorAll('.level-segment-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        setLevel(btn.dataset.level);
      });
    });

    // Bottom nav tabs
    els.navItems.forEach(item => {
      item.addEventListener('click', () => {
        switchTab(item.dataset.tab);
      });
    });

    // Session duration pills
    document.querySelectorAll('.duration-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.duration-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      });
    });

    // Start Session Button
    els.startSessionBtn.addEventListener('click', () => {
      startSession();
    });

    // Card Reveal on Tap
    els.flashcard.addEventListener('click', (e) => {
      if (e.target.closest('#ttsAudioBtn') || e.target.closest('#togglePinyinBtn')) return;
      revealAnswer();
    });

    els.showAnswerBtn.addEventListener('click', () => {
      revealAnswer();
    });

    // Audio TTS Button
    els.ttsAudioBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const item = state.sessionDeck[state.currentIndex];
      if (item) speakChinese(item.hanzi);
    });

    // Toggle Pinyin
    els.togglePinyinBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      state.isPinyinVisible = !state.isPinyinVisible;
      els.pinyinDisplay.classList.toggle('hidden', !state.isPinyinVisible);
      const t = I18N[state.lang] || I18N.th;
      els.pinyinBtnText.textContent = state.isPinyinVisible ? t.hidePinyin : t.showPinyin;
    });

    // SRS Ratings
    document.querySelectorAll('.srs-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const grade = parseInt(btn.dataset.grade);
        handleGrade(grade);
      });
    });

    // Quit session
    els.quitSessionBtn.addEventListener('click', () => {
      if (confirm(state.lang === 'th' ? 'คุณต้องการออกจากการทบทวนรอบนี้ใช่หรือไม่?' : 'Do you want to quit this session?')) {
        clearInterval(state.sessionTimerInterval);
        els.reviewActiveView.classList.add('hidden');
        els.reviewConfigView.classList.remove('hidden');
      }
    });

    // Back to home from summary
    els.backToHomeBtn.addEventListener('click', () => {
      els.reviewSummaryView.classList.add('hidden');
      els.reviewConfigView.classList.remove('hidden');
    });

    // Grammar Search Input
    els.grammarSearchInput.addEventListener('input', () => {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(loadGrammarData, 250);
    });

    // Grammar Chapter Select
    els.grammarChapterSelect.addEventListener('change', () => {
      loadGrammarData();
    });

    // Dict Search Input
    els.dictSearchInput.addEventListener('input', () => {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(searchDictionary, 250);
    });

    // Dict Chapter Select
    els.dictChapterSelect.addEventListener('change', () => {
      searchDictionary();
    });

    // Speed toggle
    document.querySelectorAll('.speed-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.speed-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.speechRate = parseFloat(btn.dataset.rate);
        localStorage.setItem('hsk_speech_rate', state.speechRate);
      });
    });

    // Select/Clear all custom chapters
    els.selectAllChaptersBtn.addEventListener('click', () => {
      document.querySelectorAll('input[name="customChapter"]').forEach(cb => cb.checked = true);
    });
    els.clearAllChaptersBtn.addEventListener('click', () => {
      document.querySelectorAll('input[name="customChapter"]').forEach(cb => cb.checked = false);
    });
  }

  // Initialization
  async function init() {
    applyTheme(state.theme);
    bindEvents();
    setLevel(state.level);
    applyLanguage(state.lang);
  }

  document.addEventListener('DOMContentLoaded', init);
})();
