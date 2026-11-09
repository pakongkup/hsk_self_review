# data_hsk2.py
# Complete HSK 2 Vocabulary, Dialogue Sentences, and Grammar Points with Thai translations
# Aligned with the FLTRP 《新HSK教程 2》 15 Chapters

hsk2_words = [
    # Lesson 1: 她请我们吃了北京烤鸭
    {"chapter_num": 1, "hanzi": "请", "pinyin": "qǐng", "english": "to treat, invite", "thai": "เลี้ยง (อาหาร), เชิญ", "pos": "v.", "ex_cn": "今天晚上我请客！", "ex_py": "Jīntiān wǎnshang wǒ qǐngkè!", "ex_en": "Tonight it's my treat!", "ex_th": "คืนนี้ฉันเลี้ยงเอง!"},
    {"chapter_num": 1, "hanzi": "烤鸭", "pinyin": "kǎoyā", "english": "roast duck", "thai": "เป็ดย่าง, เป็ดปักกิ่ง", "pos": "n.", "ex_cn": "北京烤鸭非常有名。", "ex_py": "Běijīng kǎoyā fēicháng yǒumíng.", "ex_en": "Peking duck is very famous.", "ex_th": "เป็ดปักกิ่งมีชื่อเสียงมาก"},
    {"chapter_num": 1, "hanzi": "真", "pinyin": "zhēn", "english": "really, truly", "thai": "จริง, จริงๆ", "pos": "adv.", "ex_cn": "这个菜真好吃！", "ex_py": "Zhè ge cài zhēn hǎochī!", "ex_en": "This dish is truly delicious!", "ex_th": "อาหารจานนี้อร่อยจริงๆ!"},
    {"chapter_num": 1, "hanzi": "大家", "pinyin": "dàjiā", "english": "everyone", "thai": "ทุกคน", "pos": "pron.", "ex_cn": "大家都到了吗？", "ex_py": "Dàjiā dōu dào le ma?", "ex_en": "Has everyone arrived?", "ex_th": "ทุกคนมาถึงกันหมดหรือยัง?"},
    {"chapter_num": 1, "hanzi": "让", "pinyin": "ràng", "english": "to let, make, allow", "thai": "ให้ (สั่ง/อนุญาตให้ทำ)", "pos": "v.", "ex_cn": "老师让我回答问题。", "ex_py": "Lǎoshī ràng wǒ huídá wèntí.", "ex_en": "The teacher had me answer the question.", "ex_th": "คุณครูให้ฉันตอบคำถาม"},
    {"chapter_num": 1, "hanzi": "好吃", "pinyin": "hǎochī", "english": "delicious", "thai": "อร่อย", "pos": "adj.", "ex_cn": "这家饭馆的菜很好吃。", "ex_py": "Zhè jiā fànguǎn de cài hěn hǎochī.", "ex_en": "The food at this restaurant is delicious.", "ex_th": "อาหารของร้านนี้อร่อยมาก"},

    {"chapter_num": 1, "hanzi": "鸡蛋", "pinyin": "jīdàn", "english": "egg", "thai": "ไข่ไก่", "pos": "n.", "ex_cn": "早上我吃了一个鸡蛋。", "ex_py": "Zǎoshang wǒ chī le yí ge jīdàn.", "ex_en": "I ate an egg in the morning.", "ex_th": "ตอนเช้าฉันกินไข่ไก่ไป 1 ฟอง"},
    {"chapter_num": 1, "hanzi": "面条", "pinyin": "miàntiáo", "english": "noodles", "thai": "ก๋วยเตี๋ยว, บะหมี่", "pos": "n.", "ex_cn": "中午我想吃一碗牛肉面条。", "ex_py": "Zhōngwǔ wǒ xiǎng chī yì wǎn niúròu miàntiáo.", "ex_en": "I want to eat a bowl of beef noodles at noon.", "ex_th": "ตอนเที่ยงฉันอยากกินบะหมี่เนื้อสักชาม"},
    {"chapter_num": 1, "hanzi": "牛奶", "pinyin": "niúnǎi", "english": "cow's milk", "thai": "นมวัว, นมสด", "pos": "n.", "ex_cn": "睡前喝杯热牛奶很好。", "ex_py": "Shuì qián hē bēi rè niúnǎi hěn hǎo.", "ex_en": "Drinking hot milk before sleep is good.", "ex_th": "ดื่มนมอุ่นสักแก้วก่อนนอนดีมาก"},
    {"chapter_num": 1, "hanzi": "咖啡", "pinyin": "kāfēi", "english": "coffee", "thai": "กาแฟ", "pos": "n.", "ex_cn": "服务员，来一杯美式咖啡。", "ex_py": "Fúwùyuán, lái yì bēi Měishì kāfēi.", "ex_en": "Waiter, bring a cup of Americano.", "ex_th": "บริกร ขอกาแฟอเมริกาโน่หนึ่งแก้ว"},
    {"chapter_num": 1, "hanzi": "鱼", "pinyin": "yú", "english": "fish", "thai": "ปลา", "pos": "n.", "ex_cn": "清蒸鱼的味道非常鲜美。", "ex_py": "Qīngzhēng yú de wèidao fēicháng xiānměi.", "ex_en": "The steamed fish tastes very fresh and delicious.", "ex_th": "ปลานึ่งรสชาติสดหวานมาก"},

    # Lesson 2: 还是打车去北大吧
    {"chapter_num": 2, "hanzi": "还是", "pinyin": "háishi", "english": "had better / or", "thai": "...ดีกว่า / หรือ", "pos": "adv./conj.", "ex_cn": "下雨了，我们还是打车吧。", "ex_py": "Xià yǔ le, wǒmen háishi dǎchē ba.", "ex_en": "It's raining, we'd better take a taxi.", "ex_th": "ฝนตกแล้ว พวกเรานั่งแท็กซี่ดีกว่า"},
    {"chapter_num": 2, "hanzi": "打车", "pinyin": "dǎchē", "english": "to take a taxi", "thai": "เรียกแท็กซี่, นั่งแท็กซี่", "pos": "v.", "ex_cn": "在手机上打车很方便。", "ex_py": "Zài shǒujī shang dǎchē hěn fāngbiàn.", "ex_en": "Hailing a cab on a smartphone is convenient.", "ex_th": "เรียกแท็กซี่บนมือถือสะดวกมาก"},
    {"chapter_num": 2, "hanzi": "路", "pinyin": "lù", "english": "road, route, path", "thai": "ถนน, สาย (รถเมล์)", "pos": "n.", "ex_cn": "这条路上车很多。", "ex_py": "Zhè tiáo lù shang chē hěn duō.", "ex_en": "There are many cars on this road.", "ex_th": "บนถนนสายนี้มีรถเยอะมาก"},
    {"chapter_num": 2, "hanzi": "公共汽车", "pinyin": "gōnggòng qìchē", "english": "bus", "thai": "รถเมล์, รถประจำทาง", "pos": "n.", "ex_cn": "我每天坐公共汽车上班。", "ex_py": "Wǒ měitiān zuò gōnggòng qìchē shàngbān.", "ex_en": "I take the bus to work every day.", "ex_th": "ฉันนั่งรถเมล์ไปทำงานทุกวัน"},
    {"chapter_num": 2, "hanzi": "站", "pinyin": "zhàn", "english": "station, stop", "thai": "สถานี, ป้ายรถ", "pos": "n.", "ex_cn": "下一站是北京大学。", "ex_py": "Xià yí zhàn shì Běijīng Dàxué.", "ex_en": "The next stop is Peking University.", "ex_th": "ป้ายหน้าคือมหาวิทยาลัยปักกิ่ง"},
    {"chapter_num": 2, "hanzi": "快", "pinyin": "kuài", "english": "fast, quick", "thai": "เร็ว", "pos": "adj.", "ex_cn": "坐地铁比坐公共汽车快。", "ex_py": "Zuò dìtiě bǐ zuò gōnggòng qìchē kuài.", "ex_en": "Taking the subway is faster than taking the bus.", "ex_th": "นั่งรถไฟใต้ดินเร็วกว่านั่งรถเมล์"},
    {"chapter_num": 2, "hanzi": "慢", "pinyin": "màn", "english": "slow", "thai": "ช้า", "pos": "adj.", "ex_cn": "走得慢一点儿，注意安全。", "ex_py": "Zǒu de màn yìdiǎnr, zhùyì ānquán.", "ex_en": "Walk a bit slower, mind your safety.", "ex_th": "เดินให้ช้าลงหน่อย ระวังความปลอดภัยด้วย"},

    # Lesson 3: 我想去西安旅游
    {"chapter_num": 3, "hanzi": "旅游", "pinyin": "lǚyóu", "english": "to travel, tour", "thai": "ท่องเที่ยว, เที่ยว", "pos": "v.", "ex_cn": "今年夏天我想去云南旅游。", "ex_py": "Jīnnián xiàtiān wǒ xiǎng qù Yúnnán lǚyóu.", "ex_en": "This summer I want to travel to Yunnan.", "ex_th": "ฤดูร้อนปีนี้ฉันอยากไปเที่ยวที่ยูนนาน"},
    {"chapter_num": 3, "hanzi": "觉得", "pinyin": "juéde", "english": "to think, feel", "thai": "รู้สึกว่า, คิดว่า", "pos": "v.", "ex_cn": "你觉得这个地方怎么样？", "ex_py": "Nǐ juéde zhè ge dìfang zěnmeyàng?", "ex_en": "What do you think of this place?", "ex_th": "เธอคิดว่าสถานที่แห่งนี้เป็นอย่างไรบ้าง?"},
    {"chapter_num": 3, "hanzi": "最", "pinyin": "zuì", "english": "most, -est", "thai": "ที่สุด", "pos": "adv.", "ex_cn": "秋天是北京最好的季节。", "ex_py": "Qiūtiān shì Běijīng zuì hǎo de jìjié.", "ex_en": "Autumn is the best season in Beijing.", "ex_th": "ฤดูใบไม้ร่วงเป็นฤดูกาลที่ดีที่สุดของปักกิ่ง"},
    {"chapter_num": 3, "hanzi": "玩儿", "pinyin": "wánr", "english": "to play, have fun", "thai": "เที่ยวเล่น, เล่น", "pos": "v.", "ex_cn": "周末你打算去哪儿玩儿？", "ex_py": "Zhōumò nǐ dǎsuàn qù nǎr wánr?", "ex_en": "Where do you plan to go have fun this weekend?", "ex_th": "วันหยุดสุดสัปดาห์เธอวางแผนจะไปเที่ยวเล่นที่ไหน?"},
    {"chapter_num": 3, "hanzi": "次", "pinyin": "cì", "english": "measure word for times, frequency", "thai": "ครั้ง (ลักษณนาม)", "pos": "m.", "ex_cn": "这是我第一次来西安。", "ex_py": "Zhè shì wǒ dì-yī cì lái Xī'ān.", "ex_en": "This is my first time coming to Xi'an.", "ex_th": "นี่เป็นครั้งแรกที่ฉันมาซีอาน"},
    {"chapter_num": 3, "hanzi": "完", "pinyin": "wán", "english": "to finish, complete", "thai": "เสร็จ, จบ", "pos": "v.", "ex_cn": "作业我已经写完了。", "ex_py": "Zuòyè wǒ yǐjīng xiě wán le.", "ex_en": "I have already finished my homework.", "ex_th": "การบ้านฉันเขียนเสร็จเรียบร้อยแล้ว"},

    # Lesson 4: 你穿红色的很好看
    {"chapter_num": 4, "hanzi": "穿", "pinyin": "chuān", "english": "to wear, put on", "thai": "สวม, ใส่", "pos": "v.", "ex_cn": "今天天冷，多穿点儿衣服。", "ex_py": "Jīntiān tiān lěng, duō chuān diǎnr yīfu.", "ex_en": "It's cold today, wear more clothes.", "ex_th": "วันนี้อากาศหนาว ใส่เสื้อผ้าเยอะๆ หน่อยนะ"},
    {"chapter_num": 4, "hanzi": "红", "pinyin": "hóng", "english": "red", "thai": "สีแดง", "pos": "adj.", "ex_cn": "她有一件红色的毛衣。", "ex_py": "Tā yǒu yí jiàn hóngsè de máoyī.", "ex_en": "She has a red sweater.", "ex_th": "เธอมีเสื้อไหมพรมสีแดงตัวหนึ่ง"},
    {"chapter_num": 4, "hanzi": "白", "pinyin": "bái", "english": "white", "thai": "สีขาว", "pos": "adj.", "ex_cn": "他喜欢穿白色的衬衫。", "ex_py": "Tā xǐhuan chuān báisè de chènshān.", "ex_en": "He likes wearing white shirts.", "ex_th": "เขาชอบใส่เสื้อเชิ้ตสีขาว"},
    {"chapter_num": 4, "hanzi": "黑", "pinyin": "hēi", "english": "black, dark", "thai": "สีดำ", "pos": "adj.", "ex_cn": "那双黑色的鞋子很合脚。", "ex_py": "Nà shuāng hēisè de xiézi hěn héjiǎo.", "ex_en": "Those black shoes fit very well.", "ex_th": "รองเท้าสีดำคู่นั้นพอดีเท้ามาก"},
    {"chapter_num": 4, "hanzi": "好看", "pinyin": "hǎokàn", "english": "good-looking, pretty", "thai": "ดูดี, สวยงาม, น่าดู", "pos": "adj.", "ex_cn": "这朵花真好看。", "ex_py": "Zhè duǒ huā zhēn hǎokàn.", "ex_en": "This flower is really pretty.", "ex_th": "ดอกไม้ดอกนี้สวยจริงๆ"},
    {"chapter_num": 4, "hanzi": "件", "pinyin": "jiàn", "english": "measure word for clothes, matters", "thai": "ตัว, ชิ้น, เรื่อง (ลักษณนาม)", "pos": "m.", "ex_cn": "我想买一件新大衣。", "ex_py": "Wǒ xiǎng mǎi yí jiàn xīn dàyī.", "ex_en": "I want to buy a new coat.", "ex_th": "ฉันอยากซื้อเสื้อโค้ตใหม่สักตัว"},
    {"chapter_num": 4, "hanzi": "因为", "pinyin": "yīnwèi", "english": "because", "thai": "เพราะว่า", "pos": "conj.", "ex_cn": "因为生病，他没来上课。", "ex_py": "Yīnwèi shēngbìng, tā méi lái shàngkè.", "ex_en": "Because of illness, he didn't attend class.", "ex_th": "เพราะว่าป่วย เขาจึงไม่ได้มาเรียน"},
    {"chapter_num": 4, "hanzi": "所以", "pinyin": "suǒyǐ", "english": "therefore, so", "thai": "ดังนั้น, จึง", "pos": "conj.", "ex_cn": "因为喜欢中国，所以我学中文。", "ex_py": "Yīnwèi xǐhuan Zhōngguó, suǒyǐ wǒ xué Zhōngwén.", "ex_en": "Because I like China, so I study Chinese.", "ex_th": "เพราะชอบประเทศจีน ดังนั้นฉันจึงเรียนภาษาจีน"},

    # Lesson 5: 第一次去中国朋友家
    {"chapter_num": 5, "hanzi": "进", "pinyin": "jìn", "english": "to enter, go in", "thai": "เข้า", "pos": "v.", "ex_cn": "请进，别客气！", "ex_py": "Qǐng jìn, bié kèqi!", "ex_en": "Please come in, don't stand on ceremony!", "ex_th": "เชิญเข้ามาข้างใน อย่าเกรงใจเลย!"},
    {"chapter_num": 5, "hanzi": "出", "pinyin": "chū", "english": "to go out, exit", "thai": "ออก", "pos": "v.", "ex_cn": "他刚走出校门。", "ex_py": "Tā gāng zǒu chū xiàomén.", "ex_en": "He just walked out of the school gate.", "ex_th": "เขาเพิ่งเดินออกจากประตูโรงเรียนไป"},
    {"chapter_num": 5, "hanzi": "送", "pinyin": "sòng", "english": "to deliver, gift, see off", "thai": "มอบให้, ส่ง", "pos": "v.", "ex_cn": "这是送给你的生日礼物。", "ex_py": "Zhè shì sòng gěi nǐ de shēngrì lǐwù.", "ex_en": "This is a birthday gift for you.", "ex_th": "นี่คือของขวัญวันเกิดที่มอบให้เธอ"},
    {"chapter_num": 5, "hanzi": "礼物", "pinyin": "lǐwù", "english": "gift, present", "thai": "ของขวัญ", "pos": "n.", "ex_cn": "谢谢你这么好的礼物！", "ex_py": "Xièxie nǐ zhème hǎo de lǐwù!", "ex_en": "Thank you for such a great gift!", "ex_th": "ขอบคุณสำหรับของขวัญที่ดีขนาดนี้นะ!"},
    {"chapter_num": 5, "hanzi": "都", "pinyin": "dōu", "english": "all / already (都...了)", "thai": "ทั้งหมด, ทั้งสิ้น / ป่านนี้ก็...แล้ว", "pos": "adv.", "ex_cn": "都十点了，快去睡觉吧。", "ex_py": "Dōu shí diǎn le, kuài qù shuìjiào ba.", "ex_en": "It's already 10 o'clock, hurry and go sleep.", "ex_th": "ป่านนี้สี่ทุ่มแล้ว รีบไปนอนเถอะ"},

    # Lesson 6: 小雪，生日快乐！
    {"chapter_num": 6, "hanzi": "生日", "pinyin": "shēngrì", "english": "birthday", "thai": "วันเกิด", "pos": "n.", "ex_cn": "祝你生日快乐！", "ex_py": "Zhù nǐ shēngrì kuàilè!", "ex_en": "Happy birthday to you!", "ex_th": "สุขสันต์วันเกิดนะ!"},
    {"chapter_num": 6, "hanzi": "快乐", "pinyin": "kuàilè", "english": "happy, cheerful", "thai": "มีความสุข", "pos": "adj.", "ex_cn": "祝大家周末快乐！", "ex_py": "Zhù dàjiā zhōumò kuàilè!", "ex_en": "Wish everyone a happy weekend!", "ex_th": "ขอให้ทุกคนมีความสุขในวันหยุดสุดสัปดาห์!"},
    {"chapter_num": 6, "hanzi": "给", "pinyin": "gěi", "english": "to give", "thai": "ให้", "pos": "v./prep.", "ex_cn": "我送给她一本书。", "ex_py": "Wǒ sòng gěi tā yì běn shū.", "ex_en": "I gave her a book.", "ex_th": "ฉันมอบหนังสือให้เธอหนึ่งเล่ม"},
    {"chapter_num": 6, "hanzi": "高兴", "pinyin": "gāoxìng", "english": "glad, joyful", "thai": "ดีใจ", "pos": "adj.", "ex_cn": "今天见到了老朋友，真高兴！", "ex_py": "Jīntiān jiàndào le lǎo péngyou, zhēn gāoxìng!", "ex_en": "I met an old friend today, so happy!", "ex_th": "วันนี้ได้เจอเพื่อนเก่า ดีใจจริงๆ!"},
    {"chapter_num": 6, "hanzi": "地", "pinyin": "de", "english": "structural particle for adverbs", "thai": "อย่าง... (คำช่วยเชื่อมคำวิเศษณ์)", "pos": "part.", "ex_cn": "孩子们高兴地笑了起来。", "ex_py": "Háizimen gāoxìng de xiào le qǐlái.", "ex_en": "The children laughed happily.", "ex_th": "เด็กๆ พากันหัวเราะอย่างมีความสุข"},

    # Lesson 7: 他篮球打得很好
    {"chapter_num": 7, "hanzi": "打", "pinyin": "dǎ", "english": "to play (sports with hands), hit", "thai": "เล่น (กีฬาที่ใช้มือ), ตี", "pos": "v.", "ex_cn": "他喜欢打羽毛球。", "ex_py": "Tā xǐhuan dǎ yǔmáoqiú.", "ex_en": "He likes playing badminton.", "ex_th": "เขาชอบเล่นแบดมินตัน"},
    {"chapter_num": 7, "hanzi": "篮球", "pinyin": "lánqiú", "english": "basketball", "thai": "บาสเกตบอล", "pos": "n.", "ex_cn": "下午我们去打篮球吧。", "ex_py": "Xiàwǔ wǒmen qù dǎ lánqiú ba.", "ex_en": "Let's go play basketball this afternoon.", "ex_th": "ตอนบ่ายพวกเราไปเล่นบาสเกตบอลกันเถอะ"},
    {"chapter_num": 7, "hanzi": "踢", "pinyin": "tī", "english": "to kick", "thai": "เตะ", "pos": "v.", "ex_cn": "他在草地上踢足球。", "ex_py": "Tā zài cǎodì shang tī zúqiú.", "ex_en": "He is playing soccer on the lawn.", "ex_th": "เขาเตะฟุตบอลอยู่บนสนามหญ้า"},
    {"chapter_num": 7, "hanzi": "足球", "pinyin": "zúqiú", "english": "football, soccer", "thai": "ฟุตบอล", "pos": "n.", "ex_cn": "中国有很多足球迷。", "ex_py": "Zhōngguó yǒu hěn duō zúqiúmí.", "ex_en": "China has many soccer fans.", "ex_th": "ประเทศจีนมีแฟนบอลเยอะมาก"},
    {"chapter_num": 7, "hanzi": "得", "pinyin": "de", "english": "structural particle for complement", "thai": "ได้ (คำช่วยเชื่อมคำเสริมบอกสภาพ/ระดับ)", "pos": "part.", "ex_cn": "他说汉语说得非常流利。", "ex_py": "Tā shuō Hànyǔ shuō de fēicháng liúlì.", "ex_en": "He speaks Chinese very fluently.", "ex_th": "เขาพูดภาษาจีนได้คล่องแคล่วมาก"},
    {"chapter_num": 7, "hanzi": "跑步", "pinyin": "pǎobù", "english": "to run, jog", "thai": "วิ่ง, วิ่งออกกำลังกาย", "pos": "v.", "ex_cn": "早上跑步对身体很好。", "ex_py": "Zǎoshang pǎobù duì shēntǐ hěn hǎo.", "ex_en": "Morning jogging is very good for health.", "ex_th": "วิ่งตอนเช้าดีต่อสุขภาพมาก"},
    {"chapter_num": 7, "hanzi": "游泳", "pinyin": "yóuyǒng", "english": "to swim", "thai": "ว่ายน้ำ", "pos": "v.", "ex_cn": "夏天大家都喜欢游泳。", "ex_py": "Xiàtiān dàjiā dōu xǐhuan yóuyǒng.", "ex_en": "Everyone likes swimming in summer.", "ex_th": "ฤดูร้อนทุกคนต่างชอบว่ายน้ำ"},

    # Lesson 8: 虽然你忘了，但是我记得
    {"chapter_num": 8, "hanzi": "记得", "pinyin": "jìde", "english": "to remember", "thai": "จำได้", "pos": "v.", "ex_cn": "你还记得他的电话号码吗？", "ex_py": "Nǐ hái jìde tā de diànhuà hàomǎ ma?", "ex_en": "Do you still remember his phone number?", "ex_th": "เธอยังจำหมายเลขโทรศัพท์ของเขาได้ไหม?"},
    {"chapter_num": 8, "hanzi": "忘", "pinyin": "wàng", "english": "to forget", "thai": "ลืม", "pos": "v.", "ex_cn": "别忘了带雨伞！", "ex_py": "Bié wàng le dài yǔsǎn!", "ex_en": "Don't forget to bring an umbrella!", "ex_th": "อย่าลืมพกร่มไปด้วยนะ!"},
    {"chapter_num": 8, "hanzi": "虽然", "pinyin": "suīrán", "english": "although, even though", "thai": "แม้ว่า, ถึงแม้ว่า", "pos": "conj.", "ex_cn": "虽然很累，但是很开心。", "ex_py": "Suīrán hěn lèi, dànshì hěn kāixīn.", "ex_en": "Although tired, very happy.", "ex_th": "ถึงแม้จะเหนื่อยมาก แต่ก็มีความสุขมาก"},
    {"chapter_num": 8, "hanzi": "但是", "pinyin": "dànshì", "english": "but, however", "thai": "แต่ว่า, แต่", "pos": "conj.", "ex_cn": "这件衣服好看，但是太贵了。", "ex_py": "Zhè jiàn yīfu hǎokàn, dànshì tài guì le.", "ex_en": "This piece of clothing looks good, but it's too expensive.", "ex_th": "เสื้อตัวนี้สวยนะ แต่แพงเกินไป"},
    {"chapter_num": 8, "hanzi": "比", "pinyin": "bǐ", "english": "to compare; than", "thai": "กว่า (เปรียบเทียบ)", "pos": "prep.", "ex_cn": "今天比昨天冷。", "ex_py": "Jīntiān bǐ zuótiān lěng.", "ex_en": "Today is colder than yesterday.", "ex_th": "วันนี้หนาวกว่าเมื่อวาน"},
    {"chapter_num": 8, "hanzi": "贵", "pinyin": "guì", "english": "expensive", "thai": "แพง", "pos": "adj.", "ex_cn": "这个包太贵了，不买吧。", "ex_py": "Zhè ge bāo tài guì le, bù mǎi ba.", "ex_en": "This bag is too expensive, let's not buy it.", "ex_th": "กระเป๋าใบนี้แพงเกินไป อย่าซื้อเลย"},
    {"chapter_num": 8, "hanzi": "便宜", "pinyin": "piányi", "english": "cheap, inexpensive", "thai": "ถูก (ราคาถูก)", "pos": "adj.", "ex_cn": "这里的菜又便宜又新鲜。", "ex_py": "Zhèlǐ de cài yòu piányi yòu xīnxiān.", "ex_en": "The food here is both cheap and fresh.", "ex_th": "กับข้าวที่นี่ทั้งถูกและสดใหม่"},

    # Lesson 9: 我去买杯奶茶
    {"chapter_num": 9, "hanzi": "杯", "pinyin": "bēi", "english": "cup, glass (measure word)", "thai": "แก้ว, ถ้วย (ลักษณนาม)", "pos": "m.", "ex_cn": "我想喝一杯冰咖啡。", "ex_py": "Wǒ xiǎng hē yì bēi bīng kāfēi.", "ex_en": "I'd like to drink a glass of iced coffee.", "ex_th": "ฉันอยากดื่มกาแฟเย็นสักหนึ่งแก้ว"},
    {"chapter_num": 9, "hanzi": "奶茶", "pinyin": "nǎichá", "english": "milk tea", "thai": "ชานม", "pos": "n.", "ex_cn": "中国年轻人很爱喝奶茶。", "ex_py": "Zhōngguó niánqīngrén hěn ài hē nǎichá.", "ex_en": "Young Chinese people love drinking milk tea.", "ex_th": "คนรุ่นใหม่ในจีนชอบดื่มชานมมาก"},
    {"chapter_num": 9, "hanzi": "离", "pinyin": "lí", "english": "away from (distance)", "thai": "ห่างจาก (ระยะทาง/เวลา)", "pos": "v./prep.", "ex_cn": "学校离地铁站很近。", "ex_py": "Xuéxiào lí dìtiězhàn hěn jìn.", "ex_en": "The school is very close to the subway station.", "ex_th": "โรงเรียนอยู่ใกล้สถานีรถไฟใต้ดินมาก"},
    {"chapter_num": 9, "hanzi": "远", "pinyin": "yuǎn", "english": "far, distant", "thai": "ไกล", "pos": "adj.", "ex_cn": "你家离公司远不远？", "ex_py": "Nǐ jiā lí gōngsī yuǎn bù yuǎn?", "ex_en": "Is your home far from the company?", "ex_th": "บ้านของเธออยู่ไกลจากบริษัทไหม?"},
    {"chapter_num": 9, "hanzi": "近", "pinyin": "jìn", "english": "near, close", "thai": "ใกล้", "pos": "adj.", "ex_cn": "超市离这里很近，走五分钟就到了。", "ex_py": "Chāoshì lí zhèlǐ hěn jìn, zǒu wǔ fēnzhōng jiù dào le.", "ex_en": "The supermarket is very close, a 5-minute walk.", "ex_th": "ซูเปอร์มาร์เก็ตอยู่ใกล้ที่นี่มาก เดิน 5 นาทีก็ถึงแล้ว"},
    {"chapter_num": 9, "hanzi": "等", "pinyin": "děng", "english": "to wait", "thai": "รอ", "pos": "v.", "ex_cn": "请稍等一下。", "ex_py": "Qǐng shāoděng yíxià.", "ex_en": "Please wait a moment.", "ex_th": "กรุณารอสักครู่"},

    # Lesson 10: 就要考试了
    {"chapter_num": 10, "hanzi": "考试", "pinyin": "kǎoshì", "english": "exam, test", "thai": "สอบ, การสอบ", "pos": "v./n.", "ex_cn": "下周我们有汉语考试。", "ex_py": "Xià zhōu wǒmen yǒu Hànyǔ kǎoshì.", "ex_en": "We have a Chinese exam next week.", "ex_th": "สัปดาห์หน้าพวกเรามีการสอบภาษาจีน"},
    {"chapter_num": 10, "hanzi": "要", "pinyin": "yào", "english": "to want / be going to", "thai": "จะ, ต้องการ", "pos": "v.", "ex_cn": "火车就要开了，快上车！", "ex_py": "Huǒchē jiù yào kāi le, kuài shàngchē!", "ex_en": "The train is about to leave, hurry and board!", "ex_th": "รถไฟใกล้จะออกแล้ว รีบขึ้นรถเร็ว!"},
    {"chapter_num": 10, "hanzi": "题", "pinyin": "tí", "english": "topic, exam problem", "thai": "ข้อสอบ, หัวข้อ", "pos": "n.", "ex_cn": "这次考试的题很多。", "ex_py": "Zhè cì kǎoshì de tí hěn duō.", "ex_en": "There are many questions on this exam.", "ex_th": "ข้อสอบครั้งนี้มีข้อสอบเยอะมาก"},
    {"chapter_num": 10, "hanzi": "懂", "pinyin": "dǒng", "english": "to understand, know", "thai": "เข้าใจ, รู้เรื่อง", "pos": "v.", "ex_cn": "这道题你听懂了吗？", "ex_py": "Zhè dào tí nǐ tīng dǒng le ma?", "ex_en": "Did you understand this problem?", "ex_th": "ข้อสอบข้อนี้เธอฟังเข้าใจหรือยัง?"},
    {"chapter_num": 10, "hanzi": "完", "pinyin": "wán", "english": "to finish", "thai": "เสร็จสิ้น", "pos": "v.", "ex_cn": "我一个小时就做完了。", "ex_py": "Wǒ yì ge xiǎoshí jiù zuò wán le.", "ex_en": "I finished it in one hour.", "ex_th": "ฉันทำเสร็จในหนึ่งชั่วโมงแล้ว"},

    # Lesson 11: 我最喜欢吃中国菜
    {"chapter_num": 11, "hanzi": "开", "pinyin": "kāi", "english": "to open", "thai": "เปิด", "pos": "v.", "ex_cn": "门开着呢，请进吧。", "ex_py": "Mén kāizhe ne, qǐng jìn ba.", "ex_en": "The door is open, please come in.", "ex_th": "ประตูเปิดอยู่ เชิญเข้ามาเถอะ"},
    {"chapter_num": 11, "hanzi": "关", "pinyin": "guān", "english": "to close, turn off", "thai": "ปิด", "pos": "v.", "ex_cn": "走的时候别忘了关空调。", "ex_py": "Zǒu de shíhou bié wàng le guān kōngtiáo.", "ex_en": "Don't forget to turn off the AC when leaving.", "ex_th": "ตอนออกไปอย่าลืมปิดแอร์นะ"},
    {"chapter_num": 11, "hanzi": "着", "pinyin": "zhe", "english": "aspect particle indicating ongoing state", "thai": "อยู่ (คำช่วยแสดงสภาพที่ต่อเนื่องคงอยู่)", "pos": "part.", "ex_cn": "墙上挂着一张中国地图。", "ex_py": "Qiáng shang guàzhe yì zhāng Zhōngguó dìtú.", "ex_en": "A map of China hangs on the wall.", "ex_th": "บนผนังมีแผนที่ประเทศจีนแขวนอยู่"},
    {"chapter_num": 11, "hanzi": "笑", "pinyin": "xiào", "english": "to smile, laugh", "thai": "ยิ้ม, หัวเราะ", "pos": "v.", "ex_cn": "她笑着对我点了点头。", "ex_py": "Tā xiàozhe duì wǒ diǎn le diǎn tóu.", "ex_en": "She smiled and nodded to me.", "ex_th": "เธอยิ้มและพยักหน้าให้ฉัน"},

    # Lesson 12: 这里比北京冷多了
    {"chapter_num": 12, "hanzi": "更", "pinyin": "gèng", "english": "even more, further", "thai": "ยิ่ง, ยิ่งกว่าเดิม", "pos": "adv.", "ex_cn": "明天会比今天更冷。", "ex_py": "Míngtiān huì bǐ jīntiān gèng lěng.", "ex_en": "Tomorrow will be even colder than today.", "ex_th": "พรุ่งนี้จะยิ่งหนาวกว่าวันนี้อีก"},
    {"chapter_num": 12, "hanzi": "阴", "pinyin": "yīn", "english": "overcast, cloudy", "thai": "ครึ้ม, มืดครึ้ม", "pos": "adj.", "ex_cn": "今天阴天，好像要下雨了。", "ex_py": "Jīntiān yīntiān, hǎoxiàng yào xià yǔ le.", "ex_en": "It's overcast today, looks like rain.", "ex_th": "วันนี้ฟ้าครึ้ม ดูเหมือนฝนจะตกแล้ว"},
    {"chapter_num": 12, "hanzi": "晴", "pinyin": "qíng", "english": "clear, sunny", "thai": "แจ่มใส, แดดออก", "pos": "adj.", "ex_cn": "明天是个大晴天。", "ex_py": "Míngtiān shì ge dà qíngtiān.", "ex_en": "Tomorrow will be a very sunny day.", "ex_th": "พรุ่งนี้จะเป็นวันที่แดดแจ่มใสมาก"},
    {"chapter_num": 12, "hanzi": "雪", "pinyin": "xuě", "english": "snow", "thai": "หิมะ", "pos": "n.", "ex_cn": "外面的雪下得很大。", "ex_py": "Wàimian de xuě xià de hěn dà.", "ex_en": "Snow is falling heavily outside.", "ex_th": "หิมะข้างนอกตกหนักมาก"},

    # Lesson 13: 我们爱上中文课
    {"chapter_num": 13, "hanzi": "爱", "pinyin": "ài", "english": "to love, like deeply", "thai": "รัก, ชอบมาก", "pos": "v.", "ex_cn": "我们班同学都很爱学汉语。", "ex_py": "Wǒmen bān tóngxué dōu hěn ài xué Hànyǔ.", "ex_en": "Students in our class all love studying Chinese.", "ex_th": "เพื่อนร่วมชั้นของพวกเราทุกคนรักการเรียนภาษาจีนมาก"},
    {"chapter_num": 13, "hanzi": "上课", "pinyin": "shàngkè", "english": "to attend class", "thai": "เข้าเรียน", "pos": "v.", "ex_cn": "老师进来了，开始上课吧。", "ex_py": "Lǎoshī jìnlái le, kāishǐ shàngkè ba.", "ex_en": "The teacher came in, let's start class.", "ex_th": "คุณครูเข้ามาแล้ว เริ่มเข้าเรียนกันเถอะ"},
    {"chapter_num": 13, "hanzi": "下课", "pinyin": "xiàkè", "english": "class finishes", "thai": "เลิกเรียน", "pos": "v.", "ex_cn": "下课以后我们去打球。", "ex_py": "Xiàkè yǐhòu wǒmen qù dǎqiú.", "ex_en": "After class finishes we'll play ball.", "ex_th": "หลังเลิกเรียนพวกเราจะไปเล่นบอล"},
    {"chapter_num": 13, "hanzi": "问题", "pinyin": "wèntí", "english": "question, problem", "thai": "คำถาม, ปัญหา", "pos": "n.", "ex_cn": "大家还有什么问题吗？", "ex_py": "Dàjiā hái yǒu shénme wèntí ma?", "ex_en": "Does anyone have any more questions?", "ex_th": "ทุกคนยังมีคำถามอะไรอีกไหม?"},
    {"chapter_num": 13, "hanzi": "教", "pinyin": "jiāo", "english": "to teach", "thai": "สอน", "pos": "v.", "ex_cn": "王老师教我们中国历史。", "ex_py": "Wáng lǎoshī jiāo wǒmen Zhōngguó lìshǐ.", "ex_en": "Teacher Wang teaches us Chinese history.", "ex_th": "อาจารย์หวังสอนประวัติศาสตร์จีนให้พวกเรา"},

    # Lesson 14: 一个人过年多没意思啊
    {"chapter_num": 14, "hanzi": "过", "pinyin": "guò", "english": "to spend (time), celebrate", "thai": "ฉลอง (เทศกาล), ใช้เวลา", "pos": "v.", "ex_cn": "今年你在哪儿过年？", "ex_py": "Jīnnián nǐ zài nǎr guònián?", "ex_en": "Where are you celebrating New Year this year?", "ex_th": "ปีนี้เธอจะไปฉลองปีใหม่ที่ไหน?"},
    {"chapter_num": 14, "hanzi": "年", "pinyin": "nián", "english": "year / New Year", "thai": "ปี / เทศกาลปีใหม่", "pos": "n.", "ex_cn": "新年快乐！", "ex_py": "Xīnnián kuàilè!", "ex_en": "Happy New Year!", "ex_th": "สวัสดีปีใหม่!"},
    {"chapter_num": 14, "hanzi": "意思", "pinyin": "yìsi", "english": "meaning, fun, interest", "thai": "ความหมาย, ความสนุก", "pos": "n.", "ex_cn": "这个电影真有意思！", "ex_py": "Zhè ge diànyǐng zhēn yǒu yìsi!", "ex_en": "This movie is really interesting!", "ex_th": "หนังเรื่องนี้น่าสนใจมากจริงๆ!"},
    {"chapter_num": 14, "hanzi": "多", "pinyin": "duō", "english": "how (exclamation of degree)", "thai": "ช่าง...อะไรอย่างนี้ (คำบอกระดับในประโยคอุทาน)", "pos": "adv.", "ex_cn": "大家都在一起多好啊！", "ex_py": "Dàjiā dōu zài yìqǐ duō hǎo a!", "ex_en": "How wonderful it is that everyone is together!", "ex_th": "ทุกคนได้อยู่พร้อมหน้ากันช่างดีอะไรอย่างนี้!"},

    # Lesson 15: 我想再去一次中国
    {"chapter_num": 15, "hanzi": "再", "pinyin": "zài", "english": "again, once more", "thai": "อีกครั้ง, อีก", "pos": "adv.", "ex_cn": "请您再说一遍，好吗？", "ex_py": "Qǐng nín zài shuō yí biàn, hǎo ma?", "ex_en": "Please say that once again, okay?", "ex_th": "กรุณาช่วยพูดอีกรอบหนึ่งได้ไหมครับ/ค่ะ?"},
    {"chapter_num": 15, "hanzi": "次", "pinyin": "cì", "english": "time (frequency)", "thai": "ครั้ง", "pos": "m.", "ex_cn": "我去过两次上海。", "ex_py": "Wǒ qù guò liǎng cì Shànghǎi.", "ex_en": "I have been to Shanghai twice.", "ex_th": "ฉันเคยไปเซี่ยงไฮ้มาสองครั้งแล้ว"},
    {"chapter_num": 15, "hanzi": "飞机票", "pinyin": "fēijīpiào", "english": "plane ticket", "thai": "ตั๋วเครื่องบิน", "pos": "n.", "ex_cn": "现在的飞机票很便宜。", "ex_py": "Xiànzài de fēijīpiào hěn piányi.", "ex_en": "Plane tickets right now are very cheap.", "ex_th": "ตั๋วเครื่องบินตอนนี้ราคาถูกมาก"},
    {"chapter_num": 15, "hanzi": "帮", "pinyin": "bāng", "english": "to help, assist", "thai": "ช่วย, ช่วยเหลือ", "pos": "v.", "ex_cn": "你能帮我拿一下包吗？", "ex_py": "Nǐ néng bāng wǒ ná yíxià bāo ma?", "ex_en": "Can you help me hold the bag for a moment?", "ex_th": "เธอช่วยถือกระเป๋าให้ฉันสักครู่ได้ไหม?"}
]

