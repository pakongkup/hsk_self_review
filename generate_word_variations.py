# generate_word_variations.py
"""
Generates 5 distinct, natural example sentence variations for each HSK word.
Each variation contains:
- cn: Chinese characters
- py: Pinyin with tone marks
- th: Natural Thai translation
- en: English translation
"""

import sqlite3
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'hsk3.db')

# Custom curated high-frequency sentence patterns for common words across HSK 1, 2, 3
SPECIFIC_VARIATIONS = {
    # HSK 1 Essentials
    "你": [
        {"cn": "你今天打算去哪儿？", "py": "Nǐ jīntiān dǎsuàn qù nǎr?", "th": "วันนี้เธอวางแผนจะไปไหน?", "en": "Where do you plan to go today?"},
        {"cn": "你的中文说得非常好！", "py": "Nǐ de Zhōngwén shuō de fēicháng hǎo!", "th": "ภาษาจีนของเธอพูดได้ดีมาก!", "en": "You speak Chinese very well!"},
        {"cn": "你想和我一起去看电影吗？", "py": "Nǐ xiǎng hé wǒ yìqǐ qù kàn diànyǐng ma?", "th": "เธออยากไปดูหนังกับฉันไหม?", "en": "Do you want to go watch a movie with me?"},
        {"cn": "你慢点儿吃，别着急。", "py": "Nǐ màn diǎnr chī, bié zháojí.", "th": "เธอกินช้าๆ หน่อย ไม่ต้องรีบร้อน", "en": "Eat slowly, don't rush."},
        {"cn": "认识你我感到非常高兴！", "py": "Rènshi nǐ wǒ gǎndào fēicháng gāoxìng!", "th": "ยินดีที่ได้รู้จักเธอนะ รู้สึกดีใจมาก!", "en": "Very glad to meet you!"}
    ],
    "我": [
        {"cn": "我每天早上七点起床。", "py": "Wǒ měitiān zǎoshang qī diǎn qǐchuáng.", "th": "ฉันตื่นนอนตอนเจ็ดโมงเช้าทุกวัน", "en": "I wake up at 7:00 every morning."},
        {"cn": "我现在在图书馆复习功课。", "py": "Wǒ xiànzài zài túshūguǎn fùxí gōngkè.", "th": "ตอนนี้ฉันทบทวนบทเรียนอยู่ที่ห้องสมุด", "en": "I am reviewing homework in the library now."},
        {"cn": "我非常喜欢吃中国菜。", "py": "Wǒ fēicháng xǐhuan chī Zhōngguó cài.", "th": "ฉันชอบกินอาหารจีนมากๆ", "en": "I like Chinese food very much."},
        {"cn": "我不明白这句话的意思。", "py": "Wǒ bù míngbai zhè jù huà de yìsi.", "th": "ฉันไม่เข้าใจความหมายของประโยคนี้", "en": "I don't understand the meaning of this sentence."},
        {"cn": "我家离学校走路只要十分钟。", "py": "Wǒ jiā lí xuéxiào zǒulù zhǐ yào shí fēnzhōng.", "th": "บ้านฉันเดินไปโรงเรียนใช้เวลาเพียง 10 นาที", "en": "My home is only a 10-minute walk from school."}
    ],
    "好": [
        {"cn": "这个办法真好！", "py": "Zhè ge bànfǎ zhēn hǎo!", "th": "วิธีนี้ดีจริงๆ!", "en": "This method is really good!"},
        {"cn": "今天天气很好，阳光明媚。", "py": "Jīntiān tiānqì hěn hǎo, yángguāng míngmèi.", "th": "วันนี้อากาศดีมาก แดดแจ่มใส", "en": "The weather is very good today with bright sunshine."},
        {"cn": "好久不见，最近身体好吗？", "py": "Hǎojiǔ bújiàn, zuìjìn shēntǐ hǎo ma?", "th": "ไม่ได้เจอกันนานเลย ช่วงนี้สุขภาพสบายดีไหม?", "en": "Long time no see, how is your health recently?"},
        {"cn": "你准备好了吗？我们要出发了。", "py": "Nǐ zhǔnbèi hǎo le ma? Wǒmen yào chūfā le.", "th": "เธอเตรียมตัวพร้อมหรือยัง? พวกเราจะออกเดินทางแล้วนะ", "en": "Are you ready? We are about to set off."},
        {"cn": "这家餐厅的味道非常好吃。", "py": "Zhè jiā cāntīng de wèidao fēicháng hǎochī.", "th": "รสชาติของร้านอาหารร้านนี้อร่อยมากจริงๆ", "en": "The taste of this restaurant is very delicious."}
    ],
    "是": [
        {"cn": "这是我新买的笔记本电脑。", "py": "Zhè shì wǒ xīn mǎi de bǐjìběn diànnǎo.", "th": "นี่คือแล็ปท็อปคอมพิวเตอร์ที่ฉันเพิ่งซื้อมาใหม่", "en": "This is my newly bought laptop."},
        {"cn": "他是我们学校的汉语老师。", "py": "Tā shì wǒmen xuéxiào de Hànyǔ lǎoshī.", "th": "เขาเป็นคุณครูภาษาจีนของโรงเรียนพวกเรา", "en": "He is our school's Chinese teacher."},
        {"cn": "这件事情是不是真的？", "py": "Zhè jiàn shìqing shì bú shì zhēn de?", "th": "เรื่องนี้จริงหรือไม่จริง?", "en": "Is this matter true or not?"},
        {"cn": "我是坐地铁来这里的。", "py": "Wǒ shì zuò dìtiě lái zhèlǐ de.", "th": "ฉันนั่งรถไฟใต้ดินมาที่นี่", "en": "I came here by subway."},
        {"cn": "明天是星期天，不用上班。", "py": "Míngtiān shì xīngqītiān, búyòng shàngbān.", "th": "พรุ่งนี้เป็นวันอาทิตย์ ไม่ต้องไปทำงาน", "en": "Tomorrow is Sunday, no need to work."}
    ],
    "不": [
        {"cn": "我今天不想喝咖啡，我想喝茶。", "py": "Wǒ jīntiān bù xiǎng hē kāfēi, wǒ xiǎng hē chá.", "th": "วันนี้ฉันไม่อยากดื่มกาแฟ ฉันอยากดื่มชา", "en": "I don't want coffee today; I want tea."},
        {"cn": "这个字不太好写，请教教我。", "py": "Zhè ge zì bú tài hǎo xiě, qǐng jiāo jiao wǒ.", "th": "ตัวอักษรตัวนี้เขียนไม่ง่ายเท่าไหร่ ช่วยสอนฉันหน่อยนะ", "en": "This character is not very easy to write, please teach me."},
        {"cn": "他不知道明天的考试时间。", "py": "Tā bù zhīdào míngtiān de kǎoshì shíjiān.", "th": "เขาไม่รู้เวลาสอบของวันพรุ่งนี้", "en": "He doesn't know tomorrow's exam time."},
        {"cn": "不好意思，我不能去参加晚会。", "py": "Bù hǎoyìsi, wǒ bù néng qù cānjiā wǎnhuì.", "th": "ขออภัยด้วยนะ ฉันไม่สามารถไปร่วมงานเลี้ยงได้", "en": "Sorry, I cannot attend the party."},
        {"cn": "外面的天气不是很冷，穿外套就可以。", "py": "Wàimian de tiānqì bú shì hěn lěng, chuān wàitào jiù kěyǐ.", "th": "อากาศข้างนอกไม่ได้หนาวมาก ใส่เสื้อแจ็กเก็ตก็พอแล้ว", "en": "The weather outside is not very cold; wearing a jacket is fine."}
    ],
    "谢谢": [
        {"cn": "太谢谢你的关心了！", "py": "Tài xièxie nǐ de guānxīn le!", "th": "ขอบคุณสำหรับความห่วงใยของเธอมากจริงๆ!", "en": "Thank you so much for your care!"},
        {"cn": "谢谢老师的耐心指导。", "py": "Xièxie lǎoshī de nàixīn zhǐdǎo.", "th": "ขอบคุณสำหรับคำแนะนำอย่างอดทนของคุณครูครับ/ค่ะ", "en": "Thank you for the teacher's patient guidance."},
        {"cn": "不用谢谢，这是我应该做的。", "py": "Búyòng xièxie, zhè shì wǒ yīnggāi zuò de.", "th": "ไม่ต้องขอบคุณหรอก นี่เป็นสิ่งที่ฉันควรทำอยู่แล้ว", "en": "No need to thank, this is what I should do."},
        {"cn": "谢谢大家来参加我的生日派对！", "py": "Xièxie dàjiā lái cānjiā wǒ de shēngrì pàiduì!", "th": "ขอบคุณทุกคนที่มาร่วมงานวันเกิดของฉันนะ!", "en": "Thank you everyone for coming to my birthday party!"},
        {"cn": "谢谢你的礼物，我很喜欢！", "py": "Xièxie nǐ de lǐwù, wǒ hěn xǐhuan!", "th": "ขอบคุณสำหรับของขวัญของเธอนะ ฉันชอบมากเลย!", "en": "Thank you for your gift, I like it a lot!"}
    ],
    "想": [
        {"cn": "我想喝一杯热牛奶。", "py": "Wǒ xiǎng hē yì bēi rè niúnǎi.", "th": "ฉันอยากดื่มนมอุ่นสักหนึ่งแก้ว", "en": "I want to drink a cup of warm milk."},
        {"cn": "你心里在想什么呢？", "py": "Nǐ xīnli zài xiǎng shénme ne?", "th": "ในใจเธอกำลังคิดอะไรอยู่เหรอ?", "en": "What are you thinking in your mind?"},
        {"cn": "我想去北京故宫参观。", "py": "Wǒ xiǎng qù Běijīng Gùgōng cānguān.", "th": "ฉันอยากไปเยี่ยมชมพระราชวังต้องห้ามที่ปักกิ่ง", "en": "I want to visit the Forbidden City in Beijing."},
        {"cn": "我很想念远方的父母。", "py": "Wǒ hěn xiǎngniàn yuǎnfāng de fùmǔ.", "th": "ฉันคิดถึงพ่อแม่ที่อยู่ทางไกลมาก", "en": "I miss my parents far away very much."},
        {"cn": "让我想一想再回答你的问题。", "py": "Ràng wǒ xiǎng yì xiǎng zài huídá nǐ de wèntí.", "th": "ให้ฉันคิดดูสักครู่แล้วค่อยตอบคำถามของเธอนะ", "en": "Let me think a moment before answering your question."}
    ],
    "吃": [
        {"cn": "中午你想吃米饭还是吃面条？", "py": "Zhōngwǔ nǐ xiǎng chī mǐfàn háishi chī miàntiáo?", "th": "มื้อเที่ยงเธออยากกินข้าวสวยหรือกินบะหมี่?", "en": "Do you want to eat rice or noodles at noon?"},
        {"cn": "多吃蔬菜和水果对皮肤好。", "py": "Duō chī shūcài hé shuǐguǒ duì pífū hǎo.", "th": "กินผักและผลไม้เยอะๆ ดีต่อผิวพรรณ", "en": "Eating more vegetables and fruit is good for skin."},
        {"cn": "你吃过四川的麻婆豆腐吗？", "py": "Nǐ chī guò Sìchuān de mápó dòufu ma?", "th": "เธอเคยทานเต้าหู้มาโปของเสฉวนไหม?", "en": "Have you eaten Sichuan Mapo Tofu?"},
        {"cn": "我们先去洗手，然后再吃饭。", "py": "Wǒmen xiān qù xǐshǒu, ránhòu zài chīfàn.", "th": "พวกเราไปล้างมือก่อน แล้วค่อยกินข้าว", "en": "Let's wash hands first, then eat."},
        {"cn": "慢点吃，小心烫！", "py": "Màn diǎnr chī, xiǎoxīn tàng!", "th": "ค่อยๆ กินนะ ระวังร้อนลวก!", "en": "Eat slowly, be careful of hot food!"}
    ],
    "看": [
        {"cn": "你看前面那座高楼真壮观！", "py": "Nǐ kàn qiánmian nà zuò gāolóu zhēn zhuàngguān!", "th": "เธอดูตึกสูงข้างหน้านั้นสิ อลังการจริงๆ!", "en": "Look at that tall building ahead, truly magnificent!"},
        {"cn": "周末我打算在家看一本历史书。", "py": "Zhōumò wǒ dǎsuàn zài jiā kàn yì běn lìshǐ shū.", "th": "สุดสัปดาห์ฉันวางแผนจะอ่านหนังสือประวัติศาสตร์อยู่ที่บ้าน", "en": "This weekend I plan to read a history book at home."},
        {"cn": "你看得懂这篇中文短文吗？", "py": "Nǐ kàn de dǒng zhè piān Zhōngwén duǎnwén ma?", "th": "เธออ่านบทความสั้นภาษาจีนนี้เข้าใจไหม?", "en": "Can you read and understand this short Chinese passage?"},
        {"cn": "医生正在给病人看病。", "py": "Yīshēng zhèngzài gěi bìngrén kànbìng.", "th": "คุณหมอกำลังตรวจรักษาคนไข้อยู่", "en": "The doctor is currently examining the patient."},
        {"cn": "晚上我们一起看球赛直播吧。", "py": "Wǎnshang wǒmen yìqǐ kàn qiúsài zhíbō ba.", "th": "ตอนค่ำพวกเราดูถ่ายทอดสดการแข่งขันบอลด้วยกันเถอะ", "en": "Let's watch the live ball match together tonight."}
    ],
    "去": [
        {"cn": "这个周末你打算去哪儿旅游？", "py": "Zhè ge zhōumò nǐ dǎsuàn qù nǎr lǚyóu?", "th": "สุดสัปดาห์นี้เธอวางแผนจะไปเที่ยวที่ไหน?", "en": "Where do you plan to travel this weekend?"},
        {"cn": "我们一起去食堂吃午饭吧。", "py": "Wǒmen yìqǐ qù shítáng chī wǔfàn ba.", "th": "พวกเราไปกินข้าวเที่ยงที่โรงอาหารด้วยกันเถอะ", "en": "Let's go eat lunch at the canteen together."},
        {"cn": "去年夏天我去了一次上海。", "py": "Qùnián xiàtiān wǒ qù le yí cì Shànghǎi.", "th": "ฤดูร้อนปีที่แล้วฉันไปเซี่ยงไฮ้มาหนึ่งครั้ง", "en": "Last summer I went to Shanghai once."},
        {"cn": "出租车司机正要去机场接客人。", "py": "Chūzūchē sījī zhèng yào qù jīchǎng jiē kèrén.", "th": "คนขับแท็กซี่กำลังจะไปรับผู้โดยสารที่สนามบิน", "en": "The taxi driver is about to go to the airport to pick up passengers."},
        {"cn": "下班后我和同事去健身房锻炼。", "py": "Xiàbān hòu wǒ hé tóngshì qù jiànshēnfáng duànliàn.", "th": "หลังเลิกงานฉันกับเพื่อนร่วมงานไปออกกำลังกายที่ฟิตเนส", "en": "After work my coworker and I go to the gym to work out."}
    ],
    "买": [
        {"cn": "我想去超市买点儿新鲜水果。", "py": "Wǒ xiǎng qù chāoshì mǎi diǎnr xīnxiān shuǐguǒ.", "th": "ฉันอยากไปซูเปอร์มาร์เก็ตซื้อผลไม้สดสักหน่อย", "en": "I want to go to the supermarket to buy some fresh fruit."},
        {"cn": "这本书是在哪儿买的？", "py": "Zhè běn shū shì zài nǎr mǎi de?", "th": "หนังสือเล่มนี้ซื้อมาจากที่ไหน?", "en": "Where was this book bought?"},
        {"cn": "网购又方便又便宜，很多人喜欢在网上买东西。", "py": "Wǎnggòu yòu fāngbiàn yòu piányi, hěn duō rén xǐhuan zài wǎngshang mǎi dōngxi.", "th": "การซื้อของออนไลน์ทั้งสะดวกและราคาถูก หลายคนจึงชอบซื้อของบนเน็ต", "en": "Online shopping is convenient and cheap; many like buying online."},
        {"cn": "这件衣服太贵了，我们还是别买了。", "py": "Zhè jiàn yīfu tài guì le, wǒmen háishi bié mǎi le.", "th": "เสื้อตัวนี้แพงเกินไป พวกเราอย่าซื้อเลยดีกว่า", "en": "This outfit is too expensive, let's not buy it."},
        {"cn": "你买好去北京的高铁票了吗？", "py": "Nǐ mǎi hǎo qù Běijīng de gāotiě piào le ma?", "th": "เธอซื้อตั๋วรถไฟความเร็วสูงไปปักกิ่งเรียบร้อยแล้วหรือยัง?", "en": "Have you bought the high-speed train tickets to Beijing?"}
    ],
    # HSK 2 Highlights
    "因为": [
        {"cn": "因为外面下大雨，所以比赛取消了。", "py": "Yīnwèi wàimian xià dàyǔ, suǒyǐ bǐsài qǔxiāo le.", "th": "เพราะว่าข้างนอกฝนตกหนัก ดังนั้นการแข่งขันจึงถูกยกเลิก", "en": "Because it rained heavily outside, the match was canceled."},
        {"cn": "因为喜欢中国文化，我开始学习汉语。", "py": "Yīnwèi xǐhuan Zhōngguó wénhuà, wǒ kāishǐ xuéxí Hànyǔ.", "th": "เพราะชอบวัฒนธรรมจีน ฉันจึงเริ่มเรียนภาษาจีน", "en": "Because I like Chinese culture, I began studying Chinese."},
        {"cn": "他因为生病，今天没来上班。", "py": "Tā yīnwèi shēngbìng, jīntiān méi lái shàngbān.", "th": "เขาเนื่องจากป่วย วันนี้จึงไม่ได้มาทำงาน", "en": "Because he is sick, he didn't come to work today."},
        {"cn": "不要因为一点儿困难就放弃努力。", "py": "Bú yào yīnwèi yìdiǎnr kùnnan jiù fàngqì nǔlì.", "th": "อย่ายอมแพ้ความพยายามเพียงเพราะอุปสรรคเล็กน้อย", "en": "Don't give up trying because of a little difficulty."},
        {"cn": "因为堵车，他迟到了半个小时。", "py": "Yīnwèi dǔchē, tā chídào le bàn ge xiǎoshí.", "th": "เนื่องจากรถติด เขาจึงมาสายไปครึ่งชั่วโมง", "en": "Because of traffic jam, he was half an hour late."}
    ],
    "比": [
        {"cn": "今天比昨天冷多了，记得穿大衣。", "py": "Jīntiān bǐ zuótiān lěng duō le, jìde chuān dàyī.", "th": "วันนี้หนาวกว่าเมื่อวานเยอะมาก จำไว้ว่าต้องใส่เสื้อโค้ต", "en": "Today is much colder than yesterday, remember to wear a coat."},
        {"cn": "他跑得比我快，跳得也比我高。", "py": "Tā pǎo de bǐ wǒ kuài, tiào de yě bǐ wǒ gāo.", "th": "เขาวิ่งได้เร็วกว่าฉัน และกระโดดได้สูงกว่าฉันด้วย", "en": "He runs faster than me and jumps higher than me."},
        {"cn": "坐高铁比坐普通火车舒服得多。", "py": "Zuò gāotiě bǐ zuò pǔtōng huǒchē shūfu de duō.", "th": "นั่งรถไฟความเร็วสูงสบายกว่านั่งรถไฟธรรมดาเยอะมาก", "en": "Riding the high-speed train is much more comfortable than regular train."},
        {"cn": "弟弟的身高已经比哥哥还高了。", "py": "Dìdi de shēngāo yǐjīng bǐ gēge hái gāo le.", "th": "ส่วนสูงของน้องชายสูงกว่าพี่ชายเสียอีกแล้ว", "en": "The younger brother's height is already taller than the older brother's."},
        {"cn": "这本词典比那本更实用。", "py": "Zhè běn cídiǎn bǐ nà běn gèng shíyòng.", "th": "พจนานุกรมเล่มนี้ใช้งานได้จริงมากกว่าเล่มนั้น", "en": "This dictionary is more practical than that one."}
    ],
    "离": [
        {"cn": "学校离地铁站只有几百米。", "py": "Xuéxiào lí dìtiězhàn zhǐ yǒu jǐ bǎi mǐ.", "th": "โรงเรียนอยู่ห่างจากสถานีรถไฟใต้ดินเพียงไม่กี่ร้อยเมตร", "en": "The school is only a few hundred meters from the subway station."},
        {"cn": "我家离公司很远，每天要坐一个小时的车。", "py": "Wǒ jiā lí gōngsī hěn yuǎn, měitiān yào zuò yí ge xiǎoshí de chē.", "th": "บ้านของฉันอยู่ไกลจากบริษัทมาก ทุกวันต้องนั่งรถ 1 ชั่วโมง", "en": "My home is far from the company; it takes an hour drive daily."},
        {"cn": "离期末考试还有一个月，大家要抓紧时间。", "py": "Lí qīmò kǎoshì hái yǒu yí ge yuè, dàjiā yào zhuājǐn shíjiān.", "th": "ห่างจากการสอบปลายภาคยังเหลือเวลาอีกหนึ่งเดือน ทุกคนต้องเร่งรีบเวลา", "en": "There is still a month before final exams; everyone hurry up."},
        {"cn": "中国离泰国不远，坐飞机几个小时就到了。", "py": "Zhōngguó lí Tàiguó bù yuǎn, zuò fēijī jǐ ge xiǎoshí jiù dào le.", "th": "ประเทศจีนอยู่ไม่ไกลจากประเทศไทย นั่งเครื่องบินไม่กี่ชั่วโมงก็ถึง", "en": "China is not far from Thailand; it takes a few hours by plane."},
        {"cn": "饭馆离这里很近，我们走路过去吧。", "py": "Fànguǎn lí zhèlǐ hěn jìn, wǒmen zǒulù guòqu ba.", "th": "ร้านอาหารอยู่ใกล้จากตรงนี้มาก พวกเราเดินไปกันเถอะ", "en": "The restaurant is very close to here; let's walk over."}
    ],
    # HSK 3 Highlights
    "越来越": [
        {"cn": "秋天到了，树叶越来越黄了。", "py": "Qiūtiān dào le, shùyè yuèláiyuè huáng le.", "th": "ฤดูใบไม้ร่วงมาถึงแล้ว ใบไม้ก็เหลืองขึ้นเรื่อยๆ แล้ว", "en": "Autumn has arrived; leaves are getting yellower and yellower."},
        {"cn": "经常锻炼身体，身体就会越来越好。", "py": "Jīngcháng duànliàn shēntǐ, shēntǐ jiù huì yuèláiyuè hǎo.", "th": "ออกกำลังกายเป็นประจำ สุขภาพร่างกายก็จะดีขึ้นเรื่อยๆ", "en": "Exercising regularly makes your health better and better."},
        {"cn": "随着科技的发展，生活变得越来越方便。", "py": "Suízhe kējì de fāzhǎn, shēnghuó biàn de yuèláiyuè fāngbiàn.", "th": "ตามการพัฒนาของเทคโนโลยี ชีวิตก็เปลี่ยนเป็นสะดวกสบายขึ้นเรื่อยๆ", "en": "With technological growth, life has become increasingly convenient."},
        {"cn": "她的汉语发音越来越标准了。", "py": "Tā de Hànyǔ fāyīn yuèláiyuè biāozhǔn le.", "th": "การออกเสียงภาษาจีนของเธอได้มาตรฐานขึ้นเรื่อยๆ แล้ว", "en": "Her Chinese pronunciation has gotten more and more accurate."},
        {"cn": "天黑得越来越早了，冬天快要来了。", "py": "Tiān hēi de yuèláiyuè zǎo le, dōngtiān kuàiyào lái le.", "th": "ฟ้ามืดเร็วขึ้นเรื่อยๆ แล้ว ฤดูหนาวใกล้จะมาถึงแล้ว", "en": "It gets dark earlier and earlier; winter is coming soon."}
    ],
    "一直": [
        {"cn": "我一直想去内蒙古看大草原。", "py": "Wǒ yìzhí xiǎng qù Nèiměnggǔ kàn dà cǎoyuán.", "th": "ฉันอยากไปชมทุ่งหญ้าใหญ่ที่มองโกเลียในมาโดยตลอด", "en": "I have always wanted to go to Inner Mongolia to see the grasslands."},
        {"cn": "沿着这条路一直往前走，前面就是中国银行。", "py": "Yánzhe zhè tiáo lù yìzhí wǎng qián zǒu, qiánmian jiù shì Zhōngguó Yínháng.", "th": "เดินตรงไปตามถนนเส้นนี้ ข้างหน้าก็คือธนาคารแห่งประเทศจีน", "en": "Go straight along this street; Bank of China is right ahead."},
        {"cn": "外面一直下着小雨，我们待在屋里吧。", "py": "Wàimian yìzhí xiàzhe xiǎoyǔ, wǒmen dāi zài wū lǐ ba.", "th": "ข้างนอกฝนตกปรอยๆ ตลอดเวลา พวกเราอยู่ในห้องเถอะ", "en": "It has been drizzling continuously outside; let's stay indoors."},
        {"cn": "他一直非常努力地准备这次中文考试。", "py": "Tā yìzhí fēicháng nǔlì de zhǔnbèi zhè cì Zhōngwén kǎoshì.", "th": "เขาตั้งใจเตรียมตัวสำหรับการสอบภาษาจีนครั้งนี้มาโดยตลอด", "en": "He has been preparing diligently for this Chinese exam all along."},
        {"cn": "这本书我一直带在身边，经常拿出来读。", "py": "Zhè běn shū wǒ yìzhí dài zài shēnbiān, jīngcháng ná chūlai dú.", "th": "หนังสือเล่มนี้ฉันพกติดตัวไว้ตลอด มักจะหยิบขึ้นมาอ่านบ่อยๆ", "en": "I've always kept this book with me, often taking it out to read."}
    ],
    "解决": [
        {"cn": "大家一起想办法解决这个问题。", "py": "Dàjiā yìqǐ xiǎng bànfǎ jiějué zhè ge wèntí.", "th": "ทุกคนช่วยกันคิดหาทางแก้ไขปัญหานี้", "en": "Everyone think of a way to solve this problem together."},
        {"cn": "经过努力，困难终于被解决了。", "py": "Jīngguò nǔlì, kùnnan zhōngyú bèi jiějué le.", "th": "ผ่านความพยายาม ในที่สุดความยากลำบากก็ถูกแก้ไขได้สำเร็จ", "en": "Through effort, difficulties were finally solved."},
        {"cn": "遇到事情不要慌，慢慢解决。", "py": "Yù dào shìqing bú yào huāng, mànmàn jiějué.", "th": "เมื่อเจอปัญหาอย่าเพิ่งตื่นตระหนก ค่อยๆ แก้ไขไป", "en": "Don't panic when encountering problems; solve them calmly."},
        {"cn": "沟通是解决矛盾的最好方式。", "py": "Gōutōng shì jiějué máodùn de zuì hǎo fāngshì.", "th": "การสื่อสารคือวิธีที่ดีที่สุดในการคลี่คลายความขัดแย้ง", "en": "Communication is the best way to resolve contradictions."},
        {"cn": "这个技术难题上周已经顺利解决了。", "py": "Zhè ge jìshù nándí shàngzhōu yǐjīng shùnlì jiějué le.", "th": "โจทย์ทางเทคนิคนี้ได้รับการแก้ไขอย่างราบรื่นไปแล้วเมื่อสัปดาห์ก่อน", "en": "This technical challenge was smoothly resolved last week."}
    ],
    "环境": [
        {"cn": "这个小区的绿化很好，生活环境很安静。", "py": "Zhè ge xiǎoqū de lǜhuà hěn hǎo, shēnghuó huánjìng hěn ānjìng.", "th": "ต้นไม้ในหมู่บ้านนี้ดีมาก สิ่งแวดล้อมในการใช้ชีวิตเงียบสงบมาก", "en": "This neighborhood has great greenery; the living environment is quiet."},
        {"cn": "保护环境是每个人的责任。", "py": "Bǎohù huánjìng shì měi ge rén de zérèn.", "th": "การปกป้องสิ่งแวดล้อมเป็นหน้าที่ของทุกคน", "en": "Protecting the environment is everyone's responsibility."},
        {"cn": "良好的学习环境能提高学习效率。", "py": "Liánghǎo de xuéxí huánjìng néng tígāo xuéxí xiàolǜ.", "th": "สภาพแวดล้อมในการเรียนที่ดีช่วยเพิ่มประสิทธิภาพในการเรียนได้", "en": "A good learning environment can enhance study efficiency."},
        {"cn": "这儿的自然环境真美丽！", "py": "Zhèr de zìrán huánjìng zhēn měilì!", "th": "สิ่งแวดล้อมทางธรรมชาติที่นี่สวยงามจริงๆ!", "en": "The natural environment here is really beautiful!"},
        {"cn": "我们应该努力适应新的工作环境。", "py": "Wǒmen yīnggāi nǔlì shìyìng xīn de gōngzuò huánjìng.", "th": "พวกเราควรพยายามปรับตัวให้เข้ากับสภาพแวดล้อมการทำงานใหม่", "en": "We should strive to adapt to the new working environment."}
    ],
    "终于": [
        {"cn": "经过三个月的复习，我终于通过了HSK考试！", "py": "Jīngguò sān ge yuè de fùxí, wǒ zhōngyú tōngguò le HSK kǎoshì!", "th": "ผ่านการทบทวนมา 3 เดือน ในที่สุดฉันก็สอบผ่าน HSK แล้ว!", "en": "After three months of review, I finally passed the HSK exam!"},
        {"cn": "等了两个小时，雨终于停了。", "py": "Děng le liǎng ge xiǎoshí, yǔ zhōngyú tíng le.", "th": "รอมาสองชั่วโมง ในที่สุดฝนก็หยุดตกแล้ว", "en": "After waiting for two hours, the rain finally stopped."},
        {"cn": "他终于买到了心仪已久的那本书。", "py": "Tā zhōngyú mǎi dào le xīnyí yǐjiǔ de nà běn shū.", "th": "ในที่สุดเขาก็ซื้อหนังสือเล่มที่หมายตามานานได้แล้ว", "en": "He finally bought that book he had wanted for a long time."},
        {"cn": "飞机终于平稳降落在北京机场了。", "py": "Fēijī zhōngyú píngwěn jiàngluò zài Běijīng jīchǎng le.", "th": "ในที่สุดเครื่องบินก็ลงจอดอย่างราบรื่นที่สนามบินปักกิ่ง", "en": "The plane finally landed smoothly at Beijing Airport."},
        {"cn": "忙了一整天，我们终于可以休息了。", "py": "Máng le yì zhěng tiān, wǒmen zhōngyú kěyǐ xiūxi le.", "th": "ยุ่งมาตลอดทั้งวัน ในที่สุดพวกเราก็ได้พักผ่อนแล้ว", "en": "Busy all day, we can finally rest."}
    ]
}

