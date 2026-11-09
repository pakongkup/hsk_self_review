# build_full_hsk_database.py
"""
Builds full multi-level database for HSK 1, HSK 2, and HSK 3:
- Chapters with titles and topics in Chinese, Pinyin, English, Thai
- Vocabulary words with POS, English, Thai, and authentic example sentences
- Dialogue sentences with Cloze blanks and grammar focus
- Grammar summary points with structure formulas, detailed Thai explanations, and examples
"""

import os
import sys
import json
import sqlite3

sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'hsk3.db')
JSON_PATH = os.path.join(os.path.dirname(__file__), 'data', 'hsk3_database.json')

# -------------------------------------------------------------
# 1. CHAPTERS DATA (HSK 1, 2, 3)
# -------------------------------------------------------------
chapters_data = [
    # --- HSK 1 (15 Chapters) ---
    {
        "id": 101, "level": 1, "chapter_num": 1,
        "title_cn": "你好", "title_pinyin": "Nǐ hǎo",
        "title_en": "Hello", "title_th": "สวัสดี",
        "topic_en": "Greetings & Polite Phrases", "topic_th": "การทักทายและคำสุภาพ",
        "grammar_en": ["Pronouns: 你, 您, 你们", "Basic Greeting: 你好 / 您好"],
        "grammar_th": ["คำสรรพนาม: 你, 您, 你们", "ประโยคทักทายพื้นฐาน: 你好 / 您好"]
    },
    {
        "id": 102, "level": 1, "chapter_num": 2,
        "title_cn": "谢谢你", "title_pinyin": "Xièxie nǐ",
        "title_en": "Thank You", "title_th": "ขอบคุณนะ",
        "topic_en": "Gratitude & Apologies", "topic_th": "การขอบคุณและการขอโทษ",
        "grammar_en": ["Expressing Thanks: 谢谢 / 不客气", "Apologizing: 对不起 / 没关系"],
        "grammar_th": ["การกล่าวขอบคุณและตอบรับ: 谢谢 / 不客气", "การขอโทษและตอบรับ: 对不起 / 没关系"]
    },
    {
        "id": 103, "level": 1, "chapter_num": 3,
        "title_cn": "你叫什么名字", "title_pinyin": "Nǐ jiào shénme míngzi",
        "title_en": "What's Your Name?", "title_th": "คุณชื่ออะไร",
        "topic_en": "Names, Nationality & Introductions", "topic_th": "การถามชื่อ สัญชาติ และการแนะนำตัว",
        "grammar_en": ["Interrogative Pronoun: 什么", "Asking Names: 叫什么名字", "“是” Sentence: A 是 B"],
        "grammar_th": ["คำสรรพนามคำถาม: 什么 (อะไร)", "การถามชื่อ: 叫什么名字", "ประโยค “是” (ยืนยันสถานะ/ตัวตน)"]
    },
    {
        "id": 104, "level": 1, "chapter_num": 4,
        "title_cn": "她是我的汉语老师", "title_pinyin": "Tā shì wǒ de Hànyǔ lǎoshī",
        "title_en": "She Is My Chinese Teacher", "title_th": "เธอคือครูภาษาจีนของฉัน",
        "topic_en": "Teachers, Friends & Identity", "topic_th": "ครู เพื่อน และบุคคลรอบตัว",
        "grammar_en": ["Interrogative Pronouns: 谁, 哪", "Structural Particle: 的 (Possessive)", "Modal Particle: 呢 (Reciprocal questions)"],
        "grammar_th": ["สรรพนามคำถาม: 谁 (ใคร), 哪 (ไหน)", "คำช่วยแสดงความเป็นเจ้าของ: 的 (ของ)", "คำช่วยคำถาม: 呢 (แล้ว...ล่ะ?)"]
    },
    {
        "id": 105, "level": 1, "chapter_num": 5,
        "title_cn": "她女儿今年二十岁", "title_pinyin": "Tā nǚ'ér jīnnián èrshí suì",
        "title_en": "Her Daughter Is 20 Years Old", "title_th": "ลูกสาวของเธอปีนี้อายุ 20 ปี",
        "topic_en": "Family, Age & Numbers", "topic_th": "ครอบครัว อายุ และตัวเลข",
        "grammar_en": ["Asking Age: 几岁 vs 多大", "Numbers: 1-100", "Expressing Age with 岁"],
        "grammar_th": ["การถามอายุ: 几岁 (เด็ก) vs 多大 (ผู้ใหญ่)", "การนับตัวเลข 1-100", "โครงสร้างบอกอายุด้วย 岁"]
    },
    {
        "id": 106, "level": 1, "chapter_num": 6,
        "title_cn": "我会说汉语", "title_pinyin": "Wǒ huì shuō Hànyǔ",
        "title_en": "I Can Speak Chinese", "title_th": "ฉันพูดภาษาจีนได้",
        "topic_en": "Languages & Learned Abilities", "topic_th": "ภาษาจีนและความสามารถที่ฝึกฝน",
        "grammar_en": ["Modal Verb: 会 (Learned ability)", "Question Particle: 吗", "Interrogative: 怎么 (Method)"],
        "grammar_th": ["กริยานุเคราะห์: 会 (ทำเป็น/ได้จากการฝึก)", "คำลงท้ายคำถาม: 吗 (ใช่ไหม)", "สรรพนามคำถาม: 怎么 (อย่างไร)"]
    },
    {
        "id": 107, "level": 1, "chapter_num": 7,
        "title_cn": "今天几号", "title_pinyin": "Jīntiān jǐ hào",
        "title_en": "What's the Date Today?", "title_th": "วันนี้วันที่เท่าไหร่",
        "topic_en": "Calendar, Dates & Days", "topic_th": "ปฏิทิน วันที่ และวันในสัปดาห์",
        "grammar_en": ["Dates: 年、月、号/日、星期", "Interrogative: 几 (Quantity < 10)", "Time words as Adverbials"],
        "grammar_th": ["การบอกวันเดือนปี: 年 月 号/日 星期", "สรรพนามคำถาม: 几 (กี่)", "คำบอกเวลาทำหน้าที่ขยายกริยา"]
    },
    {
        "id": 108, "level": 1, "chapter_num": 8,
        "title_cn": "我想喝茶", "title_pinyin": "Wǒ xiǎng hē chá",
        "title_en": "I'd Like Some Tea", "title_th": "ฉันอยากดื่มชา",
        "topic_en": "Food, Drinks & Shopping", "topic_th": "อาหาร เครื่องดื่ม และการซื้อของ",
        "grammar_en": ["Auxiliary Verb: 想 (Would like to)", "Interrogative: 多少 (Asking price/amount)", "Measure Words: 个, 杯, 块"],
        "grammar_th": ["กริยานุเคราะห์: 想 (อยาก/ต้องการ)", "สรรพนามคำถาม: 多少 (เท่าไหร่/ราคาเท่าไหร่)", "ลักษณนาม: 个, 杯, 块"]
    },
    {
        "id": 109, "level": 1, "chapter_num": 9,
        "title_cn": "你儿子在哪儿工作", "title_pinyin": "Nǐ érzi zài nǎr gōngzuò",
        "title_en": "Where Does Your Son Work?", "title_th": "ลูกชายของคุณทำงานที่ไหน",
        "topic_en": "Jobs, Workplaces & Locations", "topic_th": "อาชีพ สถานที่ทำงาน และตำแหน่งที่อยู่",
        "grammar_en": ["Preposition: 在 (Location of action)", "Interrogative: 哪儿 (Where)", "Verb: 有 (Existence)"],
        "grammar_th": ["คำบุพบท: 在 (ทำอะไรที่ไหน: 在 + สถานที่ + V)", "สรรพนามคำถาม: 哪儿 (ที่ไหน)", "คำกริยา: 有 (มี/อยู่ที่)"]
    },
    {
        "id": 110, "level": 1, "chapter_num": 10,
        "title_cn": "我能坐这儿吗", "title_pinyin": "Wǒ néng zuò zhèr ma",
        "title_en": "Can I Sit Here?", "title_th": "ฉันขอนั่งตรงนี้ได้ไหม",
        "topic_en": "Permissions & Seating", "topic_th": "การขออนุญาตและทิศทางตำแหน่ง",
        "grammar_en": ["Modal Verb: 能 (Permission / Ability)", "Position words: 前面, 后面", "Polite Request: 请问 / 能...吗"],
        "grammar_th": ["กริยานุเคราะห์: 能 (สามารถ/ขออนุญาต)", "คำระบุตำแหน่ง: 前面 (ข้างหน้า), 后面 (ข้างหลัง)", "ประโยคขออนุญาต: 能...吗？"]
    },
    {
        "id": 111, "level": 1, "chapter_num": 11,
        "title_cn": "现在几点", "title_pinyin": "Xiànzài jǐ diǎn",
        "title_en": "What Time Is It Now?", "title_th": "ตอนนี้กี่โมงแล้ว",
        "topic_en": "Clock Time & Daily Schedule", "topic_th": "เวลาบนหน้าปัดนาฬิกาและตารางประจำวัน",
        "grammar_en": ["Clock Time: 点, 分, 半", "Time periods: 早上, 中午, 晚上", "Temporal order in sentences"],
        "grammar_th": ["การบอกเวลา: 点 (โมง), 分 (นาที), 半 (ครึ่ง)", "ช่วงเวลา: 早上 (เช้า), 中午 (เที่ยง), 晚上 (ค่ำ)", "การเรียงลำดับเวลาในประโยคภาษาจีน"]
    },
    {
        "id": 112, "level": 1, "chapter_num": 12,
        "title_cn": "明天天气怎么样", "title_pinyin": "Míngtiān tiānqì zěnmeyàng",
        "title_en": "How Will the Weather Be Tomorrow?", "title_th": "พรุ่งนี้อากาศเป็นอย่างไรบ้าง",
        "topic_en": "Weather, Temperature & Health", "topic_th": "สภาพอากาศ อุณหภูมิ และสุขภาพ",
        "grammar_en": ["Interrogative: 怎么样 (How about)", "Exclamatory Pattern: 太...了 (Too/Extremely)", "Modal Verb: 会 (Future likelihood)"],
        "grammar_th": ["สรรพนามคำถาม: 怎么样 (เป็นอย่างไรบ้าง)", "โครงสร้างบอกระดับ: 太...了 (เกินไป/มากจริงๆ)", "การใช้ 会 คาดการณ์สิ่งที่จะเกิดขึ้นในอนาคต"]
    },
    {
        "id": 113, "level": 1, "chapter_num": 13,
        "title_cn": "他在学做中国菜呢", "title_pinyin": "Tā zài xué zuò Zhōngguó cài ne",
        "title_en": "He Is Learning to Cook Chinese Food", "title_th": "เขากำลังเรียนทำอาหารจีนอยู่",
        "topic_en": "Ongoing Actions & Hobbies", "topic_th": "การกระทำที่กำลังดำเนินอยู่และงานอดิเรก",
        "grammar_en": ["Ongoing Action: 在...呢 (Progressive aspect)", "Reading Phone Numbers (1 = yāo)", "Modal Particle: 吧 (Suggestion)"],
        "grammar_th": ["โครงสร้างกำลังกระทำ: 在...呢 (กำลัง...อยู่)", "การอ่านหมายเลขโทรศัพท์ (เลข 1 อ่านว่า yāo)", "คำช่วยน้ำเสียง: 吧 (เถอะ/นะ)"]
    },
    {
        "id": 114, "level": 1, "chapter_num": 14,
        "title_cn": "她买了不少衣服", "title_pinyin": "Tā mǎi le bù shǎo yīfu",
        "title_en": "She Bought Quite a Few Clothes", "title_th": "เธอซื้อเสื้อผ้ามาไม่น้อยเลย",
        "topic_en": "Shopping & Completed Actions", "topic_th": "การซื้อของและการกระทำที่เสร็จสิ้น",
        "grammar_en": ["Aspect Particle: 了 (Action completion)", "Quantifier: 不少 (Quite a lot)", "Structure: 后 (After doing...)"],
        "grammar_th": ["คำช่วยกริยา: 了 (เกิดขึ้นแล้ว/เสร็จสิ้นแล้ว)", "คำระบุปริมาณ: 不少 (ไม่น้อย/เยอะพอควร)", "การใช้ ...后 (หลังจาก...)"]
    },
    {
        "id": 115, "level": 1, "chapter_num": 15,
        "title_cn": "我是坐飞机来的", "title_pinyin": "Wǒ shì zuò fēijī lái de",
        "title_en": "I Came by Plane", "title_th": "ฉันนั่งเครื่องบินมา",
        "topic_en": "Travel Methods & Background Details", "topic_th": "วิธีการเดินทางและการเน้นข้อมูลในอดีต",
        "grammar_en": ["Emphatic Construction: 是...的 (Time/Manner/Place)", "Preposition / Adj: 对 (Correct / Towards)"],
        "grammar_th": ["โครงสร้างเน้นย้ำ: 是...的 (เน้นเวลา สถานที่ หรือวิธีการเดินทาง)", "การใช้คำว่า 对 (ถูกต้อง / ต่อ)"]
    },

    # --- HSK 2 (15 Chapters) ---
    {
        "id": 201, "level": 2, "chapter_num": 1,
        "title_cn": "她请我们吃了北京烤鸭", "title_pinyin": "Tā qǐng wǒmen chī le Běijīng kǎoyā",
        "title_en": "She Treated Us to Peking Duck", "title_th": "เธอเลี้ยงเป็ดปักกิ่งพวกเรา",
        "topic_en": "Dining & Treating Friends", "topic_th": "การรับประทานอาหารและการเลี้ยงเพื่อน",
        "grammar_en": ["Modal Particle: 吧 (Soliciting agreement)", "Emphatic: 是...的", "Pivotal Sentences: 请/让/叫"],
        "grammar_th": ["คำช่วยน้ำเสียง 吧 (ชักชวน/ปรึกษา)", "โครงสร้างเน้นย้ำ 是……的", "ประโยคกริยาซ้อน: 请 / 让 / 叫 (ชวน/ให้ทำ)"]
    },
    {
        "id": 202, "level": 2, "chapter_num": 2,
        "title_cn": "还是打车去北大吧", "title_pinyin": "Háishi dǎchē qù Běidà ba",
        "title_en": "Let's Take a Taxi to Peking University Instead", "title_th": "นั่งแท็กซี่ไปมหาวิทยาลัยปักกิ่งดีกว่า",
        "topic_en": "Transportation & Suggestions", "topic_th": "การเดินทางและข้อเสนอแนะ",
        "grammar_en": ["Fixed Pattern: 还是...吧 (Preference)", "Expressing Approximations with 多", "Verbal/Subject-Predicate Attributives with 的"],
        "grammar_th": ["โครงสร้าง 还是……吧 (เลือกทางนี้ดีกว่า)", "การใช้ 多 บอกจำนวนประมาณ (เช่น 三十多岁)", "วลีกริยา/วลีประธานทำหน้าที่ขยายคำนามด้วย 的"]
    },
    {
        "id": 203, "level": 2, "chapter_num": 3,
        "title_cn": "我想去西安旅游", "title_pinyin": "Wǒ xiǎng qù Xī'ān lǚyóu",
        "title_en": "I Want to Visit Xi'an", "title_th": "ฉันอยากไปเที่ยวซีอาน",
        "topic_en": "Tourism, Travel & History", "topic_th": "การท่องเที่ยวและสถานที่ทางประวัติศาสตร์",
        "grammar_en": ["Complements of Result: 懂, 完, 到, 好", "Verb Reduplication: AA (看看, 听听)", "Verb Reduplication: ABAB (学习学习, 介绍介绍)"],
        "grammar_th": ["คำเสริมบอกผล: 懂, 完, 到, 好 (เข้าใจ, เสร็จ, ถึง/ได้, เรียบร้อย)", "การซ้ำกริยาพยางค์เดียว AA (ลองทำดู)", "การซ้ำกริยาสองพยางค์ ABAB"]
    },
    {
        "id": 204, "level": 2, "chapter_num": 4,
        "title_cn": "你穿红色的很好看", "title_pinyin": "Nǐ chuān hóngsè de hěn hǎokàn",
        "title_en": "You Look Pretty Good in Red", "title_th": "เธอใส่ชุดสีแดงแล้วดูดีมาก",
        "topic_en": "Colors, Clothing & Compliments", "topic_th": "สีสัน เสื้อผ้า และคำชม",
        "grammar_en": ["Aspect Particle: 过 (Past experience)", "Causal Complex: 因为...所以...", "“的” Phrase (Nominalized)"],
        "grammar_th": ["คำช่วยแสดงประสบการณ์: 过 (เคยทำ)", "ประโยคเหตุและผล: 因为……所以……", "วลี “的” (ละคำนามไว้ในฐานที่เข้าใจ)"]
    },
    {
        "id": 205, "level": 2, "chapter_num": 5,
        "title_cn": "第一次去中国朋友家", "title_pinyin": "Dì-yī cì qù Zhōngguó péngyou jiā",
        "title_en": "Visiting a Chinese Friend's Home for the First Time", "title_th": "ไปบ้านเพื่อนคนจีนเป็นครั้งแรก",
        "topic_en": "Visiting Friends & Etiquette", "topic_th": "การไปเยี่ยมบ้านเพื่อนและมารยาท",
        "grammar_en": ["Simple Directional Complement (1): V + 来/去", "Simple Directional Complement (2): 进/出/上/下 + 来/去", "Pattern: 都...了 (Already)"],
        "grammar_th": ["คำเสริมทิศทางอย่างง่าย (1): V + 来 / 去", "คำเสริมทิศทางอย่างง่าย (2): 进/出/上/下/回 + 来/去", "โครงสร้าง 都……了 (ป่านนี้ก็...แล้ว)"]
    },
    {
        "id": 206, "level": 2, "chapter_num": 6,
        "title_cn": "小雪，生日快乐！", "title_pinyin": "Xiǎoxuě, shēngrì kuàilè!",
        "title_en": "Happy Birthday, Xiaoxue!", "title_th": "สุขสันต์วันเกิด เสี่ยวเสวี่ย!",
        "topic_en": "Birthdays, Gifts & Celebrations", "topic_th": "วันเกิด ของขวัญ และงานเลี้ยงฉลอง",
        "grammar_en": ["Adjective Reduplication: AA 的 (高高的, 红红的)", "Set Phrase: 什么的 (And so on)", "Structural Particle: 地 (Adverbial marker)"],
        "grammar_th": ["การซ้ำคำคุณศัพท์: AA 的 (เน้นลักษณะ/น่ารัก)", "วลีลงท้าย: 什么的 (และอื่นๆ)", "คำช่วยเชื่อมคำวิเศษณ์: 地 (Adj + 地 + Verb)"]
    },
    {
        "id": 207, "level": 2, "chapter_num": 7,
        "title_cn": "他篮球打得很好", "title_pinyin": "Tā lánqiú dǎ de hěn hǎo",
        "title_en": "He Plays Basketball Very Well", "title_th": "เขาเล่นบาสเกตบอลได้เก่งมาก",
        "topic_en": "Sports, Hobbies & Performance", "topic_th": "กีฬา งานอดิเรก และความสามารถ",
        "grammar_en": ["Contracted Complex: 一...就... (As soon as)", "Complement of State (1): V + 得 + Adj", "Complement of State (2): V + 得 + 不 + Adj"],
        "grammar_th": ["โครงสร้างเชื่อมประโยค: 一……就…… (พอ...ก็...ทันที)", "คำเสริมบอกสภาพ (1): V + 得 + Adj", "คำเสริมบอกสภาพ (2): V + 得 + 不 + Adj (รูปปฏิเสธ)"]
    },
    {
        "id": 208, "level": 2, "chapter_num": 8,
        "title_cn": "虽然你忘了，但是我记得", "title_pinyin": "Suīrán nǐ wàng le, dànshì wǒ jìde",
        "title_en": "Even Though You Forgot, I Remembered", "title_th": "ถึงแม้เธอจะลืม แต่ฉันยังจำได้",
        "topic_en": "Memory, Comparisons & Relationships", "topic_th": "ความจำ การเปรียบเทียบ และความสัมพันธ์",
        "grammar_en": ["Comparative Sentence (1): A 比 B + Adj", "Comparative Sentence (2): A 比 B + Adj + 一点儿/得多", "Transitional Complex: 虽然...但是..."],
        "grammar_th": ["ประโยคเปรียบเทียบ (1): A 比 B + Adj (A กว่า B)", "ประโยคเปรียบเทียบ (2): A 比 B + Adj + 一点儿 / 得多 / 多了", "ประโยคขัดแย้ง: 虽然……但是…… (แม้ว่า...แต่ว่า...)"]
    },
    {
        "id": 209, "level": 2, "chapter_num": 9,
        "title_cn": "我去买杯奶茶", "title_pinyin": "Wǒ qù mǎi bēi nǎichá",
        "title_en": "I'm Going to Buy a Cup of Bubble Tea", "title_th": "ฉันไปซื้อชานมสักแก้วนะ",
        "topic_en": "Daily Purchases, Drinks & Distance", "topic_th": "เครื่องดื่มยอดนิยมและระยะทาง",
        "grammar_en": ["Comparative Sentence (3): A 没有 B 那么/这么 + Adj", "Verb: 离 (Distance between places)", "Complement of Duration (1): V + 了 + Time"],
        "grammar_th": ["ประโยคเปรียบเทียบ (3): A 没有 B (那么/这么) + Adj (A ไม่...เท่า B)", "คำกริยาแสดงระยะห่าง: 离 (ห่างจาก: A 离 B + 近/远)", "คำเสริมบอกระยะเวลา (1): V + 了 + ช่วงเวลา"]
    },
    {
        "id": 210, "level": 2, "chapter_num": 10,
        "title_cn": "就要考试了", "title_pinyin": "Jiù yào kǎoshì le",
        "title_en": "The Exam Is Coming", "title_th": "ใกล้จะสอบแล้ว",
        "topic_en": "Exams, Preparing & Urgency", "topic_th": "การสอบ การเตรียมตัว และความเร่งด่วน",
        "grammar_en": ["Subject-Predicate as Predicate: 他身体很好", "Alternative Questions: A 还是 B？", "Pattern: 要/快要/就要...了 (Imminent action)"],
        "grammar_th": ["ประโยคที่ภาคแสดงเป็นประโยคย่อย: 他身体很好", "ประโยคคำถามเลือกตอบ: A 还是 B？ (หรือ)", "โครงสร้างแสดงเหตุการณ์ใกล้เกิด: 要/快要/就要……了 (ใกล้จะ...แล้ว)"]
    },
    {
        "id": 211, "level": 2, "chapter_num": 11,
        "title_cn": "我最喜欢吃中国菜", "title_pinyin": "Wǒ zuì xǐhuan chī Zhōngguó cài",
        "title_en": "I Like Chinese Food the Most", "title_th": "ฉันชอบกินอาหารจีนที่สุด",
        "topic_en": "Favorites, Tastes & Continuous States", "topic_th": "ความชอบ รสชาติอาหาร และสภาพที่คงอยู่",
        "grammar_en": ["Aspect Particle: 着 (1) (Continuing state)", "Aspect Particle: 着 (2) (V1 着 + V2)", "Adverb of Degree: 最 (Most / Best)"],
        "grammar_th": ["คำช่วยกริยาแสดงสภาพคงอยู่: 着 (1) (เช่น 门开着, 穿红衣服)", "การใช้ 着 เชื่อมกริยา (2): V1 着 + V2 (ทำกริยาหนึ่งในขณะที่มีสภาพอีกอย่าง)", "คำวิเศษณ์บอกระดับสูงสุด: 最 (ที่สุด)"]
    },
    {
        "id": 212, "level": 2, "chapter_num": 12,
        "title_cn": "这里比北京冷多了", "title_pinyin": "Zhèlǐ bǐ Běijīng lěng duō le",
        "title_en": "It's Much Colder Here Than in Beijing", "title_th": "ที่นี่หนาวกว่าปักกิ่งเยอะมาก",
        "topic_en": "Weather, Cities & Advanced Comparisons", "topic_th": "สภาพอากาศ เมืองต่างๆ และการเปรียบเทียบขั้นสูง",
        "grammar_en": ["Comparative (4): A 跟 B 一样/不一样", "Comparative (5): A 比 B 更/还 + Adj", "Comparative (6): A 比 B + V 得 + Adj"],
        "grammar_th": ["การเปรียบเทียบความเหมือน: A 跟 B 一样 / 不一样", "การเปรียบเทียบระดับยิ่งกว่า: A 比 B 更 / 还 + Adj", "การเปรียบเทียบผลการกระทำ: A 比 B + V 得 + Adj"]
    },
    {
        "id": 213, "level": 2, "chapter_num": 13,
        "title_cn": "我们爱上中文课", "title_pinyin": "Wǒmen ài shàng Zhōngwén kè",
        "title_en": "We Love Attending Chinese Class", "title_th": "พวกเรารักการเรียนวิชาภาษาจีน",
        "topic_en": "Classroom, Learning & Development", "topic_th": "ห้องเรียน การเรียนรู้ และการพัฒนา",
        "grammar_en": ["Double-Object Sentences (2): 送/借/还/教 + Person + Thing", "Comparative (7): A 不如 B", "Comparative (8): 越来越... (Gradual change)"],
        "grammar_th": ["ประโยคกรรมตรงกรรมรอง: 送/借/还/教 + บุคคล + สิ่งของ", "การเปรียบเทียบ: A 不如 B (A สู้ B ไม่ได้)", "โครงสร้างแสดงการเปลี่ยนแปลงตามลำดับ: 越来越…… (ขึ้นเรื่อยๆ)"]
    },
    {
        "id": 214, "level": 2, "chapter_num": 14,
        "title_cn": "一个人过年多没意思啊", "title_pinyin": "Yí ge rén guònián duō méi yìsi a",
        "title_en": "It's Boring to Celebrate Spring Festival Alone", "title_th": "ฉลองปีใหม่คนเดียวมันน่าเบื่อจะตาย",
        "topic_en": "Spring Festival & Exclamations", "topic_th": "เทศกาลตรุษจีน ประโยคอุทาน และทิศทาง",
        "grammar_en": ["Degree Adverb: 多 + Adj + 啊 (Exclamation)", "Existential Sentences: Place + V + 着/了 + Noun", "Compound Directional Complements: 上来, 下去, 回来"],
        "grammar_th": ["คำวิเศษณ์บอกระดับในประโยคอุทาน: 多 + Adj + 啊！", "ประโยคบอกการมีอยู่/คงอยู่: สถานที่ + V + 着/了 + สิ่งของ", "คำเสริมทิศทางแบบประสม: 上来, 下去, 跑回来"]
    },
    {
        "id": 215, "level": 2, "chapter_num": 15,
        "title_cn": "我想再去一次中国", "title_pinyin": "Wǒ xiǎng zài qù yí cì Zhōngguó",
        "title_en": "I Want to Go to China Again", "title_th": "ฉันอยากไปประเทศจีนอีกสักครั้ง",
        "topic_en": "Revisiting Places & Quantities", "topic_th": "การเดินทางซ้ำและจำนวนครั้ง",
        "grammar_en": ["Complement of Frequency (1): V + 次/遍", "Complement of Frequency (2): Position of Objects", "“有” Sentence (2): Reaching a Quantity/Duration"],
        "grammar_th": ["คำเสริมบอกจำนวนครั้ง (1): V + 次 / 遍", "คำเสริมบอกจำนวนครั้ง (2): ตำแหน่งของคำนามที่เป็นกรรม", "ประโยค “有” (2): มีถึง/นานถึง (有 + จำนวน เพื่อบอกว่าถึงระดับหนึ่งแล้ว)"]
    },

    # --- HSK 3 (18 Chapters) ---
    {
        "id": 301, "level": 3, "chapter_num": 1,
        "title_cn": "我们去机场接你们", "title_pinyin": "Wǒmen qù jīchǎng jiē nǐmen",
        "title_en": "We Will Pick You Up at the Airport", "title_th": "พวกเราจะไปรับพวกเธอที่สนามบิน",
        "topic_en": "Airport, Arrivals & Descriptions", "topic_th": "สนามบิน การรับส่ง และการบรรยายลักษณะบุคคล",
        "grammar_en": ["看上去 / 看起来 (Describing appearance)", "Indefinite Pronouns: 哪儿/什么/谁", "Multiple Attributives (多项定语)"],
        "grammar_th": ["看上去 / 看起来 (ดูเหมือนว่า/ดูท่าทาง)", "คำสรรพนามแสดงความไม่ชี้เฉพาะ: 哪儿 / 什么 / 谁", "บทขยายคำนามหลายชั้น (多项定语)"]
    },
    {
        "id": 302, "level": 3, "chapter_num": 2,
        "title_cn": "你们想吃什么就点什么", "title_pinyin": "Nǐmen xiǎng chī shénme jiù diǎn shénme",
        "title_en": "Order Whatever You Feel Like", "title_th": "อยากกินอะไรก็สั่งตามใจชอบได้เลย",
        "topic_en": "Restaurants, Food & Dining", "topic_th": "ร้านอาหาร วัฒนธรรมการกิน และการสั่งอาหาร",
        "grammar_en": ["Indefinite Pronouns: 什么...就...", "Parallel Conjunction: 又...又... (Both... and...)", "Dining expressions & etiquette"],
        "grammar_th": ["สรรพนามคำถามแสดงเงื่อนไข: 什么……就…… (อะไรก็...อันนั้น)", "คำเชื่อมคู่ขนาน: 又……又…… (ทั้ง...และ...)", "สำนวนการสั่งอาหารและการบริการ"]
    },
    {
        "id": 303, "level": 3, "chapter_num": 3,
        "title_cn": "这个小区挺好的", "title_pinyin": "Zhè ge xiǎoqū tǐng hǎo de",
        "title_en": "This Neighborhood Is Pretty Good", "title_th": "หมู่บ้านแห่งนี้ดีมากทีเดียว",
        "topic_en": "Housing, Renting & Appliances", "topic_th": "ที่พักอาศัย การเช่าบ้าน และเครื่องใช้ไฟฟ้า",
        "grammar_en": ["Pattern: 挺...的 (Quite / Pretty)", "Sequential Complex: 先...再... (First... then...)", "Directional Complements in Daily Life"],
        "grammar_th": ["โครงสร้างแสดงระดับ: 挺……的 (ค่อนข้าง/มากทีเดียว)", "ประโยคเชื่อมลำดับเหตุการณ์: 先……再…… (ก่อน...แล้วค่อย...)", "คำเสริมทิศทางในบริบทชีวิตประจำวัน"]
    },
    {
        "id": 304, "level": 3, "chapter_num": 4,
        "title_cn": "我借给你", "title_pinyin": "Wǒ jiè gěi nǐ",
        "title_en": "I'll Lend It to You", "title_th": "ฉันให้เธอยืม",
        "topic_en": "Travel, Borrowing & Comparing", "topic_th": "การท่องเที่ยว ยืมของ และการเปรียบเทียบ",
        "grammar_en": ["Comparative: 跟...一样/不一样", "Prepositional Phrase: 除了...以外 (Besides / Except)", "Time Adverb: 一直 (All along)"],
        "grammar_th": ["ประโยคเปรียบเทียบ: 跟……一样 / 不一样 (เหมือน/ไม่เหมือนกับ)", "วลีบุพบท: 除了……以外 (นอกจาก...แล้ว/ยกเว้น)", "คำวิเศษณ์บอกเวลา: 一直 (มาโดยตลอด/ตรงไป)"]
    },
    {
        "id": 305, "level": 3, "chapter_num": 5,
        "title_cn": "这样的照片才好看", "title_pinyin": "Zhèyàng de zhàopiàn cái hǎokàn",
        "title_en": "Photos Like This Look Good", "title_th": "รูปถ่ายแบบนี้ถึงจะดูดี",
        "topic_en": "Photography, Nature & Hobbies", "topic_th": "การถ่ายภาพ ธรรมชาติ และงานอดิเรก",
        "grammar_en": ["Adverbs: 才 vs 终于 (Only then vs Finally)", "Pattern: 对...感兴趣 (Interested in)", "Adjective Reduplication for Vivid Descriptions"],
        "grammar_th": ["คำวิเศษณ์: 才 (ถึงจะ) vs 终于 (ในที่สุดก็)", "โครงสร้าง: 对……感兴趣 (สนใจในเรื่อง...)", "การซ้ำคำคุณศัพท์เพื่อบรรยายภาพให้มีชีวิตชีวา"]
    },
    {
        "id": 306, "level": 3, "chapter_num": 6,
        "title_cn": "高铁上还可以点外卖", "title_pinyin": "Gāotiě shang hái kěyǐ diǎn wàimài",
        "title_en": "You Can Even Order Takeout on a High-Speed Train", "title_th": "บนรถไฟความเร็วสูงยังสั่งเดลิเวอรีได้ด้วย",
        "topic_en": "Transportation & Modern Technology", "topic_th": "การคมนาคม รถไฟความเร็วสูง และความสะดวกทันสมัย",
        "grammar_en": ["Pattern: 该...了 (Time to...)", "Hypothetical: 如果...就... (If... then...)", "Pattern: 越来越... (More and more)"],
        "grammar_th": ["โครงสร้าง: 该……了 (ถึงเวลาต้อง...แล้ว)", "ประโยคสมมุติ: 如果……就…… (ถ้าหาก...ก็...)", "โครงสร้างบอกความเปลี่ยนแปลง: 越来越…… (ขึ้นเรื่อยๆ)"]
    },
    {
        "id": 307, "level": 3, "chapter_num": 7,
        "title_cn": "那条裙子比短裤更好看", "title_pinyin": "Nà tiáo qúnzi bǐ duǎnkù gèng hǎokàn",
        "title_en": "That Skirt Looks Better Than the Shorts", "title_th": "กระโปรงตัวนั้นดูดีกว่ากางเกงขาสั้นอีก",
        "topic_en": "Shopping, Clothes & Sizes", "topic_th": "การช้อปปิ้ง เสื้อผ้า และการลองชุด",
        "grammar_en": ["Comparative: A 比 B + 更/还 + Adj", "Progressive Complex: 不但...而且... (Not only... but also...)", "Degree Complement: 极了 (Extremely)"],
        "grammar_th": ["ประโยคเปรียบเทียบขั้นกว่า: A 比 B + 更 / 还 + Adj (ยิ่งกว่า/ขึ้นไปอีก)", "ประโยคเชื่อมคล้อยตาม: 不但……而且…… (ไม่เพียงแต่...แถมยัง...)", "คำเสริมบอกระดับสูงสุด: 极了 (อย่างยิ่ง/สุดๆ)"]
    },
    {
        "id": 308, "level": 3, "chapter_num": 8,
        "title_cn": "他昨天出院了", "title_pinyin": "Tā zuótiān chūyuàn le",
        "title_en": "He Was Discharged from Hospital Yesterday", "title_th": "เขาออกจากโรงพยาบาลเมื่อวานนี้แล้ว",
        "topic_en": "Health, Hospital & Recovery", "topic_th": "สุขภาพ โรงพยาบาล และการฟื้นฟู",
        "grammar_en": ["Directional Complements Extended Meanings (1)", "Complement of Duration: 时量补语", "Time Prepositions: 以前 / 以后 / 前 / 后"],
        "grammar_th": ["คำเสริมทิศทางความหมายขยาย (1): 起来, 下去", "คำเสริมบอกระยะเวลา (时量补语): V + 了 + ระยะเวลา", "คำระบุความสัมพันธ์ทางเวลา: 以前 / 以后 / 前 / 后"]
    },
    {
        "id": 309, "level": 3, "chapter_num": 9,
        "title_cn": "打不好没关系", "title_pinyin": "Dǎ bù hǎo méiguānxi",
        "title_en": "It Doesn't Matter If You Don't Play Well", "title_th": "เล่นได้ไม่ดีก็ไม่เป็นไร",
        "topic_en": "Sports, Ball Games & Exercise", "topic_th": "กีฬา ลูกบอล และการออกกำลังกาย",
        "grammar_en": ["Purpose Complex: 为了... (In order to...)", "Potential Complement: 得/不 (打得好 / 打不好)", "Correlative: 越 A 越 B (The more A, the more B)"],
        "grammar_th": ["ประโยคบอกจุดประสงค์: 为了…… (เพื่อที่จะ...)", "คำเสริมบอกความเป็นไปได้ (可能补语): V + 得 / 不 + ผลลัพธ์", "โครงสร้างความสัมพันธ์ผันแปร: 越 A 越 B (ยิ่ง A ก็ยิ่ง B)"]
    },
    {
        "id": 310, "level": 3, "chapter_num": 10,
        "title_cn": "你明天再把书还给我", "title_pinyin": "Nǐ míngtiān zài bǎ shū huán gěi wǒ",
        "title_en": "You Can Return the Book to Me Tomorrow", "title_th": "พรุ่งนี้เธอค่อยคืนหนังสือให้ฉันนะ",
        "topic_en": "School, Studying & Returning Items", "topic_th": "การเรียน การอ่านหนังสือ และการคืนของ",
        "grammar_en": ["“把” Sentence (1): 把 + Object + Verb + 在/到/给", "Spatial Prepositions: 在...上 / 下 / 中", "Negative “把” Sentences with 没 / 别"],
        "grammar_th": ["ประโยค “把” (1): 把 + กรรม + กริยา + 在/到/给", "โครงสร้างบอกตำแหน่งทิศทาง: 在……上 / 下 / 中", "รูปปฏิเสธของประโยค “把” (ใช้ 没 หรือ 别 วางหน้า 把)"]
    },
    {
        "id": 311, "level": 3, "chapter_num": 11,
        "title_cn": "看来我没办法解决这个问题", "title_pinyin": "Kànlái wǒ méi bànfǎ jiějué zhè ge wèntí",
        "title_en": "It Seems I Have No Way to Solve This Problem", "title_th": "ดูท่าทางฉันคงไม่มีวิธีแก้ปัญหานี้แล้ว",
        "topic_en": "Workplace, Problem-Solving & Decisions", "topic_th": "ที่ทำงาน การแก้ปัญหา และการตัดสินใจ",
        "grammar_en": ["Choice Conjunctions: 还是 vs 或者", "“把” Sentence (2): 把 + Object + Verb + Result Complement", "Perspective Pattern: 对...来说 (As for...)"],
        "grammar_th": ["ความแตกต่างระหว่างคำว่า “还是” (คำถาม) กับ “或者” (บอกเล่า)", "ประโยค “把” (2): 把 + กรรม + กริยา + คำเสริมบอกผล", "โครงสร้างแสดงมุมมอง: 对……来说 (สำหรับ...แล้ว)"]
    },
    {
        "id": 312, "level": 3, "chapter_num": 12,
        "title_cn": "这个季节天气变化很快", "title_pinyin": "Zhè ge jìjié tiānqì biànhuà hěn kuài",
        "title_en": "The Weather Changes Quickly in This Season", "title_th": "ฤดูกาลนี้สภาพอากาศเปลี่ยนแปลงเร็วมาก",
        "topic_en": "Seasons, Climate & Daily Changes", "topic_th": "ฤดูกาล สภาพอากาศ และความเปลี่ยนแปลง",
        "grammar_en": ["Directional Complements Extended Meanings (2): 出来, 起来", "Subjectless Sentences (下雨了, 刮风了)", "Structural Particle: 地 vs 得 vs 的"],
        "grammar_th": ["คำเสริมทิศทางความหมายขยาย (2): 出来 (ปรากฏออกมา), 起来 (เริ่มต้นขึ้น)", "ประโยคไร้ประธาน (เช่น 下雨了, 刮风了)", "การแยกใช้คำช่วยไวยากรณ์ 3 ตัว: 的, 地, 得"]
    },
    {
        "id": 313, "level": 3, "chapter_num": 13,
        "title_cn": "只要努力，就一定能成功", "title_pinyin": "Zhǐyào nǔlì, jiù yídìng néng chénggōng",
        "title_en": "As Long as You Work Hard, You Will Succeed", "title_th": "ขอเพียงขยัน ก็ต้องประสบความสำเร็จได้อย่างแน่นอน",
        "topic_en": "Success, Effort & Dreams", "topic_th": "ความสำเร็จ ความพยายาม และความฝัน",
        "grammar_en": ["Conditional Complex: 只要...就... (As long as... then...)", "Adverbs: 一定 vs 必须 (Definitely vs Must)", "Noun/Adverb: 终于 (Finally at last)"],
        "grammar_th": ["ประโยคเงื่อนไขเพียงพอ: 只要……就…… (ขอเพียงแค่...ก็...)", "การใช้คำวิเศษณ์: 一定 (ต้อง...แน่ๆ) vs 必须 (จำเป็นต้อง)", "คำวิเศษณ์แสดงผลสำเร็จ: 终于 (ในที่สุดก็...สำเร็จ)"]
    },
    {
        "id": 314, "level": 3, "chapter_num": 14,
        "title_cn": "书丢了可怎么办呢", "title_pinyin": "Shū diū le kě zěnme bàn ne",
        "title_en": "What on Earth Should I Do If the Book Is Lost?", "title_th": "หนังสือหายไปแล้ว จะทำอย่างไรดีเนี่ย",
        "topic_en": "Emergencies, Accidents & Lost Items", "topic_th": "เหตุฉุกเฉิน ของหาย และการหาทางออก",
        "grammar_en": ["Emphatic Adverb: 可 (How / What on earth)", "Expression: 怎么办 (What to do)", "Passive: “被” Sentence basics (被 + Agent + Verb)"],
        "grammar_th": ["คำวิเศษณ์เน้นน้ำเสียงอารมณ์: 可 (ช่าง...เสียจริง/จะ...ได้ยังไง)", "สำนวนถามทางออก: 怎么办 (จะทำอย่างไรดี)", "ประโยคถูกกระทำ (被字句): ประธาน + 被 + ผู้กระทำ + กริยา"]
    },
    {
        "id": 315, "level": 3, "chapter_num": 15,
        "title_cn": "大家都说这儿的环境越来越好了", "title_pinyin": "Dàjiā dōu shuō zhèr de huánjìng yuèláiyuè hǎo le",
        "title_en": "Everyone Says the Environment Here Is Getting Better", "title_th": "ทุกคนต่างบอกว่าสิ่งแวดล้อมที่นี่ดีขึ้นเรื่อยๆ แล้ว",
        "topic_en": "Environment, City Life & Ecology", "topic_th": "สิ่งแวดล้อม ชีวิตในเมือง และธรรมชาติ",
        "grammar_en": ["Continuous Progress: 越来越... (Gradual change)", "Double Negation for Affirmation: 不得不 (Have to)", "Pronoun: 大家 (Everyone) with 都"],
        "grammar_th": ["โครงสร้างแสดงระดับที่เปลี่ยนไปตามเวลา: 越来越…… (ขึ้นเรื่อยๆ)", "ปฏิเสธซ้อนปฏิเสธเพื่อยืนยันหนักแน่น: 不得不 (จำใจต้อง/ปฏิเสธไม่ได้ว่า)", "การใช้สรรพนาม 大家 คู่กับ 都 เสมอ"]
    },
    {
        "id": 316, "level": 3, "chapter_num": 16,
        "title_cn": "请大家按时参加会议", "title_pinyin": "Qǐng dàjiā ànshí cānjiā huìyì",
        "title_en": "Please Attend the Meeting on Time", "title_th": "ขอให้ทุกคนเข้าร่วมการประชุมตรงเวลา",
        "topic_en": "Business Meetings, Punctuality & Schedules", "topic_th": "การประชุมธุรกิจ ความตรงต่อเวลา และตารางงาน",
        "grammar_en": ["Preposition: 按时 (On time) / 按照 (According to)", "Adverb: 互相 (Mutually / Each other)", "Polite Notification Structure: 请大家 + Verb"],
        "grammar_th": ["คำบุพบท: 按时 (ตรงตามเวลา) / 按照 (ตามที่...)", "คำวิเศษณ์: 互相 (ซึ่งกันและกัน)", "โครงสร้างแจ้งประกาศอย่างสุภาพ: 请大家 + กริยา"]
    },
    {
        "id": 317, "level": 3, "chapter_num": 17,
        "title_cn": "我要多向认真的人学习", "title_pinyin": "Wǒ yào duō xiàng rènzhēn de rén xuéxí",
        "title_en": "I Will Learn More from Conscientious People", "title_th": "ฉันจะต้องเรียนรู้จากคนที่ตั้งใจให้มากๆ",
        "topic_en": "Role Models, Work Ethic & Growth", "topic_th": "แบบอย่าง ความตั้งใจจริง และการพัฒนาตนเอง",
        "grammar_en": ["Preposition: 向 (Towards / Learning from someone)", "Rhetorical Question: 不是...吗？ (Isn't it...?)", "Restrictive Condition: 只有...才... (Only if... then...)"],
        "grammar_th": ["คำบุพบท: 向 (ไปยัง/เรียนรู้จาก: 向 + บุคคล + 学习)", "ประโยคย้อนถาม: 不是……吗？ (ไม่ใช่...หรอกหรือ?)", "ประโยคเงื่อนไขจำเป็นเพียงหนึ่งเดียว: 只有……才…… (มีเพียง...ถึงจะ...)"]
    },
    {
        "id": 318, "level": 3, "chapter_num": 18,
        "title_cn": "我学会了包饺子", "title_pinyin": "Wǒ xuéhuì le bāo jiǎozi",
        "title_en": "I've Learned How to Make Dumplings", "title_th": "ฉันห่อเกี๊ยวเป็นแล้ว",
        "topic_en": "Festivals, Cooking & Milestone Achievements", "topic_th": "เทศกาลตรุษจีน การทำอาหาร และความสำเร็จที่ภาคภูมิใจ",
        "grammar_en": ["Approximate Numbers: 几, 来, 多, 左右", "Temporal Starting Point: 从...起 (Starting from...)", "Sufficient Condition: 只要...就... (As long as...)"],
        "grammar_th": ["การบอกจำนวนตัวเลขโดยประมาณ: 几, 来, 多, 左右 (ประมาณ/ราวๆ)", "โครงสร้างบอกจุดเริ่มต้นของเวลา: 从……起 (นับตั้งแต่...เป็นต้นไป)", "ประโยคเงื่อนไข: 只要……就…… (ขอเพียงแค่...ก็...)"]
    }
]

print(f"Loaded {len(chapters_data)} chapters across HSK 1, 2, 3.")
