# data_hsk1.py
# Complete HSK 1 Vocabulary, Dialogue Sentences, and Grammar Points with Thai translations

hsk1_words = [
    # Lesson 1: 你好
    {"chapter_num": 1, "hanzi": "你", "pinyin": "nǐ", "english": "you (singular)", "thai": "เธอ, คุณ", "pos": "pron.", "ex_cn": "你好！", "ex_py": "Nǐ hǎo!", "ex_en": "Hello!", "ex_th": "สวัสดี!"},
    {"chapter_num": 1, "hanzi": "好", "pinyin": "hǎo", "english": "good, fine, well", "thai": "ดี, สบายดี", "pos": "adj.", "ex_cn": "很好，谢谢。", "ex_py": "Hěn hǎo, xièxie.", "ex_en": "Very good, thank you.", "ex_th": "สบายดีมาก ขอบคุณนะ"},
    {"chapter_num": 1, "hanzi": "您", "pinyin": "nín", "english": "you (polite/respectful)", "thai": "ท่าน (คุณแบบสุภาพ)", "pos": "pron.", "ex_cn": "老师，您好！", "ex_py": "Lǎoshī, nín hǎo!", "ex_en": "Teacher, hello!", "ex_th": "คุณครู สวัสดีครับ/ค่ะ!"},
    {"chapter_num": 1, "hanzi": "你们", "pinyin": "nǐmen", "english": "you (plural)", "thai": "พวกเธอ, พวกคุณ", "pos": "pron.", "ex_cn": "你们好！", "ex_py": "Nǐmen hǎo!", "ex_en": "Hello everyone!", "ex_th": "สวัสดีพวกเธอทุกคน!"},
    {"chapter_num": 1, "hanzi": "对不起", "pinyin": "duìbuqǐ", "english": "sorry, excuse me", "thai": "ขอโทษ", "pos": "phrase", "ex_cn": "对不起，我来晚了。", "ex_py": "Duìbuqǐ, wǒ lái wǎn le.", "ex_en": "Sorry, I am late.", "ex_th": "ขอโทษนะ ฉันมาสาย"},
    {"chapter_num": 1, "hanzi": "没关系", "pinyin": "méi guānxi", "english": "it doesn't matter, that's all right", "thai": "ไม่เป็นไร", "pos": "phrase", "ex_cn": "没关系，请进。", "ex_py": "Méi guānxi, qǐng jìn.", "ex_en": "It doesn't matter, please come in.", "ex_th": "ไม่เป็นไร เชิญเข้ามาข้างในเลย"},

    # Lesson 2: 谢谢你
    {"chapter_num": 2, "hanzi": "谢谢", "pinyin": "xièxie", "english": "to thank, thanks", "thai": "ขอบคุณ", "pos": "v.", "ex_cn": "谢谢你的帮助！", "ex_py": "Xièxie nǐ de bāngzhù!", "ex_en": "Thank you for your help!", "ex_th": "ขอบคุณสำหรับความช่วยเหลือของเธอนะ!"},
    {"chapter_num": 2, "hanzi": "不", "pinyin": "bù", "english": "no, not", "thai": "ไม่", "pos": "adv.", "ex_cn": "这不是我的书。", "ex_py": "Zhè bú shì wǒ de shū.", "ex_en": "This is not my book.", "ex_th": "นี่ไม่ใช่หนังสือของฉัน"},
    {"chapter_num": 2, "hanzi": "客气", "pinyin": "kèqi", "english": "polite, courteous", "thai": "เกรงใจ", "pos": "adj.", "ex_cn": "不客气，别这么说。", "ex_py": "Bú kèqi, bié zhème shuō.", "ex_en": "You're welcome, don't mention it.", "ex_th": "ไม่ต้องเกรงใจ อย่าพูดแบบนั้นเลย"},
    {"chapter_num": 2, "hanzi": "再见", "pinyin": "zàijiàn", "english": "goodbye, see you again", "thai": "ลาก่อน, แล้วพบกันใหม่", "pos": "v.", "ex_cn": "明天见，再见！", "ex_py": "Míngtiān jiàn, zàijiàn!", "ex_en": "See you tomorrow, goodbye!", "ex_th": "เจอกันพรุ่งนี้นะ ลาก่อน!"},

    # Lesson 3: 你叫什么名字
    {"chapter_num": 3, "hanzi": "叫", "pinyin": "jiào", "english": "to be called, call", "thai": "ชื่อว่า, เรียก", "pos": "v.", "ex_cn": "我叫李月。", "ex_py": "Wǒ jiào Lǐ Yuè.", "ex_en": "My name is Li Yue.", "ex_th": "ฉันชื่อหลี่เยว่"},
    {"chapter_num": 3, "hanzi": "什么", "pinyin": "shénme", "english": "what", "thai": "อะไร", "pos": "pron.", "ex_cn": "你叫什么名字？", "ex_py": "Nǐ jiào shénme míngzi?", "ex_en": "What is your name?", "ex_th": "คุณชื่ออะไร?"},
    {"chapter_num": 3, "hanzi": "名字", "pinyin": "míngzi", "english": "name", "thai": "ชื่อ", "pos": "n.", "ex_cn": "这个名字很好听。", "ex_py": "Zhè ge míngzi hěn hǎotīng.", "ex_en": "This name sounds very pleasant.", "ex_th": "ชื่อนี้ไพเราะมากเลย"},
    {"chapter_num": 3, "hanzi": "我", "pinyin": "wǒ", "english": "I, me", "thai": "ฉัน, ผม", "pos": "pron.", "ex_cn": "我是中国人。", "ex_py": "Wǒ shì Zhōngguórén.", "ex_en": "I am Chinese.", "ex_th": "ฉันเป็นคนจีน"},
    {"chapter_num": 3, "hanzi": "是", "pinyin": "shì", "english": "to be (am, is, are), yes", "thai": "เป็น, คือ, ใช่", "pos": "v.", "ex_cn": "他是我的朋友。", "ex_py": "Tā shì wǒ de péngyou.", "ex_en": "He is my friend.", "ex_th": "เขาคือเพื่อนของฉัน"},
    {"chapter_num": 3, "hanzi": "人", "pinyin": "rén", "english": "person, people", "thai": "คน", "pos": "n.", "ex_cn": "你是哪国人？", "ex_py": "Nǐ shì nǎ guó rén?", "ex_en": "Which country are you from?", "ex_th": "คุณเป็นคนประเทศไหน?"},
    {"chapter_num": 3, "hanzi": "中国", "pinyin": "Zhōngguó", "english": "China", "thai": "ประเทศจีน", "pos": "prop.", "ex_cn": "中国很大很漂亮。", "ex_py": "Zhōngguó hěn dà hěn piàoliang.", "ex_en": "China is very big and beautiful.", "ex_th": "ประเทศจีนใหญ่และสวยงามมาก"},
    {"chapter_num": 3, "hanzi": "美国", "pinyin": "Měiguó", "english": "United States", "thai": "ประเทศสหรัฐอเมริกา", "pos": "prop.", "ex_cn": "他是美国人。", "ex_py": "Tā shì Měiguórén.", "ex_en": "He is American.", "ex_th": "เขาเป็นคนอเมริกัน"},

    # Lesson 4: 她是我的汉语老师
    {"chapter_num": 4, "hanzi": "老师", "pinyin": "lǎoshī", "english": "teacher", "thai": "คุณครู, อาจารย์", "pos": "n.", "ex_cn": "王老师教我们汉语。", "ex_py": "Wáng lǎoshī jiāo wǒmen Hànyǔ.", "ex_en": "Teacher Wang teaches us Chinese.", "ex_th": "ครูหวังเขาสอนภาษาจีนพวกเรา"},
    {"chapter_num": 4, "hanzi": "学生", "pinyin": "xuésheng", "english": "student", "thai": "นักเรียน, นักศึกษา", "pos": "n.", "ex_cn": "我们都是大学学生。", "ex_py": "Wǒmen dōu shì dàxué xuésheng.", "ex_en": "We are all university students.", "ex_th": "พวกเราทุกคนเป็นนักศึกษามหาวิทยาลัย"},
    {"chapter_num": 4, "hanzi": "他", "pinyin": "tā", "english": "he, him", "thai": "เขา (ผู้ชาย)", "pos": "pron.", "ex_cn": "他是我的同班同学。", "ex_py": "Tā shì wǒ de tóngbān tóngxué.", "ex_en": "He is my classmate.", "ex_th": "เขาเป็นเพื่อนร่วมชั้นของฉัน"},
    {"chapter_num": 4, "hanzi": "她", "pinyin": "tā", "english": "she, her", "thai": "เธอ, หล่อน (ผู้หญิง)", "pos": "pron.", "ex_cn": "她是一名医生。", "ex_py": "Tā shì yì míng yīshēng.", "ex_en": "She is a doctor.", "ex_th": "เธอเป็นคุณหมอ"},
    {"chapter_num": 4, "hanzi": "朋友", "pinyin": "péngyou", "english": "friend", "thai": "เพื่อน", "pos": "n.", "ex_cn": "我和他是好朋友。", "ex_py": "Wǒ hé tā shì hǎo péngyou.", "ex_en": "He and I are good friends.", "ex_th": "ฉันกับเขาเป็นเพื่อนสนิทกัน"},
    {"chapter_num": 4, "hanzi": "同学", "pinyin": "tóngxué", "english": "classmate", "thai": "เพื่อนร่วมชั้น", "pos": "n.", "ex_cn": "那是我的新同学。", "ex_py": "Nà shì wǒ de xīn tóngxué.", "ex_en": "That is my new classmate.", "ex_th": "นั่นคือเพื่อนร่วมชั้นคนใหม่ของฉัน"},
    {"chapter_num": 4, "hanzi": "汉语", "pinyin": "Hànyǔ", "english": "Chinese language (Mandarin)", "thai": "ภาษาจีน", "pos": "n.", "ex_cn": "学汉语很有意思。", "ex_py": "Xué Hànyǔ hěn yǒu yìsi.", "ex_en": "Learning Chinese is very interesting.", "ex_th": "การเรียนภาษาจีนน่าสนใจมาก"},
    {"chapter_num": 4, "hanzi": "谁", "pinyin": "shéi / shuí", "english": "who, whom", "thai": "ใคร", "pos": "pron.", "ex_cn": "他是谁？", "ex_py": "Tā shì shéi?", "ex_en": "Who is he?", "ex_th": "เขาคือใคร?"},
    {"chapter_num": 4, "hanzi": "哪", "pinyin": "nǎ", "english": "which", "thai": "ไหน, อันไหน", "pos": "pron.", "ex_cn": "哪本书是你的？", "ex_py": "Nǎ běn shū shì nǐ de?", "ex_en": "Which book is yours?", "ex_th": "หนังสือเล่มไหนคือของเธอ?"},
    {"chapter_num": 4, "hanzi": "的", "pinyin": "de", "english": "possessive particle ('s, of)", "thai": "ของ, ที่ (คำช่วยแสดงความเป็นเจ้าของ)", "pos": "part.", "ex_cn": "这是我的电脑。", "ex_py": "Zhè shì wǒ de diànnǎo.", "ex_en": "This is my computer.", "ex_th": "นี่คือคอมพิวเตอร์ของฉัน"},
    {"chapter_num": 4, "hanzi": "呢", "pinyin": "ne", "english": "modal particle for follow-up questions", "thai": "ล่ะ (คำช่วยคำถามย้อน: แล้ว...ล่ะ?)", "pos": "part.", "ex_cn": "我是中国人，你呢？", "ex_py": "Wǒ shì Zhōngguórén, nǐ ne?", "ex_en": "I am Chinese, and you?", "ex_th": "ฉันเป็นคนจีน แล้วเธอล่ะ?"},

    # Lesson 5: 她女儿今年二十岁
    {"chapter_num": 5, "hanzi": "家", "pinyin": "jiā", "english": "family, home", "thai": "บ้าน, ครอบครัว", "pos": "n.", "ex_cn": "我家有四口人。", "ex_py": "Wǒ jiā yǒu sì kǒu rén.", "ex_en": "There are four people in my family.", "ex_th": "ครอบครัวฉันมี 4 คน"},
    {"chapter_num": 5, "hanzi": "有", "pinyin": "yǒu", "english": "to have, there is/are", "thai": "มี", "pos": "v.", "ex_cn": "你有一个妹妹吗？", "ex_py": "Nǐ yǒu yí ge mèimei ma?", "ex_en": "Do you have a younger sister?", "ex_th": "เธอมีน้องสาวหนึ่งคนใช่ไหม?"},
    {"chapter_num": 5, "hanzi": "口", "pinyin": "kǒu", "english": "measure word for family members / mouth", "thai": "คน (ลักษณนามสมาชิกในครอบครัว) / ปาก", "pos": "m./n.", "ex_cn": "他家有三口人。", "ex_py": "Tā jiā yǒu sān kǒu rén.", "ex_en": "His family has three members.", "ex_th": "บ้านเขามีสมาชิก 3 คน"},
    {"chapter_num": 5, "hanzi": "女儿", "pinyin": "nǚ'ér", "english": "daughter", "thai": "ลูกสาว", "pos": "n.", "ex_cn": "她女儿今年六岁。", "ex_py": "Tā nǚ'ér jīnnián liù suì.", "ex_en": "Her daughter is six years old this year.", "ex_th": "ลูกสาวของเธอปีนี้อายุ 6 ขวบ"},
    {"chapter_num": 5, "hanzi": "儿子", "pinyin": "érzi", "english": "son", "thai": "ลูกชาย", "pos": "n.", "ex_cn": "他儿子很聪明。", "ex_py": "Tā érzi hěn cōngming.", "ex_en": "His son is very smart.", "ex_th": "ลูกชายของเขาฉลาดมาก"},
    {"chapter_num": 5, "hanzi": "几", "pinyin": "jǐ", "english": "how many (usually < 10), several", "thai": "กี่, เท่าไหร่ (มักใช้กับจำนวนน้อยกว่า 10)", "pos": "pron.", "ex_cn": "你有几个苹果？", "ex_py": "Nǐ yǒu jǐ ge píngguǒ?", "ex_en": "How many apples do you have?", "ex_th": "เธอมีแอปเปิ้ลกี่ลูก?"},
    {"chapter_num": 5, "hanzi": "岁", "pinyin": "suì", "english": "years old (age)", "thai": "ขวบ, ปี (อายุ)", "pos": "m.", "ex_cn": "你今年多大了？我二十岁。", "ex_py": "Nǐ jīnnián duō dà le? Wǒ èrshí suì.", "ex_en": "How old are you this year? I am 20 years old.", "ex_th": "ปีนี้เธออายุเท่าไหร่? ฉันอายุ 20 ปี"},
    {"chapter_num": 5, "hanzi": "今年", "pinyin": "jīnnián", "english": "this year", "thai": "ปีนี้", "pos": "n.", "ex_cn": "今年我二十一岁。", "ex_py": "Jīnnián wǒ èrshíyī suì.", "ex_en": "This year I am 21 years old.", "ex_th": "ปีนี้ฉันอายุ 21 ปี"},
    {"chapter_num": 5, "hanzi": "多", "pinyin": "duō", "english": "many, much / how (in questions like 多大)", "thai": "มาก, เยอะ / เท่าไหร่ (ถามระดับ/ขนาด)", "pos": "adj./adv.", "ex_cn": "李老师多大年纪了？", "ex_py": "Lǐ lǎoshī duō dà niánjì le?", "ex_en": "How old is Teacher Li?", "ex_th": "อาจารย์หลี่อายุเท่าไหร่แล้ว?"},
    {"chapter_num": 5, "hanzi": "大", "pinyin": "dà", "english": "big, large / old in age", "thai": "ใหญ่ / โต, มาก (อายุ)", "pos": "adj.", "ex_cn": "北京是一个大城市。", "ex_py": "Běijīng shì yí ge dà chéngshì.", "ex_en": "Beijing is a big city.", "ex_th": "ปักกิ่งเป็นเมืองใหญ่"},

    # Lesson 6: 我会说汉语
    {"chapter_num": 6, "hanzi": "会", "pinyin": "huì", "english": "can, be able to (through learning)", "thai": "เป็น, ได้ (จากการเรียนรู้/ฝึกฝน)", "pos": "v.", "ex_cn": "你会写汉字吗？", "ex_py": "Nǐ huì xiě hànzì ma?", "ex_en": "Can you write Chinese characters?", "ex_th": "เธอเขียนตัวอักษรจีนเป็นไหม?"},
    {"chapter_num": 6, "hanzi": "说", "pinyin": "shuō", "english": "to speak, say", "thai": "พูด, บอก", "pos": "v.", "ex_cn": "请慢一点儿说。", "ex_py": "Qǐng màn yìdiǎnr shuō.", "ex_en": "Please speak a bit slower.", "ex_th": "กรุณาพูดช้าลงหน่อย"},
    {"chapter_num": 6, "hanzi": "妈妈", "pinyin": "māma", "english": "mother, mom", "thai": "แม่", "pos": "n.", "ex_cn": "我妈妈做饭很好吃。", "ex_py": "Wǒ māma zuòfàn hěn hǎochī.", "ex_en": "My mother cooks delicious food.", "ex_th": "แม่ของฉันทำกับข้าวอร่อยมาก"},
    {"chapter_num": 6, "hanzi": "菜", "pinyin": "cài", "english": "dish, food, vegetable", "thai": "กับข้าว, อาหาร, ผัก", "pos": "n.", "ex_cn": "中国菜非常有名。", "ex_py": "Zhōngguó cài fēicháng yǒumíng.", "ex_en": "Chinese cuisine is extremely famous.", "ex_th": "อาหารจีนมีชื่อเสียงมากจริงๆ"},
    {"chapter_num": 6, "hanzi": "很", "pinyin": "hěn", "english": "very, quite", "thai": "มาก", "pos": "adv.", "ex_cn": "今天天气很好。", "ex_py": "Jīntiān tiānqì hěn hǎo.", "ex_en": "The weather is very good today.", "ex_th": "วันนี้อากาศดีมาก"},
    {"chapter_num": 6, "hanzi": "好吃", "pinyin": "hǎochī", "english": "delicious, tasty", "thai": "อร่อย", "pos": "adj.", "ex_cn": "这个饺子真好吃！", "ex_py": "Zhè ge jiǎozi zhēn hǎochī!", "ex_en": "These dumplings are really delicious!", "ex_th": "เกี๊ยวนี้อร่อยจริงๆ!"},
    {"chapter_num": 6, "hanzi": "做", "pinyin": "zuò", "english": "to do, make, cook", "thai": "ทำ", "pos": "v.", "ex_cn": "你在做什么呢？", "ex_py": "Nǐ zài zuò shénme ne?", "ex_en": "What are you making/doing?", "ex_th": "เธอกำลังทำอะไรอยู่เหรอ?"},
    {"chapter_num": 6, "hanzi": "写", "pinyin": "xiě", "english": "to write", "thai": "เขียน", "pos": "v.", "ex_cn": "我会写这个汉字。", "ex_py": "Wǒ huì xiě zhè ge hànzì.", "ex_en": "I know how to write this character.", "ex_th": "ฉันเขียนตัวอักษรจีนตัวนี้เป็น"},
    {"chapter_num": 6, "hanzi": "汉字", "pinyin": "hànzì", "english": "Chinese character", "thai": "ตัวอักษรจีน", "pos": "n.", "ex_cn": "汉字很有意思。", "ex_py": "Hànzì hěn yǒu yìsi.", "ex_en": "Chinese characters are very interesting.", "ex_th": "ตัวอักษรจีนมีความน่าสนใจมาก"},
    {"chapter_num": 6, "hanzi": "字", "pinyin": "zì", "english": "character, word", "thai": "ตัวหนังสือ, ตัวอักษร", "pos": "n.", "ex_cn": "这个字怎么读？", "ex_py": "Zhè ge zì zěnme dú?", "ex_en": "How is this character pronounced?", "ex_th": "ตัวหนังสือตัวนี้อ่านอย่างไร?"},
    {"chapter_num": 6, "hanzi": "怎么", "pinyin": "zěnme", "english": "how (asking manner/method)", "thai": "อย่างไร", "pos": "pron.", "ex_cn": "这个汉字怎么写？", "ex_py": "Zhè ge hànzì zěnme xiě?", "ex_en": "How do you write this Chinese character?", "ex_th": "ตัวอักษรจีนตัวนี้เขียนอย่างไร?"},
    {"chapter_num": 6, "hanzi": "读", "pinyin": "dú", "english": "to read aloud, pronounce", "thai": "อ่าน, อ่านออกเสียง", "pos": "v.", "ex_cn": "请大家跟我读。", "ex_py": "Qǐng dàjiā gēn wǒ dú.", "ex_en": "Everyone please read aloud after me.", "ex_th": "ขอให้ทุกคนอ่านตามฉันนะ"},

    # Lesson 7: 今天几号
    {"chapter_num": 7, "hanzi": "请", "pinyin": "qǐng", "english": "please, to invite", "thai": "กรุณา, โปรด, เชิญ, เลี้ยง", "pos": "v.", "ex_cn": "请问，现在几点了？", "ex_py": "Qǐngwèn, xiànzài jǐ diǎn le?", "ex_en": "Excuse me, what time is it now?", "ex_th": "ขอถามหน่อย ตอนนี้กี่โมงแล้ว?"},
    {"chapter_num": 7, "hanzi": "问", "pinyin": "wèn", "english": "to ask", "thai": "ถาม", "pos": "v.", "ex_cn": "我想问你一个问题。", "ex_py": "Wǒ xiǎng wèn nǐ yí ge wèntí.", "ex_en": "I'd like to ask you a question.", "ex_th": "ฉันอยากจะถามคำถามเธอสักข้อหนึ่ง"},
    {"chapter_num": 7, "hanzi": "今天", "pinyin": "jīntiān", "english": "today", "thai": "วันนี้", "pos": "n.", "ex_cn": "今天星期三。", "ex_py": "Jīntiān xīngqīsān.", "ex_en": "Today is Wednesday.", "ex_th": "วันนี้วันพุธ"},
    {"chapter_num": 7, "hanzi": "号", "pinyin": "hào", "english": "day of month / number", "thai": "วันที่ / เบอร์, หมายเลข", "pos": "n./m.", "ex_cn": "今天九月一号。", "ex_py": "Jīntiān jiǔ yuè yī hào.", "ex_en": "Today is September 1st.", "ex_th": "วันนี้วันที่ 1 กันยายน"},
    {"chapter_num": 7, "hanzi": "月", "pinyin": "yuè", "english": "month, moon", "thai": "เดือน, พระจันทร์", "pos": "n.", "ex_cn": "一年有十二个月。", "ex_py": "Yì nián yǒu shí'èr ge yuè.", "ex_en": "A year has twelve months.", "ex_th": "หนึ่งปีมี 12 เดือน"},
    {"chapter_num": 7, "hanzi": "星期", "pinyin": "xīngqī", "english": "week, day of the week", "thai": "สัปดาห์, วันในสัปดาห์", "pos": "n.", "ex_cn": "这个星期我很忙。", "ex_py": "Zhè ge xīngqī wǒ hěn máng.", "ex_en": "I am very busy this week.", "ex_th": "สัปดาห์นี้ฉันยุ่งมาก"},
    {"chapter_num": 7, "hanzi": "昨天", "pinyin": "zuótiān", "english": "yesterday", "thai": "เมื่อวาน", "pos": "n.", "ex_cn": "昨天是星期二。", "ex_py": "Zuótiān shì xīngqī'èr.", "ex_en": "Yesterday was Tuesday.", "ex_th": "เมื่อวานเป็นวันอังคาร"},
    {"chapter_num": 7, "hanzi": "明天", "pinyin": "míngtiān", "english": "tomorrow", "thai": "พรุ่งนี้", "pos": "n.", "ex_cn": "明天你有空吗？", "ex_py": "Míngtiān nǐ yǒu kòng ma?", "ex_en": "Do you have free time tomorrow?", "ex_th": "พรุ่งนี้เธอว่างไหม?"},
    {"chapter_num": 7, "hanzi": "学校", "pinyin": "xuéxiào", "english": "school", "thai": "โรงเรียน", "pos": "n.", "ex_cn": "我们学校很大。", "ex_py": "Wǒmen xuéxiào hěn dà.", "ex_en": "Our school is very large.", "ex_th": "โรงเรียนของพวกเราใหญ่มาก"},
    {"chapter_num": 7, "hanzi": "看", "pinyin": "kàn", "english": "to look, see, watch, read", "thai": "ดู, มอง, อ่าน", "pos": "v.", "ex_cn": "我在看一本中文书。", "ex_py": "Wǒ zài kàn yì běn Zhōngwén shū.", "ex_en": "I am reading a Chinese book.", "ex_th": "ฉันกำลังอ่านหนังสือภาษาจีนอยู่หนึ่งเล่ม"},
    {"chapter_num": 7, "hanzi": "书", "pinyin": "shū", "english": "book", "thai": "หนังสือ", "pos": "n.", "ex_cn": "桌子上有一本书。", "ex_py": "Zhuōzi shang yǒu yì běn shū.", "ex_en": "There is a book on the table.", "ex_th": "บนโต๊ะมีหนังสืออยู่หนึ่งเล่ม"},

    # Lesson 8: 我想喝茶
    {"chapter_num": 8, "hanzi": "想", "pinyin": "xiǎng", "english": "would like, want / to think", "thai": "อยาก, คิด", "pos": "v.", "ex_cn": "我想喝一杯茶。", "ex_py": "Wǒ xiǎng hē yì bēi chá.", "ex_en": "I would like to drink a cup of tea.", "ex_th": "ฉันอยากดื่มชาสักหนึ่งถ้วย"},
    {"chapter_num": 8, "hanzi": "喝", "pinyin": "hē", "english": "to drink", "thai": "ดื่ม", "pos": "v.", "ex_cn": "你要喝水吗？", "ex_py": "Nǐ yào hē shuǐ ma?", "ex_en": "Do you want to drink water?", "ex_th": "เธออยากดื่มน้ำไหม?"},
    {"chapter_num": 8, "hanzi": "茶", "pinyin": "chá", "english": "tea", "thai": "ชา", "pos": "n.", "ex_cn": "中国人很喜欢喝绿茶。", "ex_py": "Zhōngguórén hěn xǐhuan hē lǜchá.", "ex_en": "Chinese people like drinking green tea very much.", "ex_th": "คนจีนชอบดื่มชาเขียวมาก"},
    {"chapter_num": 8, "hanzi": "吃", "pinyin": "chī", "english": "to eat", "thai": "กิน, ทาน", "pos": "v.", "ex_cn": "你想吃什么？", "ex_py": "Nǐ xiǎng chī shénme?", "ex_en": "What do you want to eat?", "ex_th": "เธออยากกินอะไร?"},
    {"chapter_num": 8, "hanzi": "米饭", "pinyin": "mǐfàn", "english": "cooked rice", "thai": "ข้าวสวย", "pos": "n.", "ex_cn": "我吃了一碗米饭。", "ex_py": "Wǒ chī le yì wǎn mǐfàn.", "ex_en": "I ate a bowl of rice.", "ex_th": "ฉันกินข้าวสวยไปหนึ่งถ้วย"},
    {"chapter_num": 8, "hanzi": "下午", "pinyin": "xiàwǔ", "english": "afternoon", "thai": "ตอนบ่าย", "pos": "n.", "ex_cn": "今天下午我去买东西。", "ex_py": "Jīntiān xiàwǔ wǒ qù mǎi dōngxi.", "ex_en": "This afternoon I will go shopping.", "ex_th": "บ่ายวันนี้ฉันจะไปซื้อของ"},
    {"chapter_num": 8, "hanzi": "商店", "pinyin": "shāngdiàn", "english": "shop, store", "thai": "ร้านค้า", "pos": "n.", "ex_cn": "商店里有很多人。", "ex_py": "Shāngdiàn lǐ yǒu hěn duō rén.", "ex_en": "There are many people in the store.", "ex_th": "ในร้านค้ามีคนเยอะมาก"},
    {"chapter_num": 8, "hanzi": "买", "pinyin": "mǎi", "english": "to buy", "thai": "ซื้อ", "pos": "v.", "ex_cn": "我想买一个新杯子。", "ex_py": "Wǒ xiǎng mǎi yí ge xīn bēizi.", "ex_en": "I want to buy a new cup.", "ex_th": "ฉันอยากซื้อแก้วน้ำใบใหม่สักใบ"},
    {"chapter_num": 8, "hanzi": "个", "pinyin": "ge", "english": "general measure word", "thai": "อัน, ชิ้น, คน (ลักษณนามทั่วไป)", "pos": "m.", "ex_cn": "给我一个苹果吧。", "ex_py": "Gěi wǒ yí ge píngguǒ ba.", "ex_en": "Give me an apple please.", "ex_th": "ขอแอปเปิ้ลให้ฉันสักลูกเถอะ"},
    {"chapter_num": 8, "hanzi": "杯子", "pinyin": "bēizi", "english": "cup, glass", "thai": "แก้วน้ำ, ถ้วย", "pos": "n.", "ex_cn": "这个杯子多少钱？", "ex_py": "Zhè ge bēizi duōshao qián?", "ex_en": "How much is this cup?", "ex_th": "แก้วน้ำใบนี้ราคาเท่าไหร่?"},
    {"chapter_num": 8, "hanzi": "这", "pinyin": "zhè", "english": "this", "thai": "นี่, นี้", "pos": "pron.", "ex_cn": "这是我的汉语书。", "ex_py": "Zhè shì wǒ de Hànyǔ shū.", "ex_en": "This is my Chinese book.", "ex_th": "นี่คือหนังสือภาษาจีนของฉัน"},
    {"chapter_num": 8, "hanzi": "多少", "pinyin": "duōshao", "english": "how many, how much", "thai": "เท่าไหร่", "pos": "pron.", "ex_cn": "这个多少钱？", "ex_py": "Zhè ge duōshao qián?", "ex_en": "How much is this?", "ex_th": "อันนี้ราคาเท่าไหร่?"},
    {"chapter_num": 8, "hanzi": "钱", "pinyin": "qián", "english": "money", "thai": "เงิน", "pos": "n.", "ex_cn": "我没有多少钱。", "ex_py": "Wǒ méiyǒu duōshao qián.", "ex_en": "I don't have much money.", "ex_th": "ฉันไม่มีเงินเท่าไหร่"},
    {"chapter_num": 8, "hanzi": "块", "pinyin": "kuài", "english": "measure word for money (yuan) / piece", "thai": "หยวน (ภาษาพูด), ก้อน, ชิ้น", "pos": "m.", "ex_cn": "这本书二十块钱。", "ex_py": "Zhè běn shū èrshí kuài qián.", "ex_en": "This book costs 20 yuan.", "ex_th": "หนังสือเล่มนี้ราคา 20 หยวน"},
    {"chapter_num": 8, "hanzi": "那", "pinyin": "nà", "english": "that", "thai": "นั่น, นั้น", "pos": "pron.", "ex_cn": "那是谁的书？", "ex_py": "Nà shì shéi de shū?", "ex_en": "Whose book is that?", "ex_th": "นั่นคือหนังสือของใคร?"},

    # Lesson 9: 你儿子在哪儿工作
    {"chapter_num": 9, "hanzi": "小", "pinyin": "xiǎo", "english": "small, little, young", "thai": "เล็ก, น้อย", "pos": "adj.", "ex_cn": "这个小猫真可爱。", "ex_py": "Zhè ge xiǎo māo zhēn kě'ài.", "ex_en": "This little cat is really cute.", "ex_th": "ลูกแมวตัวนี้ช่างน่ารักจริงๆ"},
    {"chapter_num": 9, "hanzi": "猫", "pinyin": "māo", "english": "cat", "thai": "แมว", "pos": "n.", "ex_cn": "我的小猫在哪儿？", "ex_py": "Wǒ de xiǎo māo zài nǎr?", "ex_en": "Where is my kitten?", "ex_th": "ลูกแมวของฉันอยู่ที่ไหน?"},
    {"chapter_num": 9, "hanzi": "在", "pinyin": "zài", "english": "at, in, on / existing", "thai": "อยู่, ที่ (บอกตำแหน่ง)", "pos": "prep./v.", "ex_cn": "我在家看书。", "ex_py": "Wǒ zài jiā kàn shū.", "ex_en": "I am reading at home.", "ex_th": "ฉันอ่านหนังสืออยู่ที่บ้าน"},
    {"chapter_num": 9, "hanzi": "那儿", "pinyin": "nàr", "english": "there", "thai": "ที่นั่น", "pos": "pron.", "ex_cn": "那儿有一只狗。", "ex_py": "Nàr yǒu yì zhī gǒu.", "ex_en": "There is a dog over there.", "ex_th": "ตรงนั้นมีสุนัขอยู่หนึ่งตัว"},
    {"chapter_num": 9, "hanzi": "狗", "pinyin": "gǒu", "english": "dog", "thai": "สุนัข, หมา", "pos": "n.", "ex_cn": "我家有一只大狗。", "ex_py": "Wǒ jiā yǒu yì zhī dà gǒu.", "ex_en": "My family has a big dog.", "ex_th": "บ้านฉันมีสุนัขตัวใหญ่หนึ่งตัว"},
    {"chapter_num": 9, "hanzi": "椅", "pinyin": "yǐ", "english": "chair (in 椅子)", "thai": "เก้าอี้ (ใน 椅子)", "pos": "n.", "ex_cn": "坐在椅子上。", "ex_py": "Zuò zài yǐzi shang.", "ex_en": "Sit on the chair.", "ex_th": "นั่งลงบนเก้าอี้"},
    {"chapter_num": 9, "hanzi": "椅子", "pinyin": "yǐzi", "english": "chair", "thai": "เก้าอี้", "pos": "n.", "ex_cn": "椅子下有一只猫。", "ex_py": "Yǐzi xià yǒu yì zhī māo.", "ex_en": "There is a cat under the chair.", "ex_th": "ใต้เก้าอี้มีแมวอยู่ตัวหนึ่ง"},
    {"chapter_num": 9, "hanzi": "下面", "pinyin": "xiàmian", "english": "under, below", "thai": "ด้านล่าง, ข้างใต้", "pos": "n.", "ex_cn": "书在桌子下面。", "ex_py": "Shū zài zhuōzi xiàmian.", "ex_en": "The book is under the table.", "ex_th": "หนังสืออยู่ข้างใต้โต๊ะ"},
    {"chapter_num": 9, "hanzi": "哪儿", "pinyin": "nǎr", "english": "where", "thai": "ที่ไหน", "pos": "pron.", "ex_cn": "你在哪儿工作？", "ex_py": "Nǐ zài nǎr gōngzuò?", "ex_en": "Where do you work?", "ex_th": "เธอทำงานอยู่ที่ไหน?"},
    {"chapter_num": 9, "hanzi": "工作", "pinyin": "gōngzuò", "english": "job, work; to work", "thai": "ทำงาน, งาน", "pos": "v./n.", "ex_cn": "我爸爸在医院工作。", "ex_py": "Wǒ bàba zài yīyuàn gōngzuò.", "ex_en": "My father works at the hospital.", "ex_th": "พ่อของฉันทำงานอยู่ที่โรงพยาบาล"},
    {"chapter_num": 9, "hanzi": "儿子", "pinyin": "érzi", "english": "son", "thai": "ลูกชาย", "pos": "n.", "ex_cn": "他儿子是一名医生。", "ex_py": "Tā érzi shì yì míng yīshēng.", "ex_en": "His son is a doctor.", "ex_th": "ลูกชายของเขาเป็นหมอ"},
    {"chapter_num": 9, "hanzi": "医院", "pinyin": "yīyuàn", "english": "hospital", "thai": "โรงพยาบาล", "pos": "n.", "ex_cn": "我家离医院很近。", "ex_py": "Wǒ jiā lí yīyuàn hěn jìn.", "ex_en": "My home is very close to the hospital.", "ex_th": "บ้านของฉันอยู่ใกล้โรงพยาบาลมาก"},
    {"chapter_num": 9, "hanzi": "医生", "pinyin": "yīshēng", "english": "doctor", "thai": "หมอ, แพทย์", "pos": "n.", "ex_cn": "张医生很热情。", "ex_py": "Zhāng yīshēng hěn rèqíng.", "ex_en": "Doctor Zhang is very warm and friendly.", "ex_th": "คุณหมอจางมีความเป็นกันเองมาก"},
    {"chapter_num": 9, "hanzi": "爸爸", "pinyin": "bàba", "english": "father, dad", "thai": "พ่อ", "pos": "n.", "ex_cn": "我爸爸很喜欢中国茶。", "ex_py": "Wǒ bàba hěn xǐhuan Zhōngguó chá.", "ex_en": "My father likes Chinese tea very much.", "ex_th": "พ่อของฉันชอบดื่มชาจีนมาก"},

    # Lesson 10: 我能坐这儿吗
    {"chapter_num": 10, "hanzi": "桌子", "pinyin": "zhuōzi", "english": "desk, table", "thai": "โต๊ะ", "pos": "n.", "ex_cn": "桌子上放着一台电脑。", "ex_py": "Zhuōzi shang fàngzhe yì tái diànnǎo.", "ex_en": "A computer is placed on the desk.", "ex_th": "บนโต๊ะมีคอมพิวเตอร์วางอยู่หนึ่งเครื่อง"},
    {"chapter_num": 10, "hanzi": "上", "pinyin": "shàng", "english": "up, on, above", "thai": "บน, ข้างบน", "pos": "n./prep.", "ex_cn": "书在桌子上。", "ex_py": "Shū zài zhuōzi shang.", "ex_en": "The book is on the table.", "ex_th": "หนังสืออยู่บนโต๊ะ"},
    {"chapter_num": 10, "hanzi": "电脑", "pinyin": "diànnǎo", "english": "computer", "thai": "คอมพิวเตอร์", "pos": "n.", "ex_cn": "我想买一台新电脑。", "ex_py": "Wǒ xiǎng mǎi yì tái xīn diànnǎo.", "ex_en": "I want to buy a new computer.", "ex_th": "ฉันอยากซื้อคอมพิวเตอร์เครื่องใหม่สักเครื่อง"},
    {"chapter_num": 10, "hanzi": "和", "pinyin": "hé", "english": "and, with", "thai": "และ, กับ", "pos": "conj.", "ex_cn": "我和我朋友一起去。", "ex_py": "Wǒ hé wǒ péngyou yìqǐ qù.", "ex_en": "My friend and I are going together.", "ex_th": "ฉันกับเพื่อนไปด้วยกัน"},
    {"chapter_num": 10, "hanzi": "本", "pinyin": "běn", "english": "measure word for books", "thai": "เล่ม (ลักษณนามหนังสือ)", "pos": "m.", "ex_cn": "这里有两本书。", "ex_py": "Zhèlǐ yǒu liǎng běn shū.", "ex_en": "There are two books here.", "ex_th": "ตรงนี้มีหนังสือสองเล่ม"},
    {"chapter_num": 10, "hanzi": "里", "pinyin": "lǐ", "english": "inside, inner", "thai": "ใน, ด้านใน", "pos": "n.", "ex_cn": "房间里没有人。", "ex_py": "Fángjiān lǐ méiyǒu rén.", "ex_en": "There is no one inside the room.", "ex_th": "ในห้องไม่มีใครเลย"},
    {"chapter_num": 10, "hanzi": "前面", "pinyin": "qiánmian", "english": "front, ahead", "thai": "ด้านหน้า, ข้างหน้า", "pos": "n.", "ex_cn": "前面那个人是谁？", "ex_py": "Qiánmian nà ge rén shì shéi?", "ex_en": "Who is that person in front?", "ex_th": "คนที่อยู่ข้างหน้านั้นคือใคร?"},
    {"chapter_num": 10, "hanzi": "后面", "pinyin": "hòumian", "english": "back, behind", "thai": "ด้านหลัง, ข้างหลัง", "pos": "n.", "ex_cn": "学校后面有一个大公园。", "ex_py": "Xuéxiào hòumian yǒu yí ge dà gōngyuán.", "ex_en": "There is a big park behind the school.", "ex_th": "ด้านหลังโรงเรียนมีสวนสาธารณะขนาดใหญ่หนึ่งแห่ง"},
    {"chapter_num": 10, "hanzi": "这儿", "pinyin": "zhèr", "english": "here", "thai": "ที่นี่, ตรงนี้", "pos": "pron.", "ex_cn": "这儿的环境真好。", "ex_py": "Zhèr de huánjìng zhēn hǎo.", "ex_en": "The environment here is really nice.", "ex_th": "สิ่งแวดล้อมตรงนี้ดีจริงๆ"},
    {"chapter_num": 10, "hanzi": "没有", "pinyin": "méiyǒu", "english": "not have, there is not", "thai": "ไม่มี", "pos": "v.", "ex_cn": "这儿没有人坐。", "ex_py": "Zhèr méiyǒu rén zuò.", "ex_en": "No one is sitting here.", "ex_th": "ตรงนี้ไม่มีคนนั่ง"},
    {"chapter_num": 10, "hanzi": "能", "pinyin": "néng", "english": "can, be able to (permission)", "thai": "สามารถ, ได้ (อนุญาต)", "pos": "v.", "ex_cn": "我能坐这儿吗？", "ex_py": "Wǒ néng zuò zhèr ma?", "ex_en": "Can I sit here?", "ex_th": "ฉันขอนั่งตรงนี้ได้ไหม?"},
    {"chapter_num": 10, "hanzi": "坐", "pinyin": "zuò", "english": "to sit / to travel by", "thai": "นั่ง / โดยสาร", "pos": "v.", "ex_cn": "请坐，喝杯水吧。", "ex_py": "Qǐng zuò, hē bēi shuǐ ba.", "ex_en": "Please sit down and have a cup of water.", "ex_th": "เชิญนั่ง ดื่มน้ำสักแก้วก่อนนะ"},

    # Lesson 11: 现在几点
    {"chapter_num": 11, "hanzi": "现在", "pinyin": "xiànzài", "english": "now", "thai": "ตอนนี้, เดี๋ยวนี้", "pos": "n.", "ex_cn": "现在八点半了。", "ex_py": "Xiànzài bā diǎn bàn le.", "ex_en": "It is 8:30 now.", "ex_th": "ตอนนี้แปดโมงครึ่งแล้ว"},
    {"chapter_num": 11, "hanzi": "点", "pinyin": "diǎn", "english": "o'clock, dot, point", "thai": "โมง, นาฬิกา, จุด", "pos": "m./n.", "ex_cn": "我们九点去上课。", "ex_py": "Wǒmen jiǔ diǎn qù shàngkè.", "ex_en": "We go to class at 9 o'clock.", "ex_th": "พวกเราไปเข้าเรียนตอนเก้าโมง"},
    {"chapter_num": 11, "hanzi": "分", "pinyin": "fēn", "english": "minute", "thai": "นาที", "pos": "m.", "ex_cn": "差五分十点。", "ex_py": "Chà wǔ fēn shí diǎn.", "ex_en": "Five minutes to ten.", "ex_th": "อีกห้านาทีสิบโมง"},
    {"chapter_num": 11, "hanzi": "中午", "pinyin": "zhōngwǔ", "english": "noon, midday", "thai": "ตอนเที่ยง", "pos": "n.", "ex_cn": "中午我们一起吃午饭吧。", "ex_py": "Zhōngwǔ wǒmen yìqǐ chī wǔfàn ba.", "ex_en": "Let's have lunch together at noon.", "ex_th": "ตอนเที่ยงพวกเราไปกินข้าวกลางวันด้วยกันเถอะ"},
    {"chapter_num": 11, "hanzi": "吃饭", "pinyin": "chīfàn", "english": "to have a meal, eat food", "thai": "กินข้าว, รับประทานอาหาร", "pos": "v.", "ex_cn": "你吃饭了吗？", "ex_py": "Nǐ chīfàn le ma?", "ex_en": "Have you eaten?", "ex_th": "เธอกินข้าวหรือยัง?"},
    {"chapter_num": 11, "hanzi": "时候", "pinyin": "shíhou", "english": "time, moment", "thai": "เวลา, ตอนที่", "pos": "n.", "ex_cn": "你什么时候回家？", "ex_py": "Nǐ shénme shíhou huí jiā?", "ex_en": "When are you returning home?", "ex_th": "เธอจะกลับบ้านเมื่อไหร่?"},
    {"chapter_num": 11, "hanzi": "回", "pinyin": "huí", "english": "to return, go back", "thai": "กลับ", "pos": "v.", "ex_cn": "我想早点儿回宿舍。", "ex_py": "Wǒ xiǎng zǎodiǎnr huí sùshè.", "ex_en": "I want to go back to the dorm earlier.", "ex_th": "ฉันอยากกลับหอพักเร็วหน่อย"},
    {"chapter_num": 11, "hanzi": "我们", "pinyin": "wǒmen", "english": "we, us", "thai": "พวกเรา", "pos": "pron.", "ex_cn": "我们都是留学生。", "ex_py": "Wǒmen dōu shì liúxuéshēng.", "ex_en": "We are all international students.", "ex_th": "พวกเราล้วนเป็นนักเรียนต่างชาติ"},
    {"chapter_num": 11, "hanzi": "电影", "pinyin": "diànyǐng", "english": "movie, film", "thai": "ภาพยนตร์, หนัง", "pos": "n.", "ex_cn": "这部电影很好看。", "ex_py": "Zhè bù diànyǐng hěn hǎokàn.", "ex_en": "This movie is very good.", "ex_th": "หนังเรื่องนี้สนุกมาก"},
    {"chapter_num": 11, "hanzi": "住", "pinyin": "zhù", "english": "to live, stay", "thai": "พัก, อาศัยอยู่", "pos": "v.", "ex_cn": "你住在哪个城市？", "ex_py": "Nǐ zhù zài nǎ ge chéngshì?", "ex_en": "Which city do you live in?", "ex_th": "เธออาศัยอยู่ที่เมืองไหน?"},
    {"chapter_num": 11, "hanzi": "前", "pinyin": "qián", "english": "before, ago, front", "thai": "ก่อน, ข้างหน้า", "pos": "n.", "ex_cn": "三天前他出国了。", "ex_py": "Sān tiān qián tā chūguó le.", "ex_en": "He went abroad three days ago.", "ex_th": "เมื่อสามวันก่อนเขาเดินทางไปต่างประเทศแล้ว"},

    # Lesson 12: 明天天气怎么样
    {"chapter_num": 12, "hanzi": "天气", "pinyin": "tiānqì", "english": "weather", "thai": "สภาพอากาศ", "pos": "n.", "ex_cn": "今天天气非常晴朗。", "ex_py": "Jīntiān tiānqì fēicháng qínglǎng.", "ex_en": "The weather is very sunny today.", "ex_th": "วันนี้สภาพอากาศแจ่มใสมาก"},
    {"chapter_num": 12, "hanzi": "怎么样", "pinyin": "zěnmeyàng", "english": "how about, how is", "thai": "เป็นอย่างไรบ้าง", "pos": "pron.", "ex_cn": "你最近身体怎么样？", "ex_py": "Nǐ zuìjìn shēntǐ zěnmeyàng?", "ex_en": "How is your health recently?", "ex_th": "ช่วงนี้สุขภาพเธอเป็นอย่างไรบ้าง?"},
    {"chapter_num": 12, "hanzi": "太", "pinyin": "tài", "english": "too, extremely", "thai": "เกินไป, มาก", "pos": "adv.", "ex_cn": "今天太热了！", "ex_py": "Jīntiān tài rè le!", "ex_en": "Today is too hot!", "ex_th": "วันนี้ร้อนเกินไปแล้ว!"},
    {"chapter_num": 12, "hanzi": "热", "pinyin": "rè", "english": "hot, heat", "thai": "ร้อน", "pos": "adj.", "ex_cn": "夏天的北京很热。", "ex_py": "Xiàtiān de Běijīng hěn rè.", "ex_en": "Beijing in summer is very hot.", "ex_th": "ฤดูร้อนของปักกิ่งร้อนมาก"},
    {"chapter_num": 12, "hanzi": "冷", "pinyin": "lěng", "english": "cold", "thai": "หนาว, เย็น", "pos": "adj.", "ex_cn": "外面太冷了，穿件大衣吧。", "ex_py": "Wàimian tài lěng le, chuān jiàn dàyī ba.", "ex_en": "It's too cold outside, put on an overcoat.", "ex_th": "ข้างนอกหนาวเกินไป ใส่เสื้อโค้ตสักตัวเถอะ"},
    {"chapter_num": 12, "hanzi": "下雨", "pinyin": "xià yǔ", "english": "to rain", "thai": "ฝนตก", "pos": "v.", "ex_cn": "外面下雨了，带把伞吧。", "ex_py": "Wàimian xià yǔ le, dài bǎ sǎn ba.", "ex_en": "It's raining outside, bring an umbrella.", "ex_th": "ข้างนอกฝนตกแล้ว พกร่มไปด้วยนะ"},
    {"chapter_num": 12, "hanzi": "小姐", "pinyin": "xiǎojiě", "english": "Miss, young lady", "thai": "คุณผู้หญิง, นางสาว", "pos": "n.", "ex_cn": "李小姐在办公室吗？", "ex_py": "Lǐ xiǎojiě zài bàngōngshì ma?", "ex_en": "Is Miss Li in the office?", "ex_th": "คุณหลี่อยู่ในออฟฟิศไหม?"},
    {"chapter_num": 12, "hanzi": "来", "pinyin": "lái", "english": "to come, arrive", "thai": "มา", "pos": "v.", "ex_cn": "他明天来我家。", "ex_py": "Tā míngtiān lái wǒ jiā.", "ex_en": "He will come to my house tomorrow.", "ex_th": "พรุ่งนี้เขาจะมาบ้านฉัน"},
    {"chapter_num": 12, "hanzi": "身体", "pinyin": "shēntǐ", "english": "body, health", "thai": "ร่างกาย, สุขภาพ", "pos": "n.", "ex_cn": "多运动对身体好。", "ex_py": "Duō yùndòng duì shēntǐ hǎo.", "ex_en": "Exercising more is good for your health.", "ex_th": "ออกกำลังกายให้เยอะมีผลดีต่อสุขภาพ"},
    {"chapter_num": 12, "hanzi": "爱", "pinyin": "ài", "english": "to love, like", "thai": "รัก, ชอบ", "pos": "v.", "ex_cn": "我很爱我的家人。", "ex_py": "Wǒ hěn ài wǒ de jiārén.", "ex_en": "I love my family very much.", "ex_th": "ฉันรักคนในครอบครัวของฉันมาก"},
    {"chapter_num": 12, "hanzi": "些", "pinyin": "xiē", "english": "some, few (a measure of quantity)", "thai": "บ้าง, เหล่านี้ (บางส่วน)", "pos": "m.", "ex_cn": "多吃些水果吧。", "ex_py": "Duō chī xiē shuǐguǒ ba.", "ex_en": "Eat some more fruit.", "ex_th": "กินผลไม้เพิ่มอีกสักหน่อยเถอะ"},
    {"chapter_num": 12, "hanzi": "水果", "pinyin": "shuǐguǒ", "english": "fruit", "thai": "ผลไม้", "pos": "n.", "ex_cn": "水果非常新鲜。", "ex_py": "Shuǐguǒ fēicháng xīnxiān.", "ex_en": "The fruit is extremely fresh.", "ex_th": "ผลไม้สดใหม่มากๆ"},
    {"chapter_num": 12, "hanzi": "水", "pinyin": "shuǐ", "english": "water", "thai": "น้ำ", "pos": "n.", "ex_cn": "每天要多喝水。", "ex_py": "Měitiān yào duō hē shuǐ.", "ex_en": "Drink plenty of water every day.", "ex_th": "ทุกวันต้องดื่มน้ำเยอะๆ"},

    # Lesson 13: 他在学做中国菜呢
    {"chapter_num": 13, "hanzi": "喂", "pinyin": "wèi", "english": "hello (on phone), hey", "thai": "ฮัลโหล (รับสายโทรศัพท์)", "pos": "int.", "ex_cn": "喂，请问王老师在吗？", "ex_py": "Wèi, qǐngwèn Wáng lǎoshī zài ma?", "ex_en": "Hello, is Teacher Wang there?", "ex_th": "ฮัลโหล ขอถามหน่อยอาจารย์หวังอยู่ไหมครับ?"},
    {"chapter_num": 13, "hanzi": "也", "pinyin": "yě", "english": "also, too", "thai": "ก็...เช่นกัน, ด้วย", "pos": "adv.", "ex_cn": "我也很喜欢学中文。", "ex_py": "Wǒ yě hěn xǐhuan xué Zhōngwén.", "ex_en": "I also like learning Chinese very much.", "ex_th": "ฉันก็ชอบเรียนภาษาจีนมากเช่นกัน"},
    {"chapter_num": 13, "hanzi": "学习", "pinyin": "xuéxí", "english": "to study, learn", "thai": "เรียน, ศึกษา", "pos": "v.", "ex_cn": "努力学习就会进步。", "ex_py": "Nǔlì xuéxí jiù huì jìnbù.", "ex_en": "Studying hard leads to progress.", "ex_th": "ขยันเรียนรู้ก็จะก้าวหน้า"},
    {"chapter_num": 13, "hanzi": "上午", "pinyin": "shàngwǔ", "english": "morning (late morning)", "thai": "ตอนสาย, ช่วงเช้า", "pos": "n.", "ex_cn": "上午我有两节课。", "ex_py": "Shàngwǔ wǒ yǒu liǎng jié kè.", "ex_en": "I have two classes in the morning.", "ex_th": "ช่วงเช้าฉันมีเรียนสองคาบ"},
    {"chapter_num": 13, "hanzi": "睡觉", "pinyin": "shuìjiào", "english": "to sleep, go to bed", "thai": "นอนหลับ", "pos": "v.", "ex_cn": "早点儿睡觉对身体好。", "ex_py": "Zǎodiǎnr shuìjiào duì shēntǐ hǎo.", "ex_en": "Sleeping earlier is good for health.", "ex_th": "เข้านอนแต่หัวค่ำดีต่อสุขภาพ"},
    {"chapter_num": 13, "hanzi": "电视", "pinyin": "diànshì", "english": "television, TV", "thai": "โทรทัศน์, ทีวี", "pos": "n.", "ex_cn": "他正在看电视。", "ex_py": "Tā zhèngzài kàn diànshì.", "ex_en": "He is watching TV right now.", "ex_th": "เขากำลังดูทีวีอยู่"},
    {"chapter_num": 13, "hanzi": "喜欢", "pinyin": "xǐhuan", "english": "to like, love", "thai": "ชอบ", "pos": "v.", "ex_cn": "你喜欢踢足球吗？", "ex_py": "Nǐ xǐhuan tī zúqiú ma?", "ex_en": "Do you like playing soccer?", "ex_th": "เธอชอบเตะฟุตบอลไหม?"},
    {"chapter_num": 13, "hanzi": "给", "pinyin": "gěi", "english": "to give / to, for", "thai": "ให้, แก่, แด่", "pos": "v./prep.", "ex_cn": "请给我一杯咖啡。", "ex_py": "Qǐng gěi wǒ yì bēi kāfēi.", "ex_en": "Please give me a cup of coffee.", "ex_th": "ขอให้กาแฟฉันสักแก้วนะ"},
    {"chapter_num": 13, "hanzi": "打电话", "pinyin": "dǎ diànhuà", "english": "to make a phone call", "thai": "โทรศัพท์", "pos": "v.", "ex_cn": "我晚上给你打电话。", "ex_py": "Wǒ wǎnshang gěi nǐ dǎ diànhuà.", "ex_en": "I will call you tonight.", "ex_th": "ตอนค่ำฉันจะโทรหาเธอนะ"},
    {"chapter_num": 13, "hanzi": "吧", "pinyin": "ba", "english": "modal particle for suggestion/consultation", "thai": "เถอะ, นะ (ชักชวน/ปรึกษา)", "pos": "part.", "ex_cn": "我们一起去吃饭吧！", "ex_py": "Wǒmen yìqǐ qù chīfàn ba!", "ex_en": "Let's go have a meal together!", "ex_th": "พวกเราไปกินข้าวด้วยกันเถอะ!"},

    # Lesson 14: 她买了不少衣服
    {"chapter_num": 14, "hanzi": "东西", "pinyin": "dōngxi", "english": "thing, stuff, object", "thai": "สิ่งของ, ของ", "pos": "n.", "ex_cn": "你买什么东西了？", "ex_py": "Nǐ mǎi shénme dōngxi le?", "ex_en": "What things did you buy?", "ex_th": "เธอซื้อสิ่งของอะไรมาบ้าง?"},
    {"chapter_num": 14, "hanzi": "一点儿", "pinyin": "yìdiǎnr", "english": "a little bit", "thai": "นิดหน่อย, สักเล็กน้อย", "pos": "m.", "ex_cn": "我想喝一点儿水。", "ex_py": "Wǒ xiǎng hē yìdiǎnr shuǐ.", "ex_en": "I'd like to drink a little water.", "ex_th": "ฉันอยากดื่มน้ำสักเล็กน้อย"},
    {"chapter_num": 14, "hanzi": "苹果", "pinyin": "píngguǒ", "english": "apple", "thai": "แอปเปิ้ล", "pos": "n.", "ex_cn": "苹果很甜很好吃。", "ex_py": "Píngguǒ hěn tián hěn hǎochī.", "ex_en": "The apples are very sweet and tasty.", "ex_th": "แอปเปิ้ลหวานและอร่อยมาก"},
    {"chapter_num": 14, "hanzi": "看见", "pinyin": "kànjiàn", "english": "to see, catch sight of", "thai": "มองเห็น, เห็น", "pos": "v.", "ex_cn": "你看见我的手机了吗？", "ex_py": "Nǐ kànjiàn wǒ de shǒujī le ma?", "ex_en": "Have you seen my phone?", "ex_th": "เธอเห็นโทรศัพท์มือถือของฉันไหม?"},
    {"chapter_num": 14, "hanzi": "先生", "pinyin": "xiānsheng", "english": "Mr., sir, husband", "thai": "คุณผู้ชาย, นาย, สามี", "pos": "n.", "ex_cn": "张先生是我们的经理。", "ex_py": "Zhāng xiānsheng shì wǒmen de jīnglǐ.", "ex_en": "Mr. Zhang is our manager.", "ex_th": "คุณจางเป็นผู้จัดการของพวกเรา"},
    {"chapter_num": 14, "hanzi": "开", "pinyin": "kāi", "english": "to open, drive", "thai": "เปิด, ขับ (รถ)", "pos": "v.", "ex_cn": "他会开车。", "ex_py": "Tā huì kāichē.", "ex_en": "He can drive a car.", "ex_th": "เขาขับรถเป็น"},
    {"chapter_num": 14, "hanzi": "车", "pinyin": "chē", "english": "vehicle, car", "thai": "รถ, รถยนต์", "pos": "n.", "ex_cn": "路上的车很多。", "ex_py": "Lù shang de chē hěn duō.", "ex_en": "There are many cars on the road.", "ex_th": "บนถนนมีรถเยอะมาก"},
    {"chapter_num": 14, "hanzi": "回来", "pinyin": "huílái", "english": "to return, come back", "thai": "กลับมา", "pos": "v.", "ex_cn": "他四点就回来了。", "ex_py": "Tā sì diǎn jiù huílái le.", "ex_en": "He came back at 4 o'clock already.", "ex_th": "สี่โมงเขาก็กลับมาแล้ว"},
    {"chapter_num": 14, "hanzi": "分钟", "pinyin": "fēnzhōng", "english": "minute (duration)", "thai": "นาที (หน่วยเวลา)", "pos": "n.", "ex_cn": "我等了你二十分钟。", "ex_py": "Wǒ děng le nǐ èrshí fēnzhōng.", "ex_en": "I waited for you for twenty minutes.", "ex_th": "ฉันรอเธอมา 20 นาทีแล้ว"},
    {"chapter_num": 14, "hanzi": "后", "pinyin": "hòu", "english": "after, afterwards, behind", "thai": "หลัง, หลังจาก", "pos": "n.", "ex_cn": "五分钟后出发。", "ex_py": "Wǔ fēnzhōng hòu chūfā.", "ex_en": "Depart in five minutes.", "ex_th": "อีก 5 นาทีจะออกเดินทาง"},
    {"chapter_num": 14, "hanzi": "衣服", "pinyin": "yīfu", "english": "clothes, clothing", "thai": "เสื้อผ้า", "pos": "n.", "ex_cn": "这件衣服真漂亮。", "ex_py": "Zhè jiàn yīfu zhēn piàoliang.", "ex_en": "This piece of clothing is really pretty.", "ex_th": "เสื้อผ้าชุดนี้สวยจริงๆ"},
    {"chapter_num": 14, "hanzi": "漂亮", "pinyin": "piàoliang", "english": "pretty, beautiful", "thai": "สวย, สวยงาม", "pos": "adj.", "ex_cn": "今天你真漂亮！", "ex_py": "Jīntiān nǐ zhēn piàoliang!", "ex_en": "You look really pretty today!", "ex_th": "วันนี้เธอดูสวยจังเลย!"},
    {"chapter_num": 14, "hanzi": "啊", "pinyin": "a", "english": "modal particle expressing affirmation/delight", "thai": "นะ, สินะ (คำช่วยเสริมน้ำเสียง)", "pos": "part.", "ex_cn": "这里的风景真好啊！", "ex_py": "Zhèlǐ de fēngjǐng zhēn hǎo a!", "ex_en": "The scenery here is truly wonderful!", "ex_th": "วิวทิวทัศน์ที่นี่ดีจังเลยนะ!"},
    {"chapter_num": 14, "hanzi": "少", "pinyin": "shǎo", "english": "few, little, less", "thai": "น้อย", "pos": "adj.", "ex_cn": "今天来的人很少。", "ex_py": "Jīntiān lái de rén hěn shǎo.", "ex_en": "Very few people came today.", "ex_th": "วันนี้มีคนมาน้อยมาก"},
    {"chapter_num": 14, "hanzi": "不少", "pinyin": "bù shǎo", "english": "quite a few, a lot", "thai": "ไม่น้อย, ค่อนข้างเยอะ", "pos": "phrase", "ex_cn": "他买了不少东西。", "ex_py": "Tā mǎi le bù shǎo dōngxi.", "ex_en": "He bought quite a lot of things.", "ex_th": "เขาซื้อของมาไม่น้อยเลย"},

    # Lesson 15: 我是坐飞机来的
    {"chapter_num": 15, "hanzi": "认识", "pinyin": "rènshi", "english": "to know, recognize, meet", "thai": "รู้จัก", "pos": "v.", "ex_cn": "很高兴认识你！", "ex_py": "Hěn gāoxìng rènshi nǐ!", "ex_en": "Very pleased to meet you!", "ex_th": "ยินดีมากที่ได้รู้จักเธอ!"},
    {"chapter_num": 15, "hanzi": "年", "pinyin": "nián", "english": "year", "thai": "ปี", "pos": "n.", "ex_cn": "我学汉语学了一年。", "ex_py": "Wǒ xué Hànyǔ xué le yì nián.", "ex_en": "I studied Chinese for a year.", "ex_th": "ฉันเรียนภาษาจีนมาได้หนึ่งปีแล้ว"},
    {"chapter_num": 15, "hanzi": "大学", "pinyin": "dàxué", "english": "university, college", "thai": "มหาวิทยาลัย", "pos": "n.", "ex_cn": "他是北京大学的学生。", "ex_py": "Tā shì Běijīng Dàxué de xuésheng.", "ex_en": "He is a student at Peking University.", "ex_th": "เขาเป็นนักศึกษามหาวิทยาลัยปักกิ่ง"},
    {"chapter_num": 15, "hanzi": "饭店", "pinyin": "fàndiàn", "english": "restaurant, hotel", "thai": "ร้านอาหาร, ภัตตาคาร", "pos": "n.", "ex_cn": "我们在饭店门口见。", "ex_py": "Wǒmen zài fàndiàn ménkǒu jiàn.", "ex_en": "Let's meet at the entrance of the restaurant.", "ex_th": "พวกเราเจอกันตรงทางเข้าร้านอาหารนะ"},
    {"chapter_num": 15, "hanzi": "出租车", "pinyin": "chūzūchē", "english": "taxi", "thai": "รถแท็กซี่", "pos": "n.", "ex_cn": "坐出租车很方便。", "ex_py": "Zuò chūzūchē hěn fāngbiàn.", "ex_en": "Taking a taxi is very convenient.", "ex_th": "นั่งรถแท็กซี่สะดวกมาก"},
    {"chapter_num": 15, "hanzi": "一起", "pinyin": "yìqǐ", "english": "together", "thai": "ด้วยกัน, พร้อมกัน", "pos": "adv.", "ex_cn": "我们一起去公园散步吧。", "ex_py": "Wǒmen yìqǐ qù gōngyuán sànbù ba.", "ex_en": "Let's go take a walk in the park together.", "ex_th": "พวกเราไปเดินเล่นที่สวนสาธารณะด้วยกันเถอะ"},
    {"chapter_num": 15, "hanzi": "高兴", "pinyin": "gāoxìng", "english": "happy, glad", "thai": "ดีใจ, มีความสุข", "pos": "adj.", "ex_cn": "今天大家都很高兴。", "ex_py": "Jīntiān dàjiā dōu hěn gāoxìng.", "ex_en": "Everyone is very happy today.", "ex_th": "วันนี้ทุกคนต่างดีใจมาก"},
    {"chapter_num": 15, "hanzi": "听", "pinyin": "tīng", "english": "to listen, hear", "thai": "ฟัง", "pos": "v.", "ex_cn": "我喜欢听中国音乐。", "ex_py": "Wǒ xǐhuan tīng Zhōngguó yīnyuè.", "ex_en": "I like listening to Chinese music.", "ex_th": "ฉันชอบฟังเพลงจีน"},
    {"chapter_num": 15, "hanzi": "飞机", "pinyin": "fēijī", "english": "airplane", "thai": "เครื่องบิน", "pos": "n.", "ex_cn": "坐飞机两个小时就到了。", "ex_py": "Zuò fēijī liǎng ge xiǎoshí jiù dào le.", "ex_en": "Taking an airplane takes just two hours.", "ex_th": "นั่งเครื่องบินสองชั่วโมงก็ถึงแล้ว"}
]