hsk2_sentences = [
    # Lesson 1
    {"chapter_num": 1, "context": "การเลี้ยงอาหารเพื่อนคนจีน", "hanzi": "今天晚上王老师请我们吃了地道的北京烤鸭。", "pinyin": "Jīntiān wǎnshang Wáng lǎoshī qǐng wǒmen chī le dìdao de Běijīng kǎoyā.", "english": "Tonight Teacher Wang treated us to authentic Peking duck.", "thai": "คืนนี้อาจารย์หวังเลี้ยงเป็ดปักกิ่งรสชาติดั้งเดิมแก่พวกเรา", "cloze_target": "请", "cloze_hint_en": "to treat", "cloze_hint_th": "เลี้ยง", "grammar_en": "Pivotal sentence with 请", "grammar_th": "ประโยคกริยาซ้อนด้วย 请"},
    {"chapter_num": 1, "context": "การชวนตัดสินใจร่วมกัน", "hanzi": "我们今天就点烤鸭吧！", "pinyin": "Wǒmen jīntiān jiù diǎn kǎoyā ba!", "english": "Let's order roast duck today!", "thai": "วันนี้พวกเราสั่งเป็ดย่างกันเถอะ!", "cloze_target": "吧", "cloze_hint_en": "suggestion particle", "cloze_hint_th": "เถอะ", "grammar_en": "Modal particle 吧 for suggestions", "grammar_th": "คำช่วยน้ำเสียง 吧 ชักชวน"},

    # Lesson 2
    {"chapter_num": 2, "context": "การเสนอแนะทางเลือกที่ดีกว่า", "hanzi": "现在坐公交太挤了，我们还是打车去北大吧。", "pinyin": "Xiànzài zuò gōngjiāo tài jǐ le, wǒmen háishi dǎchē qù Běidà ba.", "english": "Taking the bus now is too crowded; let's take a cab to PKU instead.", "thai": "ตอนนี้นั่งรถเมล์คนแน่นเกินไป พวกเรานั่งแท็กซี่ไป ม.ปักกิ่ง ดีกว่า", "cloze_target": "还是", "cloze_hint_en": "had better", "cloze_hint_th": "...ดีกว่า", "grammar_en": "Fixed pattern 还是...吧", "grammar_th": "โครงสร้าง 还是……吧"},
    {"chapter_num": 2, "context": "การกะอายุโดยประมาณ", "hanzi": "开出租车的司机师傅有三十多岁。", "pinyin": "Kāi chūzūchē de sījī shīfu yǒu sānshí duō suì.", "english": "The taxi driver is in his thirties.", "thai": "คนขับแท็กซี่มีอายุสามสิบกว่าปี", "cloze_target": "多", "cloze_hint_en": "more than / approximate", "cloze_hint_th": "กว่า", "grammar_en": "Approximation with 多", "grammar_th": "การใช้ 多 บอกจำนวนประมาณ"},

    # Lesson 3
    {"chapter_num": 3, "context": "การบอกแผนการท่องเที่ยว", "hanzi": "下个月我想去西安旅游，看看兵马俑。", "pinyin": "Xià ge yuè wǒ xiǎng qù Xī'ān lǚyóu, kànkan bīngmǎyǒng.", "english": "Next month I want to travel to Xi'an and see the Terracotta Army.", "thai": "เดือนหน้าฉันอยากไปเที่ยวซีอาน ไปดูสุสานทหารดินเผาสักหน่อย", "cloze_target": "旅游", "cloze_hint_en": "to travel", "cloze_hint_th": "ท่องเที่ยว", "grammar_en": "Verb reduplication 看看", "grammar_th": "การซ้ำกริยา 看看 (ลองดูสักหน่อย)"},
    {"chapter_num": 3, "context": "การบอกว่าฟังเข้าใจเนื้อหาแล้ว", "hanzi": "导游介绍的历史我都听懂了。", "pinyin": "Dǎoyóu jièshào de lìshǐ wǒ dōu tīng dǒng le.", "english": "I understood all the history introduced by the tour guide.", "thai": "ประวัติศาสตร์ที่มัคคุเทศก์แนะนำฉันฟังเข้าใจหมดแล้ว", "cloze_target": "懂", "cloze_hint_en": "understand (result)", "cloze_hint_th": "เข้าใจ (ผลลัพธ์)", "grammar_en": "Result complement 懂", "grammar_th": "คำเสริมบอกผล 懂"},

    # Lesson 4
    {"chapter_num": 4, "context": "การชมเชยการแต่งกาย", "hanzi": "你今天穿红色的毛衣真好看！", "pinyin": "Nǐ jīntiān chuān hóngsè de máoyī zhēn hǎokàn!", "english": "You look really pretty wearing a red sweater today!", "thai": "วันนี้เธอใส่เสื้อไหมพรมสีแดงดูดีจริงๆ!", "cloze_target": "红色的", "cloze_hint_en": "red one", "cloze_hint_th": "สีแดง", "grammar_en": "“的” phrase for omitted noun", "grammar_th": "วลี “的” ละคำนาม"},
    {"chapter_num": 4, "context": "การอธิบายเหตุผลของการกระทำ", "hanzi": "因为外面下大雨，所以我们没去公园。", "pinyin": "Yīnwèi wàimian xià dàyǔ, suǒyǐ wǒmen méi qù gōngyuán.", "english": "Because it rained heavily outside, so we did not go to the park.", "thai": "เพราะว่าข้างนอกฝนตกหนัก ดังนั้นพวกเราจึงไม่ได้ไปสวนสาธารณะ", "cloze_target": "所以", "cloze_hint_en": "so / therefore", "cloze_hint_th": "ดังนั้น", "grammar_en": "Causal conjunction 因为...所以...", "grammar_th": "คำเชื่อมบอกเหตุผล 因为……所以……"},

    # Lesson 5
    {"chapter_num": 5, "context": "การเชิญเพื่อนเข้าบ้าน", "hanzi": "快请进来吧，外面风太大了！", "pinyin": "Kuài qǐng jìnlái ba, wàimian fēng tài dà le!", "english": "Please come in quickly, the wind is too strong outside!", "thai": "รีบเชิญเข้ามาข้างในเถอะ ข้างนอกลมแรงเกินไปแล้ว!", "cloze_target": "进来", "cloze_hint_en": "come in", "cloze_hint_th": "เข้ามา", "grammar_en": "Directional complement 进来", "grammar_th": "คำเสริมบอกทิศทาง 进来"},
    {"chapter_num": 5, "context": "การเน้นย้ำว่าดึกมากแล้ว", "hanzi": "都晚上十一点了，你怎么还没睡觉？", "pinyin": "Dōu wǎnshang shíyī diǎn le, nǐ zěnme hái méi shuìjiào?", "english": "It's already 11:00 PM, why haven't you slept yet?", "thai": "ป่านนี้ห้าทุ่มแล้ว ทำไมเธอยังไม่นอนอีก?", "cloze_target": "都", "cloze_hint_en": "already (emphasis)", "cloze_hint_th": "ป่านนี้ก็...แล้ว", "grammar_en": "Pattern 都...了", "grammar_th": "โครงสร้าง 都……了"},

    # Lesson 6
    {"chapter_num": 6, "context": "การอวยพรวันเกิดพร้อมมอบของขวัญ", "hanzi": "小雪，祝你生日快乐，这是送给你的礼物！", "pinyin": "Xiǎoxuě, zhù nǐ shēngrì kuàilè, zhè shì sòng gěi nǐ de lǐwù!", "english": "Xiaoxue, happy birthday to you, this is a gift for you!", "thai": "เสี่ยวเสวี่ย สุขสันต์วันเกิดนะ นี่คือของขวัญที่ให้เธอ!", "cloze_target": "快乐", "cloze_hint_en": "happy", "cloze_hint_th": "มีความสุข", "grammar_en": "Greeting formula 生日快乐", "grammar_th": "คำอวยพร 生日快乐"},
    {"chapter_num": 6, "context": "การบรรยายกิริยาด้วยคำช่วย 地", "hanzi": "她高兴地接过了生日蛋糕。", "pinyin": "Tā gāoxìng de jiē guò le shēngrì dàngāo.", "english": "She happily took the birthday cake.", "thai": "เธอรับเค้กวันเกิดมาอย่างดีใจ", "cloze_target": "地", "cloze_hint_en": "adverbial marker", "cloze_hint_th": "อย่าง (คำช่วยเชื่อม)", "grammar_en": "Structural particle 地", "grammar_th": "คำช่วยเชื่อมกริยาวิเศษณ์ 地"},

    # Lesson 7
    {"chapter_num": 7, "context": "การชมเชยความสามารถด้านกีฬา", "hanzi": "他篮球打得很好，跑得也非常快。", "pinyin": "Tā lánqiú dǎ de hěn hǎo, pǎo de fēicháng kuài.", "english": "He plays basketball very well and runs extremely fast.", "thai": "เขาเล่นบาสเกตบอลได้เก่งมาก และวิ่งได้เร็วมากด้วย", "cloze_target": "得", "cloze_hint_en": "degree marker", "cloze_hint_th": "ได้ (บอกระดับ)", "grammar_en": "Complement of state V + 得 + Adj", "grammar_th": "คำเสริมบอกสภาพ V + 得 + Adj"},
    {"chapter_num": 7, "context": "การบอกสองเหตุการณ์ที่เกิดขึ้นติดกัน", "hanzi": "他一打完篮球就回家洗澡了。", "pinyin": "Tā yì dǎ wán lánqiú jiù huí jiā xǐzǎo le.", "english": "As soon as he finished playing basketball, he went home to shower.", "thai": "พอเขาเล่นบาสเกตบอลเสร็จก็กลับบ้านไปอาบน้ำทันที", "cloze_target": "一", "cloze_hint_en": "as soon as", "cloze_hint_th": "พอ...", "grammar_en": "Contracted complex 一...就...", "grammar_th": "โครงสร้างเชื่อมประโยค 一……就……"},

    # Lesson 8
    {"chapter_num": 8, "context": "การเปรียบเทียบระดับความจำ", "hanzi": "虽然你忘了这件事，但是我一直记得。", "pinyin": "Suīrán nǐ wàng le zhè jiàn shì, dànshì wǒ yìzhí jìde.", "english": "Although you forgot this matter, I have remembered it all along.", "thai": "ถึงแม้เธอจะลืมเรื่องนี้ไปแล้ว แต่ฉันยังคงจำได้มาตลอด", "cloze_target": "虽然", "cloze_hint_en": "although", "cloze_hint_th": "ถึงแม้ว่า", "grammar_en": "Transitional complex 虽然...但是...", "grammar_th": "ประโยคแสดงความขัดแย้ง 虽然……但是……"},
    {"chapter_num": 8, "context": "การเปรียบเทียบสิ่งของสองชิ้น", "hanzi": "这件黑色的衣服比那件红色的便宜得多。", "pinyin": "Zhè jiàn hēisè de yīfu bǐ nà jiàn hóngsè de piányi de duō.", "english": "This black outfit is much cheaper than that red one.", "thai": "เสื้อผ้าสีดำตัวนี้ราคาถูกกว่าตัวสีแดงตัวนั้นเยอะมาก", "cloze_target": "比", "cloze_hint_en": "compared to / than", "cloze_hint_th": "กว่า (เปรียบเทียบ)", "grammar_en": "Comparative A 比 B + Adj + 得多", "grammar_th": "ประโยคเปรียบเทียบ A 比 B + Adj + 得多"},

    # Lesson 9
    {"chapter_num": 9, "context": "การบอกระยะทางสถานที่", "hanzi": "那家奶茶店离我们学校不远，走五分钟就到了。", "pinyin": "Nà jiā nǎichádiàn lí wǒmen xuéxiào bù yuǎn, zǒu wǔ fēnzhōng jiù dào le.", "english": "That milk tea shop isn't far from our school; it's a 5-minute walk.", "thai": "ร้านชานมร้านนั้นอยู่ไม่ไกลจากโรงเรียนพวกเรา เดิน 5 นาทีก็ถึงแล้ว", "cloze_target": "离", "cloze_hint_en": "away from", "cloze_hint_th": "ห่างจาก", "grammar_en": "Distance preposition 离", "grammar_th": "คำบุพบทบอกระยะทาง 离"},
    {"chapter_num": 9, "context": "การบอกระยะเวลาการรอคอย", "hanzi": "我在这儿等了你半个小时了。", "pinyin": "Wǒ zài zhèr děng le nǐ bàn ge xiǎoshí le.", "english": "I have been waiting for you here for half an hour.", "thai": "ฉันรอเธออยู่ตรงนี้มาครึ่งชั่วโมงแล้วนะ", "cloze_target": "等", "cloze_hint_en": "to wait", "cloze_hint_th": "รอ", "grammar_en": "Complement of duration", "grammar_th": "คำเสริมบอกระยะเวลา (时量补语)"},

    # Lesson 10
    {"chapter_num": 10, "context": "การเตือนเรื่องการสอบที่ใกล้เข้ามา", "hanzi": "下周就要考试了，大家一定要认真复习。", "pinyin": "Xià zhōu jiù yào kǎoshì le, dàjiā yídìng yào rènzhēn fùxí.", "english": "The exam is coming next week, everyone must review diligently.", "thai": "สัปดาห์หน้าใกล้จะสอบแล้ว ทุกคนต้องตั้งใจทบทวนอย่างจริงจัง", "cloze_target": "就要", "cloze_hint_en": "about to / soon", "cloze_hint_th": "ใกล้จะ...แล้ว", "grammar_en": "Imminent action 就要...了", "grammar_th": "โครงสร้างเหตุการณ์ใกล้เกิดขึ้น 就要……了"},
    {"chapter_num": 10, "context": "การถามให้เลือกระหว่างสองทางเลือก", "hanzi": "你想喝热咖啡还是冰奶茶？", "pinyin": "Nǐ xiǎng hē rè kāfēi háishi bīng nǎichá?", "english": "Would you like hot coffee or iced milk tea?", "thai": "เธออยากดื่มกาแฟร้อนหรือชานมเย็น?", "cloze_target": "还是", "cloze_hint_en": "or (in questions)", "cloze_hint_th": "หรือ (คำถาม)", "grammar_en": "Alternative question with 还是", "grammar_th": "คำถามเลือกตอบด้วย 还是"},

    # Lesson 11
    {"chapter_num": 11, "context": "การบอกสภาพที่ดำเนินอยู่ด้วย 着", "hanzi": "门开着呢，他穿着一身黑色的衣服。", "pinyin": "Mén kāizhe ne, tā chuānzhe yì shēn hēisè de yīfu.", "english": "The door is open; he is wearing a black outfit.", "thai": "ประตูเปิดอยู่ เขาใส่เสื้อผ้าชุดสีดำอยู่ทั้งชุด", "cloze_target": "着", "cloze_hint_en": "continuous aspect", "cloze_hint_th": "อยู่ (สภาพต่อเนื่อง)", "grammar_en": "Aspect particle 着 for state", "grammar_th": "คำช่วยกริยา 着 แสดงสภาพต่อเนื่อง"},
    {"chapter_num": 11, "context": "การบอกอาหารที่ชื่นชอบมากที่สุด", "hanzi": "在中国菜里面，我最喜欢吃麻婆豆腐。", "pinyin": "Zài Zhōngguó cài lǐmiàn, wǒ zuì xǐhuan chī mápó dòufu.", "english": "Among Chinese dishes, I like eating Mapo Tofu the most.", "thai": "ในบรรดาอาหารจีน ฉันชอบกินเต้าหู้มาโปที่สุด", "cloze_target": "最", "cloze_hint_en": "most / best", "cloze_hint_th": "ที่สุด", "grammar_en": "Superlative adverb 最", "grammar_th": "คำวิเศษณ์บอกระดับสูงสุด 最"},

    # Lesson 12
    {"chapter_num": 12, "context": "การเปรียบเทียบสภาพอากาศระหว่างสองเมือง", "hanzi": "这里的冬天下大雪，比北京冷多了。", "pinyin": "Zhèlǐ de dōngtiān xià dàxuě, bǐ Běijīng lěng duō le.", "english": "It snows heavily here in winter, much colder than in Beijing.", "thai": "ฤดูหนาวที่นี่หิมะตกหนัก หนาวกว่าปักกิ่งเยอะมาก", "cloze_target": "比", "cloze_hint_en": "than", "cloze_hint_th": "กว่า", "grammar_en": "Comparative A 比 B + Adj + 多了", "grammar_th": "การเปรียบเทียบ A 比 B + Adj + 多了"},
    {"chapter_num": 12, "context": "การเปรียบเทียบความเหมือนกัน", "hanzi": "我的想法跟你的一样。", "pinyin": "Wǒ de xiǎngfǎ gēn nǐ de yíyàng.", "english": "My thoughts are the same as yours.", "thai": "ความคิดของฉันเหมือนกับของเธอเลย", "cloze_target": "一样", "cloze_hint_en": "the same", "cloze_hint_th": "เหมือนกัน", "grammar_en": "Comparison A 跟 B 一样", "grammar_th": "การเปรียบเทียบความเหมือน A 跟 B 一样"},

    # Lesson 13
    {"chapter_num": 13, "context": "การบอกความเปลี่ยนแปลงอย่างค่อยเป็นค่อยไป", "hanzi": "学了半年以后，我的中文水平越来越高了。", "pinyin": "Xué le bàn nián yǐhòu, wǒ de Zhōngwén shuǐpíng yuèláiyuè gāo le.", "english": "After studying for half a year, my Chinese level has gotten higher and higher.", "thai": "หลังจากเรียนมาครึ่งปี ระดับภาษาจีนของฉันก็พัฒนาสูงขึ้นเรื่อยๆ แล้ว", "cloze_target": "越来越", "cloze_hint_en": "more and more", "cloze_hint_th": "ขึ้นเรื่อยๆ", "grammar_en": "Pattern 越来越...", "grammar_th": "โครงสร้างแสดงการพัฒนา 越来越……"},
    {"chapter_num": 13, "context": "ประโยคที่มีกรรมตรงและกรรมรอง", "hanzi": "王老师教我们汉语发音和中国书法。", "pinyin": "Wáng lǎoshī jiāo wǒmen Hànyǔ fāyīn hé Zhōngguó shūfǎ.", "english": "Teacher Wang teaches us Chinese pronunciation and calligraphy.", "thai": "อาจารย์หวังสอนการออกเสียงภาษาจีนและการเขียนพู่กันจีนให้พวกเรา", "cloze_target": "教", "cloze_hint_en": "to teach", "cloze_hint_th": "สอน", "grammar_en": "Double-object sentence with 教", "grammar_th": "ประโยคกรรมตรงกรรมรองด้วย 教"},

    # Lesson 14
    {"chapter_num": 14, "context": "การอุทานแสดงความรู้สึกในเทศกาล", "hanzi": "除夕夜大家在一起包饺子多有意思啊！", "pinyin": "Chúxī yè dàjiā zài yìqǐ bāo jiǎozi duō yǒu yìsi a!", "english": "How fun it is for everyone to make dumplings together on New Year's Eve!", "thai": "คืนส่งท้ายปีเก่าทุกคนได้มาห่อเกี๊ยวด้วยกันช่างสนุกอะไรอย่างนี้!", "cloze_target": "多", "cloze_hint_en": "how / so (exclamation)", "cloze_hint_th": "ช่าง...เหลือเกิน", "grammar_en": "Exclamatory pattern 多 + Adj + 啊", "grammar_th": "โครงสร้างประโยคอุทาน 多 + Adj + 啊"},
    {"chapter_num": 14, "context": "คำเสริมทิศทางบอกการเคลื่อนที่", "hanzi": "楼下有朋友找你，你快走下去吧。", "pinyin": "Lóuxià yǒu péngyou zhǎo nǐ, nǐ kuài zǒu xiàqù ba.", "english": "A friend is looking for you downstairs, hurry and walk down.", "thai": "ชั้นล่างมีเพื่อนมาหาเธอ เธอรีบเดินลงไปเถอะ", "cloze_target": "下去", "cloze_hint_en": "down (away from speaker)", "cloze_hint_th": "ลงไป", "grammar_en": "Compound directional complement 下去", "grammar_th": "คำเสริมทิศทางประสม 下去 (ลงไป)"},

    # Lesson 15
    {"chapter_num": 15, "context": "การระบุจำนวนครั้งที่เคยทำกิจกรรม", "hanzi": "中国太美丽了，我想再去一次北京。", "pinyin": "Zhōngguó tài měilì le, wǒ xiǎng zài qù yí cì Běijīng.", "english": "China is so beautiful; I want to go to Beijing once again.", "thai": "ประเทศจีนสวยงามเหลือเกิน ฉันอยากไปปักกิ่งอีกสักครั้งหนึ่ง", "cloze_target": "次", "cloze_hint_en": "time / frequency", "cloze_hint_th": "ครั้ง", "grammar_en": "Complement of frequency 次", "grammar_th": "คำเสริมบอกจำนวนครั้ง 次"},
    {"chapter_num": 15, "context": "การใช้ 有 ระบุระยะเวลาที่ยาวนาน", "hanzi": "我们有两年没见面了吧？真是太想念你了！", "pinyin": "Wǒmen yǒu liǎng nián méi jiànmiàn le ba? Zhēn shì tài xiǎngniàn nǐ le!", "english": "We haven't seen each other for two years, right? I really missed you!", "thai": "พวกเราไม่ได้เจอกันตั้งสองปีแล้วใช่ไหม? คิดถึงเธอมากจริงๆ!", "cloze_target": "有", "cloze_hint_en": "reaching a duration", "cloze_hint_th": "มีถึง/นานถึง", "grammar_en": "“有” sentence for duration", "grammar_th": "ประโยค “有” บอกระยะเวลาถึงเกณฑ์"}
]