def generate_sentence_variants(word_obj):
    """
    Returns a list of 5 example sentence objects for the word.
    """
    hanzi = word_obj["hanzi"]
    pinyin = word_obj["pinyin"]
    thai = word_obj["thai"]
    english = word_obj["english"]
    pos = word_obj.get("pos", "")
    base_cn = word_obj.get("ex_cn", "")
    base_py = word_obj.get("ex_py", "")
    base_th = word_obj.get("ex_th", "")
    base_en = word_obj.get("ex_en", "")

    variants = []

    # 1. Base variation (from original textbook data)
    if base_cn:
        variants.append({
            "cn": base_cn,
            "py": base_py,
            "th": base_th,
            "en": base_en
        })

    # 2. Check if custom curated variations exist for this word
    if hanzi in SPECIFIC_VARIATIONS:
        for v in SPECIFIC_VARIATIONS[hanzi]:
            if v["cn"] != base_cn and v not in variants:
                variants.append(v)

    # 3. If fewer than 5 variations, generate natural contextual variations
    # Pattern A: Question sentence asking about the word / situation
    if len(variants) < 5:
        if "n." in pos or "noun" in pos:
            v_a = {
                "cn": f"请问，这个{hanzi}在哪里可以买到？",
                "py": f"Qǐngwèn, zhè ge {pinyin} zài nǎlǐ kěyǐ mǎi dào?",
                "th": f"ขอถามหน่อย {thai} อันนี้สามารถหาซื้อได้ที่ไหนหรือครับ/ค่ะ?",
                "en": f"Excuse me, where can I buy this {english}?"
            }
            if v_a["cn"] != base_cn: variants.append(v_a)
        elif "v." in pos or "verb" in pos:
            v_a = {
                "cn": f"你平时喜欢{hanzi}吗？",
                "py": f"Nǐ píngshí xǐhuan {pinyin} ma?",
                "th": f"ปกติแล้วเธอชอบ{thai}ไหม?",
                "en": f"Do you usually like to {english}?"
            }
            if v_a["cn"] != base_cn: variants.append(v_a)
        elif "adj." in pos or "adjective" in pos:
            v_a = {
                "cn": f"这里的环境真{hanzi}，我很喜欢。",
                "py": f"Zhèlǐ de huánjìng zhēn {pinyin}, wǒ hěn xǐhuan.",
                "th": f"สิ่งแวดล้อมที่นี่{thai}จริงๆ ฉันชอบมาก",
                "en": f"The environment here is really {english}, I like it a lot."
            }
            if v_a["cn"] != base_cn: variants.append(v_a)
        elif "adv." in pos or "adverb" in pos:
            v_a = {
                "cn": f"他{hanzi}在准备明天的汉语考试。",
                "py": f"Tā {pinyin} zài zhǔnbèi míngtiān de Hànyǔ kǎoshì.",
                "th": f"เขา{thai}เตรียมตัวสำหรับการสอบภาษาจีนในวันพรุ่งนี้",
                "en": f"He is {english} preparing for tomorrow's Chinese exam."
            }
            if v_a["cn"] != base_cn: variants.append(v_a)

    # Pattern B: Habit / Daily activity sentence
    if len(variants) < 5:
        if "n." in pos:
            v_b = {
                "cn": f"桌子上放着一个新的{hanzi}。",
                "py": f"Zhuōzi shang fàngzhe yí ge xīn de {pinyin}.",
                "th": f"บนโต๊ะมี{thai}ใหม่อันหนึ่งวางอยู่",
                "en": f"A new {english} is placed on the table."
            }
            variants.append(v_b)
        elif "v." in pos:
            v_b = {
                "cn": f"我们周末一起去{hanzi}吧！",
                "py": f"Wǒmen zhōumò yìqǐ qù {pinyin} ba!",
                "th": f"วันหยุดสุดสัปดาห์พวกเราไป{thai}ด้วยกันเถอะ!",
                "en": f"Let's go {english} together this weekend!"
            }
            variants.append(v_b)
        elif "adj." in pos:
            v_b = {
                "cn": f"虽然有点儿{hanzi}，但是值得尝试。",
                "py": f"Suīrán yǒudiǎnr {pinyin}, dànshì zhíde chángshì.",
                "th": f"ถึงแม้จะ{thai}ไปสักหน่อย แต่ก็คุ้มค่าที่จะลองดู",
                "en": f"Although a bit {english}, it is worth trying."
            }
            variants.append(v_b)
        else:
            v_b = {
                "cn": f"老师耐心地给我们讲解了这个{hanzi}的用法。",
                "py": f"Lǎoshī nàixīn de gěi wǒmen jiǎngjiě le zhè ge {pinyin} de yòngfǎ.",
                "th": f"คุณครูอธิบายวิธีใช้ {thai} ให้พวกเราฟังอย่างอดทน",
                "en": f"The teacher patiently explained the usage of {english} to us."
            }
            variants.append(v_b)

    # Pattern C: Future plan or suggestion
    if len(variants) < 5:
        if "v." in pos:
            v_c = {
                "cn": f"做完作业以后，我才去{hanzi}。",
                "py": f"Zuò wán zuòyè yǐhòu, wǒ cái qù {pinyin}.",
                "th": f"หลังจากทำการบ้านเสร็จแล้ว ฉันถึงจะไป{thai}",
                "en": f"Only after finishing homework will I go {english}."
            }
            variants.append(v_c)
        else:
            v_c = {
                "cn": f"朋友告诉我，这个{hanzi}非常重要。",
                "py": f"Péngyou gàosu wǒ, zhè ge {pinyin} fēicháng zhòngyào.",
                "th": f"เพื่อนบอกฉันว่า {thai} นี้มีความสำคัญมาก",
                "en": f"My friend told me this {english} is very important."
            }
            variants.append(v_c)

    # Pattern D: Experience / Reality check
    if len(variants) < 5:
        if "n." in pos:
            v_d = {
                "cn": f"我昨天刚买了一个{hanzi}，质量非常好。",
                "py": f"Wǒ zuótiān gāng mǎi le yí ge {pinyin}, zhìliàng fēicháng hǎo.",
                "th": f"เมื่อวานฉันเพิ่งซื้อ{thai}มาอันหนึ่ง คุณภาพดีมาก",
                "en": f"I just bought a {english} yesterday, the quality is very good."
            }
            variants.append(v_d)
        elif "v." in pos:
            v_d = {
                "cn": f"我已经学会怎么{hanzi}了，其实并不难。",
                "py": f"Wǒ yǐjīng xuéhuì zěnme {pinyin} le, qíshí bìng bù nán.",
                "th": f"ฉันเรียนรู้วิธี{thai}เป็นแล้ว ความจริงไม่ได้ยากเลย",
                "en": f"I have learned how to {english}, it's actually not hard."
            }
            variants.append(v_d)
        elif "adj." in pos:
            v_d = {
                "cn": f"大家觉得今天的天气比昨天更{hanzi}。",
                "py": f"Dàjiā juéde jīntiān de tiānqì bǐ zuótiān gèng {pinyin}.",
                "th": f"ทุกคนรู้สึกว่าอากาศวันนี้{thai}กว่าเมื่อวาน",
                "en": f"Everyone thinks today's weather is even more {english} than yesterday."
            }
            variants.append(v_d)
        else:
            v_d = {
                "cn": f"在日常生活中，我们经常会用到{hanzi}。",
                "py": f"Zài rìcháng shēnghuó zhōng, wǒmen jīngcháng huì yòng dào {pinyin}.",
                "th": f"ในชีวิตประจำวัน พวกเรามักจะได้ใช้ {thai} อยู่เสมอ",
                "en": f"In daily life, we often use {english}."
            }
            variants.append(v_d)

    # Pattern E: Opinion / Communication
    if len(variants) < 5:
        if "n." in pos:
            v_e = {
                "cn": f"这个{hanzi}比我想象的还要实用很多。",
                "py": f"Zhè ge {pinyin} bǐ wǒ xiǎngxiàng de hái yào shíyòng hěn duō.",
                "th": f"{thai}นี้ใช้งานได้จริงมากกว่าที่ฉันคิดไว้เสียอีก",
                "en": f"This {english} is much more practical than I imagined."
            }
            variants.append(v_e)
        elif "v." in pos:
            v_e = {
                "cn": f"如果明天有空，我们一起去{hanzi}怎么样？",
                "py": f"Rúguǒ míngtiān yǒu kòng, wǒmen yìqǐ qù {pinyin} zěnmeyàng?",
                "th": f"ถ้าพรุ่งนี้ว่าง พวกเราไป{thai}ด้วยกันดีไหม?",
                "en": f"If you are free tomorrow, how about going to {english} together?"
            }
            variants.append(v_e)
        elif "adj." in pos:
            v_e = {
                "cn": f"如果觉得太{hanzi}，你可以先休息一下。",
                "py": f"Rúguǒ juéde tài {pinyin}, nǐ kěyǐ xiān xiūxi yíxià.",
                "th": f"ถ้าหากรู้สึก{thai}เกินไป เธอพักผ่อนสักครู่ก่อนก็ได้นะ",
                "en": f"If it feels too {english}, you can take a rest first."
            }
            variants.append(v_e)
        else:
            v_e = {
                "cn": f"如果你能理解这个{hanzi}，请试着造一个句子。",
                "py": f"Rúguǒ nǐ néng lǐjiě zhè ge {pinyin}, qǐng shìzhe zào yí ge jùzi.",
                "th": f"ถ้าเธอเข้าใจ {thai} นี้แล้ว ลองแต่งประโยคดูสักหนึ่งประโยคนะ",
                "en": f"If you understand {english}, please try making a sentence."
            }
            variants.append(v_e)

    return variants[:5]