hsk1_sentences = [
    # Lesson 1
    {"chapter_num": 1, "context": "การทักทายระหว่างอาจารย์และนักเรียน", "hanzi": "老师，您好！", "pinyin": "Lǎoshī, nín hǎo!", "english": "Teacher, hello!", "thai": "คุณครู สวัสดีครับ/ค่ะ!", "cloze_target": "您", "cloze_hint_en": "you (polite)", "cloze_hint_th": "ท่าน (คำสุภาพ)", "grammar_en": "Polite pronoun 您", "grammar_th": "คำสรรพนามสุภาพ 您"},
    {"chapter_num": 1, "context": "การตอบรับเมื่ออีกฝ่ายกล่าวขอโทษ", "hanzi": "没关系，请进！", "pinyin": "Méi guānxi, qǐng jìn!", "english": "It doesn't matter, please come in!", "thai": "ไม่เป็นไร เชิญเข้ามาเลย!", "cloze_target": "没关系", "cloze_hint_en": "it doesn't matter", "cloze_hint_th": "ไม่เป็นไร", "grammar_en": "Response to apologies", "grammar_th": "การตอบรับคำขอโทษ"},

    # Lesson 2
    {"chapter_num": 2, "context": "การตอบรับคำขอบคุณ", "hanzi": "不客气，不用谢。", "pinyin": "Bú kèqi, búyòng xiè.", "english": "You're welcome, no need to thank.", "thai": "ไม่ต้องเกรงใจ ไม่ต้องขอบคุณหรอก", "cloze_target": "不客气", "cloze_hint_en": "you're welcome", "cloze_hint_th": "ไม่ต้องเกรงใจ", "grammar_en": "Response to thanks", "grammar_th": "การตอบรับคำขอบคุณ"},
    {"chapter_num": 2, "context": "การกล่าวคำลาก่อนแยกย้าย", "hanzi": "明天见，再见！", "pinyin": "Míngtiān jiàn, zàijiàn!", "english": "See you tomorrow, goodbye!", "thai": "เจอกันพรุ่งนี้นะ ลาก่อน!", "cloze_target": "再见", "cloze_hint_en": "goodbye", "cloze_hint_th": "ลาก่อน", "grammar_en": "Farewell phrase", "grammar_th": "คำกล่าวลา"},

    # Lesson 3
    {"chapter_num": 3, "context": "การถามชื่อเพื่อนใหม่", "hanzi": "你叫什么名字？", "pinyin": "Nǐ jiào shénme míngzi?", "english": "What is your name?", "thai": "เธอชื่ออะไร?", "cloze_target": "什么", "cloze_hint_en": "what", "cloze_hint_th": "อะไร", "grammar_en": "Question with 什么", "grammar_th": "ประโยคคำถามด้วย 什么"},
    {"chapter_num": 3, "context": "การบอกสัญชาติของตนเอง", "hanzi": "我是中国人。", "pinyin": "Wǒ shì Zhōngguórén.", "english": "I am Chinese.", "thai": "ฉันเป็นคนจีน", "cloze_target": "是", "cloze_hint_en": "to be", "cloze_hint_th": "เป็น/คือ", "grammar_en": "“是” sentence", "grammar_th": "ประโยค “是” บ่งบอกสถานะ"},

    # Lesson 4
    {"chapter_num": 4, "context": "การแนะนำคุณครูภาษาจีน", "hanzi": "她是我的汉语老师。", "pinyin": "Tā shì wǒ de Hànyǔ lǎoshī.", "english": "She is my Chinese teacher.", "thai": "เธอคือครูสอนภาษาจีนของฉัน", "cloze_target": "的", "cloze_hint_en": "possessive particle", "cloze_hint_th": "ของ", "grammar_en": "Possessive particle 的", "grammar_th": "คำช่วยแสดงความเป็นเจ้าของ 的"},
    {"chapter_num": 4, "context": "การถามย้อนกลับไปยังคู่สนทนา", "hanzi": "我是美国人，你呢？", "pinyin": "Wǒ shì Měiguórén, nǐ ne?", "english": "I am American, and you?", "thai": "ฉันเป็นคนอเมริกัน แล้วเธอล่ะ?", "cloze_target": "呢", "cloze_hint_en": "follow-up particle", "cloze_hint_th": "แล้ว...ล่ะ?", "grammar_en": "Follow-up question with 呢", "grammar_th": "คำช่วยคำถามย้อน 呢"},

    # Lesson 5
    {"chapter_num": 5, "context": "การบอกจำนวนสมาชิกในครอบครัว", "hanzi": "我家有四口人。", "pinyin": "Wǒ jiā yǒu sì kǒu rén.", "english": "There are four people in my family.", "thai": "บ้านฉันมีสมาชิก 4 คน", "cloze_target": "口", "cloze_hint_en": "measure word for family", "cloze_hint_th": "คน (ลักษณนามครอบครัว)", "grammar_en": "Measure word 口 for family", "grammar_th": "ลักษณนาม 口 สำหรับสมาชิกครอบครัว"},
    {"chapter_num": 5, "context": "การบอกอายุในปัจจุบัน", "hanzi": "她女儿今年二十岁。", "pinyin": "Tā nǚ'ér jīnnián èrshí suì.", "english": "Her daughter is 20 years old this year.", "thai": "ลูกสาวของเธอปีนี้อายุ 20 ปี", "cloze_target": "岁", "cloze_hint_en": "years old", "cloze_hint_th": "ปี (อายุ)", "grammar_en": "Expressing age with 岁", "grammar_th": "โครงสร้างบอกอายุด้วย 岁"},

    # Lesson 6
    {"chapter_num": 6, "context": "การบอกทักษะภาษาจีนที่เรียนรู้มา", "hanzi": "我会说汉语，也会写汉字。", "pinyin": "Wǒ huì shuō Hànyǔ, yě huì xiě hànzì.", "english": "I can speak Chinese and also write Chinese characters.", "thai": "ฉันพูดภาษาจีนเป็น และเขียนอักษรจีนเป็นด้วย", "cloze_target": "会", "cloze_hint_en": "can / know how to", "cloze_hint_th": "ทำเป็น (จากฝึกฝน)", "grammar_en": "Auxiliary verb 会", "grammar_th": "กริยานุเคราะห์ 会"},
    {"chapter_num": 6, "context": "การถามวิธีการเขียนตัวอักษร", "hanzi": "这个汉字怎么写？", "pinyin": "Zhè ge hànzì zěnme xiě?", "english": "How do you write this Chinese character?", "thai": "ตัวอักษรจีนตัวนี้เขียนอย่างไร?", "cloze_target": "怎么", "cloze_hint_en": "how", "cloze_hint_th": "อย่างไร", "grammar_en": "Interrogative 怎么", "grammar_th": "สรรพนามคำถาม 怎么 ถามวิธีทำ"},

    # Lesson 7
    {"chapter_num": 7, "context": "การถามวันที่ในปัจจุบัน", "hanzi": "请问，今天几号？", "pinyin": "Qǐngwèn, jīntiān jǐ hào?", "english": "Excuse me, what is today's date?", "thai": "ขอถามหน่อย วันนี้วันที่เท่าไหร่?", "cloze_target": "几", "cloze_hint_en": "how many (date)", "cloze_hint_th": "กี่/เท่าไหร่", "grammar_en": "Asking date with 几号", "grammar_th": "การถามวันที่ด้วย 几号"},
    {"chapter_num": 7, "context": "การบอกวันในสัปดาห์", "hanzi": "明天是星期五，我去学校看书。", "pinyin": "Míngtiān shì xīngqīwǔ, wǒ qù xuéxiào kàn shū.", "english": "Tomorrow is Friday, I am going to school to read.", "thai": "พรุ่งนี้เป็นวันศุกร์ ฉันจะไปโรงเรียนเพื่ออ่านหนังสือ", "cloze_target": "星期", "cloze_hint_en": "week / day", "cloze_hint_th": "สัปดาห์/วัน", "grammar_en": "Days of the week", "grammar_th": "การบอกวันในสัปดาห์ 星期"},

    # Lesson 8
    {"chapter_num": 8, "context": "การสั่งเครื่องดื่มที่ต้องการ", "hanzi": "我想喝一杯中国茶。", "pinyin": "Wǒ xiǎng hē yì bēi Zhōngguó chá.", "english": "I would like to drink a cup of Chinese tea.", "thai": "ฉันอยากดื่มชาจีนสักหนึ่งแก้ว", "cloze_target": "想", "cloze_hint_en": "would like", "cloze_hint_th": "อยาก/คิดจะ", "grammar_en": "Auxiliary verb 想", "grammar_th": "กริยานุเคราะห์ 想"},
    {"chapter_num": 8, "context": "การถามราคาของสินค้า", "hanzi": "这个杯子多少钱？", "pinyin": "Zhè ge bēizi duōshao qián?", "english": "How much is this cup?", "thai": "แก้วน้ำใบนี้ราคาเท่าไหร่?", "cloze_target": "多少", "cloze_hint_en": "how much", "cloze_hint_th": "เท่าไหร่", "grammar_en": "Asking price with 多少钱", "grammar_th": "การถามราคาด้วย 多少钱"},

    # Lesson 9
    {"chapter_num": 9, "context": "การระบุตำแหน่งของสิ่งของ", "hanzi": "小猫在椅子下面呢。", "pinyin": "Xiǎo māo zài yǐzi xiàmian ne.", "english": "The kitten is under the chair.", "thai": "ลูกแมวอยู่ข้างใต้เก้าอี้แน่ะ", "cloze_target": "在", "cloze_hint_en": "at / in / on", "cloze_hint_th": "อยู่/ที่", "grammar_en": "Preposition 在 for location", "grammar_th": "คำบุพบท 在 ระบุตำแหน่ง"},
    {"chapter_num": 9, "context": "การถามสถานที่ทำงานของบุคคล", "hanzi": "你儿子在哪儿工作？", "pinyin": "Nǐ érzi zài nǎr gōngzuò?", "english": "Where does your son work?", "thai": "ลูกชายของเธอทำงานอยู่ที่ไหน?", "cloze_target": "哪儿", "cloze_hint_en": "where", "cloze_hint_th": "ที่ไหน", "grammar_en": "Location question with 哪儿", "grammar_th": "การถามสถานที่ด้วย 哪儿"},

    # Lesson 10
    {"chapter_num": 10, "context": "การขออนุญาตอย่างสุภาพ", "hanzi": "请问，我能坐这儿吗？", "pinyin": "Qǐngwèn, wǒ néng zuò zhèr ma?", "english": "Excuse me, can I sit here?", "thai": "ขอถามหน่อย ฉันขอนั่งตรงนี้ได้ไหม?", "cloze_target": "能", "cloze_hint_en": "can (permission)", "cloze_hint_th": "สามารถ/ได้", "grammar_en": "Modal verb 能 for permission", "grammar_th": "กริยานุเคราะห์ 能 ขออนุญาต"},
    {"chapter_num": 10, "context": "การบอกสิ่งของที่วางอยู่บนโต๊ะ", "hanzi": "桌子上有一台电脑和一本书。", "pinyin": "Zhuōzi shang yǒu yì tái diànnǎo hé yì běn shū.", "english": "There is a computer and a book on the desk.", "thai": "บนโต๊ะมีคอมพิวเตอร์เครื่องหนึ่งและหนังสือเล่มหนึ่ง", "cloze_target": "上", "cloze_hint_en": "on / above", "cloze_hint_th": "บน", "grammar_en": "Location word 上", "grammar_th": "คำบอกทิศทาง 上 (บน)"},

    # Lesson 11
    {"chapter_num": 11, "context": "การถามเวลาปัจจุบัน", "hanzi": "请问，现在几点？", "pinyin": "Qǐngwèn, xiànzài jǐ diǎn?", "english": "Excuse me, what time is it now?", "thai": "ขอถามหน่อย ตอนนี้กี่โมงแล้ว?", "cloze_target": "点", "cloze_hint_en": "o'clock", "cloze_hint_th": "โมง", "grammar_en": "Telling time with 点", "grammar_th": "การบอกเวลาด้วย 点"},
    {"chapter_num": 11, "context": "การนัดหมายช่วงเวลาในแต่ละวัน", "hanzi": "我们中午十二点去吃饭吧。", "pinyin": "Wǒmen zhōngwǔ shí'èr diǎn qù chīfàn ba.", "english": "Let's go eat lunch at 12:00 noon.", "thai": "พวกเราไปกินข้าวตอนเที่ยงสิบสองนาฬิกากันเถอะ", "cloze_target": "中午", "cloze_hint_en": "noon", "cloze_hint_th": "ตอนเที่ยง", "grammar_en": "Time words as adverbials", "grammar_th": "คำบอกเวลาทำหน้าที่ขยายกริยา"},

    # Lesson 12
    {"chapter_num": 12, "context": "การถามสภาพอากาศของวันพรุ่งนี้", "hanzi": "明天天气怎么样？", "pinyin": "Míngtiān tiānqì zěnmeyàng?", "english": "How will the weather be tomorrow?", "thai": "พรุ่งนี้สภาพอากาศเป็นอย่างไรบ้าง?", "cloze_target": "怎么样", "cloze_hint_en": "how is it", "cloze_hint_th": "เป็นอย่างไรบ้าง", "grammar_en": "Question with 怎么样", "grammar_th": "การถามสภาพด้วย 怎么样"},
    {"chapter_num": 12, "context": "การแสดงความรู้สึกว่าร้อนมากเกินไป", "hanzi": "今天太热了，多喝点儿水吧。", "pinyin": "Jīntiān tài rè le, duō hē diǎnr shuǐ ba.", "english": "It is too hot today, drink more water.", "thai": "วันนี้ร้อนเกินไปแล้ว ดื่มน้ำเยอะๆ หน่อยนะ", "cloze_target": "太", "cloze_hint_en": "too / extremely", "cloze_hint_th": "เกินไป/มาก", "grammar_en": "Pattern 太...了", "grammar_th": "โครงสร้าง 太……了"},

    # Lesson 13
    {"chapter_num": 13, "context": "การบอกสิ่งที่กำลังทำอยู่ในขณะนั้น", "hanzi": "他在学做中国菜呢。", "pinyin": "Tā zài xué zuò Zhōngguó cài ne.", "english": "He is learning to cook Chinese food.", "thai": "เขากำลังเรียนทำอาหารจีนอยู่", "cloze_target": "在", "cloze_hint_en": "in progress", "cloze_hint_th": "กำลัง...อยู่", "grammar_en": "Progressive aspect 在...呢", "grammar_th": "โครงสร้างแสดงการกระทำต่อเนื่อง 在……呢"},
    {"chapter_num": 13, "context": "การบอกว่าจะติดต่อกลับทางโทรศัพท์", "hanzi": "我晚上给你打电话吧。", "pinyin": "Wǒ wǎnshang gěi nǐ dǎ diànhuà ba.", "english": "I will call you on the phone tonight.", "thai": "ตอนค่ำฉันค่อยโทรหาเธอนะ", "cloze_target": "给", "cloze_hint_en": "to / for", "cloze_hint_th": "ให้/แก่", "grammar_en": "Preposition 给 in 给...打电话", "grammar_th": "โครงสร้าง 给……打电话"},

    # Lesson 14
    {"chapter_num": 14, "context": "การบอกการซื้อของที่เสร็จสิ้นแล้ว", "hanzi": "她在商店买了不少新衣服。", "pinyin": "Tā zài shāngdiàn mǎi le bù shǎo xīn yīfu.", "english": "She bought quite a few new clothes at the store.", "thai": "เธอซื้อเสื้อผ้าใหม่มาไม่น้อยเลยที่ร้านค้า", "cloze_target": "了", "cloze_hint_en": "completion particle", "cloze_hint_th": "แล้ว (เสร็จสิ้น)", "grammar_en": "Aspect particle 了", "grammar_th": "คำช่วยกริยาแสดงการเสร็จสิ้น 了"},
    {"chapter_num": 14, "context": "การกะระยะเวลาก่อนทำกิจกรรม", "hanzi": "四十分钟后他才能回来。", "pinyin": "Sìshí fēnzhōng hòu tā cái néng huílái.", "english": "Only after 40 minutes can he come back.", "thai": "อีก 40 นาทีเขาถึงจะกลับมาได้", "cloze_target": "后", "cloze_hint_en": "after", "cloze_hint_th": "หลังจาก", "grammar_en": "Time word 后", "grammar_th": "การบอกเวลา ...后 (หลังจาก...)"},

    # Lesson 15
    {"chapter_num": 15, "context": "การเน้นย้ำวิธีการเดินทางที่เกิดขึ้นแล้ว", "hanzi": "我们是坐飞机来北京的。", "pinyin": "Wǒmen shì zuò fēijī lái Běijīng de.", "english": "We came to Beijing by airplane.", "thai": "พวกเรานั่งเครื่องบินมาปักกิ่ง", "cloze_target": "是", "cloze_hint_en": "emphatic is", "cloze_hint_th": "คือ (เน้นย้ำ)", "grammar_en": "Emphatic 是...的 structure", "grammar_th": "โครงสร้างเน้นย้ำ 是……的"},
    {"chapter_num": 15, "context": "การกล่าวแสดงความยินดีที่ได้รู้จัก", "hanzi": "很高兴在大学里认识你！", "pinyin": "Hěn gāoxìng zài dàxué lǐ rènshi nǐ!", "english": "Very pleased to meet you in university!", "thai": "ดีใจมากที่ได้รู้จักเธอในมหาวิทยาลัย!", "cloze_target": "认识", "cloze_hint_en": "to meet / know", "cloze_hint_th": "รู้จัก", "grammar_en": "Verb 认识", "grammar_th": "คำกริยา 认识"}
]