hsk2_grammar = [
    # Lesson 1
    {
        "chapter_num": 1, "point_num": 1,
        "title_cn": "语气助词“吧”（2）表示商量与提议",
        "title_th": "คำช่วยน้ำเสียง “吧” (การปรึกษาหารือและเสนอแนะ)",
        "structure": "动词短语 + 吧！ / 吧？",
        "explanation_th": "ใช้ท้ายประโยคเพื่อแสดงการเสนอแนะอย่างสุภาพ ปรึกษาหารือ หรือขอความเห็นพ้องจากคู่สนทนา ทำให้น้ำเสียงดูนุ่มนวลและเป็นกันเอง เช่น '我们吃烤鸭吧！' (พวกเรากินเป็ดย่างกันเถอะ)",
        "examples": [
            {"cn": "今天我请客，你们想吃什么就点什么吧！", "py": "Jīntiān wǒ qǐngkè, nǐmen xiǎng chī shénme jiù diǎn shénme ba!", "th": "วันนี้ฉันเลี้ยงเอง พวกเธออยากกินอะไรก็สั่งตามสบายเลยนะ!"},
            {"cn": "时间不早了，我们走吧。", "py": "Shíjiān bù zǎo le, wǒmen zǒu ba.", "th": "เวลาไม่เช้าแล้ว พวกเราไปกันเถอะ"}
        ]
    },
    {
        "chapter_num": 1, "point_num": 2,
        "title_cn": "兼语句：用“请、让、叫”表示使令",
        "title_th": "ประโยคกริยาซ้อน (兼语句): ใช้ 请, 让, 叫",
        "structure": "主语 + 请 / 让 / 叫 + 兼语 (กรรมตัวแรก/ประธานตัวสอง) + 动词短语",
        "explanation_th": "คำนามที่อยู่ตรงกลางทำหน้าที่เป็นทั้งกรรมของกริยาตัวแรก (请/让/叫) และเป็นประธานของกริยาตัวหลัง: '请' ใช้เมื่อเลี้ยงหรือเชิญ, '让' แปลว่าอนุญาตหรือให้ทำ, '叫' มักใช้ในการสั่งหรือบอกให้ทำ",
        "examples": [
            {"cn": "王老师请我们吃北京烤鸭。", "py": "Wáng lǎoshī qǐng wǒmen chī Běijīng kǎoyā.", "th": "อาจารย์หวังเลี้ยงเป็ดปักกิ่งพวกเรา (我们 เป็นกรรมของ 请 และเป็นผู้กิน 烤鸭)"},
            {"cn": "妈妈让我每天多喝水。", "py": "Māma ràng wǒ měitiān duō hē shuǐ.", "th": "แม่บอกให้ฉันดื่มน้ำเยอะๆ ทุกวัน"}
        ]
    },
    {
        "chapter_num": 1, "point_num": 3,
        "title_cn": "强调句“是……的”（强调施事或对象）",
        "title_th": "โครงสร้างเน้นย้ำ “是……的” (เน้นผู้กระทำหรือบุคคลเป้าหมาย)",
        "structure": "主语 + 是 + [ผู้กระทำ/เป้าหมาย] + 动词 + 的",
        "explanation_th": "นอกจากจะเน้นเวลา สถานที่ และวิธีการแล้ว โครงสร้าง '是……的' ยังสามารถใช้เน้นว่า 'ใครเป็นผู้เชิญ' หรือ 'ทำเพื่อใคร' ได้อีกด้วย",
        "examples": [
            {"cn": "这顿饭是王老师请的。", "py": "Zhè dùn fàn shì Wáng lǎoshī qǐng de.", "th": "อาหารมื้อนี้อาจารย์หวังเป็นคนเลี้ยง (เน้นว่าใครเลี้ยง)"},
            {"cn": "这本书是我送给他的。", "py": "Zhè běn shū shì wǒ sòng gěi tā de.", "th": "หนังสือเล่มนี้ฉันเป็นคนให้เขาเอง"}
        ]
    },

    # Lesson 2
    {
        "chapter_num": 2, "point_num": 1,
        "title_cn": "固定格式“还是……吧”表达选择意向",
        "title_th": "โครงสร้าง “还是……吧” (เลือกทางนี้ดีกว่า / แนะนำทางเลือกที่ดีที่สุด)",
        "structure": "主语 + 还是 + 动词短语 + 吧",
        "explanation_th": "ใช้เมื่อเปรียบเทียบทางเลือกตั้งแต่สองทางขึ้นไป แล้วตัดสินใจว่าทางเลือกนี้น่าจะเหมาะสมหรือดีที่สุดในสถานการณ์นั้น เช่น '还是打车去吧' (นั่งแท็กซี่ไปดีกว่า)",
        "examples": [
            {"cn": "外面雨太大了，我们还是坐地铁去吧。", "py": "Wàimian yǔ tài dà le, wǒmen háishi zuò dìtiě qù ba.", "th": "ข้างนอกฝนตกหนักเกินไป พวกเรานั่งรถไฟใต้ดินไปดีกว่า"},
            {"cn": "咖啡太苦了，我还是喝茶吧。", "py": "Kāfēi tài kǔ le, wǒ háishi hē chá ba.", "th": "กาแฟขมเกินไป ฉันดื่มชาดีกว่า"}
        ]
    },
    {
        "chapter_num": 2, "point_num": 2,
        "title_cn": "用“多”表达概数",
        "title_th": "การใช้ “多” บอกจำนวนตัวเลขโดยประมาณ (กว่า / เศษ)",
        "structure": "หลักสิบขึ้นไป: เลขกลม + 多 + ลักษณนาม / ต่ำกว่าสิบ: ตัวเลข + ลักษณนาม + 多",
        "explanation_th": "ถ้าตัวเลขลงท้ายด้วย 0 (เช่น 10, 20, 30) ให้วาง '多' หน้าลักษณนาม เช่น 三十多个人 (สามสิบกว่าคน); แต่ถ้าเป็นตัวเลขเดี่ยว (1-9) ให้วาง '多' หลังลักษณนาม เช่น 三个多月 (สามเดือนกว่าๆ)",
        "examples": [
            {"cn": "那位出租车司机有四十多岁。", "py": "Nà wèi chūzūchē sījī yǒu sìshí duō suì.", "th": "คนขับแท็กซี่ท่านนั้นอายุสี่สิบกว่าปี (四十多岁)"},
            {"cn": "我在中国住了一个多月。", "py": "Wǒ zài Zhōngguó zhù le yí ge duō yuè.", "th": "ฉันอาศัยอยู่ที่ประเทศจีนมาหนึ่งเดือนกว่าแล้ว (一个多月)"}
        ]
    },
    {
        "chapter_num": 2, "point_num": 3,
        "title_cn": "动词短语与主谓短语作定语",
        "title_th": "วลีกริยาและวลีประธานทำหน้าที่เป็นบทขยายคำนาม (ด้วย 的)",
        "structure": "[วลีกริยา / วลีประธาน] + 的 + คำนามหลัก",
        "explanation_th": "ในภาษาจีน คำขยายต้องอยู่ข้างหน้าคำนามเสมอ หากนำกริยาหรือประโยคย่อยมาขยายคำนาม จะต้องเชื่อมด้วย '的' เช่น '开车的司机' (คนขับที่เป็นคนขับรถ), '我买的书' (หนังสือที่ฉันซื้อ)",
        "examples": [
            {"cn": "开出租车的那个人是我哥哥的朋友。", "py": "Kāi chūzūchē de nà ge rén shì wǒ gēge de péngyou.", "th": "คนที่ขับแท็กซี่คนนั้นเป็นเพื่อนของพี่ชายฉัน"},
            {"cn": "昨天你介绍的那个饭馆挺不错的。", "py": "Zuótiān nǐ jièshào de nà ge fànguǎn tǐng búcuò de.", "th": "ร้านอาหารที่เธอแนะนำเมื่อวานนี้ดีมากทีเดียว"}
        ]
    },

    # Lesson 3
    {
        "chapter_num": 3, "point_num": 1,
        "title_cn": "结果补语：懂、完、到、好",
        "title_th": "คำเสริมบอกผล (结果补语): 懂, 完, 到, 好",
        "structure": "动词 + 结果补语 (听懂 / 做完 / 找到 / 准备好)",
        "explanation_th": "วางติดหลังคำกริยาเพื่อระบุผลลัพธ์ที่เกิดขึ้นทันทีจากการกระทำนั้น: '懂' (เข้าใจ), '完' (เสร็จสิ้น/หมด), '到' (ถึง/สำเร็จ), '好' (เรียบร้อย/สมบูรณ์)",
        "examples": [
            {"cn": "导游说的中文我都听懂了。", "py": "Dǎoyóu shuō de Zhōngwén wǒ dōu tīng dǒng le.", "th": "ภาษาจีนที่ไกด์พูดฉันฟังเข้าใจทั้งหมดแล้ว"},
            {"cn": "今天的作业你写完了吗？", "py": "Jīntiān de zuòyè nǐ xiě wán le ma?", "th": "การบ้านของวันนี้เธอเขียนเสร็จหรือยัง?"},
            {"cn": "去西安的火车票我买到了！", "py": "Qù Xī'ān de huǒchēpiào wǒ mǎi dào le!", "th": "ตั๋วรถไฟไปซีอานฉันซื้อได้แล้ว!"}
        ]
    },
    {
        "chapter_num": 3, "point_num": 2,
        "title_cn": "动词重叠（AA / A一A / ABAB）表示尝试或轻松",
        "title_th": "การซ้ำคำกริยา (ลองทำดู / กริยาใช้เวลาสั้นๆ)",
        "structure": "พยางค์เดียว: 看看 / 看一看 / 听听 / ตรวจสอบ: 学习学习 / 介绍介绍",
        "explanation_th": "การซ้ำคำกริยาช่วยลดทอนความเข้มงวด ทำให้น้ำเสียงผ่อนคลายและสุภาพขึ้น สื่อความหมายว่า 'ลองทำดูสักหน่อย' หรือการกระทำนั้นใช้เวลาเพียงครู่เดียว",
        "examples": [
            {"cn": "你看看这件红色的衣服怎么样？", "py": "Nǐ kànkan zhè jiàn hóngsè de yīfu zěnmeyàng?", "th": "เธอลองดูเสื้อสีแดงตัวนี้หน่อยเป็นอย่างไรบ้าง?"},
            {"cn": "周末我想去公园散散步，放松放松。", "py": "Zhōumò wǒ xiǎng qù gōngyuán sànsanbù, fàngsōng fàngsōng.", "th": "สุดสัปดาห์ฉันอยากไปเดินเล่นที่สวนสาธารณะ ผ่อนคลายสักหน่อย"}
        ]
    },

    # Lesson 4
    {
        "chapter_num": 4, "point_num": 1,
        "title_cn": "动态助词“过”表示过去经历",
        "title_th": "คำช่วยแสดงประสบการณ์ “过” (เคย...มาแล้วในอดีต)",
        "structure": "主语 + 动词 + 过 + 宾语 / 否定: 没(有) + 动词 + 过",
        "explanation_th": "วางหลังคำกริยาเพื่อแสดงว่าเคยมีประสบการณ์ทำสิ่งนั้นมาก่อนในอดีต และเหตุการณ์นั้นไม่ได้ดำเนินต่อเนื่องมาถึงปัจจุบัน รูปปฏิเสธใช้ '没(有) + กริยา + 过'",
        "examples": [
            {"cn": "你去过中国西安吗？我去过一次。", "py": "Nǐ qù guò Zhōngguó Xī'ān ma? Wǒ qù guò yí cì.", "th": "เธอเคยไปเมืองซีอานประเทศจีนไหม? ฉันเคยไปหนึ่งครั้ง"},
            {"cn": "我以前没吃过北京烤鸭。", "py": "Wǒ yǐqián méi chī guò Běijīng kǎoyā.", "th": "เมื่อก่อนฉันไม่เคยทานเป็ดปักกิ่งมาก่อนเลย"}
        ]
    },
    {
        "chapter_num": 4, "point_num": 2,
        "title_cn": "因果复句“因为……，所以……”",
        "title_th": "ประโยคบอกเหตุผล “因为……，所以……” (เพราะว่า... จึง...)",
        "structure": "因为 + [สาเหตุ] ， 所以 + [ผลลัพธ์]",
        "explanation_th": "ใช้เชื่อมประโยคเพื่ออธิบายเหตุและผลอย่างชัดเจน สามารถใช้คู่กันทั้งสองคำ หรือละคำใดคำหนึ่งได้ในภาษาพูดที่ไม่เป็นทางการ",
        "examples": [
            {"cn": "因为今天下大雪，所以我们都在家复习。", "py": "Yīnwèi jīntiān xià dàxuě, suǒyǐ wǒmen dōu zài jiā fùxí.", "th": "เพราะว่าวันนี้หิมะตกหนัก ดังนั้นพวกเราจึงทบทวนหนังสืออยู่ที่บ้าน"},
            {"cn": "因为喜欢中国文化，他来到了北京大学。", "py": "Yīnwèi xǐhuan Zhōngguó wénhuà, tā lái dào le Běijīng Dàxué.", "th": "เพราะชอบวัฒนธรรมจีน เขาจึงได้มาเรียนที่มหาวิทยาลัยปักกิ่ง"}
        ]
    },

    # Lesson 5
    {
        "chapter_num": 5, "point_num": 1,
        "title_cn": "简单趋向补语：动词 + 来 / 去",
        "title_th": "คำเสริมบอกทิศทางอย่างง่าย (V + 来 / 去)",
        "structure": "动词 + 来 (เข้าหาผู้พูด) / 动词 + 去 (ออกจากผู้พูด)",
        "explanation_th": "'来' แสดงว่าทิศทางการกระทำกำลังมุ่งตรงเข้ามาหาตำแหน่งของผู้พูด ส่วน '去' แสดงว่าทิศทางการกระทำกำลังเคลื่อนที่ออกห่างจากตำแหน่งของผู้พูด เช่น 进来 (เข้ามา) vs 进去 (เข้าไป)",
        "examples": [
            {"cn": "他在屋里，对我说：“快进来吧！”", "py": "Tā zài wū lǐ, duì wǒ shuō: “Kuài jìnlái ba!”", "th": "เขาอยู่ในห้องแล้วพูดกับฉันว่า: 'รีบเข้ามาเถอะ!' (ผู้พูดอยู่ในห้องจึงใช้ 来)"},
            {"cn": "外面太冷了，我们快进去吧。", "py": "Wàimian tài lěng le, wǒmen kuài jìnqù ba.", "th": "ข้างนอกหนาวเกินไป พวกเรารีบเข้าไปเถอะ (ผู้พูดอยู่ข้างนอกจึงใช้ 去)"}
        ]
    },
    {
        "chapter_num": 5, "point_num": 2,
        "title_cn": "固定格式“都……了”强调时间已晚或程度深",
        "title_th": "โครงสร้าง “都……了” (ป่านนี้ก็...แล้ว / เน้นเวลาหรือระดับ)",
        "structure": "都 + 时间词 / 数量词 / 程度词 + 了",
        "explanation_th": "ใช้เน้นย้ำเชิงตำหนิหรือเตือนสติว่าเวลาล่วงเลยไปมาก หรือระดับของสิ่งนั้นสูงมากแล้ว มักแปลว่า 'ป่านนี้ก็...แล้ว' หรือ 'ตั้ง...แล้ว'",
        "examples": [
            {"cn": "都十二点了，你快去睡觉吧！", "py": "Dōu shí'èr diǎn le, nǐ kuài qù shuìjiào ba!", "th": "ป่านนี้เที่ยงคืนแล้ว เธอรีบไปนอนเถอะ!"},
            {"cn": "我们都等了他一个小时了，他怎么还不来？", "py": "Wǒmen dōu děng le tā yí ge xiǎoshí le, tā zěnme hái bù lái?", "th": "พวกเรารอเขาตั้งหนึ่งชั่วโมงแล้ว ทำไมเขายังไม่มาอีก?"}
        ]
    },

    # Lesson 7
    {
        "chapter_num": 7, "point_num": 1,
        "title_cn": "状态补语：动词 + 得 + 形容词短语",
        "title_th": "คำเสริมบอกสภาพและระดับ: V + 得 + Adj",
        "structure": "动词 + 得 + 形容词 / 如果有宾语: 动词 + 宾语 + 动词 + 得 + 形容词",
        "explanation_th": "ใช้ประเมินหรือบรรยายว่าการกระทำนั้นทำออกมาได้ผลลัพธ์หรือระดับอย่างไร เช่น '跑得很快' (วิ่งได้เร็วมาก) หากมีกรรม ต้องซ้ำกริยาก่อนหนึ่งรอบ เช่น '他说汉语说得很好'",
        "examples": [
            {"cn": "他篮球打得很好，跳得也很高。", "py": "Tā lánqiú dǎ de hěn hǎo, tiào de yě hěn gāo.", "th": "เขาเล่นบาสเกตบอลได้เก่งมาก และกระโดดได้สูงมากด้วย"},
            {"cn": "她汉字写得非常漂亮。", "py": "Tā hànzì xiě de fēicháng piàoliang.", "th": "เธอเขียนตัวอักษรจีนได้สวยงามมาก"}
        ]
    },
    {
        "chapter_num": 7, "point_num": 2,
        "title_cn": "紧缩复句“一……就……”表示紧接着发生",
        "title_th": "โครงสร้างเชื่อมประโยค “一……就……” (พอ...ก็...ทันที)",
        "structure": "主语 + 一 + 动词1 + 就 + 动词2",
        "explanation_th": "แสดงเหตุการณ์สองอย่างที่เกิดขึ้นต่อเนื่องกันติดๆ โดยทันที เมื่อการกระทำที่ 1 เกิดขึ้น การกระทำที่ 2 ก็จะตามมาโดยไม่รอช้า",
        "examples": [
            {"cn": "他一打完球就回家洗澡了。", "py": "Tā yì dǎ wán qiú jiù huí jiā xǐzǎo le.", "th": "พอเขาเล่นบอลเสร็จก็กลับบ้านไปอาบน้ำทันที"},
            {"cn": "我一到北京就给你打电话。", "py": "Wǒ yí dào Běijīng jiù gěi nǐ dǎ diànhuà.", "th": "พอฉันถึงปักกิ่งปุ๊บจะโทรหาเธอปั๊บ"}
        ]
    },

    # Lesson 8
    {
        "chapter_num": 8, "point_num": 1,
        "title_cn": "比较句（1）：A 比 B + 形容词",
        "title_th": "ประโยคเปรียบเทียบขั้นกว่า: A 比 B + คุณศัพท์",
        "structure": "A + 比 + B + 形容词 / 具体差距: A + 比 + B + 形容词 + 一点儿 / 得多 / 数量",
        "explanation_th": "โครงสร้างเปรียบเทียบมาตรฐานในภาษาจีน แปลว่า 'A ...กว่า B' หากต้องการบอกความต่างเล็กน้อยให้เติม '一点儿', ถ้าต่างกันมากให้เติม '得多' หรือ '多了' ไว้ท้ายประโยค",
        "examples": [
            {"cn": "今天比昨天冷多了。", "py": "Jīntiān bǐ zuótiān lěng duō le.", "th": "วันนี้หนาวกว่าเมื่อวานเยอะมาก"},
            {"cn": "这本书比那本书贵二十块钱。", "py": "Zhè běn shū bǐ nà běn shū guì èrshí kuài qián.", "th": "หนังสือเล่มนี้แพงกว่าเล่มนั้น 20 หยวน"}
        ]
    },
    {
        "chapter_num": 8, "point_num": 2,
        "title_cn": "转折复句“虽然……，但是……”",
        "title_th": "ประโยคแสดงความขัดแย้ง: 虽然……，但是…… (แม้ว่า...แต่ว่า...)",
        "structure": "虽然 + [ข้อเท็จจริง/อุปสรรค] ， 但是 + [ผลลัพธ์ที่ขัดแย้ง]",
        "explanation_th": "ใช้บอกความสัมพันธ์ที่ประโยคหลังขัดแย้งกับสิ่งที่คาดหวังจากประโยคแรก เช่น แม้จะยากแต่ก็น่าสนใจ หรือแม้จะเหนื่อยแต่ก็มีความสุข",
        "examples": [
            {"cn": "虽然学汉字有点儿难，但是非常有意思。", "py": "Suīrán xué hànzì yǒudiǎnr nán, dànshì fēicháng yǒu yìsi.", "th": "แม้ว่าการเรียนอักษรจีนจะค่อนข้างยาก แต่ก็น่าสนใจมากจริงๆ"},
            {"cn": "虽然今天天气很冷，但是大家都很热情。", "py": "Suīrán jīntiān tiānqì hěn lěng, dànshì dàjiā dōu hěn rèqíng.", "th": "แม้ว่าวันนี้อากาศจะหนาวมาก แต่ทุกคนต่างก็อบอุ่นและกระตือรือร้น"}
        ]
    },

    # Lesson 9
    {
        "chapter_num": 9, "point_num": 1,
        "title_cn": "介词“离”表示空间与时间距离",
        "title_th": "คำบุพบท “离” ระบุระยะทางและเวลา (ห่างจาก...)",
        "structure": "地点A + 离 + 地点B + 很近 / 很远 / 有 + 距离",
        "explanation_th": "ใช้ระบุว่าสถานที่ A อยู่ห่างจากสถานที่ B เป็นระยะทางเท่าใด หรือเวลาในปัจจุบันห่างจากเหตุการณ์สำคัญเท่าใด",
        "examples": [
            {"cn": "我家离学校很近，走路只要十分钟。", "py": "Wǒ jiā lí xuéxiào hěn jìn, zǒulù zhǐ yào shí fēnzhōng.", "th": "บ้านของฉันอยู่ใกล้โรงเรียนมาก เดินแค่ 10 นาทีก็ถึง"},
            {"cn": "离考试还有两个星期，大家要加油！", "py": "Lí kǎoshì hái yǒu liǎng ge xīngqī, dàjiā yào jiāyóu!", "th": "ห่างจากการสอบยังเหลือเวลาอีก 2 สัปดาห์ ทุกคนต้องสู้ๆ นะ!"}
        ]
    },

    # Lesson 10
    {
        "chapter_num": 10, "point_num": 1,
        "title_cn": "快行体“快要 / 就要……了”表示动作即将发生",
        "title_th": "โครงสร้างเหตุการณ์ใกล้เกิดขึ้น: 快要 / 就要……了 (ใกล้จะ...แล้ว)",
        "structure": "主语 + 快要 / 就要 + 动词短语 + 了",
        "explanation_th": "ใช้แสดงว่าการกระทำหรือเหตุการณ์นั้นกำลังจะเกิดขึ้นในเวลาอันใกล้มาก หากมีคำบอกเวลาที่แน่นอนระบุไว้ในประโยค (เช่น 明天, 下周) จะต้องใช้ '就要……了' เท่านั้น ห้ามใช้ '快要'",
        "examples": [
            {"cn": "下课铃响了，就要放学了。", "py": "Xiàkè líng xiǎng le, jiù yào fàngxué le.", "th": "กริ่งหมดเวลาดังแล้ว ใกล้จะเลิกเรียนแล้ว"},
            {"cn": "天黑了，快要下雨了，我们快回家吧。", "py": "Tiān hēi le, kuàiyào xià yǔ le, wǒmen kuài huí jiā ba.", "th": "ฟ้ามืดแล้ว ใกล้จะฝนตกแล้ว พวกเรารีบกลับบ้านเถอะ"}
        ]
    },

    # Lesson 11
    {
        "chapter_num": 11, "point_num": 1,
        "title_cn": "动态助词“着”表示动作或状态的持续",
        "title_th": "คำช่วยกริยา “着” แสดงสภาพที่ต่อเนื่องคงอยู่",
        "structure": "动词 + 着 / 两个动作伴随: V1 + 着 + V2",
        "explanation_th": "ต่างจาก '在' ที่เน้นการกระทำกำลังขยับทำอยู่ แต่ '着' เน้น 'สภาพนิ่งที่คงอยู่ต่อเนื่อง' เช่น ประตูเปิดค้างอยู่ (门开着) หรือสวมเสื้อผ้าชุดนั้นอยู่ (穿着红衣服) และใช้บอกกิริยาที่ทำร่วมกัน เช่น ยืนพูด (站着说)",
        "examples": [
            {"cn": "门开着呢，请直接进来吧。", "py": "Mén kāizhe ne, qǐng zhíjiē jìnlái ba.", "th": "ประตูเปิดค้างไว้อยู่ เชิญเข้ามาข้างในได้เลย"},
            {"cn": "老师笑着对我们说：“大家考得很好！”", "py": "Lǎoshī xiàozhe duì wǒmen shuō: “Dàjiā kǎo de hěn hǎo!”", "th": "คุณครูพูดกับพวกเราอย่างยิ้มแย้มว่า: 'ทุกคนสอบได้คะแนนดีมาก!'"}
        ]
    },

    # Lesson 13
    {
        "chapter_num": 13, "point_num": 1,
        "title_cn": "固定格式“越来越……”表示程度随时间加深",
        "title_th": "โครงสร้าง “越来越……” (ยิ่ง...ขึ้นเรื่อยๆ ตามกาลเวลา)",
        "structure": "主语 + 越来越 + 形容词 / 心理动词",
        "explanation_th": "แสดงการเปลี่ยนแปลงของระดับที่ค่อยเป็นค่อยไปตามลำดับเวลา เช่น อากาศหนาวขึ้นเรื่อยๆ หรือเก่งขึ้นเรื่อยๆ ข้อควรระวัง: ห้ามใส่ '很' หรือ '非常' ซ้อนเข้าไปหลัง 越来越 เด็ดขาด",
        "examples": [
            {"cn": "多说多练，我的中文越来越好了。", "py": "Duō shuō duō liàn, wǒ de Zhōngwén yuèláiyuè hǎo le.", "th": "พูดเยอะๆ ฝึกบ่อยๆ ภาษาจีนของฉันก็เก่งขึ้นเรื่อยๆ แล้ว"},
            {"cn": "天气越来越冷，出门要多穿点儿衣服。", "py": "Tiānqì yuèláiyuè lěng, chūmén yào duō chuān diǎnr yīfu.", "th": "สภาพอากาศหนาวขึ้นเรื่อยๆ ออกจากบ้านต้องใส่เสื้อผ้าหนาๆ หน่อย"}
        ]
    },

    # Lesson 14
    {
        "chapter_num": 14, "point_num": 1,
        "title_cn": "程度副词“多”在感叹句中的用法",
        "title_th": "คำวิเศษณ์บอกระดับ “多” ในประโยคอุทาน (多 + Adj + 啊！)",
        "structure": "主语 + 多 + 形容词 + 啊！",
        "explanation_th": "ใช้ในประโยคแสดงอารมณ์ความรู้สึกตื่นเต้น ประทับใจ หรือเห็นใจ เพื่อเน้นย้ำว่าสิ่งนั้นมีระดับสูงมาก แปลว่า 'ช่าง...อะไรอย่างนี้!' หรือ 'ช่าง...เหลือเกิน!'",
        "examples": [
            {"cn": "一家人在一起过年多幸福啊！", "py": "Yì jiā rén zài yìqǐ guònián duō xìngfú a!", "th": "คนทั้งครอบครัวได้อยู่ด้วยกันฉลองปีใหม่ช่างมีความสุขเหลือเกิน!"},
            {"cn": "你看，外面的雪景多漂亮啊！", "py": "Nǐ kàn, wàimian de xuějǐng duō piàoliang a!", "th": "เธอดูสิ วิวหิมะข้างนอกช่างสวยงามอะไรอย่างนี้!"}
        ]
    },

    # Lesson 15
    {
        "chapter_num": 15, "point_num": 1,
        "title_cn": "动量补语“次、遍”表示动作发生的频次",
        "title_th": "คำเสริมบอกจำนวนครั้ง (动量补语): 次, 遍",
        "structure": "动词 + 过 / 了 + 数量词 (一次 / 两遍) + 宾语",
        "explanation_th": "'次' หมายถึงจำนวนครั้งทั่วไป ส่วน '遍' เน้นย้ำการทำตั้งแต่จุดเริ่มต้นจนจบกระบวนการครบ 1 รอบ เช่น อ่านหนังสือ 1 รอบ (看了一遍) หากกรรมเป็นคำสรรพนาม (เช่น 他, 我) คำบอกจำนวนครั้งต้องวางไว้ข้างหลังกรรม",
        "examples": [
            {"cn": "中国太美了，我想再去一次北京。", "py": "Zhōngguó tài měi le, wǒ xiǎng zài qù yí cì Běijīng.", "th": "ประเทศจีนสวยงามมาก ฉันอยากไปปักกิ่งอีกสักครั้งหนึ่ง"},
            {"cn": "这篇文章很有意思，我读了两遍。", "py": "Zhè piān wénzhāng hěn yǒu yìsi, wǒ dú le liǎng biàn.", "th": "บทความนี้น่าสนใจมาก ฉันอ่านไปสองรอบครบถ้วน"}
        ]
    }
]

print(f"HSK 2: {len(hsk2_words)} words, {len(hsk2_sentences)} sentences, {len(hsk2_grammar)} grammar points.")