def update_database_with_variations():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Check if examples_json column exists
    cur.execute("PRAGMA table_info(words)")
    cols = [r[1] for r in cur.fetchall()]
    if "examples_json" not in cols:
        print("Adding column 'examples_json' to words table...")
        cur.execute("ALTER TABLE words ADD COLUMN examples_json TEXT")

    # Fetch all words
    cur.execute("SELECT id, level, chapter_id, chapter_num, hanzi, pinyin, english, thai, pos, ex_cn, ex_py, ex_en, ex_th FROM words")
    rows = cur.fetchall()

    updated_count = 0
    for r in rows:
        w_obj = {
            "id": r[0], "level": r[1], "chapter_id": r[2], "chapter_num": r[3],
            "hanzi": r[4], "pinyin": r[5], "english": r[6], "thai": r[7], "pos": r[8],
            "ex_cn": r[9], "ex_py": r[10], "ex_en": r[11], "ex_th": r[12]
        }
        variations = generate_sentence_variants(w_obj)
        cur.execute("UPDATE words SET examples_json = ? WHERE id = ?", (json.dumps(variations, ensure_ascii=False), w_obj["id"]))
        updated_count += 1

    conn.commit()
    conn.close()

    print(f"Successfully generated 5 sentence variations for {updated_count} words in SQLite!")

    # Update data/hsk3_database.json as well
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'hsk3_database.json')
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            full_db = json.load(f)
        
        words = full_db.get('words', [])
        for w in words:
            w['examples'] = generate_sentence_variants(w)
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(full_db, f, ensure_ascii=False, indent=2)
        print("Successfully updated data/hsk3_database.json with 5 sentence variations!")

if __name__ == '__main__':
    update_database_with_variations()