hsk1_grammar = [
    # Chapter 1
    {
        "chapter_num": 1, "point_num": 1,
        "title_cn": "人称代词“你、您、你们”",
        "title_th": "คำสรรพนามบุรุษที่สอง 你, 您, 你们",
        "structure": "你 (เธอ/คุณ ทั่วไป) / 您 (ท่าน สุภาพ/ให้เกียรติ) / 你们 (พวกเธอ พหูพจน์)",
        "explanation_th": "ใช้ระบุผู้ฟัง โดย '你' ใช้ในสถานการณ์ทั่วไปหรือคุยกับเพื่อน, '您' เติม 心 ไว้ข้างล่าง ใช้แสดงความเคารพต่อผู้อาวุโส ครู หรือลูกค้า, ส่วน '们' ใช้เติมท้ายสรรพนามเพื่อบอกความเป็นพหูพจน์ (มากกว่า 1 คน)",
        "examples": [
            {"cn": "你好！", "py": "Nǐ hǎo!", "th": "สวัสดี!"},
            {"cn": "老师，您好！", "py": "Lǎoshī, nín hǎo!", "th": "คุณครู สวัสดีครับ/ค่ะ (ใช้ 您 สุภาพ)"},
            {"cn": "你们好！", "py": "Nǐmen hǎo!", "th": "สวัสดีพวกเธอทุกคน!"}
        ]
    },
    {
        "chapter_num": 1, "point_num": 2,
        "title_cn": "礼貌交际用语“对不起”与“没关系”",
        "title_th": "สำนวนขอโทษและการตอบรับ: 对不起 / 没关系",
        "structure": "A: 对不起！ -> B: 没关系。",
        "explanation_th": "เมื่อทำสิ่งผิดพลาดหรือมารบกวนผู้อื่น ให้กล่าวว่า '对不起' (ขอโทษ) และผู้ฟังจะตอบรับอย่างสุภาพด้วย '没关系' (ไม่เป็นไร / ไม่มีความเกี่ยวข้องกันจนต้องกังวล)",
        "examples": [
            {"cn": "对不起，我来晚了。", "py": "Duìbuqǐ, wǒ lái wǎn le.", "th": "ขอโทษนะ ฉันมาสายแล้ว"},
            {"cn": "没关系，请进！", "py": "Méi guānxi, qǐng jìn!", "th": "ไม่เป็นไร เชิญเข้ามาเลย"}
        ]
    },

    # Chapter 2
    {
        "chapter_num": 2, "point_num": 1,
        "title_cn": "致谢与回答“谢谢”与“不客气”",
        "title_th": "การขอบคุณและการตอบรับ: 谢谢 / 不客气",
        "structure": "A: 谢谢 / 谢谢你！ -> B: 不客气 / 不用谢。",
        "explanation_th": "'谢谢' ใช้กล่าวขอบใจหรือขอบคุณ และอีกฝ่ายจะตอบว่า '不客气' (ไม่ต้องเกรงใจ) หรือ '不用谢' (ไม่ต้องขอบคุณหรอก เป็นความเต็มใจ)",
        "examples": [
            {"cn": "谢谢你的帮助！", "py": "Xièxie nǐ de bāngzhù!", "th": "ขอบคุณสำหรับความช่วยเหลือของเธอนะ!"},
            {"cn": "不客气，大家是朋友。", "py": "Bú kèqi, dàjiā shì péngyou.", "th": "ไม่ต้องเกรงใจ พวกเราเป็นเพื่อนกัน"}
        ]
    },
    {
        "chapter_num": 2, "point_num": 2,
        "title_cn": "否定副词“不”的用法与变调",
        "title_th": "คำวิเศษณ์ปฏิเสธ 不 (การใช้งานและการเปลี่ยนเสียง)",
        "structure": "不 + กริยา / คุณศัพท์ (ไม่...)",
        "explanation_th": "ปกติคำว่า '不' ออกเสียงวรรณยุกต์เสียงที่ 4 (bù) แต่ถ้าคำที่ตามหลังมาเป็นวรรณยุกต์เสียงที่ 4 เหมือนกัน '不' จะเปลี่ยนเสียงเป็นเสียงที่ 2 (bú) อัตโนมัติ เช่น 不是 (bú shì), 不客气 (bú kèqi)",
        "examples": [
            {"cn": "我不是老师，我是学生。", "py": "Wǒ bú shì lǎoshī, wǒ shì xuésheng.", "th": "ฉันไม่ใช่ครู ฉันเป็นนักเรียน (不 เปลี่ยนเป็นเสียง 2)"},
            {"cn": "我不喝茶，我想喝水。", "py": "Wǒ bù hē chá, wǒ xiǎng hē shuǐ.", "th": "ฉันไม่ดื่มชา ฉันอยากดื่มน้ำ (不 เป็นเสียง 4 ตามปกติ)"}
        ]
    },

    # Chapter 3
    {
        "chapter_num": 3, "point_num": 1,
        "title_cn": "疑问代词“什么”询问事物与名称",
        "title_th": "สรรพนามคำถาม 什么 (อะไร)",
        "structure": "主语 + 叫 + 什么 + 名字？ / 这是 + 什么？",
        "explanation_th": "'什么' แปลว่า 'อะไร' สามารถใช้เดี่ยวๆ เพื่อถามสิ่งของ หรือวางหน้าคำนามเพื่อทำหน้าที่ขยาย เช่น 什么名字 (ชื่ออะไร), 什么书 (หนังสืออะไร) โดยตำแหน่งในประโยคภาษาจีนจะอยู่ตำแหน่งเดียวกับคำตอบ",
        "examples": [
            {"cn": "你叫什么名字？", "py": "Nǐ jiào shénme míngzi?", "th": "เธอชื่ออะไร?"},
            {"cn": "这是什么书？", "py": "Zhè shì shénme shū?", "th": "นี่คือหนังสืออะไร?"}
        ]
    },
    {
        "chapter_num": 3, "point_num": 2,
        "title_cn": "判断动词“是”字句（1）",
        "title_th": "ประโยคบอกเล่าด้วยคำกริยา “是” (A เป็น/คือ B)",
        "structure": "主语(A) + 是 + 宾语(B) / 否定: 主语 + 不是 + 宾语",
        "explanation_th": "กริยา '是' ทำหน้าที่เทียบเท่า verb to be ในภาษาอังกฤษ เพื่อยืนยันว่าประธานคือใคร เป็นอะไร หรือมีสถานะใด รูปปฏิเสธใช้ '不是'",
        "examples": [
            {"cn": "李月是我的老师。", "py": "Lǐ Yuè shì wǒ de lǎoshī.", "th": "หลี่เยว่คือคุณครูของฉัน"},
            {"cn": "他不是美国人，他是中国人。", "py": "Tā bú shì Měiguórén, tā shì Zhōngguórén.", "th": "เขาไม่ใช่คนอเมริกัน เขาเป็นคนจีน"}
        ]
    },

    # Chapter 4
    {
        "chapter_num": 4, "point_num": 1,
        "title_cn": "结构助词“的”表示领属关系",
        "title_th": "คำช่วยแสดงความเป็นเจ้าของ “的” (ของ)",
        "structure": "定语 (ผู้เป็นเจ้าของ) + 的 + 中心语 (สิ่งของ/บุคคล)",
        "explanation_th": "'的' วางไว้ระหว่างผู้ครอบครองกับสิ่งที่ถูกครอบครอง แปลว่า 'ของ' แต่ถ้าความสัมพันธ์ใกล้ชิดมาก เช่น ครอบครัว หรือองค์กร สามารถละ '的' ได้ (เช่น 我家, 我妈妈)",
        "examples": [
            {"cn": "这是我的汉语书。", "py": "Zhè shì wǒ de Hànyǔ shū.", "th": "นี่คือหนังสือภาษาจีนของฉัน"},
            {"cn": "她是我的好朋友。", "py": "Tā shì wǒ de hǎo péngyou.", "th": "เธอคือเพื่อนที่ดีของฉัน"}
        ]
    },
    {
        "chapter_num": 4, "point_num": 2,
        "title_cn": "语气助词“呢”用于回问",
        "title_th": "คำช่วยน้ำเสียง “呢” ในการถามย้อนกลับ (แล้ว...ล่ะ?)",
        "structure": "名词 / 代词 + 呢？",
        "explanation_th": "ใช้ละคำถามเต็มเมื่อต้องการถามเรื่องเดียวกันกลับไปยังคู่สนทนา หรือถามหาตำแหน่งของสิ่งของที่หายไป เช่น '你呢？' (แล้วเธอล่ะ?), '我的书呢？' (แล้วหนังสือของฉันล่ะ?)",
        "examples": [
            {"cn": "我是中国人，你呢？", "py": "Wǒ shì Zhōngguórén, nǐ ne?", "th": "ฉันเป็นคนจีน แล้วเธอล่ะ?"},
            {"cn": "我的手机呢？在桌子上呢。", "py": "Wǒ de shǒujī ne? Zài zhuōzi shang ne.", "th": "โทรศัพท์ฉันล่ะ? อยู่บนโต๊ะนั่นไง"}
        ]
    },

    # Chapter 5
    {
        "chapter_num": 5, "point_num": 1,
        "title_cn": "年龄表达法与“岁”",
        "title_th": "การบอกอายุและการถามอายุในภาษาจีน",
        "structure": "ถามเด็ก (<10 ปี): 几岁？ / ถามผู้ใหญ่: 多大？ / บอกอายุ: 数字 + 岁",
        "explanation_th": "การถามอายุของเด็กเล็กมักใช้ '你几岁了？' ส่วนวัยรุ่นหรือผู้ใหญ่ใช้ '你多大了？' หรือ '您多大年纪了？' สำหรับผู้อาวุโส การตอบจะใช้ตัวเลขตามด้วยคำลักษณนาม '岁' เสมอ",
        "examples": [
            {"cn": "你女儿今年几岁了？她五岁了。", "py": "Nǐ nǚ'ér jīnnián jǐ suì le? Tā wǔ suì le.", "th": "ลูกสาวเธอปีนี้กี่ขวบแล้ว? เธออายุ 5 ขวบแล้ว"},
            {"cn": "李老师今年多大了？他五十岁了。", "py": "Lǐ lǎoshī jīnnián duō dà le? Tā wǔshí suì le.", "th": "อาจารย์หลี่ปีนี้อายุเท่าไหร่แล้ว? ท่านอายุ 50 ปีแล้ว"}
        ]
    },

    # Chapter 6
    {
        "chapter_num": 6, "point_num": 1,
        "title_cn": "能愿动词“会”表示学会的能力",
        "title_th": "กริยานุเคราะห์ “会” (ทำเป็น/ทำได้ จากการเรียนรู้ฝึกฝน)",
        "structure": "主语 + 会 + 动词 / 否定: 主语 + 不会 + 动词",
        "explanation_th": "'会' ใช้บอกความสามารถที่มนุษย์ต้องผ่านการเรียนรู้ ฝึกฝน หรืออบรมจึงจะทำได้ เช่น พูดภาษา ขับรถ ทำอาหาร ต่างจาก '能' ที่เน้นความสามารถทางร่างกายหรือสถานการณ์เอื้ออำนวย",
        "examples": [
            {"cn": "我会说汉语，不会写汉字。", "py": "Wǒ huì shuō Hànyǔ, bú huì xiě hànzì.", "th": "ฉันพูดภาษาจีนเป็น แต่เขียนอักษรจีนไม่เป็น"},
            {"cn": "你妈妈会做中国菜吗？", "py": "Nǐ māma huì zuò Zhōngguó cài ma?", "th": "แม่ของเธอทำอาหารจีนเป็นไหม?"}
        ]
    },

    # Chapter 7
    {
        "chapter_num": 7, "point_num": 1,
        "title_cn": "汉语日期的表达顺序（年、月、日/号、星期）",
        "title_th": "ลำดับการบอกวันเดือนปีในภาษาจีน (จากใหญ่ไปหาเล็ก)",
        "structure": "……年 + ……月 + ……号/日 + 星期……",
        "explanation_th": "คนจีนจะเรียงลำดับเวลาจากหน่วยที่ใหญ่ที่สุดลงมายังหน่วยเล็กที่สุดเสมอ: ปี -> เดือน -> วันที่ -> วันในสัปดาห์ เช่น '2026年11月9日星期一' ในภาษาพูดมักใช้คำว่า '号' แทน '日'",
        "examples": [
            {"cn": "今天九月一号，星期三。", "py": "Jīntiān jiǔ yuè yī hào, xīngqīsān.", "th": "วันนี้วันที่ 1 กันยายน วันพุธ"},
            {"cn": "明天是十月二十五号。", "py": "Míngtiān shì shí yuè èrshíwǔ hào.", "th": "พรุ่งนี้คือวันที่ 25 ตุลาคม"}
        ]
    },

    # Chapter 8
    {
        "chapter_num": 8, "point_num": 1,
        "title_cn": "用“多少钱”询问价格与货币单位“块”",
        "title_th": "การถามราคาสินค้าด้วย “多少钱” และหน่วยเงิน “块”",
        "structure": "东西 + 多少钱？ / 回答: 数字 + 块 (钱)",
        "explanation_th": "เมื่อต้องการถามราคาให้ใช้คำว่า '多少钱？' ในภาษาจีนพูด หน่วยเงินหยวน (元) มักถูกเรียกว่า '块' (kuài) เสมอ และสามารถละคำว่า 钱 ที่อยู่ท้ายสุดได้",
        "examples": [
            {"cn": "这个茶杯多少钱？十五块。", "py": "Zhè ge chábēi duōshao qián? Shíwǔ kuài.", "th": "ถ้วยชานี้ราคาเท่าไหร่? 15 หยวน"},
            {"cn": "这些苹果多少钱一斤？", "py": "Zhèxiē píngguǒ duōshao qián yì jīn?", "th": "แอปเปิ้ลเหล่านี้ราคาครึ่งกิโลละเท่าไหร่?"}
        ]
    },

    # Chapter 9
    {
        "chapter_num": 9, "point_num": 1,
        "title_cn": "介词“在”表示动作发生的地点",
        "title_th": "คำบุพบท “在” ระบุสถานที่ทำกิจกรรม",
        "structure": "主语 + 在 + 地点 + 动词 + 宾语",
        "explanation_th": "ในภาษาจีน โครงสร้างบอกสถานที่ทำกิจกรรมจะต้องนำ '在 + สถานที่' มาวางไว้ข้างหน้าคำกริยาเสมอ (ต่างจากภาษาไทยที่มักพูดกริยาก่อนสถานที่)",
        "examples": [
            {"cn": "我在家看书，没去学校。", "py": "Wǒ zài jiā kàn shū, méi qù xuéxiào.", "th": "ฉันอ่านหนังสืออยู่ที่บ้าน ไม่ได้ไปโรงเรียน"},
            {"cn": "他儿子在医院工作。", "py": "Tā érzi zài yīyuàn gōngzuò.", "th": "ลูกชายของเขาทำงานอยู่ที่โรงพยาบาล"}
        ]
    },

    # Chapter 10
    {
        "chapter_num": 10, "point_num": 1,
        "title_cn": "能愿动词“能”表示许可或情理允许",
        "title_th": "กริยานุเคราะห์ “能” ในการขออนุญาต",
        "structure": "我能 + 动词 + 吗？ / 否定: 不能 + 动词",
        "explanation_th": "ใช้ถามหรือขออนุญาตว่าสามารถทำสิ่งนั้นได้หรือไม่ตามกติกาหรือความเหมาะสม เช่น '我能坐这儿吗？' (ฉันขอนั่งตรงนี้ได้ไหม) ถ้าอนุญาตให้ตอบว่า '可以 / 能' ถ้าไม่อนุญาตตอบ '不能'",
        "examples": [
            {"cn": "请问，我能坐这儿吗？能，请坐。", "py": "Qǐngwèn, wǒ néng zuò zhèr ma? Néng, qǐng zuò.", "th": "ขอถามหน่อย ฉันขอนั่งตรงนี้ได้ไหม? ได้ครับ เชิญนั่ง"},
            {"cn": "图书馆里不能大声说话。", "py": "Túshūguǎn lǐ bù néng dàshēng shuōhuà.", "th": "ในห้องสมุดไม่สามารถพูดคุยเสียงดังได้"}
        ]
    },

    # Chapter 11
    {
        "chapter_num": 11, "point_num": 1,
        "title_cn": "钟点表达法（点、分、半、差）",
        "title_th": "การบอกเวลาบนหน้าปัดนาฬิกา (点, 分, 半)",
        "structure": "数字 + 点 + (数字 + 分) / 数字 + 点半",
        "explanation_th": "'点' คือชั่วโมงหรือโมง, '分' คือนาที, '半' แปลว่าครึ่ง (30 นาที) หากมีช่วงเวลาของวัน ให้เอาช่วงเวลานำหน้าเสมอ เช่น 早上八点 (แปดโมงเช้า), 晚上七点半 (หนึ่งทุ่มครึ่ง)",
        "examples": [
            {"cn": "现在几点？现在九点十分。", "py": "Xiànzài jǐ diǎn? Xiànzài jiǔ diǎn shí fēn.", "th": "ตอนนี้กี่โมงแล้ว? ตอนนี้เก้าโมงสิบนาที"},
            {"cn": "我们中午十二点半吃饭。", "py": "Wǒmen zhōngwǔ shí'èr diǎn bàn chīfàn.", "th": "พวกเรากินข้าวตอนเที่ยงสิบสองโมงครึ่ง"}
        ]
    },

    # Chapter 12
    {
        "chapter_num": 12, "point_num": 1,
        "title_cn": "程度副词固定结构“太……了”",
        "title_th": "โครงสร้างบอกระดับอารมณ์ความรู้สึก “太……了” (เกินไป/มากจริงๆ)",
        "structure": "太 + 形容词 / 动词 + 了",
        "explanation_th": "ใช้แสดงการอุทานว่าสิ่งนั้นมีระดับสูงมาก หรือเกินขอบเขตที่พอดี เช่น '太热了' (ร้อนเกินไปแล้ว), '太好了！' (ดีจังเลย!) หากเป็นรูปปฏิเสธให้ใช้ '不太 + Adj' โดยตัด 了 ทิ้ง (แปลว่า ไม่ค่อย...เท่าไหร่)",
        "examples": [
            {"cn": "今天天气太好了，我们出去玩吧！", "py": "Jīntiān tiānqì tài hǎo le, wǒmen chūqù wán ba!", "th": "วันนี้อากาศดีจังเลย พวกเราออกไปเที่ยวกันเถอะ!"},
            {"cn": "这件衣服太大了，有小一点儿的吗？", "py": "Zhè jiàn yīfu tài dà le, yǒu xiǎo yìdiǎnr de ma?", "th": "เสื้อตัวนี้ใหญ่เกินไป มีตัวเล็กกว่านี้หน่อยไหม?"}
        ]
    },

    # Chapter 13
    {
        "chapter_num": 13, "point_num": 1,
        "title_cn": "动作进行态“在……呢”",
        "title_th": "โครงสร้างแสดงการกระทำที่กำลังดำเนินอยู่ (在……呢)",
        "structure": "主语 + (正)在 + 动词 + 宾语 + (呢)",
        "explanation_th": "ใช้บอกว่าในขณะนี้ประธาน 'กำลังทำกริยานั้นอยู่' สามารถใช้คำว่า '在', '正在' หรือใส่ '呢' ท้ายประโยคเพื่อเน้นน้ำเสียง รูปปฏิเสธใช้ '没在 + กริยา'",
        "examples": [
            {"cn": "他在学做中国菜呢。", "py": "Tā zài xué zuò Zhōngguó cài ne.", "th": "เขากำลังเรียนทำอาหารจีนอยู่"},
            {"cn": "你打电话的时候，我正在睡觉呢。", "py": "Nǐ dǎ diànhuà de shíhou, wǒ zhèngzài shuìjiào ne.", "th": "ตอนที่เธอโทรศัพท์มา ฉันกำลังนอนหลับอยู่พอดี"}
        ]
    },

    # Chapter 14
    {
        "chapter_num": 14, "point_num": 1,
        "title_cn": "动态助词“了”表示动作的完成与实现",
        "title_th": "คำช่วยแสดงการเสร็จสิ้นของกริยา “了” (เกิดขึ้นแล้ว/เสร็จแล้ว)",
        "structure": "动词 + 了 + 数量词 + 宾语 / 否定: 没(有) + 动词",
        "explanation_th": "'了' วางไว้ติดหลังคำกริยาเพื่อแสดงว่าการกระทำนั้นได้เกิดขึ้นจริงและเสร็จสิ้นแล้ว มักมีคำระบุจำนวนหรือบทขยายกรรมอยู่ด้วย รูปปฏิเสธต้องใช้ '没' หรือ '没有' นำหน้ากริยา และห้ามใส่ 了 เด็ดขาด",
        "examples": [
            {"cn": "她买了不少漂亮的衣服。", "py": "Tā mǎi le bù shǎo piàoliang de yīfu.", "th": "เธอซื้อเสื้อผ้าสวยๆ มาไม่น้อยเลย"},
            {"cn": "我没买苹果，我买了西瓜。", "py": "Wǒ méi mǎi píngguǒ, wǒ mǎi le xīguā.", "th": "ฉันไม่ได้ซื้อแอปเปิ้ล ฉันซื้อแตงโมมา"}
        ]
    },

    # Chapter 15
    {
        "chapter_num": 15, "point_num": 1,
        "title_cn": "强调句式“是……的”（强调时间、地点、方式）",
        "title_th": "โครงสร้างเน้นย้ำ “是……的” (เน้นเวลา สถานที่ หรือวิธีการในอดีต)",
        "structure": "主语 + 是 + [时间 / 地点 / 方式] + 动词 + 的",
        "explanation_th": "ใช้เมื่อเหตุการณ์นั้นเกิดขึ้นในอดีตเป็นที่รับรู้กันแล้วทั้งสองฝ่าย แต่ผู้พูดต้องการเน้นย้ำเฉพาะ 'เวลาไหน', 'ที่ไหน', หรือ 'ด้วยวิธีการใด' เช่น นั่งเครื่องบินมา หรือมากับใคร ในประโยคบอกเล่าสามารถละ '是' ได้ แต่รูปปฏิเสธต้องใช้ '不是……的' เสมอ",
        "examples": [
            {"cn": "我是坐飞机来北京的。", "py": "Wǒ shì zuò fēijī lái Běijīng de.", "th": "ฉันนั่งเครื่องบินมาปักกิ่ง (เน้นวิธีการเดินทาง)"},
            {"cn": "我们是在大学里认识的。", "py": "Wǒmen shì zài dàxué lǐ rènshi de.", "th": "พวกเรารู้จักกันในมหาวิทยาลัย (เน้นสถานที่)"},
            {"cn": "他不是一个人来的，是跟朋友一起的。", "py": "Tā bú shì yí ge rén lái de, shì gēn péngyou yìqǐ de.", "th": "เขาไม่ได้มาคนเดียว เขามากับเพื่อน (เน้นลักษณะการมา)"}
        ]
    }
]

print(f"HSK 1: {len(hsk1_words)} words, {len(hsk1_sentences)} sentences, {len(hsk1_grammar)} grammar points.")
