// HSK 3 Daily Review Web Application JS - Bilingual (Thai / English)
(function() {
  'use strict';

  // UI Translations
  const I18N = {
    th: {
      appSubtitle: '《新HSK教程 3级》 ทบทวนวันละ 10-15 นาที',
      langBtn: '🇹🇭 ภาษาไทย',
      streakUnit: 'วัน',
      cfgTitle: 'ทบทวนประจำวัน 10-15 นาที',
      cfgSubtitle: 'ระบบดึงความจำแบบ Active Recall ผสาน Spaced Repetition ครอบคลุมคำศัพท์และประโยคสนทนาจริงจากบทเรียน',
      lblScope: '1. เลือกบทเรียน / ขอบเขต',
      scopeAll: 'ทุกบท (1-18)',
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
      chapHeading: '《新HSK教程 3级》 ทั้ง 18 บทเรียน',
      chapSubheading: 'ดูเนื้อหาไวยากรณ์ คำศัพท์ และกดเริ่มฝึกรายบทได้ทันที',
      practiceLessonBtn: (n) => `🎯 ฝึกบทที่ ${n} (10 นาที)`,
      dictHeading: 'พจนานุกรมคำศัพท์ & ประโยค HSK 3',
      dictSubheading: 'ค้นหาได้ทั้งภาษาไทย (เช่น สนามบิน, แอร์), ตัวจีน (机场), พินอิน (jīchǎng) หรือภาษาอังกฤษ',
      dictSearchPlaceholder: 'พิมพ์ค้นหาคำแปลไทย (เช่น แอร์), จีน, หรือพินอิน...',
      allLessonsOpt: 'ทุกบทเรียน',
      dictFoundPrefix: 'พบทั้งหมด',
      dictFoundSuffix: 'คำศัพท์',
      statsHeading: 'ความคืบหน้า & การตั้งค่า',
      statsSubheading: 'สถิติการจำคำศัพท์ Spaced Repetition และสตรีคประจำวัน',
      lblTotalVocab: 'คำศัพท์ HSK 3 ทั้งหมด',
      lblMastered: 'จำได้แม่นแล้ว (ช่วงห่าง > 3 วัน)',
      lblLearning: 'กำลังเรียนรู้ / ทบทวน',
      lblNeedsReview: 'ต้องฝึกฝนเพิ่ม',
      audioSettingsTitle: 'การออกเสียง (Audio Pronunciation)',
      lblSpeed: 'ความเร็วเสียงอ่าน:',
      audioHint: 'ใช้ระบบสังเคราะห์เสียงจีนมาตรฐาน (zh-CN) บน iOS โดยตรง ทำงานได้รวดเร็ว เสียงชัดเจน และรองรับออฟไลน์',
      aboutTitle: 'เกี่ยวกับแอปพลิเคชัน',
      aboutP1: 'ออกแบบสำหรับการทบทวนภาษาจีน HSK 3 ในเวลาสั้นๆ 10-15 นาทีบน iPhone, iPad และเว็บเบราว์เซอร์',
      aboutP2: 'พร้อมสำหรับนำขึ้นรันบน PythonAnywhere',
      navReview: 'ทบทวน',
      navLessons: 'บทเรียน',
      navDict: 'พจนานุกรม',
      navStats: 'สถิติ'
    },
    en: {
      appSubtitle: '《New HSK Course 3》 10-15 Min Daily Review',
      langBtn: '🇬🇧 English',
      streakUnit: 'Days',
      cfgTitle: '10-15 Min Daily Review Session',
      cfgSubtitle: 'Active recall spaced repetition for HSK 3.0 vocabulary and authentic sentence dialogues',
      lblScope: '1. Scope Chapters / Lessons',
      scopeAll: 'All Lessons (1-18)',
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
      chapHeading: '《New HSK Course 3》 18 Lessons',
      chapSubheading: 'Browse syllabus, grammar points, and practice any chapter directly',
      practiceLessonBtn: (n) => `🎯 Practice Lesson ${n} (10 Min)`,
      dictHeading: 'HSK 3 Vocabulary & Sentence Finder',
      dictSubheading: 'Search by Thai, Chinese (机场), Pinyin (jīchǎng), or English',
      dictSearchPlaceholder: 'Search Thai (แอร์), Hanzi, Pinyin, or English...',
      allLessonsOpt: 'All Lessons',
      dictFoundPrefix: 'Showing',
      dictFoundSuffix: 'vocabulary entries',
      statsHeading: 'Learning Progress & Settings',
      statsSubheading: 'Spaced repetition mastery stats and daily streak',
      lblTotalVocab: 'Total HSK 3 Words',
      lblMastered: 'Mastered (Interval > 3d)',
      lblLearning: 'Learning / Reviewing',
      lblNeedsReview: 'Needs Practice',
      audioSettingsTitle: 'Audio Pronunciation',
      lblSpeed: 'Speech Speed:',
      audioHint: 'Uses native iOS speech synthesizer (zh-CN) for zero-latency, offline-capable clear audio',
      aboutTitle: 'About This Application',
      aboutP1: 'Designed for 10-15 minute daily review on iPhone, iPad, and desktop web browsers',
      aboutP2: 'Ready for 1-click deployment on PythonAnywhere',
      navReview: 'Review',
      navLessons: 'Lessons',
      navDict: 'Dictionary',
      navStats: 'Progress'
    }
  };

  // State
  const state = {
    lang: localStorage.getItem('hsk3_lang') || 'th', // Default to Thai
    chapters: [],
    deck: [],
    currentIndex: 0,
    currentCard: null,
    isFlipped: false,
    timerInterval: null,
    timeRemainingSec: 600,
    timeSpentSec: 0,
    sessionStats: {
      total: 0,
      again: 0,
      hard: 0,
      good: 0,
      easy: 0,
      weakCards: []
    },
    audioRate: 0.85,
    selectedScope: 'all',
    selectedCustomChapters: new Set(),
    activeTab: 'tabReview'
  };

  // DOM Elements
  const el = {
    langToggleBtn: document.getElementById('langToggleBtn'),
    headerSubtitle: document.getElementById('headerSubtitle'),
    themeToggleBtn: document.getElementById('themeToggleBtn'),
    streakCount: document.getElementById('streakCount'),
    streakUnit: document.getElementById('streakUnit'),
    navItems: document.querySelectorAll('.nav-item'),
    tabPanels: document.querySelectorAll('.tab-panel'),

    // Nav Labels
    navReview: document.getElementById('navReview'),
    navLessons: document.getElementById('navLessons'),
    navDict: document.getElementById('navDict'),
    navStats: document.getElementById('navStats'),

    // Review Config View
    reviewConfigView: document.getElementById('reviewConfigView'),
    cfgTitle: document.getElementById('cfgTitle'),
    cfgSubtitle: document.getElementById('cfgSubtitle'),
    lblScope: document.getElementById('lblScope'),
    scopePills: document.querySelectorAll('.scope-pill'),
    customScopeBtn: document.getElementById('customScopeBtn'),
    customChapterSelect: document.getElementById('customChapterSelect'),
    chapterCheckboxesGrid: document.getElementById('chapterCheckboxesGrid'),
    selectAllChaptersBtn: document.getElementById('selectAllChaptersBtn'),
    clearAllChaptersBtn: document.getElementById('clearAllChaptersBtn'),
    lblMaterial: document.getElementById('lblMaterial'),
    modeCards: document.querySelectorAll('.mode-card'),
    modeMixedTitle: document.getElementById('modeMixedTitle'),
    modeMixedDesc: document.getElementById('modeMixedDesc'),
    modeWordsTitle: document.getElementById('modeWordsTitle'),
    modeWordsDesc: document.getElementById('modeWordsDesc'),
    modeSentTitle: document.getElementById('modeSentTitle'),
    modeSentDesc: document.getElementById('modeSentDesc'),
    lblLength: document.getElementById('lblLength'),
    len10Text: document.getElementById('len10Text'),
    len15Text: document.getElementById('len15Text'),
    lenIntenseText: document.getElementById('lenIntenseText'),
    lengthPills: document.querySelectorAll('.length-pill'),
    weakTitle: document.getElementById('weakTitle'),
    weakDesc: document.getElementById('weakDesc'),
    onlyWeakToggle: document.getElementById('onlyWeakToggle'),
    startSessionBtn: document.getElementById('startSessionBtn'),

    // Active Study View
    reviewActiveView: document.getElementById('reviewActiveView'),
    exitSessionBtn: document.getElementById('exitSessionBtn'),
    sessionProgressText: document.getElementById('sessionProgressText'),
    sessionTimerText: document.getElementById('sessionTimerText'),
    sessionProgressBar: document.getElementById('sessionProgressBar'),
    audioSpeechBtn: document.getElementById('audioSpeechBtn'),
    flashcard: document.getElementById('flashcard'),
    cardBadgeKind: document.getElementById('cardBadgeKind'),
    cardBadgeChapter: document.getElementById('cardBadgeChapter'),
    frontAudioBtn: document.getElementById('frontAudioBtn'),
    togglePinyinBtn: document.getElementById('togglePinyinBtn'),
    tapHintWord: document.getElementById('tapHintWord'),
    tapHintSent: document.getElementById('tapHintSent'),

    // Word Front/Back
    wordFrontContent: document.getElementById('wordFrontContent'),
    cardHanzi: document.getElementById('cardHanzi'),
    cardPinyin: document.getElementById('cardPinyin'),
    wordBackContent: document.getElementById('wordBackContent'),
    cardBackHanzi: document.getElementById('cardBackHanzi'),
    cardBackPinyin: document.getElementById('cardBackPinyin'),
    cardBackThai: document.getElementById('cardBackThai'),
    cardBackEnglish: document.getElementById('cardBackEnglish'),
    lblExContext: document.getElementById('lblExContext'),
    cardBackExCn: document.getElementById('cardBackExCn'),
    cardBackExPy: document.getElementById('cardBackExPy'),
    cardBackExTh: document.getElementById('cardBackExTh'),
    cardBackExEn: document.getElementById('cardBackExEn'),
    exampleAudioBtn: document.getElementById('exampleAudioBtn'),

    // Sentence Front/Back
    sentenceFrontContent: document.getElementById('sentenceFrontContent'),
    cardSentenceContext: document.getElementById('cardSentenceContext'),
    cardSentenceHanzi: document.getElementById('cardSentenceHanzi'),
    cardClozeBox: document.getElementById('cardClozeBox'),
    lblMissing: document.getElementById('lblMissing'),
    cardClozeHint: document.getElementById('cardClozeHint'),
    sentenceBackContent: document.getElementById('sentenceBackContent'),
    cardBackSentHanzi: document.getElementById('cardBackSentHanzi'),
    cardBackSentPinyin: document.getElementById('cardBackSentPinyin'),
    cardBackSentThai: document.getElementById('cardBackSentThai'),
    cardBackSentEnglish: document.getElementById('cardBackSentEnglish'),
    lblGrammarFocus: document.getElementById('lblGrammarFocus'),
    cardBackGrammar: document.getElementById('cardBackGrammar'),

    backBadgeKind: document.getElementById('backBadgeKind'),
    backBadgePos: document.getElementById('backBadgePos'),
    backAudioBtn: document.getElementById('backAudioBtn'),
    flipCardBtn: document.getElementById('flipCardBtn'),
    srsButtonGroup: document.getElementById('srsButtonGroup'),
    srsButtons: document.querySelectorAll('.btn-srs'),
    srsLblAgain: document.getElementById('srsLblAgain'),
    srsSubAgain: document.getElementById('srsSubAgain'),
    srsLblHard: document.getElementById('srsLblHard'),
    srsLblGood: document.getElementById('srsLblGood'),
    srsLblEasy: document.getElementById('srsLblEasy'),

    // Finished View
    reviewFinishedView: document.getElementById('reviewFinishedView'),
    finTitle: document.getElementById('finTitle'),
    finSubtitle: document.getElementById('finSubtitle'),
    summaryTotalCards: document.getElementById('summaryTotalCards'),
    summaryTimeSpent: document.getElementById('summaryTimeSpent'),
    summaryAccuracy: document.getElementById('summaryAccuracy'),
    lblSummaryCards: document.getElementById('lblSummaryCards'),
    lblSummaryTime: document.getElementById('lblSummaryTime'),
    lblSummaryAcc: document.getElementById('lblSummaryAcc'),
    lblBreakdown: document.getElementById('lblBreakdown'),
    txtFinEasy: document.getElementById('txtFinEasy'),
    txtFinGood: document.getElementById('txtFinGood'),
    txtFinHard: document.getElementById('txtFinHard'),
    txtFinAgain: document.getElementById('txtFinAgain'),
    countEasy: document.getElementById('countEasy'),
    countGood: document.getElementById('countGood'),
    countHard: document.getElementById('countHard'),
    countAgain: document.getElementById('countAgain'),
    awardStreakText: document.getElementById('awardStreakText'),
    reviewAgainWeakBtn: document.getElementById('reviewAgainWeakBtn'),
    finishBackBtn: document.getElementById('finishBackBtn'),

    // Chapters & Dict
    chapHeading: document.getElementById('chapHeading'),
    chapSubheading: document.getElementById('chapSubheading'),
    chaptersList: document.getElementById('chaptersList'),
    dictHeading: document.getElementById('dictHeading'),
    dictSubheading: document.getElementById('dictSubheading'),
    dictSearchInput: document.getElementById('dictSearchInput'),
    dictChapterSelect: document.getElementById('dictChapterSelect'),
    dictResultPrefix: document.getElementById('dictResultPrefix'),
    dictResultCount: document.getElementById('dictResultCount'),
    dictResultSuffix: document.getElementById('dictResultSuffix'),
    dictResultsList: document.getElementById('dictResultsList'),

    // Stats
    statsHeading: document.getElementById('statsHeading'),
    statsSubheading: document.getElementById('statsSubheading'),
    statsTotalWords: document.getElementById('statsTotalWords'),
    statsMasteredWords: document.getElementById('statsMasteredWords'),
    statsReviewingWords: document.getElementById('statsReviewingWords'),
    statsNeedReviewWords: document.getElementById('statsNeedReviewWords'),
    lblTotalVocab: document.getElementById('lblTotalVocab'),
    lblMastered: document.getElementById('lblMastered'),
    lblLearning: document.getElementById('lblLearning'),
    lblNeedsReview: document.getElementById('lblNeedsReview'),
    audioSettingsTitle: document.getElementById('audioSettingsTitle'),
    lblSpeed: document.getElementById('lblSpeed'),
    audioHint: document.getElementById('audioHint'),
    aboutTitle: document.getElementById('aboutTitle'),
    aboutP1: document.getElementById('aboutP1'),
    aboutP2: document.getElementById('aboutP2'),
    speedBtns: document.querySelectorAll('.speed-btn')
  };

  /* -------------------------------------------------------------
     Audio / Speech Synthesis Engine (Native zh-CN)
     ------------------------------------------------------------- */
  let chineseVoice = null;

  function initVoices() {
    if (!('speechSynthesis' in window)) return;
    const voices = window.speechSynthesis.getVoices();
    chineseVoice = voices.find(v => v.lang.startsWith('zh') || v.lang === 'zh-CN') || null;
  }

  if ('speechSynthesis' in window) {
    initVoices();
    window.speechSynthesis.onvoiceschanged = initVoices;
  }

  function speak(text) {
    if (!('speechSynthesis' in window) || !text) return;
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'zh-CN';
    utterance.rate = state.audioRate;
    if (chineseVoice) utterance.voice = chineseVoice;
    window.speechSynthesis.speak(utterance);
  }

  /* -------------------------------------------------------------
     Language Management (Thai / English)
     ------------------------------------------------------------- */
  function toggleLanguage() {
    state.lang = state.lang === 'th' ? 'en' : 'th';
    localStorage.setItem('hsk3_lang', state.lang);
    applyLanguage();
  }

  function applyLanguage() {
    const t = I18N[state.lang];
    document.documentElement.lang = state.lang;

    if (el.langToggleBtn) el.langToggleBtn.textContent = t.langBtn;
    if (el.headerSubtitle) el.headerSubtitle.textContent = t.appSubtitle;
    if (el.streakUnit) el.streakUnit.textContent = t.streakUnit;

    // Nav
    if (el.navReview) el.navReview.textContent = t.navReview;
    if (el.navLessons) el.navLessons.textContent = t.navLessons;
    if (el.navDict) el.navDict.textContent = t.navDict;
    if (el.navStats) el.navStats.textContent = t.navStats;

    // Config view
    if (el.cfgTitle) el.cfgTitle.textContent = t.cfgTitle;
    if (el.cfgSubtitle) el.cfgSubtitle.textContent = t.cfgSubtitle;
    if (el.lblScope) el.lblScope.textContent = t.lblScope;
    if (el.lblMaterial) el.lblMaterial.textContent = t.lblMaterial;
    if (el.modeMixedTitle) el.modeMixedTitle.textContent = t.modeMixedTitle;
    if (el.modeMixedDesc) el.modeMixedDesc.textContent = t.modeMixedDesc;
    if (el.modeWordsTitle) el.modeWordsTitle.textContent = t.modeWordsTitle;
    if (el.modeWordsDesc) el.modeWordsDesc.textContent = t.modeWordsDesc;
    if (el.modeSentTitle) el.modeSentTitle.textContent = t.modeSentTitle;
    if (el.modeSentDesc) el.modeSentDesc.textContent = t.modeSentDesc;
    if (el.lblLength) el.lblLength.textContent = t.lblLength;
    if (el.len10Text) el.len10Text.textContent = t.len10;
    if (el.len15Text) el.len15Text.textContent = t.len15;
    if (el.lenIntenseText) el.lenIntenseText.textContent = t.lenIntense;
    if (el.weakTitle) el.weakTitle.textContent = t.weakTitle;
    if (el.weakDesc) el.weakDesc.textContent = t.weakDesc;
    if (el.startSessionBtn) el.startSessionBtn.textContent = t.startBtn;
    if (el.selectAllChaptersBtn) el.selectAllChaptersBtn.textContent = t.selectAll;
    if (el.clearAllChaptersBtn) el.clearAllChaptersBtn.textContent = t.clearAll;

    // Study cards
    if (el.frontAudioBtn) el.frontAudioBtn.textContent = t.listenAudio;
    if (el.backAudioBtn) el.backAudioBtn.textContent = t.listenAudio;
    if (el.togglePinyinBtn && el.cardPinyin) {
      el.togglePinyinBtn.textContent = el.cardPinyin.classList.contains('hidden') ? t.showPinyin : t.hidePinyin;
    }
    if (el.tapHintWord) el.tapHintWord.textContent = t.tapHintWord;
    if (el.tapHintSent) el.tapHintSent.textContent = t.tapHintSent;
    if (el.lblMissing) el.lblMissing.textContent = t.missingLabel;
    if (el.lblExContext) el.lblExContext.textContent = t.exContextLabel;
    if (el.lblGrammarFocus) el.lblGrammarFocus.textContent = t.grammarFocusLabel;
    if (el.flipCardBtn) el.flipCardBtn.textContent = t.showAnswerBtn;
    if (el.srsLblAgain) el.srsLblAgain.textContent = t.srsAgain;
    if (el.srsSubAgain) el.srsSubAgain.textContent = t.srsAgainSub;
    if (el.srsLblHard) el.srsLblHard.textContent = t.srsHard;
    if (el.srsLblGood) el.srsLblGood.textContent = t.srsGood;
    if (el.srsLblEasy) el.srsLblEasy.textContent = t.srsEasy;

    // Finished view
    if (el.finTitle) el.finTitle.textContent = t.finTitle;
    if (el.finSubtitle) el.finSubtitle.textContent = t.finSubtitle;
    if (el.lblSummaryCards) el.lblSummaryCards.textContent = t.finCards;
    if (el.lblSummaryTime) el.lblSummaryTime.textContent = t.finTime;
    if (el.lblSummaryAcc) el.lblSummaryAcc.textContent = t.finAcc;
    if (el.lblBreakdown) el.lblBreakdown.textContent = t.finBreakdown;
    if (el.txtFinEasy) el.txtFinEasy.textContent = t.finEasy;
    if (el.txtFinGood) el.txtFinGood.textContent = t.finGood;
    if (el.txtFinHard) el.txtFinHard.textContent = t.finHard;
    if (el.txtFinAgain) el.txtFinAgain.textContent = t.finAgain;
    if (el.finishBackBtn) el.finishBackBtn.textContent = t.backHomeBtn;

    // Chapters
    if (el.chapHeading) el.chapHeading.textContent = t.chapHeading;
    if (el.chapSubheading) el.chapSubheading.textContent = t.chapSubheading;
    renderChapters();

    // Dictionary
    if (el.dictHeading) el.dictHeading.textContent = t.dictHeading;
    if (el.dictSubheading) el.dictSubheading.textContent = t.dictSubheading;
    if (el.dictSearchInput) el.dictSearchInput.placeholder = t.dictSearchPlaceholder;
    if (el.dictResultPrefix) el.dictResultPrefix.textContent = t.dictFoundPrefix;
    if (el.dictResultSuffix) el.dictResultSuffix.textContent = t.dictFoundSuffix;
    loadDictionary();

    // Stats
    if (el.statsHeading) el.statsHeading.textContent = t.statsHeading;
    if (el.statsSubheading) el.statsSubheading.textContent = t.statsSubheading;
    if (el.lblTotalVocab) el.lblTotalVocab.textContent = t.lblTotalVocab;
    if (el.lblMastered) el.lblMastered.textContent = t.lblMastered;
    if (el.lblLearning) el.lblLearning.textContent = t.lblLearning;
    if (el.lblNeedsReview) el.lblNeedsReview.textContent = t.lblNeedsReview;
    if (el.audioSettingsTitle) el.audioSettingsTitle.textContent = t.audioSettingsTitle;
    if (el.lblSpeed) el.lblSpeed.textContent = t.lblSpeed;
    if (el.audioHint) el.audioHint.textContent = t.audioHint;
    if (el.aboutTitle) el.aboutTitle.textContent = t.aboutTitle;
    if (el.aboutP1) el.aboutP1.textContent = t.aboutP1;
    if (el.aboutP2) el.aboutP2.textContent = t.aboutP2;

    // Re-render current card if study session is active
    if (state.currentCard && !el.reviewActiveView.classList.contains('hidden')) {
      renderCard();
    }
  }

  /* -------------------------------------------------------------
     Theme Support
     ------------------------------------------------------------- */
  function initTheme() {
    const savedTheme = localStorage.getItem('hsk3_theme');
    if (savedTheme) {
      document.documentElement.setAttribute('data-theme', savedTheme);
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      document.documentElement.setAttribute('data-theme', 'dark');
    }
    updateThemeIcon();
  }

  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('hsk3_theme', next);
    updateThemeIcon();
  }

  function updateThemeIcon() {
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    if (el.themeToggleBtn) el.themeToggleBtn.textContent = isDark ? '☀️' : '🌙';
  }

  /* -------------------------------------------------------------
     Navigation Tabs
     ------------------------------------------------------------- */
  function switchTab(tabId) {
    state.activeTab = tabId;
    el.navItems.forEach(item => {
      item.classList.toggle('active', item.dataset.tab === tabId);
    });
    el.tabPanels.forEach(panel => {
      panel.classList.toggle('active', panel.id === tabId);
    });

    if (tabId === 'tabDict') loadDictionary();
    if (tabId === 'tabStats') loadStats();
    if (tabId === 'tabChapters') renderChapters();
  }

  /* -------------------------------------------------------------
     Initialization & Data Loading
     ------------------------------------------------------------- */
  async function initApp() {
    initTheme();
    setupEventListeners();
    await loadChapters();
    await loadStats();
    applyLanguage(); // Apply Thai or English
  }

  async function loadChapters() {
    try {
      const res = await fetch('/api/chapters');
      state.chapters = await res.json();
      renderChapterCheckboxes();
      renderChapters();
      populateDictChapterDropdown();
    } catch (err) {
      console.error('Failed to load chapters:', err);
    }
  }

  async function loadStats() {
    try {
      const res = await fetch('/api/stats');
      const stats = await res.json();
      if (el.streakCount) el.streakCount.textContent = stats.current_streak || 0;
      if (el.statsTotalWords) el.statsTotalWords.textContent = stats.total_words || 261;
      if (el.statsMasteredWords) el.statsMasteredWords.textContent = stats.mastered_words || 0;
      if (el.statsReviewingWords) el.statsReviewingWords.textContent = (stats.reviewed_words - stats.mastered_words) || 0;
      if (el.statsNeedReviewWords) el.statsNeedReviewWords.textContent = stats.need_review_words || 0;
    } catch (err) {
      console.error('Failed to load stats:', err);
    }
  }

  function renderChapterCheckboxes() {
    if (!el.chapterCheckboxesGrid) return;
    el.chapterCheckboxesGrid.innerHTML = state.chapters.map(c => `
      <label class="ch-item-label">
        <input type="checkbox" value="${c.id}" class="ch-checkbox">
        <span>L${c.id}: ${c.title_cn}</span>
      </label>
    `).join('');

    el.chapterCheckboxesGrid.querySelectorAll('.ch-checkbox').forEach(cb => {
      cb.addEventListener('change', (e) => {
        const val = parseInt(e.target.value);
        if (e.target.checked) state.selectedCustomChapters.add(val);
        else state.selectedCustomChapters.delete(val);
      });
    });
  }

  function populateDictChapterDropdown() {
    if (!el.dictChapterSelect) return;
    const currentVal = el.dictChapterSelect.value;
    const allText = state.lang === 'th' ? 'ทุกบทเรียน' : 'All Lessons';
    el.dictChapterSelect.innerHTML = `<option value="all">${allText}</option>` + 
      state.chapters.map(c => {
        const title = state.lang === 'th' ? c.title_th : c.title_en;
        return `<option value="${c.id}">Lesson ${c.id}: ${c.title_cn} (${title})</option>`;
      }).join('');
    el.dictChapterSelect.value = currentVal || 'all';
  }

  /* -------------------------------------------------------------
     Study Session Management (10-15 Min Core)
     ------------------------------------------------------------- */
  async function startStudySession(customChapterId = null) {
    let chaptersParam = 'all';

    if (customChapterId !== null) {
      chaptersParam = String(customChapterId);
    } else if (state.selectedScope === 'all') {
      chaptersParam = 'all';
    } else if (state.selectedScope === 'custom') {
      if (state.selectedCustomChapters.size > 0) {
        chaptersParam = Array.from(state.selectedCustomChapters).join(',');
      } else {
        alert(state.lang === 'th' ? 'กรุณาเลือกอย่างน้อยหนึ่งบทเรียน หรือเลือก "ทุกบท"' : 'Please select at least one chapter.');
        return;
      }
    } else if (state.selectedScope.includes('-')) {
      const [start, end] = state.selectedScope.split('-').map(Number);
      const list = [];
      for (let i = start; i <= end; i++) list.push(i);
      chaptersParam = list.join(',');
    }

    const type = document.querySelector('input[name="sessionType"]:checked')?.value || 'mixed';
    const count = parseInt(document.querySelector('input[name="sessionLength"]:checked')?.value || '15');
    const onlyWeak = el.onlyWeakToggle && el.onlyWeakToggle.checked ? '1' : '0';

    try {
      const url = `/api/session?chapters=${chaptersParam}&type=${type}&count=${count}&only_weak=${onlyWeak}`;
      const res = await fetch(url);
      const data = await res.json();

      if (!data.items || data.items.length === 0) {
        alert(state.lang === 'th' ? 'ไม่พบการ์ดสำหรับตัวเลือกนี้ ลองเลือก "ทุกบท" หรือปิด "เน้นคำที่ยังจำไม่แม่น"' : 'No cards found for this selection.');
        return;
      }

      state.deck = data.items;
      state.currentIndex = 0;
      state.timeRemainingSec = count <= 15 ? 600 : 900;
      state.timeSpentSec = 0;
      state.sessionStats = {
        total: state.deck.length,
        again: 0,
        hard: 0,
        good: 0,
        easy: 0,
        weakCards: []
      };

      el.reviewConfigView.classList.add('hidden');
      el.reviewFinishedView.classList.add('hidden');
      el.reviewActiveView.classList.remove('hidden');

      startTimer();
      renderCard();
    } catch (err) {
      console.error('Failed to start session:', err);
      alert('Error connecting to backend.');
    }
  }

  function startTimer() {
    clearInterval(state.timerInterval);
    updateTimerDisplay();
    state.timerInterval = setInterval(() => {
      state.timeSpentSec++;
      if (state.timeRemainingSec > 0) {
        state.timeRemainingSec--;
      }
      updateTimerDisplay();
    }, 1000);
  }

  function updateTimerDisplay() {
    if (!el.sessionTimerText) return;
    const m = Math.floor(state.timeRemainingSec / 60);
    const s = state.timeRemainingSec % 60;
    el.sessionTimerText.textContent = `⏱️ ${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
  }

  function renderCard() {
    if (state.currentIndex >= state.deck.length) {
      finishSession();
      return;
    }

    const t = I18N[state.lang];
    const item = state.deck[state.currentIndex];
    state.currentCard = item;
    state.isFlipped = false;

    el.flashcard.classList.remove('flipped');
    el.flipCardBtn.classList.remove('hidden');
    el.srsButtonGroup.classList.add('hidden');

    const total = state.deck.length;
    const current = state.currentIndex + 1;
    el.sessionProgressText.textContent = `${state.lang === 'th' ? 'การ์ดที่' : 'Card'} ${current} / ${total}`;
    el.sessionProgressBar.style.width = `${Math.round((current / total) * 100)}%`;

    el.cardBadgeChapter.textContent = `${t.lessonPrefix} ${item.chapter}`;
    el.cardBadgeKind.textContent = item.kind === 'word' ? t.cardWordBadge : t.cardSentBadge;
    el.cardBadgeKind.className = `badge ${item.kind === 'word' ? 'badge-word' : 'badge-sentence'}`;

    el.backBadgeKind.textContent = item.kind === 'word' ? t.cardWordBadge : t.cardSentBadge;
    el.backBadgeKind.className = `badge ${item.kind === 'word' ? 'badge-word' : 'badge-sentence'}`;

    if (item.kind === 'word') {
      el.wordFrontContent.classList.remove('hidden');
      el.sentenceFrontContent.classList.add('hidden');
      el.wordBackContent.classList.remove('hidden');
      el.sentenceBackContent.classList.add('hidden');

      el.cardHanzi.textContent = item.hanzi;
      el.cardPinyin.textContent = item.pinyin;
      el.cardPinyin.classList.add('hidden');
      el.togglePinyinBtn.classList.remove('hidden');

      // Back content
      el.cardBackHanzi.textContent = item.hanzi;
      el.cardBackPinyin.textContent = item.pinyin;
      
      // Thai and English translations
      el.cardBackThai.textContent = item.thai || item.english || '';
      el.cardBackEnglish.textContent = item.english || '';
      el.backBadgePos.textContent = item.pos || 'w.';

      el.cardBackExCn.textContent = item.ex_cn || '';
      el.cardBackExPy.textContent = item.ex_py || '';
      el.cardBackExTh.textContent = item.ex_th || '';
      el.cardBackExEn.textContent = item.ex_en || '';
    } else {
      el.wordFrontContent.classList.add('hidden');
      el.sentenceFrontContent.classList.remove('hidden');
      el.wordBackContent.classList.add('hidden');
      el.sentenceBackContent.classList.remove('hidden');

      el.cardSentenceContext.textContent = item.context || `${t.lessonPrefix} ${item.chapter}`;

      let displayHanzi = item.hanzi;
      if (item.cloze_target && displayHanzi.includes(item.cloze_target)) {
        displayHanzi = displayHanzi.replace(
          item.cloze_target,
          `<span class="cloze-blank">[ ___ ]</span>`
        );
      }
      el.cardSentenceHanzi.innerHTML = displayHanzi;

      // Cloze hint in Thai or English
      const hint = state.lang === 'th' ? (item.cloze_hint_th || item.cloze_hint_en) : (item.cloze_hint_en || item.cloze_hint_th);
      el.cardClozeHint.textContent = hint || item.cloze_target || '';

      // Back content
      el.cardBackSentHanzi.textContent = item.hanzi;
      el.cardBackSentPinyin.textContent = item.pinyin;
      el.cardBackSentThai.textContent = item.thai || '';
      el.cardBackSentEnglish.textContent = item.english || '';

      const grammar = state.lang === 'th' ? (item.grammar_th || item.grammar_en) : (item.grammar_en || item.grammar_th);
      el.cardBackGrammar.textContent = grammar || 'HSK 3 Standard Structure';
    }
  }

  function flipCard() {
    if (state.isFlipped) return;
    state.isFlipped = true;
    el.flashcard.classList.add('flipped');
    el.flipCardBtn.classList.add('hidden');
    el.srsButtonGroup.classList.remove('hidden');

    const textToSpeak = state.currentCard.kind === 'word' ? state.currentCard.hanzi : state.currentCard.hanzi;
    speak(textToSpeak);
  }

  async function handleGrade(grade) {
    const item = state.currentCard;
    if (!item) return;

    if (grade === 1) {
      state.sessionStats.again++;
      state.sessionStats.weakCards.push(item);
      state.deck.splice(Math.min(state.currentIndex + 4, state.deck.length), 0, item);
    } else if (grade === 2) {
      state.sessionStats.hard++;
      state.sessionStats.weakCards.push(item);
    } else if (grade === 3) {
      state.sessionStats.good++;
    } else if (grade === 4) {
      state.sessionStats.easy++;
    }

    try {
      fetch('/api/review', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          item_type: item.kind,
          item_id: item.id,
          grade: grade,
          seconds_spent: 10
        })
      });
    } catch (e) {
      console.warn('Failed to post review grade', e);
    }

    state.currentIndex++;
    renderCard();
  }

  function finishSession() {
    clearInterval(state.timerInterval);
    const t = I18N[state.lang];

    el.reviewActiveView.classList.add('hidden');
    el.reviewFinishedView.classList.remove('hidden');

    const minutes = Math.floor(state.timeSpentSec / 60);
    const seconds = state.timeSpentSec % 60;
    el.summaryTimeSpent.textContent = `${minutes}m ${seconds}s`;

    const totalRated = state.sessionStats.again + state.sessionStats.hard + state.sessionStats.good + state.sessionStats.easy;
    el.summaryTotalCards.textContent = totalRated;

    const successful = state.sessionStats.good + state.sessionStats.easy;
    const accuracy = totalRated > 0 ? Math.round((successful / totalRated) * 100) : 100;
    el.summaryAccuracy.textContent = `${accuracy}%`;

    el.countEasy.textContent = state.sessionStats.easy;
    el.countGood.textContent = state.sessionStats.good;
    el.countHard.textContent = state.sessionStats.hard;
    el.countAgain.textContent = state.sessionStats.again;

    if (state.sessionStats.weakCards.length > 0) {
      el.reviewAgainWeakBtn.classList.remove('hidden');
      el.reviewAgainWeakBtn.textContent = t.practiceWeakAgain(state.sessionStats.weakCards.length);
    } else {
      el.reviewAgainWeakBtn.classList.add('hidden');
    }

    loadStats().then(() => {
      const currentStreak = parseInt(el.streakCount.textContent) || 1;
      el.awardStreakText.textContent = t.finStreak(currentStreak);
    });
  }

  function practiceWeakCardsAgain() {
    if (state.sessionStats.weakCards.length === 0) return;
    const weakList = [...state.sessionStats.weakCards];
    state.deck = weakList;
    state.currentIndex = 0;
    state.timeRemainingSec = 300;
    state.timeSpentSec = 0;
    state.sessionStats = {
      total: weakList.length,
      again: 0,
      hard: 0,
      good: 0,
      easy: 0,
      weakCards: []
    };

    el.reviewFinishedView.classList.add('hidden');
    el.reviewActiveView.classList.remove('hidden');
    startTimer();
    renderCard();
  }

  /* -------------------------------------------------------------
     Chapters Explorer Rendering
     ------------------------------------------------------------- */
  function renderChapters() {
    if (!el.chaptersList) return;
    const t = I18N[state.lang];

    el.chaptersList.innerHTML = state.chapters.map(c => {
      const title = state.lang === 'th' ? c.title_th : c.title_en;
      const topic = state.lang === 'th' ? c.topic_th : c.topic_en;
      const grammarList = state.lang === 'th' ? (c.grammar_th || c.grammar_en) : (c.grammar_en || c.grammar_th);

      return `
        <div class="chapter-card-item">
          <div class="chapter-card-top">
            <div>
              <span class="ch-number">${t.lessonPrefix} ${c.id}</span>
              <div class="ch-title-cn">${c.title_cn}</div>
              <div class="ch-title-en">${title} (${c.title_pinyin})</div>
              <div class="ch-topic">📌 ${topic}</div>
            </div>
          </div>
          <div class="ch-grammar-tags">
            ${grammarList.map(g => `<span class="grammar-chip">💡 ${g}</span>`).join('')}
          </div>
          <button class="btn btn-secondary btn-practice-ch" data-chapter-id="${c.id}">
            ${t.practiceLessonBtn(c.id)}
          </button>
        </div>
      `;
    }).join('');

    el.chaptersList.querySelectorAll('.btn-practice-ch').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const chId = parseInt(e.currentTarget.dataset.chapterId);
        switchTab('tabReview');
        startStudySession(chId);
      });
    });
  }

  /* -------------------------------------------------------------
     Dictionary Search & Browse (with Thai search support)
     ------------------------------------------------------------- */
  let dictTimeout = null;

  async function loadDictionary() {
    const q = el.dictSearchInput ? el.dictSearchInput.value : '';
    const ch = el.dictChapterSelect ? el.dictChapterSelect.value : 'all';

    try {
      const res = await fetch(`/api/dictionary?q=${encodeURIComponent(q)}&chapter=${ch}`);
      const words = await res.json();

      el.dictResultCount.textContent = words.length;
      el.dictResultsList.innerHTML = words.map(w => {
        const primaryMeaning = state.lang === 'th' ? (w.thai || w.english) : (w.english || w.thai);
        const secondaryMeaning = state.lang === 'th' ? w.english : w.thai;
        const exMeaning = state.lang === 'th' ? (w.ex_th || w.ex_en) : (w.ex_en || w.ex_th);

        return `
          <div class="dict-item">
            <div class="dict-item-top">
              <span class="dict-hanzi">${w.hanzi}</span>
              <span class="dict-pinyin">${w.pinyin}</span>
              <button class="dict-audio-btn" data-speak="${w.hanzi}">🔊</button>
              <span class="dict-pos">${w.pos || ''} · L${w.chapter}</span>
            </div>
            <div class="dict-thai"><strong>${primaryMeaning}</strong></div>
            ${secondaryMeaning && secondaryMeaning !== primaryMeaning ? `<div class="dict-english">${secondaryMeaning}</div>` : ''}
            ${w.ex_cn ? `
              <div class="dict-example">
                <strong>例:</strong> ${w.ex_cn} <br>
                <em>${w.ex_py}</em> - ${exMeaning}
              </div>
            ` : ''}
          </div>
        `;
      }).join('');

      el.dictResultsList.querySelectorAll('.dict-audio-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
          speak(e.currentTarget.dataset.speak);
        });
      });
    } catch (err) {
      console.error('Failed to load dictionary:', err);
    }
  }

  /* -------------------------------------------------------------
     Event Listeners & Keybindings
     ------------------------------------------------------------- */
  function setupEventListeners() {
    // Language toggle
    if (el.langToggleBtn) el.langToggleBtn.addEventListener('click', toggleLanguage);

    // Theme toggle
    if (el.themeToggleBtn) el.themeToggleBtn.addEventListener('click', toggleTheme);

    // Nav items
    el.navItems.forEach(item => {
      item.addEventListener('click', () => switchTab(item.dataset.tab));
    });

    // Scope Pills
    el.scopePills.forEach(pill => {
      pill.addEventListener('click', (e) => {
        el.scopePills.forEach(p => p.classList.remove('active'));
        e.currentTarget.classList.add('active');
        state.selectedScope = e.currentTarget.dataset.scope || 'custom';
        if (state.selectedScope === 'custom') {
          el.customChapterSelect.classList.remove('hidden');
        } else {
          el.customChapterSelect.classList.add('hidden');
        }
      });
    });

    // Custom pick buttons
    if (el.selectAllChaptersBtn) {
      el.selectAllChaptersBtn.addEventListener('click', () => {
        document.querySelectorAll('.ch-checkbox').forEach(cb => {
          cb.checked = true;
          state.selectedCustomChapters.add(parseInt(cb.value));
        });
      });
    }

    if (el.clearAllChaptersBtn) {
      el.clearAllChaptersBtn.addEventListener('click', () => {
        document.querySelectorAll('.ch-checkbox').forEach(cb => {
          cb.checked = false;
        });
        state.selectedCustomChapters.clear();
      });
    }

    // Mode Cards
    el.modeCards.forEach(card => {
      card.addEventListener('click', () => {
        el.modeCards.forEach(c => c.classList.remove('selected'));
        card.classList.add('selected');
        card.querySelector('input').checked = true;
      });
    });

    // Length Pills
    el.lengthPills.forEach(pill => {
      pill.addEventListener('click', () => {
        el.lengthPills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        pill.querySelector('input').checked = true;
      });
    });

    // Start Session Button
    if (el.startSessionBtn) {
      el.startSessionBtn.addEventListener('click', () => startStudySession());
    }

    // Exit Session
    if (el.exitSessionBtn) {
      el.exitSessionBtn.addEventListener('click', () => {
        const msg = state.lang === 'th' ? 'คุณแน่ใจหรือไม่ว่าต้องการจบการทบทวนรอบนี้?' : 'Are you sure you want to end this review session?';
        if (confirm(msg)) {
          clearInterval(state.timerInterval);
          el.reviewActiveView.classList.add('hidden');
          el.reviewConfigView.classList.remove('hidden');
        }
      });
    }

    // Flip Card triggers
    if (el.flashcard) el.flashcard.addEventListener('click', flipCard);
    if (el.flipCardBtn) el.flipCardBtn.addEventListener('click', flipCard);

    // Toggle Pinyin
    if (el.togglePinyinBtn) {
      el.togglePinyinBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        el.cardPinyin.classList.toggle('hidden');
        const t = I18N[state.lang];
        el.togglePinyinBtn.textContent = el.cardPinyin.classList.contains('hidden') ? t.showPinyin : t.hidePinyin;
      });
    }

    // Audio triggers on card
    if (el.frontAudioBtn) {
      el.frontAudioBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        if (state.currentCard) speak(state.currentCard.hanzi);
      });
    }
    if (el.backAudioBtn) {
      el.backAudioBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        if (state.currentCard) speak(state.currentCard.hanzi);
      });
    }
    if (el.audioSpeechBtn) {
      el.audioSpeechBtn.addEventListener('click', () => {
        if (state.currentCard) speak(state.currentCard.hanzi);
      });
    }
    if (el.exampleAudioBtn) {
      el.exampleAudioBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        if (state.currentCard && state.currentCard.ex_cn) speak(state.currentCard.ex_cn);
      });
    }

    // SRS Ratings
    el.srsButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const grade = parseInt(e.currentTarget.dataset.grade);
        handleGrade(grade);
      });
    });

    // Finished view buttons
    if (el.finishBackBtn) {
      el.finishBackBtn.addEventListener('click', () => {
        el.reviewFinishedView.classList.add('hidden');
        el.reviewConfigView.classList.remove('hidden');
      });
    }
    if (el.reviewAgainWeakBtn) {
      el.reviewAgainWeakBtn.addEventListener('click', practiceWeakCardsAgain);
    }

    // Dict search inputs
    if (el.dictSearchInput) {
      el.dictSearchInput.addEventListener('input', () => {
        clearTimeout(dictTimeout);
        dictTimeout = setTimeout(loadDictionary, 250);
      });
    }
    if (el.dictChapterSelect) {
      el.dictChapterSelect.addEventListener('change', loadDictionary);
    }

    // Speed buttons
    el.speedBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        el.speedBtns.forEach(b => b.classList.remove('active'));
        e.currentTarget.classList.add('active');
        state.audioRate = parseFloat(e.currentTarget.dataset.rate);
      });
    });

    // Touch swipe gesture for iPhone / iPad
    let touchStartX = 0;
    let touchEndX = 0;

    if (el.flashcard) {
      el.flashcard.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
      }, { passive: true });

      el.flashcard.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        const diff = touchEndX - touchStartX;
        if (Math.abs(diff) > 60) {
          if (!state.isFlipped) {
            flipCard();
          } else {
            if (diff < -60) handleGrade(2);
            else if (diff > 60) handleGrade(3);
          }
        }
      }, { passive: true });
    }

    // Keyboard Shortcuts (Space to flip, 1-4 for SRS, S for speak)
    window.addEventListener('keydown', (e) => {
      if (state.activeTab !== 'tabReview' || el.reviewActiveView.classList.contains('hidden')) return;
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;

      if (e.code === 'Space') {
        e.preventDefault();
        flipCard();
      } else if (e.key === 's' || e.key === 'S') {
        if (state.currentCard) speak(state.currentCard.hanzi);
      } else if (state.isFlipped) {
        if (e.key === '1') handleGrade(1);
        if (e.key === '2') handleGrade(2);
        if (e.key === '3') handleGrade(3);
        if (e.key === '4') handleGrade(4);
      }
    });
  }

  document.addEventListener('DOMContentLoaded', initApp);
})();
