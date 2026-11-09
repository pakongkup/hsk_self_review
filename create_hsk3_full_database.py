# create_hsk3_full_database.py
import json
import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

chapters_data = [
    {
        "id": 1,
        "title_cn": "我们去机场接你们",
        "title_pinyin": "Wǒmen qù jīchǎng jiē nǐmen",
        "title_en": "We Will Pick You Up at the Airport",
        "topic": "Airport, Arrivals & Descriptions",
        "grammar": ["看上去 / 看起来 (Describing appearance)", "疑问代词非疑问用法 (Indefinite: 哪儿/什么/谁)", "多项定语 (Multiple Attributives)"]
    },
    {
        "id": 2,
        "title_cn": "你们想吃什么就点什么",
        "title_pinyin": "Nǐmen xiǎng chī shénme jiù diǎn shénme",
        "title_en": "Order Whatever You Feel Like",
        "topic": "Restaurants, Food & Dining",
        "grammar": ["疑问代词指代任何对象 (什么...就...)", "并列复句“又...又...” (Both... and...)", "就餐常用词与句式"]
    },
    {
        "id": 3,
        "title_cn": "这个小区挺好的",
        "title_pinyin": "Zhè ge xiǎoqū tǐng hǎo de",
        "title_en": "This Neighborhood Is Pretty Good",
        "topic": "Housing, Renting & Appliances",
        "grammar": ["固定短语“挺...的” (Quite / Pretty)", "承接复句“先...再...” (First... then...)", "趋向补语基础用法"]
    },
    {
        "id": 4,
        "title_cn": "我借给你",
        "title_pinyin": "Wǒ jiè gěi nǐ",
        "title_en": "I'll Lend It to You",
        "topic": "Travel, Borrowing & Comparing",
        "grammar": ["比较句“跟...一样/不一样”", "介词短语“除了...以外” (Besides / Except)", "时间副词“一直”"]
    },
    {
        "id": 5,
        "title_cn": "这样的照片才好看",
        "title_pinyin": "Zhèyàng de zhàopiàn cái hǎokàn",
        "title_en": "Photos Like This Look Good",
        "topic": "Photography, Nature & Hobbies",
        "grammar": ["副词“才”与“终于” (Only then / Finally)", "固定短语“对...感兴趣” (Be interested in)", "形容词重叠与描述"]
    },
    {
        "id": 6,
        "title_cn": "高铁上还可以点外卖",
        "title_pinyin": "Gāotiě shang hái kěyǐ diǎn wàimài",
        "title_en": "You Can Even Order Takeout on a High-Speed Train",
        "topic": "Transportation & High-Speed Rail",
        "grammar": ["固定格式“该...了” (It's time to...)", "假设复句“如果...就...” (If... then...)", "固定短语“越来越...” (More and more)"]
    },
    {
        "id": 7,
        "title_cn": "那条裙子比短裤更好看",
        "title_pinyin": "Nà tiáo qúnzi bǐ duǎnkù gèng hǎokàn",
        "title_en": "That Skirt Looks Better Than the Shorts",
        "topic": "Shopping, Clothes & Sizes",
        "grammar": ["比较句“A 比 B + 更/还 + 形容词”", "递进复句“不但...而且...” (Not only... but also...)", "程度补语“极了”"]
    },
    {
        "id": 8,
        "title_cn": "他昨天出院了",
        "title_pinyin": "Tā zuótiān chūyuàn le",
        "title_en": "He Was Discharged from the Hospital Yesterday",
        "topic": "Health, Hospital & Illness",
        "grammar": ["趋向补语引申用法 (1)", "时量补语 (Duration of Actions)", "固定格式“以前 / 以后 / 前 / 后”"]
    },
    {
        "id": 9,
        "title_cn": "打不好没关系",
        "title_pinyin": "Dǎ bù hǎo méiguānxi",
        "title_en": "It Doesn't Matter If You Don't Play Well",
        "topic": "Sports, Ball Games & Competition",
        "grammar": ["目的复句“为了...” (In order to...)", "可能补语 (得/不: 打得好 / 打不好)", "固定格式“越 A 越 B”"]
    },
    {
        "id": 10,
        "title_cn": "你明天再把书还给我",
        "title_pinyin": "Nǐ míngtiān zài bǎ shū huán gěi wǒ",
        "title_en": "You Can Return the Book to Me Tomorrow",
        "topic": "School, Studying & Homework",
        "grammar": ["“把”字句 (1): 把 + 宾语 + 动词 + 在/到/给", "方位结构“在...上 / 下 / 中”", "“把”字句否定形式"]
    },
    {
        "id": 11,
        "title_cn": "看来我没办法解决这个问题",
        "title_pinyin": "Kànlái wǒ méi bànfǎ jiějué zhè ge wèntí",
        "title_en": "It Seems I Have No Way to Solve This Problem",
        "topic": "Workplace, Problem-Solving & Meetings",
        "grammar": ["“还是”与“或者”用法对比", "“把”字句 (3): 把 + 宾语 + 动词 + 结果补语", "固定格式“对...来说”"]
    },
    {
        "id": 12,
        "title_cn": "这个季节天气变化很快",
        "title_pinyin": "Zhè ge jìjié tiānqì biànhuà hěn kuài",
        "title_en": "The Weather Changes Rapidly in This Season",
        "topic": "Weather, Four Seasons & Climate",
        "grammar": ["选择复句“或者...或者...”", "趋向补语引申“出来 / 起来”", "范围副词“就”"]
    },
    {
        "id": 13,
        "title_cn": "我的新邻居来自英国",
        "title_pinyin": "Wǒ de xīn línjū láizì Yīngguó",
        "title_en": "My New Neighbors Come from the UK",
        "topic": "Neighbors, Social Visits & Cultural Life",
        "grammar": ["假设复句“...的话，就...”", "“把”字句 (4): 把 + 宾语 + 动词 + 成", "并列复句“一边...一边...”"]
    },
    {
        "id": 14,
        "title_cn": "这本书被别人借走了",
        "title_pinyin": "Zhè běn shū bèi biérén jiè zǒu le",
        "title_en": "This Book Was Borrowed by Someone Else",
        "topic": "Library, Books & Media",
        "grammar": ["被动句 (1): 主语 + 被 + 施事 + 动词 + 其他", "承接复句“先...然后...再...”", "固定格式“X 什么 X”"]
    },
    {
        "id": 15,
        "title_cn": "我是半个南京人",
        "title_pinyin": "Wǒ shì bàn ge Nánjīng rén",
        "title_en": "I Am Basically Half a Nanjing Local",
        "topic": "Hometown, City Travel & Local Culture",
        "grammar": ["介词“根据” (According to)", "数量重叠“数+量+数+量”", "固定短语“在...看来”与“不一会儿”"]
    },
    {
        "id": 16,
        "title_cn": "我听说有的熊猫出国了",
        "title_pinyin": "Wǒ tīngshuō yǒude xióngmāo chūguó le",
        "title_en": "I Heard That Some Pandas Have Gone Abroad",
        "topic": "Animals, Giant Pandas & Nature",
        "grammar": ["介词“关于” (Concerning / Regarding)", "固定短语“一般来说” (Generally speaking)", "比较句综合运用"]
    },
    {
        "id": 17,
        "title_cn": "我要多向认真的人学习",
        "title_pinyin": "Wǒ yào duō xiàng rènzhēn de rén xuéxí",
        "title_en": "I Will Learn More from Conscientious People",
        "topic": "Role Models & Study Attitude",
        "grammar": ["介词“向” (Towards / From someone)", "反问句“不是...吗？” (Isn't it...?)", "固定短语“只有...才...”"]
    },
    {
        "id": 18,
        "title_cn": "我学会了包饺子",
        "title_pinyin": "Wǒ xuéhuì le bāo jiǎozi",
        "title_en": "I've Learned How to Make Dumplings",
        "topic": "Spring Festival, Cooking & Personal Growth",
        "grammar": ["概数表达法 (Approximate Numbers)", "固定格式“从...起” (Starting from...)", "条件复句“只要...就...” (As long as...)"]
    }
]

# Vocabulary items by chapter with parts of speech, English translations, and context example sentences
words_data = [
    # Lesson 1
    {"chapter": 1, "hanzi": "以为", "pinyin": "yǐwéi", "english": "to think, believe erroneously", "pos": "v.", "ex_cn": "我还以为是同乐呢，他们看上去有点儿像。", "ex_py": "Wǒ hái yǐwéi shì Tónglè ne, tāmen kànshàngqù yǒudiǎnr xiàng.", "ex_en": "I mistakenly thought it was Tongle; they look a bit alike."},
    {"chapter": 1, "hanzi": "像", "pinyin": "xiàng", "english": "to be like, resemble", "pos": "v.", "ex_cn": "他们长得有点儿像。", "ex_py": "Tāmen zhǎng de yǒudiǎnr xiàng.", "ex_en": "They look somewhat alike."},
    {"chapter": 1, "hanzi": "长", "pinyin": "zhǎng", "english": "to grow, look like", "pos": "v.", "ex_cn": "你长得更像你妈妈。", "ex_py": "Nǐ zhǎng de gèng xiàng nǐ māma.", "ex_en": "You look more like your mother."},
    {"chapter": 1, "hanzi": "身高", "pinyin": "shēngāo", "english": "height", "pos": "n.", "ex_cn": "他身高有一米八。", "ex_py": "Tā shēngāo yǒu yì mǐ bā.", "ex_en": "His height is 1.8 meters."},
    {"chapter": 1, "hanzi": "米", "pinyin": "mǐ", "english": "meter", "pos": "m.", "ex_cn": "他比同乐高，身高有一米八。", "ex_py": "Tā bǐ Tónglè gāo, shēngāo yǒu yì mǐ bā.", "ex_en": "He is taller than Tongle, 1.8 meters tall."},
    {"chapter": 1, "hanzi": "瘦", "pinyin": "shòu", "english": "thin, slim", "pos": "adj.", "ex_cn": "他看起来也比同乐瘦一点儿。", "ex_py": "Tā kànqǐlái yě bǐ Tónglè shòu yìdiǎnr.", "ex_en": "He also looks a bit thinner than Tongle."},
    {"chapter": 1, "hanzi": "接", "pinyin": "jiē", "english": "to meet, pick up (someone)", "pos": "v.", "ex_cn": "我去机场接他们。", "ex_py": "Wǒ qù jīchǎng jiē tāmen.", "ex_en": "I'm going to the airport to pick them up."},
    {"chapter": 1, "hanzi": "箱子", "pinyin": "xiāngzi", "english": "suitcase, box", "pos": "n.", "ex_cn": "是一个黑色的箱子，上面写着我的名字。", "ex_py": "Shì yí ge hēisè de xiāngzi, shàngmian xiězhe wǒ de míngzi.", "ex_en": "It's a black suitcase with my name written on it."},
    {"chapter": 1, "hanzi": "行李", "pinyin": "xíngli", "english": "luggage, baggage", "pos": "n.", "ex_cn": "我的行李怎么还没出来？", "ex_py": "Wǒ de xíngli zěnme hái méi chūlái?", "ex_en": "Why hasn't my luggage come out yet?"},
    {"chapter": 1, "hanzi": "丢", "pinyin": "diū", "english": "to lose, go missing", "pos": "v.", "ex_cn": "行李箱丢了，请帮我找找。", "ex_py": "Xínglixiāng diū le, qǐng bāng wǒ zhǎozhao.", "ex_en": "The suitcase is lost, please help me look for it."},
    {"chapter": 1, "hanzi": "护照", "pinyin": "hùzhào", "english": "passport", "pos": "n.", "ex_cn": "我们拿着护照和机票去服务台。", "ex_py": "Wǒmen názhe hùzhào hé jīpiào qù fúwùtái.", "ex_en": "Let's take our passports and tickets to the service desk."},
    {"chapter": 1, "hanzi": "服务台", "pinyin": "fúwùtái", "english": "service desk, information counter", "pos": "n.", "ex_cn": "服务台在前面，我们过去问问吧。", "ex_py": "Fúwùtái zài qiánmian, wǒmen guòqù wènwen ba.", "ex_en": "The service desk is up ahead; let's go ask."},
    {"chapter": 1, "hanzi": "重要", "pinyin": "zhòngyào", "english": "important", "pos": "adj.", "ex_cn": "箱子里有不少重要的东西。", "ex_py": "Xiāngzi lǐ yǒu bù shǎo zhòngyào de dōngxi.", "ex_en": "There are quite a few important things inside the suitcase."},
    {"chapter": 1, "hanzi": "短", "pinyin": "duǎn", "english": "short (length)", "pos": "adj.", "ex_cn": "那个短头发的年轻人是谁？", "ex_py": "Nà ge duǎn tóufa de niánqīngrén shì shéi?", "ex_en": "Who is that young man with short hair?"},
    {"chapter": 1, "hanzi": "头发", "pinyin": "tóufa", "english": "hair", "pos": "n.", "ex_cn": "那个穿着黑衣服、短头发的人就是李文。", "ex_py": "Nà ge chuānzhe hēi yīfu, duǎn tóufa de rén jiù shì Lǐ Wén.", "ex_en": "That person wearing black clothes with short hair is Li Wen."},
    {"chapter": 1, "hanzi": "年轻", "pinyin": "niánqīng", "english": "young", "pos": "adj.", "ex_cn": "她看起来比照片上年轻。", "ex_py": "Tā kànqǐlái bǐ zhàopiàn shang niánqīng.", "ex_en": "She looks younger than in the photograph."},
    {"chapter": 1, "hanzi": "中间", "pinyin": "zhōngjiān", "english": "middle, center", "pos": "n.", "ex_cn": "我们站到中间去吧，这样他们好找一些。", "ex_py": "Wǒmen zhàn dào zhōngjiān qù ba, zhèyàng tāmen hǎo zhǎo yìxiē.", "ex_en": "Let's stand in the middle so it's easier for them to spot us."},
    {"chapter": 1, "hanzi": "站", "pinyin": "zhàn", "english": "to stand", "pos": "v.", "ex_cn": "我们在大厅中间站着等他们。", "ex_py": "Wǒmen zài dàtīng zhōngjiān zhànzhe děng tāmen.", "ex_en": "We are standing in the middle of the hall waiting for them."},
    {"chapter": 1, "hanzi": "着急", "pinyin": "zháojí", "english": "anxious, hurried", "pos": "adj.", "ex_cn": "别着急，服务台会帮我们找到行李的。", "ex_py": "Bié zháojí, fúwùtái huì bāng wǒmen zhǎodào xíngli de.", "ex_en": "Don't worry; the service desk will help us find the luggage."},
    {"chapter": 1, "hanzi": "帮助", "pinyin": "bāngzhù", "english": "to help; assistance", "pos": "v./n.", "ex_cn": "谢谢您的帮助！", "ex_py": "Xièxie nín de bāngzhù!", "ex_en": "Thank you for your assistance!"},
    {"chapter": 1, "hanzi": "发现", "pinyin": "fāxiàn", "english": "to discover, find out", "pos": "v.", "ex_cn": "到机场的时候，白家月发现行李箱不见了。", "ex_py": "Dào jīchǎng de shíhou, Bái Jiāyuè fāxiàn xínglixiāng bújiàn le.", "ex_en": "When arriving at the airport, Bai Jiayue discovered her suitcase was missing."},
    {"chapter": 1, "hanzi": "不见", "pinyin": "bújiàn", "english": "disappeared, missing", "pos": "v.", "ex_cn": "我的护照不见了，你看见了吗？", "ex_py": "Wǒ de hùzhào bújiàn le, nǐ kànjiàn le ma?", "ex_en": "My passport went missing, have you seen it?"},
    {"chapter": 1, "hanzi": "号码", "pinyin": "hàomǎ", "english": "number", "pos": "n.", "ex_cn": "箱子上面写着我的名字和电话号码。", "ex_py": "Xiāngzi shàngmian xiězhe wǒ de míngzi hé diànhuà hàomǎ.", "ex_en": "My name and phone number are written on the suitcase."},
    {"chapter": 1, "hanzi": "照片", "pinyin": "zhàopiàn", "english": "photo, picture", "pos": "n.", "ex_cn": "照片上的这个人是你男朋友吗？", "ex_py": "Zhàopiàn shang de zhè ge rén shì nǐ nánpéngyou ma?", "ex_en": "Is the person in this photo your boyfriend?"},

    # Lesson 2
    {"chapter": 2, "hanzi": "菜单", "pinyin": "càidān", "english": "menu", "pos": "n.", "ex_cn": "你们看看菜单，想吃什么就点什么。", "ex_py": "Nǐmen kànkan càidān, xiǎng chī shénme jiù diǎn shénme.", "ex_en": "Take a look at the menu and order whatever you feel like."},
    {"chapter": 2, "hanzi": "饿", "pinyin": "è", "english": "hungry", "pos": "adj.", "ex_cn": "我现在真是又饿又渴。", "ex_py": "Wǒ xiànzài zhēn shì yòu è yòu kě.", "ex_en": "I am truly both hungry and thirsty right now."},
    {"chapter": 2, "hanzi": "渴", "pinyin": "kě", "english": "thirsty", "pos": "adj.", "ex_cn": "跑完步以后口渴极了。", "ex_py": "Pǎo wán bù yǐhòu kǒukě jí le.", "ex_en": "After running, I was extremely thirsty."},
    {"chapter": 2, "hanzi": "又", "pinyin": "yòu", "english": "both... and... / again", "pos": "adv.", "ex_cn": "这个饭馆的菜又便宜又好吃。", "ex_py": "Zhè ge fànguǎn de cài yòu piányi yòu hǎochī.", "ex_en": "The food in this restaurant is both cheap and delicious."},
    {"chapter": 2, "hanzi": "鸡", "pinyin": "jī", "english": "chicken", "pos": "n.", "ex_cn": "那我们点一个鸡肉吧。", "ex_py": "Nà wǒmen diǎn yí ge jīròu ba.", "ex_en": "Then let's order a chicken dish."},
    {"chapter": 2, "hanzi": "尝", "pinyin": "cháng", "english": "to taste, try", "pos": "v.", "ex_cn": "你想尝尝地道的北京烤鸭吗？", "ex_py": "Nǐ xiǎng chángchang dìdao de Běijīng kǎoyā ma?", "ex_en": "Do you want to taste authentic Beijing roast duck?"},
    {"chapter": 2, "hanzi": "简单", "pinyin": "jiǎndān", "english": "simple, uncomplicated", "pos": "adj.", "ex_cn": "这个菜的做法非常简单。", "ex_py": "Zhè ge cài de zuòfǎ fēicháng jiǎndān.", "ex_en": "The recipe for this dish is very simple."},
    {"chapter": 2, "hanzi": "筷子", "pinyin": "kuàizi", "english": "chopsticks", "pos": "n.", "ex_cn": "你会用筷子吃饭吗？", "ex_py": "Nǐ huì yòng kuàizi chīfàn ma?", "ex_en": "Do you know how to eat with chopsticks?"},
    {"chapter": 2, "hanzi": "勺子", "pinyin": "sháozi", "english": "spoon", "pos": "n.", "ex_cn": "服务员，请给我们拿两个勺子。", "ex_py": "Fúwùyuán, qǐng gěi wǒmen ná liǎng ge sháozi.", "ex_en": "Waiter, please bring us two spoons."},
    {"chapter": 2, "hanzi": "碗", "pinyin": "wǎn", "english": "bowl", "pos": "n.", "ex_cn": "我吃了一碗面条。", "ex_py": "Wǒ chī le yì wǎn miàntiáo.", "ex_en": "I ate a bowl of noodles."},
    {"chapter": 2, "hanzi": "双", "pinyin": "shuāng", "english": "pair (measure word)", "pos": "m.", "ex_cn": "服务员，请再拿一双筷子。", "ex_py": "Fúwùyuán, qǐng zài ná yì shuāng kuàizi.", "ex_en": "Waiter, please bring another pair of chopsticks."},
    {"chapter": 2, "hanzi": "盘子", "pinyin": "pánzi", "english": "plate, dish", "pos": "n.", "ex_cn": "桌子上放着几个漂亮的盘子。", "ex_py": "Zhuōzi shang fàngzhe jǐ ge piàoliang de pánzi.", "ex_en": "Several pretty plates are placed on the table."},
    {"chapter": 2, "hanzi": "饮料", "pinyin": "yǐnliào", "english": "drink, beverage", "pos": "n.", "ex_cn": "你想喝什么饮料？", "ex_py": "Nǐ xiǎng hē shénme yǐnliào?", "ex_en": "What beverage would you like to drink?"},
    {"chapter": 2, "hanzi": "蛋糕", "pinyin": "dàngāo", "english": "cake", "pos": "n.", "ex_cn": "今天是他的生日，我们买了蛋糕。", "ex_py": "Jīntiān shì tā de shēngrì, wǒmen mǎi le dàngāo.", "ex_en": "Today is his birthday; we bought a cake."},
    {"chapter": 2, "hanzi": "外卖", "pinyin": "wàimài", "english": "takeout, delivery food", "pos": "n.", "ex_cn": "今天不想做饭，我们点外卖吧。", "ex_py": "Jīntiān bù xiǎng zuòfàn, wǒmen diǎn wàimài ba.", "ex_en": "I don't feel like cooking today; let's order takeout."},
    {"chapter": 2, "hanzi": "方便面", "pinyin": "fāngbiànmiàn", "english": "instant noodles", "pos": "n.", "ex_cn": "偶尔吃一次方便面挺方便的。", "ex_py": "Ǒu'ěr chī yí cì fāngbiànmiàn tǐng fāngbiàn de.", "ex_en": "Eating instant noodles once in a while is pretty convenient."},
    {"chapter": 2, "hanzi": "方便", "pinyin": "fāngbiàn", "english": "convenient", "pos": "adj.", "ex_cn": "坐地铁去学校非常方便。", "ex_py": "Zuò dìtiě qù xuéxiào fēicháng fāngbiàn.", "ex_en": "Taking the subway to school is very convenient."},
    {"chapter": 2, "hanzi": "服务", "pinyin": "fúwù", "english": "service; to serve", "pos": "v./n.", "ex_cn": "这家饭馆的服务态度很热情。", "ex_py": "Zhè jiā fànguǎn de fúwù tàidu hěn rèqíng.", "ex_en": "The service attitude at this restaurant is very warm."},
    {"chapter": 2, "hanzi": "热情", "pinyin": "rèqíng", "english": "warm, enthusiastic", "pos": "adj.", "ex_cn": "中国人对客人非常热情。", "ex_py": "Zhōngguórén duì kèrén fēicháng rèqíng.", "ex_en": "Chinese people are very hospitable towards guests."},
    {"chapter": 2, "hanzi": "选", "pinyin": "xuǎn", "english": "to choose, select", "pos": "v.", "ex_cn": "菜单上菜太多了，你帮我选一个吧。", "ex_py": "Càidān shang cài tài duō le, nǐ bāng wǒ xuǎn yí ge ba.", "ex_en": "There are too many dishes on the menu; help me pick one."},
    {"chapter": 2, "hanzi": "记", "pinyin": "jì", "english": "to remember, note down", "pos": "v.", "ex_cn": "服务员把我们点的菜都记下来了。", "ex_py": "Fúwùyuán bǎ wǒmen diǎn de cài dōu jì xiàlái le.", "ex_en": "The waiter noted down all the dishes we ordered."},
    {"chapter": 2, "hanzi": "马上", "pinyin": "mǎshàng", "english": "immediately, right away", "pos": "adv.", "ex_cn": "菜马上就做好，请稍等。", "ex_py": "Cài mǎshàng jiù zuò hǎo, qǐng shāoděng.", "ex_en": "The food will be ready right away; please wait a moment."},
    {"chapter": 2, "hanzi": "不用", "pinyin": "búyòng", "english": "need not, no need", "pos": "adv.", "ex_cn": "不用客气，大家随便吃。", "ex_py": "Búyòng kèqi, dàjiā suíbiàn chī.", "ex_en": "No need to be polite, everyone help yourselves."},
    {"chapter": 2, "hanzi": "好久", "pinyin": "hǎojiǔ", "english": "a long time", "pos": "adv.", "ex_cn": "好久不见，最近怎么样？", "ex_py": "Hǎojiǔ bújiàn, zuìjìn zěnmeyàng?", "ex_en": "Long time no see, how have you been lately?"},
    {"chapter": 2, "hanzi": "只", "pinyin": "zhǐ", "english": "only, just / measure word for animals", "pos": "adv./m.", "ex_cn": "我今天只点了一盘菜。", "ex_py": "Wǒ jīntiān zhǐ diǎn le yì pán cài.", "ex_en": "I only ordered one dish today."},

    # Lesson 3
    {"chapter": 3, "hanzi": "小区", "pinyin": "xiǎoqū", "english": "residential community, neighborhood", "pos": "n.", "ex_cn": "这个小区挺好的，环境很安静。", "ex_py": "Zhè ge xiǎoqū tǐng hǎo de, huánjìng hěn ānjìng.", "ex_en": "This neighborhood is pretty good, the surroundings are very quiet."},
    {"chapter": 3, "hanzi": "挺", "pinyin": "tǐng", "english": "quite, pretty, very", "pos": "adv.", "ex_cn": "这里的房子挺大的。", "ex_py": "Zhèlǐ de fángzi tǐng dà de.", "ex_en": "The apartments here are quite spacious."},
    {"chapter": 3, "hanzi": "环境", "pinyin": "huánjìng", "english": "environment, surroundings", "pos": "n.", "ex_cn": "学校周围的环境很不错。", "ex_py": "Xuéxiào zhōuwéi de huánjìng hěn búcuò.", "ex_en": "The surroundings around the school are quite nice."},
    {"chapter": 3, "hanzi": "房子", "pinyin": "fángzi", "english": "house, apartment", "pos": "n.", "ex_cn": "你想租什么样的房子？", "ex_py": "Nǐ xiǎng zū shénmeyàng de fángzi?", "ex_en": "What kind of apartment do you want to rent?"},
    {"chapter": 3, "hanzi": "搬家", "pinyin": "bānjiā", "english": "to move house", "pos": "v.", "ex_cn": "下个月我打算搬家。", "ex_py": "Xià ge yuè wǒ dǎsuàn bānjiā.", "ex_en": "I plan to move house next month."},
    {"chapter": 3, "hanzi": "层", "pinyin": "céng", "english": "floor, story, layer", "pos": "m.", "ex_cn": "我住在五层，有电梯。", "ex_py": "Wǒ zhù zài wǔ céng, yǒu diàntī.", "ex_en": "I live on the 5th floor; there is an elevator."},
    {"chapter": 3, "hanzi": "打扫", "pinyin": "dǎsǎo", "english": "to clean, sweep", "pos": "v.", "ex_cn": "我们周末把房间打扫打扫吧。", "ex_py": "Wǒmen zhōumò bǎ fángjiān dǎsǎo dǎsǎo ba.", "ex_en": "Let's clean the room this weekend."},
    {"chapter": 3, "hanzi": "冰箱", "pinyin": "bīngxiāng", "english": "refrigerator", "pos": "n.", "ex_cn": "冰箱里有水果和饮料。", "ex_py": "Bīngxiāng lǐ yǒu shuǐguǒ hé yǐnliào.", "ex_en": "There are fruits and drinks in the refrigerator."},
    {"chapter": 3, "hanzi": "洗衣机", "pinyin": "xǐyījī", "english": "washing machine", "pos": "n.", "ex_cn": "这个房子的洗衣机是新买的。", "ex_py": "Zhè ge fángzi de xǐyījī shì xīn mǎi de.", "ex_en": "The washing machine in this apartment is newly bought."},
    {"chapter": 3, "hanzi": "空调", "pinyin": "kōngtiáo", "english": "air conditioner", "pos": "n.", "ex_cn": "夏天屋里必须开空调。", "ex_py": "Xiàtiān wū lǐ bìxū kāi kōngtiáo.", "ex_en": "In summer, the air conditioner must be turned on inside."},
    {"chapter": 3, "hanzi": "卫生间", "pinyin": "wèishēngjiān", "english": "bathroom, toilet", "pos": "n.", "ex_cn": "主卧里面有一个独立的卫生间。", "ex_py": "Zhǔwò lǐmiàn yǒu yí ge dúlì de wèishēngjiān.", "ex_en": "The master bedroom has an en-suite bathroom."},
    {"chapter": 3, "hanzi": "花园", "pinyin": "huāyuán", "english": "garden", "pos": "n.", "ex_cn": "小区中间有一个漂亮的花园。", "ex_py": "Xiǎoqū zhōngjiān yǒu yí ge piàoliang de huāyuán.", "ex_en": "There is a beautiful garden in the center of the neighborhood."},
    {"chapter": 3, "hanzi": "灯", "pinyin": "dēng", "english": "lamp, light", "pos": "n.", "ex_cn": "出门的时候别忘了关灯。", "ex_py": "Chūmén de shíhou bié wàng le guān dēng.", "ex_en": "Don't forget to turn off the lights when you go out."},
    {"chapter": 3, "hanzi": "关", "pinyin": "guān", "english": "to close, turn off", "pos": "v.", "ex_cn": "把窗户关上吧，外面很冷。", "ex_py": "Bǎ chuānghu guān shang ba, wàimian hěn lěng.", "ex_en": "Close the window; it's very cold outside."},
    {"chapter": 3, "hanzi": "银行", "pinyin": "yínháng", "english": "bank", "pos": "n.", "ex_cn": "小区门口就有一家中国银行。", "ex_py": "Xiǎoqū ménkǒu jiù yǒu yì jiā Zhōngguó Yínháng.", "ex_en": "There is a Bank of China right at the entrance of the community."},
    {"chapter": 3, "hanzi": "信用卡", "pinyin": "xìnyòngkǎ", "english": "credit card", "pos": "n.", "ex_cn": "这里可以刷信用卡吗？", "ex_py": "Zhèlǐ kěyǐ shuā xìnyòngkǎ ma?", "ex_en": "Can I swipe a credit card here?"},
    {"chapter": 3, "hanzi": "办", "pinyin": "bàn", "english": "to handle, manage, do", "pos": "v.", "ex_cn": "我想去银行办一张银行卡。", "ex_py": "Wǒ xiǎng qù yínháng bàn yì zhāng yínhángkǎ.", "ex_en": "I want to go to the bank to apply for a bank card."},
    {"chapter": 3, "hanzi": "换", "pinyin": "huàn", "english": "to change, exchange", "pos": "v.", "ex_cn": "我想换一间朝南的房间。", "ex_py": "Wǒ xiǎng huàn yì jiān cháonán de fángjiān.", "ex_en": "I'd like to change to a south-facing room."},
    {"chapter": 3, "hanzi": "还", "pinyin": "huán", "english": "to return (something borrowed)", "pos": "v.", "ex_cn": "看完以后记得把书还给我。", "ex_py": "Kàn wán yǐhòu jìde bǎ shū huán gěi wǒ.", "ex_en": "Remember to return the book to me after reading it."},
    {"chapter": 3, "hanzi": "听说", "pinyin": "tīngshuō", "english": "to hear of, be told", "pos": "v.", "ex_cn": "听说这附近的交通很方便。", "ex_py": "Tīngshuō zhè fùjìn de jiāotōng hěn fāngbiàn.", "ex_en": "I heard that the transportation near here is very convenient."},
    {"chapter": 3, "hanzi": "咱们", "pinyin": "zánmen", "english": "we, us (inclusive)", "pos": "pron.", "ex_cn": "咱们先去看房子，再去吃饭。", "ex_py": "Zánmen xiān qù kàn fángzi, zài qù chīfàn.", "ex_en": "Let's go look at the apartment first, then eat."},
    {"chapter": 3, "hanzi": "需要", "pinyin": "xūyào", "english": "to need, require", "pos": "v./n.", "ex_cn": "你还需要买什么家具吗？", "ex_py": "Nǐ hái xūyào mǎi shénme jiājù ma?", "ex_en": "Do you still need to buy any furniture?"},

    # Lesson 4
    {"chapter": 4, "hanzi": "借", "pinyin": "jiè", "english": "to borrow, lend", "pos": "v.", "ex_cn": "我的照相机借给你用吧。", "ex_py": "Wǒ de zhàoxiàngjī jiè gěi nǐ yòng ba.", "ex_en": "I'll lend my camera to you to use."},
    {"chapter": 4, "hanzi": "相机", "pinyin": "xiàngjī", "english": "camera", "pos": "n.", "ex_cn": "去旅游一定要带照相机。", "ex_py": "Qù lǚyóu yídìng yào dài zhàoxiàngjī.", "ex_en": "When traveling, you must bring a camera."},
    {"chapter": 4, "hanzi": "一样", "pinyin": "yíyàng", "english": "the same, alike", "pos": "adj.", "ex_cn": "他的想法跟我一样。", "ex_py": "Tā de xiǎngfǎ gēn wǒ yíyàng.", "ex_en": "His thoughts are the same as mine."},
    {"chapter": 4, "hanzi": "除了", "pinyin": "chúle", "english": "except, besides", "pos": "prep.", "ex_cn": "除了英语以外，他还会说中文。", "ex_py": "Chúle Yīngyǔ yǐwài, tā hái huì shuō Zhōngwén.", "ex_en": "Besides English, he can also speak Chinese."},
    {"chapter": 4, "hanzi": "以外", "pinyin": "yǐwài", "english": "beyond, except", "pos": "postp.", "ex_cn": "除了周日以外，图书馆每天都开门。", "ex_py": "Chúle Zhōurì yǐwài, túshūguǎn měitiān dōu kāimén.", "ex_en": "Except for Sunday, the library is open every day."},
    {"chapter": 4, "hanzi": "一直", "pinyin": "yìzhí", "english": "all along, continuously", "pos": "adv.", "ex_cn": "我一直想去内蒙古看大草原。", "ex_py": "Wǒ yìzhí xiǎng qù Nèiměnggǔ kàn dà cǎoyuán.", "ex_en": "I have always wanted to go to Inner Mongolia to see the grasslands."},
    {"chapter": 4, "hanzi": "草原", "pinyin": "cǎoyuán", "english": "grassland, prairie", "pos": "n.", "ex_cn": "草原上的风景美丽极了。", "ex_py": "Cǎoyuán shang de fēngjǐng měilì jí le.", "ex_en": "The scenery on the grassland is exceedingly beautiful."},
    {"chapter": 4, "hanzi": "马", "pinyin": "mǎ", "english": "horse", "pos": "n.", "ex_cn": "在草原上你可以学会骑马。", "ex_py": "Zài cǎoyuán shang nǐ kěyǐ xuéhuì qímǎ.", "ex_en": "On the grassland, you can learn to ride horses."},
    {"chapter": 4, "hanzi": "骑", "pinyin": "qí", "english": "to ride (horse, bike)", "pos": "v.", "ex_cn": "你敢骑大马吗？", "ex_py": "Nǐ gǎn qí dàmǎ ma?", "ex_en": "Do you dare to ride a big horse?"},
    {"chapter": 4, "hanzi": "牛", "pinyin": "niú", "english": "cow, ox, cattle", "pos": "n.", "ex_cn": "草地上有很多牛和羊。", "ex_py": "Cǎodì shang yǒu hěn duō niú hé yáng.", "ex_en": "There are many cattle and sheep on the meadow."},
    {"chapter": 4, "hanzi": "羊", "pinyin": "yáng", "english": "sheep, goat", "pos": "n.", "ex_cn": "内蒙古的烤全羊很有名。", "ex_py": "Nèiměnggǔ de kǎoquányáng hěn yǒumíng.", "ex_en": "Inner Mongolia's roasted whole lamb is very famous."},
    {"chapter": 4, "hanzi": "假期", "pinyin": "jiàqī", "english": "vacation, holiday", "pos": "n.", "ex_cn": "这个假期你有什么计划？", "ex_py": "Zhè ge jiàqī nǐ yǒu shénme jìhuà?", "ex_en": "What plans do you have for this vacation?"},
    {"chapter": 4, "hanzi": "宾馆", "pinyin": "bīnguǎn", "english": "hotel, guesthouse", "pos": "n.", "ex_cn": "我们已经在网上订好了宾馆。", "ex_py": "Wǒmen yǐjīng zài wǎngshang dìng hǎo le bīnguǎn.", "ex_en": "We have already booked the hotel online."},
    {"chapter": 4, "hanzi": "起飞", "pinyin": "qǐfēi", "english": "to take off (flight)", "pos": "v.", "ex_cn": "飞机准时起飞了。", "ex_py": "Fēijī zhǔnshí qǐfēi le.", "ex_en": "The plane took off on schedule."},
    {"chapter": 4, "hanzi": "司机", "pinyin": "sījī", "english": "driver", "pos": "n.", "ex_cn": "出租车司机的服务态度很好。", "ex_py": "Chūzūchē sījī de fúwù tàidu hěn hǎo.", "ex_en": "The taxi driver's service attitude was very good."},
    {"chapter": 4, "hanzi": "特别", "pinyin": "tèbié", "english": "especially, special", "pos": "adv./adj.", "ex_cn": "这里的羊肉特别好吃。", "ex_py": "Zhèlǐ de yángròu tèbié hǎochī.", "ex_en": "The mutton here is especially delicious."},
    {"chapter": 4, "hanzi": "月亮", "pinyin": "yuèliang", "english": "moon", "pos": "n.", "ex_cn": "今晚的月亮又大又圆。", "ex_py": "Jīnwǎn de yuèliang yòu dà yòu yuán.", "ex_en": "Tonight's moon is both large and round."},
    {"chapter": 4, "hanzi": "主意", "pinyin": "zhǔyi", "english": "idea, suggestion", "pos": "n.", "ex_cn": "这是一个不错的主意！", "ex_py": "Zhè shì yí ge búcuò de zhǔyi!", "ex_en": "This is a great idea!"},
    {"chapter": 4, "hanzi": "满意", "pinyin": "mǎnyì", "english": "satisfied, pleased", "pos": "adj.", "ex_cn": "我们对这次旅行非常满意。", "ex_py": "Wǒmen duì zhè cì lǚxíng fēicháng mǎnyì.", "ex_en": "We are very satisfied with this trip."},
    {"chapter": 4, "hanzi": "干净", "pinyin": "gānjìng", "english": "clean, neat", "pos": "adj.", "ex_cn": "房间打扫得非常干净。", "ex_py": "Fángjiān dǎsǎo de fēicháng gānjìng.", "ex_en": "The room was cleaned very neatly."},

    # Lesson 5
    {"chapter": 5, "hanzi": "拍照", "pinyin": "pāizhào", "english": "to take photos", "pos": "v.", "ex_cn": "登上山顶以后，大家都在拍照。", "ex_py": "Dēngshàng shāndǐng yǐhòu, dàjiā dōu zài pāizhào.", "ex_en": "After reaching the mountaintop, everyone was taking photos."},
    {"chapter": 5, "hanzi": "山", "pinyin": "shān", "english": "mountain, hill", "pos": "n.", "ex_cn": "爬山是一项很好的锻炼。", "ex_py": "Páshān shì yí xiàng hěn hǎo de duànliàn.", "ex_en": "Mountain climbing is a great exercise."},
    {"chapter": 5, "hanzi": "爬", "pinyin": "pá", "english": "to climb, crawl", "pos": "v.", "ex_cn": "虽然很累，但我们终于爬到了山顶。", "ex_py": "Suīrán hěn lèi, dàn wǒmen zhōngyú pá dào le shāndǐng.", "ex_en": "Although tired, we finally climbed to the peak."},
    {"chapter": 5, "hanzi": "终于", "pinyin": "zhōngyú", "english": "finally, at last", "pos": "adv.", "ex_cn": "经过努力，他终于通过了考试。", "ex_py": "Jīngguò nǔlì, tā zhōngyú tōngguò le kǎoshì.", "ex_en": "Through hard work, he finally passed the test."},
    {"chapter": 5, "hanzi": "才", "pinyin": "cái", "english": "only then, just", "pos": "adv.", "ex_cn": "站在这儿拍照才好看呢！", "ex_py": "Zhàn zài zhèr pāizhào cái hǎokàn ne!", "ex_en": "Only by standing right here will the photo look good!"},
    {"chapter": 5, "hanzi": "感兴趣", "pinyin": "gǎn xìngqù", "english": "to be interested in", "pos": "v.", "ex_cn": "我对中国书法非常感兴趣。", "ex_py": "Wǒ duì Zhōngguó shūfǎ fēicháng gǎn xìngqù.", "ex_en": "I am extremely interested in Chinese calligraphy."},
    {"chapter": 5, "hanzi": "水平", "pinyin": "shuǐpíng", "english": "level, proficiency", "pos": "n.", "ex_cn": "他的汉语水平提高得很快。", "ex_py": "Tā de Hànyǔ shuǐpíng tígāo de hěn kuài.", "ex_en": "His Chinese proficiency has improved very rapidly."},
    {"chapter": 5, "hanzi": "太阳", "pinyin": "tàiyáng", "english": "sun", "pos": "n.", "ex_cn": "今天的太阳很大，记得防晒。", "ex_py": "Jīntiān de tàiyáng hěn dà, jìde fángshài.", "ex_en": "The sun is very strong today, remember sun protection."},
    {"chapter": 5, "hanzi": "树", "pinyin": "shù", "english": "tree", "pos": "n.", "ex_cn": "山上有许多高大的树。", "ex_py": "Shān shang yǒu xǔduō gāodà de shù.", "ex_en": "There are many tall trees on the mountain."},
    {"chapter": 5, "hanzi": "难看", "pinyin": "nánkàn", "english": "ugly, bad-looking", "pos": "adj.", "ex_cn": "逆光拍照会很难看。", "ex_py": "Nìguāng pāizhào huì hěn nánkàn.", "ex_en": "Taking photos against the light will look bad."},
    {"chapter": 5, "hanzi": "难过", "pinyin": "nánguò", "english": "sad, sorrowful", "pos": "adj.", "ex_cn": "比赛输了，大家都很难过。", "ex_py": "Bǐsài shū le, dàjiā dōu hěn nánguò.", "ex_en": "Having lost the match, everyone felt very sad."},
    {"chapter": 5, "hanzi": "锻炼", "pinyin": "duànliàn", "english": "to exercise, train", "pos": "v.", "ex_cn": "他每天早上坚持锻炼身体。", "ex_py": "Tā měitiān zǎoshang jiānchí duànliàn shēntǐ.", "ex_en": "He insists on exercising every morning."},
    {"chapter": 5, "hanzi": "总是", "pinyin": "zǒngshì", "english": "always", "pos": "adv.", "ex_cn": "周末他总是去图书馆看书。", "ex_py": "Zhōumò tā zǒngshì qù túshūguǎn kànshū.", "ex_en": "On weekends he always goes to the library to read."},
    {"chapter": 5, "hanzi": "音乐", "pinyin": "yīnyuè", "english": "music", "pos": "n.", "ex_cn": "我喜欢边散步边听音乐。", "ex_py": "Wǒ xǐhuan biān sànbù biān tīng yīnyuè.", "ex_en": "I like listening to music while taking a walk."},
    {"chapter": 5, "hanzi": "结束", "pinyin": "jiéshù", "english": "to finish, end", "pos": "v.", "ex_cn": "会议五点钟准时结束。", "ex_py": "Huìyì wǔ diǎn zhōng zhǔnshí jiéshù.", "ex_en": "The meeting ended punctually at five o'clock."},
    {"chapter": 5, "hanzi": "收到", "pinyin": "shōudào", "english": "to receive", "pos": "v.", "ex_cn": "我昨天收到了朋友寄来的明信片。", "ex_py": "Wǒ zuótiān shōudào le péngyou jì lái de míngxìnpiàn.", "ex_en": "Yesterday I received a postcard sent by my friend."},

    # Lesson 6
    {"chapter": 6, "hanzi": "高铁", "pinyin": "gāotiě", "english": "high-speed train", "pos": "n.", "ex_cn": "坐高铁从北京到上海只要四个多小时。", "ex_py": "Zuò gāotiě cóng Běijīng dào Shànghǎi zhǐ yào sì ge duō xiǎoshí.", "ex_en": "Taking the bullet train from Beijing to Shanghai takes just over four hours."},
    {"chapter": 6, "hanzi": "该", "pinyin": "gāi", "english": "should, ought to / time to", "pos": "v./aux.", "ex_cn": "时间不早了，该上车了。", "ex_py": "Shíjiān bù zǎo le, gāi shàngchē le.", "ex_en": "It's getting late; it's time to board the train."},
    {"chapter": 6, "hanzi": "如果", "pinyin": "rúguǒ", "english": "if, in case", "pos": "conj.", "ex_cn": "如果路上堵车，我们就坐地铁去。", "ex_py": "Rúguǒ lùshang dǔchē, wǒmen jiù zuò dìtiě qù.", "ex_en": "If there is a traffic jam on the road, we'll take the subway."},
    {"chapter": 6, "hanzi": "越", "pinyin": "yuè", "english": "the more... (越...越...)", "pos": "adv.", "ex_cn": "高铁的速度越来越快了。", "ex_py": "Gāotiě de sùdù yuè lái yuè kuài le.", "ex_en": "The speed of bullet trains is getting faster and faster."},
    {"chapter": 6, "hanzi": "充电宝", "pinyin": "chōngdiànbǎo", "english": "power bank, portable charger", "pos": "n.", "ex_cn": "手机快没电了，你带充电宝了吗？", "ex_py": "Shǒujī kuài méi diàn le, nǐ dài chōngdiànbǎo le ma?", "ex_en": "My phone battery is nearly dead; did you bring a power bank?"},
    {"chapter": 6, "hanzi": "迟到", "pinyin": "chídào", "english": "to arrive late", "pos": "v.", "ex_cn": "今天早上差点儿迟到了。", "ex_py": "Jīntiān zǎoshang chàdiǎnr chídào le.", "ex_en": "I was almost late this morning."},
    {"chapter": 6, "hanzi": "耳机", "pinyin": "ěrjī", "english": "headphones, earphones", "pos": "n.", "ex_cn": "在车厢里听音乐最好戴上耳机。", "ex_py": "Zài chēxiāng lǐ tīng yīnyuè zuìhǎo dài shang ěrjī.", "ex_en": "When listening to music in the carriage, it's best to put on earphones."},
    {"chapter": 6, "hanzi": "检票", "pinyin": "jiǎnpiào", "english": "to check tickets", "pos": "v.", "ex_cn": "列车现在开始检票了。", "ex_py": "Lièchē xiànzài kāishǐ jiǎnpiào le.", "ex_en": "The train is now starting ticket inspection."},
    {"chapter": 6, "hanzi": "检查", "pinyin": "jiǎnchá", "english": "to check, inspect", "pos": "v.", "ex_cn": "出门前请仔细检查身份证和车票。", "ex_py": "Chūmén qián qǐng zǐxì jiǎnchá shēnfènzhèng hé chēpiào.", "ex_en": "Before going out, please carefully check your ID and train ticket."},
    {"chapter": 6, "hanzi": "电梯", "pinyin": "diàntī", "english": "elevator, escalator", "pos": "n.", "ex_cn": "坐电梯直接上二楼检票口。", "ex_py": "Zuò diàntī zhíjiē shàng èr lóu jiǎnpiàokǒu.", "ex_en": "Take the elevator straight up to the second floor ticket gate."},
    {"chapter": 6, "hanzi": "红绿灯", "pinyin": "hóng-lǜdēng", "english": "traffic light", "pos": "n.", "ex_cn": "过马路一定要看红绿灯。", "ex_py": "Guò mǎlù yídìng yào kàn hóng-lǜdēng.", "ex_en": "When crossing the road, you must watch the traffic lights."},
    {"chapter": 6, "hanzi": "路口", "pinyin": "lùkǒu", "english": "intersection, crossroad", "pos": "n.", "ex_cn": "在前面的十字路口向右拐。", "ex_py": "Zài qiánmian de shízì lùkǒu xiàng yòu guǎi.", "ex_en": "Turn right at the intersection ahead."},
    {"chapter": 6, "hanzi": "小心", "pinyin": "xiǎoxīn", "english": "careful; watch out", "pos": "adj./v.", "ex_cn": "路上有水，小心滑倒。", "ex_py": "Lùshang yǒu shuǐ, xiǎoxīn huádǎo.", "ex_en": "There is water on the road; be careful not to slip."},
    {"chapter": 6, "hanzi": "必须", "pinyin": "bìxū", "english": "must, have to", "pos": "adv.", "ex_cn": "进站前必须通过安全检查。", "ex_py": "Jìn zhàn qián bìxū tōngguò ānquán jiǎnchá.", "ex_en": "Before entering the station, you must pass security check."},
    {"chapter": 6, "hanzi": "放假", "pinyin": "fàngjià", "english": "to have a holiday, vacation", "pos": "v.", "ex_cn": "国庆节学校放假七天。", "ex_py": "Guóqìngjié xuéxiào fàngjià qī tiān.", "ex_en": "The school has a 7-day vacation for National Day."},

    # Lesson 7
    {"chapter": 7, "hanzi": "裙子", "pinyin": "qúnzi", "english": "skirt, dress", "pos": "n.", "ex_cn": "那条裙子比短裤更好看。", "ex_py": "Nà tiáo qúnzi bǐ duǎnkù gèng hǎokàn.", "ex_en": "That skirt looks better than the shorts."},
    {"chapter": 7, "hanzi": "短裤", "pinyin": "duǎnkù", "english": "shorts", "pos": "n.", "ex_cn": "夏天穿短裤比较凉快。", "ex_py": "Xiàtiān chuān duǎnkù bǐjiào liángkuai.", "ex_en": "Wearing shorts in summer is quite cool."},
    {"chapter": 7, "hanzi": "更", "pinyin": "gèng", "english": "even more, furthermore", "pos": "adv.", "ex_cn": "这件衣服的颜色更适合你。", "ex_py": "Zhè jiàn yīfu de yánsè gèng shìhé nǐ.", "ex_en": "The color of this piece suits you even more."},
    {"chapter": 7, "hanzi": "不但", "pinyin": "búdàn", "english": "not only", "pos": "conj.", "ex_cn": "这件衣服不但好看，而且很舒服。", "ex_py": "Zhè jiàn yīfu búdàn hǎokàn, érqiě hěn shūfu.", "ex_en": "This piece of clothing is not only nice-looking, but also comfortable."},
    {"chapter": 7, "hanzi": "而且", "pinyin": "érqiě", "english": "and also, furthermore", "pos": "conj.", "ex_cn": "他不但会打网球，而且打得很好。", "ex_py": "Tā búdàn huì dǎ wǎngqiú, érqiě dǎ de hěn hǎo.", "ex_en": "Not only can he play tennis, but he plays very well."},
    {"chapter": 7, "hanzi": "合适", "pinyin": "héshì", "english": "suitable, fitting", "pos": "adj.", "ex_cn": "这条裤子的大小刚刚合适。", "ex_py": "Zhè tiáo kùzi de dàxiǎo gānggāng héshì.", "ex_en": "The size of these trousers is just right."},
    {"chapter": 7, "hanzi": "试", "pinyin": "shì", "english": "to try, try on", "pos": "v.", "ex_cn": "我可以试一下这件大衣吗？", "ex_py": "Wǒ kěyǐ shì yíxià zhè jiàn dàyī ma?", "ex_en": "May I try on this overcoat?"},
    {"chapter": 7, "hanzi": "大小", "pinyin": "dàxiǎo", "english": "size", "pos": "n.", "ex_cn": "这双鞋的大小正合适。", "ex_py": "Zhè shuāng xié de dàxiǎo zhèng héshì.", "ex_en": "The size of this pair of shoes fits perfectly."},
    {"chapter": 7, "hanzi": "新鲜", "pinyin": "xīnxiān", "english": "fresh", "pos": "adj.", "ex_cn": "超市里的西瓜非常新鲜。", "ex_py": "Chāoshì lǐ de xīguā fēicháng xīnxiān.", "ex_en": "The watermelons in the supermarket are very fresh."},
    {"chapter": 7, "hanzi": "甜", "pinyin": "tián", "english": "sweet", "pos": "adj.", "ex_cn": "这个西瓜真甜！", "ex_py": "Zhè ge xīguā zhēn tián!", "ex_en": "This watermelon is really sweet!"},
    {"chapter": 7, "hanzi": "西瓜", "pinyin": "xīguā", "english": "watermelon", "pos": "n.", "ex_cn": "夏天吃西瓜特别解渴。", "ex_py": "Xiàtiān chī xīguā tèbié jiěkě.", "ex_en": "Eating watermelon in summer quenches thirst remarkably well."},
    {"chapter": 7, "hanzi": "香蕉", "pinyin": "xiāngjiāo", "english": "banana", "pos": "n.", "ex_cn": "我买了两斤香蕉。", "ex_py": "Wǒ mǎi le liǎng jīn xiāngjiāo.", "ex_en": "I bought two jin (1 kg) of bananas."},
    {"chapter": 7, "hanzi": "公斤", "pinyin": "gōngjīn", "english": "kilogram", "pos": "m.", "ex_cn": "请给我称一公斤苹果。", "ex_py": "Qǐng gěi wǒ chēng yì gōngjīn píngguǒ.", "ex_en": "Please weigh one kilogram of apples for me."},
    {"chapter": 7, "hanzi": "极", "pinyin": "jí", "english": "extremely (...极了)", "pos": "adv.", "ex_cn": "这里的风景漂亮极了。", "ex_py": "Zhèlǐ de fēngjǐng piàoliang jí le.", "ex_en": "The scenery here is gorgeous beyond compare."},
    {"chapter": 7, "hanzi": "决定", "pinyin": "juédìng", "english": "to decide; decision", "pos": "v./n.", "ex_cn": "我决定买这件红色的毛衣。", "ex_py": "Wǒ juédìng mǎi zhè jiàn hóngsè de máoyī.", "ex_en": "I've decided to buy this red sweater."},

    # Lesson 8
    {"chapter": 8, "hanzi": "出院", "pinyin": "chūyuàn", "english": "to be discharged from hospital", "pos": "v.", "ex_cn": "医生说他明天就可以出院了。", "ex_py": "Yīshēng shuō tā míngtiān jiù kěyǐ chūyuàn le.", "ex_en": "The doctor said he can be discharged tomorrow."},
    {"chapter": 8, "hanzi": "发烧", "pinyin": "fāshāo", "english": "to have a fever", "pos": "v.", "ex_cn": "昨天晚上孩子突然发烧了。", "ex_py": "Zuótiān wǎnshang háizi tūrán fāshāo le.", "ex_en": "Last night the child suddenly had a fever."},
    {"chapter": 8, "hanzi": "感冒", "pinyin": "gǎnmào", "english": "to catch a cold; common cold", "pos": "v./n.", "ex_cn": "天气变化快，小心感冒。", "ex_py": "Tiānqì biànhuà kuài, xiǎoxīn gǎnmào.", "ex_en": "The weather changes quickly; be careful not to catch a cold."},
    {"chapter": 8, "hanzi": "担心", "pinyin": "dānxīn", "english": "to worry, feel anxious", "pos": "v.", "ex_cn": "别担心，医生检查后说没什么大问题。", "ex_py": "Bié dānxīn, yīshēng jiǎnchá hòu shuō méi shénme dà wèntí.", "ex_en": "Don't worry; after checking, the doctor said it's nothing serious."},
    {"chapter": 8, "hanzi": "健康", "pinyin": "jiànkāng", "english": "healthy; health", "pos": "adj./n.", "ex_cn": "多运动对身体健康很有好处。", "ex_py": "Duō yùndòng duì shēntǐ jiànkāng hěn yǒu hǎochu.", "ex_en": "Exercising more is very beneficial to one's health."},
    {"chapter": 8, "hanzi": "习惯", "pinyin": "xíguàn", "english": "habit; to be used to", "pos": "n./v.", "ex_cn": "早睡早起是一个好习惯。", "ex_py": "Zǎo shuì zǎo qǐ shì yí ge hǎo xíguàn.", "ex_en": "Going to bed early and rising early is a good habit."},
    {"chapter": 8, "hanzi": "得", "pinyin": "děi", "english": "must, have to", "pos": "aux.", "ex_cn": "你感冒了，得按时吃药。", "ex_py": "Nǐ gǎnmào le, děi ànshí chīyào.", "ex_en": "You have a cold; you must take your medicine on time."},
    {"chapter": 8, "hanzi": "腿", "pinyin": "tuǐ", "english": "leg", "pos": "n.", "ex_cn": "跑步跑多了，腿有点儿疼。", "ex_py": "Pǎobù pǎo duō le, tuǐ yǒudiǎnr téng.", "ex_en": "Having run a lot, my legs ache a little."},
    {"chapter": 8, "hanzi": "耳朵", "pinyin": "ěrduo", "english": "ear", "pos": "n.", "ex_cn": "大象有一对大大的耳朵。", "ex_py": "Dàxiàng yǒu yí duì dàdà de ěrduo.", "ex_en": "An elephant has a pair of large ears."},
    {"chapter": 8, "hanzi": "关心", "pinyin": "guānxīn", "english": "to care for, show concern", "pos": "v.", "ex_cn": "老师非常关心同学们的学习和生活。", "ex_py": "Lǎoshī fēicháng guānxīn tóngxuémen de xuéxí hé shēnghuó.", "ex_en": "The teacher cares deeply about the students' studies and daily lives."},
    {"chapter": 8, "hanzi": "突然", "pinyin": "tūrán", "english": "sudden, unexpected", "pos": "adj./adv.", "ex_cn": "刚才天还晴着，突然下起雨来。", "ex_py": "Gāngcái tiān hái qíngzhe, tūrán xià qǐ yǔ lái.", "ex_en": "Just now the sky was clear, and suddenly it started raining."},
    {"chapter": 8, "hanzi": "最近", "pinyin": "zuìjìn", "english": "recently, lately", "pos": "adv.", "ex_cn": "你最近身体恢复得怎么样？", "ex_py": "Nǐ zuìjìn shēntǐ huīfù de zěnmeyàng?", "ex_en": "How has your health recovery been going lately?"},

    # Lesson 9
    {"chapter": 9, "hanzi": "比赛", "pinyin": "bǐsài", "english": "match, competition; to compete", "pos": "n./v.", "ex_cn": "今天的网球比赛非常精彩。", "ex_py": "Jīntiān de wǎngqiú bǐsài fēicháng jīngcǎi.", "ex_en": "Today's tennis match was extremely exciting."},
    {"chapter": 9, "hanzi": "网球", "pinyin": "wǎngqiú", "english": "tennis", "pos": "n.", "ex_cn": "打不好没关系，多练习就会了。", "ex_py": "Dǎ bù hǎo méiguānxi, duō liànxí jiù huì le.", "ex_en": "It doesn't matter if you can't play well; with more practice you will get it."},
    {"chapter": 9, "hanzi": "为了", "pinyin": "wèile", "english": "in order to, for the sake of", "pos": "prep.", "ex_cn": "为了准备这次比赛，他每天训练三小时。", "ex_py": "Wèile zhǔnbèi zhè cì bǐsài, tā měitiān xùnliàn sān xiǎoshí.", "ex_en": "In order to prepare for this tournament, he trains three hours every day."},
    {"chapter": 9, "hanzi": "参加", "pinyin": "cānjiā", "english": "to attend, participate in", "pos": "v.", "ex_cn": "你想参加下个月的校园运动会吗？", "ex_py": "Nǐ xiǎng cānjiā xià ge yuè de xiàoyuán yùndònghuì ma?", "ex_en": "Do you want to participate in next month's campus sports meet?"},
    {"chapter": 9, "hanzi": "成绩", "pinyin": "chéngjì", "english": "result, score, achievement", "pos": "n.", "ex_cn": "经过努力，他在比赛中取得了优异的成绩。", "ex_py": "Jīngguò nǔlì, tā zài bǐsài zhōng qǔdé le yōuyì de chéngjì.", "ex_en": "Through diligence, he attained outstanding results in the tournament."},
    {"chapter": 9, "hanzi": "紧张", "pinyin": "jǐnzhāng", "english": "nervous, tense", "pos": "adj.", "ex_cn": "第一次上场比赛，心里有点儿紧张。", "ex_py": "Dì-yī cì shàngchǎng bǐsài, xīnlǐ yǒudiǎnr jǐnzhāng.", "ex_en": "Stepping onto the court for the first time, I felt a bit nervous inside."},
    {"chapter": 9, "hanzi": "练习", "pinyin": "liànxí", "english": "to practice; exercise", "pos": "v./n.", "ex_cn": "熟能生巧，越练越有信心。", "ex_py": "Shúnéngshēngqiǎo, yuè liàn yuè yǒu xìnxīn.", "ex_en": "Practice makes perfect; the more you practice, the more confident you become."},
    {"chapter": 9, "hanzi": "体育", "pinyin": "tǐyù", "english": "physical education, sports", "pos": "n.", "ex_cn": "学校非常重视体育锻炼。", "ex_py": "Xuéxiào fēicháng zhòngshì tǐyù duànliàn.", "ex_en": "The school attaches great importance to sports training."},
    {"chapter": 9, "hanzi": "影响", "pinyin": "yǐngxiǎng", "english": "influence; to affect", "pos": "n./v.", "ex_cn": "天气不好影响了比赛的发挥。", "ex_py": "Tiānqì bù hǎo yǐngxiǎng le bǐsài de fāhuī.", "ex_en": "Bad weather affected performance in the match."},
    {"chapter": 9, "hanzi": "受到", "pinyin": "shòudào", "english": "to receive, suffer, obtain", "pos": "v.", "ex_cn": "他在学校受到了老师和同学的好评。", "ex_py": "Tā zài xuéxiào shòudào le lǎoshī hé tóngxué de hǎopíng.", "ex_en": "He received praise from teachers and peers at school."},
    {"chapter": 9, "hanzi": "几乎", "pinyin": "jīhū", "english": "almost, nearly", "pos": "adv.", "ex_cn": "全校学生几乎都来观看比赛了。", "ex_py": "Quán xiào xuésheng jīhū dōu lái guānkàn bǐsài le.", "ex_en": "Almost all students in the school came to watch the match."},
    {"chapter": 9, "hanzi": "运动会", "pinyin": "yùndònghuì", "english": "sports games, athletic meet", "pos": "n.", "ex_cn": "下周我们学校要开春季运动会。", "ex_py": "Xià zhōu wǒmen xuéxiào yào kāi chūnjì yùndònghuì.", "ex_en": "Next week our school will host the spring sports meet."},

    # Lesson 10
    {"chapter": 10, "hanzi": "作业", "pinyin": "zuòyè", "english": "homework, task", "pos": "n.", "ex_cn": "今天的中文作业你做完了吗？", "ex_py": "Jīntiān de Zhōngwén zuòyè nǐ zuò wán le ma?", "ex_en": "Have you finished today's Chinese homework?"},
    {"chapter": 10, "hanzi": "黑板", "pinyin": "hēibǎn", "english": "blackboard", "pos": "n.", "ex_cn": "老师把重要的新词写在黑板上。", "ex_py": "Lǎoshī bǎ zhòngyào de xīn cí xiě zài hēibǎn shang.", "ex_en": "The teacher wrote the important new words on the blackboard."},
    {"chapter": 10, "hanzi": "办公室", "pinyin": "bàngōngshì", "english": "office", "pos": "n.", "ex_cn": "放学后你把本子送到老师办公室。", "ex_py": "Fàngxué hòu nǐ bǎ běnzi sòng dào lǎoshī bàngōngshì.", "ex_en": "After school, take the notebooks to the teacher's office."},
    {"chapter": 10, "hanzi": "认真", "pinyin": "rènzhēn", "english": "serious, conscientious", "pos": "adj.", "ex_cn": "只要认真复习，考试一定没问题。", "ex_py": "Zhǐyào rènzhēn fùxí, kǎoshì yídìng méi wèntí.", "ex_en": "As long as you review conscientiously, the exam will surely be fine."},
    {"chapter": 10, "hanzi": "复习", "pinyin": "fùxí", "english": "to review, revise", "pos": "v.", "ex_cn": "每天晚上花十分钟复习生词。", "ex_py": "Měitiān wǎnshang huā shí fēnzhōng fùxí shēngcí.", "ex_en": "Spend ten minutes every evening reviewing new words."},
    {"chapter": 10, "hanzi": "讲", "pinyin": "jiǎng", "english": "to explain, speak, lecture", "pos": "v.", "ex_cn": "老师讲得很清楚，大家都听懂了。", "ex_py": "Lǎoshī jiǎng de hěn qīngchu, dàjiā dōu tīng dǒng le.", "ex_en": "The teacher explained very clearly, and everyone understood."},
    {"chapter": 10, "hanzi": "清楚", "pinyin": "qīngchu", "english": "clear, distinct", "pos": "adj.", "ex_cn": "这道数学题老师讲得很清楚。", "ex_py": "Zhè dào shùxuétí lǎoshī jiǎng de hěn qīngchu.", "ex_en": "The teacher explained this math problem very clearly."},
    {"chapter": 10, "hanzi": "明白", "pinyin": "míngbai", "english": "to understand; clear", "pos": "v./adj.", "ex_cn": "听完他的解释，我终于明白了。", "ex_py": "Tīng wán tā de jiěshì, wǒ zhōngyú míngbai le.", "ex_en": "After hearing his explanation, I finally understood."},
    {"chapter": 10, "hanzi": "提高", "pinyin": "tígāo", "english": "to improve, raise", "pos": "v.", "ex_cn": "多读中文书能提高阅读能力。", "ex_py": "Duō dú Zhōngwén shū néng tígāo yuèdú nénglì.", "ex_en": "Reading more Chinese books can improve reading ability."},
    {"chapter": 10, "hanzi": "要求", "pinyin": "yāoqiú", "english": "requirement; to request", "pos": "n./v.", "ex_cn": "老师对我们的作业要求很严格。", "ex_py": "Lǎoshī duì wǒmen de zuòyè yāoqiú hěn yángé.", "ex_en": "The teacher has strict requirements for our homework."},
    {"chapter": 10, "hanzi": "句子", "pinyin": "jùzi", "english": "sentence", "pos": "n.", "ex_cn": "请用这个生词造一个完整的句子。", "ex_py": "Qǐng yòng zhè ge shēngcí zào yí ge wánzhěng de jùzi.", "ex_en": "Please make a complete sentence using this new word."},
    {"chapter": 10, "hanzi": "努力", "pinyin": "nǔlì", "english": "diligent; to strive", "pos": "adj./v.", "ex_cn": "只要努力，就一定能取得好成绩。", "ex_py": "Zhǐyào nǔlì, jiù yídìng néng qǔdé hǎo chéngjì.", "ex_en": "As long as you work hard, you can surely achieve good grades."},

    # Lesson 11
    {"chapter": 11, "hanzi": "办法", "pinyin": "bànfǎ", "english": "method, way, solution", "pos": "n.", "ex_cn": "看来我没办法解决这个问题。", "ex_py": "Kànlái wǒ méi bànfǎ jiějué zhè ge wèntí.", "ex_en": "It seems I have no way to solve this problem."},
    {"chapter": 11, "hanzi": "解决", "pinyin": "jiějué", "english": "to solve, resolve", "pos": "v.", "ex_cn": "大家一起想办法解决困难。", "ex_py": "Dàjiā yìqǐ xiǎng bànfǎ jiějué kùnnan.", "ex_en": "Let's work together to figure out a solution to the difficulty."},
    {"chapter": 11, "hanzi": "经理", "pinyin": "jīnglǐ", "english": "manager", "pos": "n.", "ex_cn": "张经理正在会议室开会。", "ex_py": "Zhāng jīnglǐ zhèngzài huìyìshì kāihuì.", "ex_en": "Manager Zhang is holding a meeting in the conference room."},
    {"chapter": 11, "hanzi": "会议", "pinyin": "huìyì", "english": "meeting, conference", "pos": "n.", "ex_cn": "今天的会议讨论了新项目。", "ex_py": "Jīntiān de huìyì tǎolùn le xīn xiàngmù.", "ex_en": "Today's conference discussed the new project."},
    {"chapter": 11, "hanzi": "或者", "pinyin": "huòzhě", "english": "or (in statements)", "pos": "conj.", "ex_cn": "你发邮件或者打电话给我都行。", "ex_py": "Nǐ fā yóujiàn huòzhě dǎ diànhuà gěi wǒ dōu xíng.", "ex_en": "Either sending me an email or calling me is fine."},
    {"chapter": 11, "hanzi": "同事", "pinyin": "tóngshì", "english": "colleague, coworker", "pos": "n.", "ex_cn": "我和同事们相处得非常愉快。", "ex_py": "Wǒ hé tóngshìmen xiāngchǔ de fēicháng yúkuài.", "ex_en": "My colleagues and I get along very well."},
    {"chapter": 11, "hanzi": "笔记本", "pinyin": "bǐjìběn", "english": "notebook / laptop", "pos": "n.", "ex_cn": "我把会议内容记在笔记本电脑上了。", "ex_py": "Wǒ bǎ huìyì nèiróng jì zài bǐjìběn diànnǎo shang le.", "ex_en": "I took notes of the meeting on my laptop."},
    {"chapter": 11, "hanzi": "别人", "pinyin": "biérén", "english": "other people, others", "pos": "pron.", "ex_cn": "多听听别人的意见很有帮助。", "ex_py": "Duō tīngting biérén de yìjiàn hěn yǒu bāngzhù.", "ex_en": "Listening more to others' opinions is very helpful."},
    {"chapter": 11, "hanzi": "城市", "pinyin": "chéngshì", "english": "city", "pos": "n.", "ex_cn": "北京是一座历史悠久的现代化大城市。", "ex_py": "Běijīng shì yí zuò lìshǐ yōujiǔ de xiàndàihuà dà chéngshì.", "ex_en": "Beijing is a modern metropolis with a long history."},
    {"chapter": 11, "hanzi": "离开", "pinyin": "líkāi", "english": "to leave, depart from", "pos": "v.", "ex_cn": "他下周就要离开这家公司了。", "ex_py": "Tā xià zhōu jiù yào líkāi zhè jiā gōngsī le.", "ex_en": "He will be leaving this company next week."},
    {"chapter": 11, "hanzi": "发", "pinyin": "fā", "english": "to send out, deliver", "pos": "v.", "ex_cn": "请把文件发到我的邮箱。", "ex_py": "Qǐng bǎ wénjiàn fā dào wǒ de yóuxiāng.", "ex_en": "Please send the file to my mailbox."},
    {"chapter": 11, "hanzi": "愿意", "pinyin": "yuànyì", "english": "willing, to wish", "pos": "aux.", "ex_cn": "大家都愿意帮助新来的同事。", "ex_py": "Dàjiā dōu yuànyì bāngzhù xīn lái de tóngshì.", "ex_en": "Everyone is willing to assist the newcomer colleague."},

    # Lesson 12
    {"chapter": 12, "hanzi": "季节", "pinyin": "jìjié", "english": "season", "pos": "n.", "ex_cn": "这个季节天气变化很快。", "ex_py": "Zhè ge jìjié tiānqì biànhuà hěn kuài.", "ex_en": "The weather changes rapidly during this season."},
    {"chapter": 12, "hanzi": "变化", "pinyin": "biànhuà", "english": "change, variation; to change", "pos": "n./v.", "ex_cn": "这几年城市的变化真大。", "ex_py": "Zhè jǐ nián chéngshì de biànhuà zhēn dà.", "ex_en": "The changes in the city over these few years are truly immense."},
    {"chapter": 12, "hanzi": "风", "pinyin": "fēng", "english": "wind", "pos": "n.", "ex_cn": "今天外面刮大风，出门穿厚点儿。", "ex_py": "Jīntiān wàimian guā dàfēng, chūmén chuān hòu diǎnr.", "ex_en": "Strong wind is blowing outside today; bundle up when going out."},
    {"chapter": 12, "hanzi": "刮", "pinyin": "guā", "english": "to blow (wind)", "pos": "v.", "ex_cn": "昨晚刮了一整夜的大风。", "ex_py": "Zuówǎn guā le yì zhěng yè de dàfēng.", "ex_en": "Strong winds blew all night yesterday."},
    {"chapter": 12, "hanzi": "春天", "pinyin": "chūntiān", "english": "spring", "pos": "n.", "ex_cn": "春天到了，公园里的花都开了。", "ex_py": "Chūntiān dào le, gōngyuán lǐ de huā dōu kāi le.", "ex_en": "Spring has arrived, and the flowers in the park are all blooming."},
    {"chapter": 12, "hanzi": "夏天", "pinyin": "xiàtiān", "english": "summer", "pos": "n.", "ex_cn": "夏天的北京挺热的。", "ex_py": "Xiàtiān de Běijīng tǐng rè de.", "ex_en": "Beijing's summer is quite hot."},
    {"chapter": 12, "hanzi": "秋天", "pinyin": "qiūtiān", "english": "autumn, fall", "pos": "n.", "ex_cn": "秋天是北京最好的季节。", "ex_py": "Qiūtiān shì Běijīng zuì hǎo de jìjié.", "ex_en": "Autumn is the best season in Beijing."},
    {"chapter": 12, "hanzi": "冬天", "pinyin": "dōngtiān", "english": "winter", "pos": "n.", "ex_cn": "冬天北方经常下大雪。", "ex_py": "Dōngtiān běifāng jīngcháng xià dàxuě.", "ex_en": "In winter, it often snows heavily in the north."},
    {"chapter": 12, "hanzi": "伞", "pinyin": "sǎn", "english": "umbrella", "pos": "n.", "ex_cn": "看天气预报要下雨，记得带伞。", "ex_py": "Kàn tiānqì yùbào yào xiàyǔ, jìde dài sǎn.", "ex_en": "The weather forecast says it will rain; remember to bring an umbrella."},
    {"chapter": 12, "hanzi": "凉快", "pinyin": "liángkuai", "english": "cool, pleasantly cool", "pos": "adj.", "ex_cn": "一场秋雨过后，天气凉快多了。", "ex_py": "Yì cháng qiūyǔ guòhòu, tiānqì liángkuai duō le.", "ex_en": "After an autumn rain, the weather turned much cooler."},
    {"chapter": 12, "hanzi": "新闻", "pinyin": "xīnwén", "english": "news", "pos": "n.", "ex_cn": "每天早晨爸爸都习惯看早间新闻。", "ex_py": "Měitiān zǎochén bàba dōu xíguàn kàn zǎojiān xīnwén.", "ex_en": "Every morning Dad is accustomed to watching the morning news."},
    {"chapter": 12, "hanzi": "公园", "pinyin": "gōngyuán", "english": "park", "pos": "n.", "ex_cn": "老人们喜欢在公园里打太极拳。", "ex_py": "Lǎorénmen xǐhuan zài gōngyuán lǐ dǎ tàijíquán.", "ex_en": "Elderly folks enjoy practicing Tai Chi in the park."},

    # Lesson 13
    {"chapter": 13, "hanzi": "邻居", "pinyin": "línjū", "english": "neighbor", "pos": "n.", "ex_cn": "我的新邻居来自英国，非常友好。", "ex_py": "Wǒ de xīn línjū láizì Yīngguó, fēicháng yǒuhǎo.", "ex_en": "My new neighbors come from the UK and are very friendly."},
    {"chapter": 13, "hanzi": "来自", "pinyin": "láizì", "english": "to come from", "pos": "v.", "ex_cn": "我们班的同学来自不同的国家。", "ex_py": "Wǒmen bān de tóngxué láizì bùtóng de guójiā.", "ex_en": "The students in our class come from different countries."},
    {"chapter": 13, "hanzi": "不同", "pinyin": "bùtóng", "english": "different, distinct", "pos": "adj.", "ex_cn": "南北方的生活习惯有很大不同。", "ex_py": "Nánběifāng de shēnghuó xíguàn yǒu hěn dà bùtóng.", "ex_en": "Living habits between north and south have great differences."},
    {"chapter": 13, "hanzi": "北方", "pinyin": "běifāng", "english": "north, northern region", "pos": "n.", "ex_cn": "北方人喜欢吃面食，南方人喜欢吃米饭。", "ex_py": "Běifāngrén xǐhuan chī miànshí, nánfāngrén xǐhuan chī mǐfàn.", "ex_en": "Northerners like wheat foods, while southerners prefer rice."},
    {"chapter": 13, "hanzi": "南方", "pinyin": "nánfāng", "english": "south, southern region", "pos": "n.", "ex_cn": "南方冬天的空气比北方湿润。", "ex_py": "Nánfāng dōngtiān de kōngqì bǐ běifāng shīrùn.", "ex_en": "In winter, southern air is more humid than in the north."},
    {"chapter": 13, "hanzi": "文化", "pinyin": "wénhuà", "english": "culture", "pos": "n.", "ex_cn": "了解不同的文化能开阔眼界。", "ex_py": "Liǎojiě bùtóng de wénhuà néng kāikuò yǎnjiè.", "ex_en": "Understanding different cultures broadens one's horizons."},
    {"chapter": 13, "hanzi": "礼物", "pinyin": "lǐwù", "english": "gift, present", "pos": "n.", "ex_cn": "我给新邻居准备了一份中国茶作为礼物。", "ex_py": "Wǒ gěi xīn línjū zhǔnbèi le yí fèn Zhōngguó chá zuòwéi lǐwù.", "ex_en": "I prepared some Chinese tea as a gift for the new neighbor."},
    {"chapter": 13, "hanzi": "一边", "pinyin": "yìbiān", "english": "simultaneously (一边...一边...)", "pos": "adv.", "ex_cn": "我们一边喝茶，一边愉快地聊天儿。", "ex_py": "Wǒmen yìbiān hēchá, yìbiān yúkuài de liáotiānr.", "ex_en": "We drank tea while chatting merrily."},
    {"chapter": 13, "hanzi": "聊天儿", "pinyin": "liáotiānr", "english": "to chat", "pos": "v.", "ex_cn": "周末有空咱们一起聊天儿吧。", "ex_py": "Zhōumò yǒukòng zánmen yìqǐ liáotiānr ba.", "ex_en": "If free this weekend, let's chat together."},
    {"chapter": 13, "hanzi": "请客", "pinyin": "qǐngkè", "english": "to treat someone (to a meal)", "pos": "v.", "ex_cn": "今天我升职了，晚上我请客！", "ex_py": "Jīntiān wǒ shēngzhí le, wǎnshang wǒ qǐngkè!", "ex_en": "I got promoted today, dinner is on me tonight!"},
    {"chapter": 13, "hanzi": "放心", "pinyin": "fàngxīn", "english": "to rest assured, feel relieved", "pos": "v./adj.", "ex_cn": "请放心，事情我已经办好了。", "ex_py": "Qǐng fàngxīn, shìqing wǒ yǐjīng bàn hǎo le.", "ex_en": "Please rest assured, I have already settled the matter."},

    # Lesson 14
    {"chapter": 14, "hanzi": "被", "pinyin": "bèi", "english": "passive marker (by)", "pos": "prep.", "ex_cn": "这本书被别人借走了。", "ex_py": "Zhè běn shū bèi biérén jiè zǒu le.", "ex_en": "This book was borrowed by someone else."},
    {"chapter": 14, "hanzi": "图书馆", "pinyin": "túshūguǎn", "english": "library", "pos": "n.", "ex_cn": "去图书馆借书要带学生卡。", "ex_py": "Qù túshūguǎn jiè shū yào dài xuéshengkǎ.", "ex_en": "To borrow books at the library, bring your student card."},
    {"chapter": 14, "hanzi": "报纸", "pinyin": "bàozhǐ", "english": "newspaper", "pos": "n.", "ex_cn": "爷爷每天早晨坐在沙发上看报纸。", "ex_py": "Yéye měitiān zǎochén zuò zài shāfā shang kàn bàozhǐ.", "ex_en": "Grandpa sits on the sofa reading the newspaper every morning."},
    {"chapter": 14, "hanzi": "电子书", "pinyin": "diànzǐshū", "english": "e-book", "pos": "n.", "ex_cn": "在手机上看电子书非常方便。", "ex_py": "Zài shǒujī shang kàn diànzǐshū fēicháng fāngbiàn.", "ex_en": "Reading e-books on a mobile phone is very convenient."},
    {"chapter": 14, "hanzi": "忘记", "pinyin": "wàngjì", "english": "to forget", "pos": "v.", "ex_cn": "我忘记带钥匙了，真麻烦。", "ex_py": "Wǒ wàngjì dài yàoshi le, zhēn máfan.", "ex_en": "I forgot to bring my keys; what a hassle."},
    {"chapter": 14, "hanzi": "相信", "pinyin": "xiāngxìn", "english": "to believe, trust", "pos": "v.", "ex_cn": "我相信你一定能做得更好。", "ex_py": "Wǒ xiāngxìn nǐ yídìng néng zuò de gèng hǎo.", "ex_en": "I believe you can certainly do even better."},
    {"chapter": 14, "hanzi": "故事", "pinyin": "gùshi", "english": "story, tale", "pos": "n.", "ex_cn": "这个成语故事很有哲理。", "ex_py": "Zhè ge chéngyǔ gùshi hěn yǒu zhélǐ.", "ex_en": "This idiom story is full of philosophical wisdom."},
    {"chapter": 14, "hanzi": "节目", "pinyin": "jiémù", "english": "program, show", "pos": "n.", "ex_cn": "春晚的舞台节目丰富多样。", "ex_py": "Chūnwǎn de wǔtái jiémù fēngfù duōyàng.", "ex_en": "The Spring Festival Gala's stage programs are rich and diverse."},
    {"chapter": 14, "hanzi": "表演", "pinyin": "biǎoyǎn", "english": "performance; to perform", "pos": "n./v.", "ex_cn": "留学生们在晚会上表演了中文歌曲。", "ex_py": "Liúxuéshēngmen zài wǎnhuì shang biǎoyǎn le Zhōngwén gēqǔ.", "ex_en": "The international students performed Chinese songs at the party."},
    {"chapter": 14, "hanzi": "然后", "pinyin": "ránhòu", "english": "then, afterwards", "pos": "conj.", "ex_cn": "我们先查资料，然后再开始写论文。", "ex_py": "Wǒmen xiān chá zīliào, ránhòu zài kāishǐ xiě lùnwén.", "ex_en": "Let's look up data first, and then begin writing the paper."},
    {"chapter": 14, "hanzi": "最好", "pinyin": "zuìhǎo", "english": "had better, best", "pos": "adv.", "ex_cn": "借书到期前最好提前归还。", "ex_py": "Jiè shū dàoqī qián zuìhǎo tíqián guīhuán.", "ex_en": "Before the borrowed books expire, it's best to return them in advance."},
    {"chapter": 14, "hanzi": "怎么办", "pinyin": "zěnme bàn", "english": "what to do", "pos": "phrase", "ex_cn": "书丢了可怎么办呢？", "ex_py": "Shū diū le kě zěnme bàn ne?", "ex_en": "The book is lost; what on earth should I do?"},

    # Lesson 15
    {"chapter": 15, "hanzi": "根据", "pinyin": "gēnjù", "english": "according to, based on", "pos": "prep.", "ex_cn": "根据天气预报，明天下午有雷阵雨。", "ex_py": "Gēnjù tiānqì yùbào, míngtiān xiàwǔ yǒu léizhènyǔ.", "ex_en": "According to the weather forecast, there will be thunderstorms tomorrow afternoon."},
    {"chapter": 15, "hanzi": "关系", "pinyin": "guānxì", "english": "relationship, connection", "pos": "n.", "ex_cn": "他们俩的关系一直非常好。", "ex_py": "Tāmen liǎ de guānxì yìzhí fēicháng hǎo.", "ex_en": "The relationship between the two of them has always been great."},
    {"chapter": 15, "hanzi": "有名", "pinyin": "yǒumíng", "english": "famous, well-known", "pos": "adj.", "ex_cn": "南京是一座历史有名的古都。", "ex_py": "Nánjīng shì yí zuò lìshǐ yǒumíng de gǔdū.", "ex_en": "Nanjing is a historically famous ancient capital."},
    {"chapter": 15, "hanzi": "景点", "pinyin": "jǐngdiǎn", "english": "scenic spot, tourist attraction", "pos": "n.", "ex_cn": "夫子庙是南京最著名的景点之一。", "ex_py": "Fūzǐmiào shì Nánjīng zuì zhùmíng de jǐngdiǎn zhīyī.", "ex_en": "The Confucius Temple is one of Nanjing's most renowned attractions."},
    {"chapter": 15, "hanzi": "游客", "pinyin": "yóukè", "english": "tourist, traveler", "pos": "n.", "ex_cn": "每年有很多中外游客来这里旅游。", "ex_py": "Měinián yǒu hěn duō zhōngwài yóukè lái zhèlǐ lǚyóu.", "ex_en": "Every year many Chinese and foreign tourists come here to travel."},
    {"chapter": 15, "hanzi": "河", "pinyin": "hé", "english": "river", "pos": "n.", "ex_cn": "黄河是中华民族的母亲河。", "ex_py": "Huáng Hé shì Zhōnghuá mínzú de mǔqīn hé.", "ex_en": "The Yellow River is the mother river of the Chinese nation."},
    {"chapter": 15, "hanzi": "平时", "pinyin": "píngshí", "english": "usually, ordinarily", "pos": "n./adv.", "ex_cn": "平时我喜欢打羽毛球和看书。", "ex_py": "Píngshí wǒ xǐhuan dǎ yǔmáoqiú hé kànshū.", "ex_en": "In ordinary times I enjoy playing badminton and reading books."},
    {"chapter": 15, "hanzi": "经过", "pinyin": "jīngguò", "english": "to pass by; through, process", "pos": "v./prep.", "ex_cn": "去学校的路上要经过一条大河。", "ex_py": "Qù xuéxiào de lùshang yào jīngguò yì tiáo dà hé.", "ex_en": "On the way to school, one must pass by a big river."},
    {"chapter": 15, "hanzi": "了解", "pinyin": "liǎojiě", "english": "to understand thoroughly, know", "pos": "v.", "ex_cn": "在南京生活了五年，我对这里非常了解。", "ex_py": "Zài Nánjīng shēnghuó le wǔ nián, wǒ duì zhèlǐ fēicháng liǎojiě.", "ex_en": "Having lived in Nanjing for 5 years, I know this place thoroughly."},
    {"chapter": 15, "hanzi": "附近", "pinyin": "fùjìn", "english": "vicinity, nearby", "pos": "n.", "ex_cn": "我家附近有一个很大的公园。", "ex_py": "Wǒ jiā fùjìn yǒu yí ge hěn dà de gōngyuán.", "ex_en": "There is a very large park near my home."},

    # Lesson 16
    {"chapter": 16, "hanzi": "大熊猫", "pinyin": "dàxióngmāo", "english": "giant panda", "pos": "n.", "ex_cn": "大熊猫是中国特有的国宝动物。", "ex_py": "Dàxióngmāo shì Zhōngguó tèyǒu de guóbǎo dòngwù.", "ex_en": "The giant panda is a national treasure animal unique to China."},
    {"chapter": 16, "hanzi": "关于", "pinyin": "guānyú", "english": "about, regarding", "pos": "prep.", "ex_cn": "关于大熊猫的保护，专家们做了大量工作。", "ex_py": "Guānyú dàxióngmāo de bǎohù, zhuānjiāmen zuò le dàliàng gōngzuò.", "ex_en": "Regarding panda conservation, experts have carried out massive work."},
    {"chapter": 16, "hanzi": "动物园", "pinyin": "dòngwùyuán", "english": "zoo", "pos": "n.", "ex_cn": "周末许多家长带孩子去动物园看熊猫。", "ex_py": "Zhōumò xǔduō jiāzhǎng dài háizi qù dòngwùyuán kàn xióngmāo.", "ex_en": "On weekends, many parents take children to the zoo to see pandas."},
    {"chapter": 16, "hanzi": "可爱", "pinyin": "kě'ài", "english": "cute, lovely", "pos": "adj.", "ex_cn": "大熊猫吃竹子的样子非常可爱。", "ex_py": "Dàxióngmāo chī zhúzi de yàngzi fēicháng kě'ài.", "ex_en": "The way pandas eat bamboo is extraordinarily cute."},
    {"chapter": 16, "hanzi": "竹子", "pinyin": "zhúzi", "english": "bamboo", "pos": "n.", "ex_cn": "竹子是大熊猫最主要的食物。", "ex_py": "Zhúzi shì dàxióngmāo zuì zhǔyào de shíwù.", "ex_en": "Bamboo is the giant panda's primary food."},
    {"chapter": 16, "hanzi": "照顾", "pinyin": "zhàogù", "english": "to take care of, look after", "pos": "v.", "ex_cn": "饲养员每天细心照顾生病的小熊猫。", "ex_py": "Sìyǎngyuán měitiān xìxīn zhàogù shēngbìng de xiǎo xióngmāo.", "ex_en": "The keeper takes care of the sick little panda meticulously every day."},
    {"chapter": 16, "hanzi": "其实", "pinyin": "qíshí", "english": "actually, in fact", "pos": "adv.", "ex_cn": "其实大熊猫跑得一点儿也不慢。", "ex_py": "Qíshí dàxióngmāo pǎo de yìdiǎnr yě bú màn.", "ex_en": "Actually, giant pandas do not run slowly at all."},
    {"chapter": 16, "hanzi": "周末", "pinyin": "zhōumò", "english": "weekend", "pos": "n.", "ex_cn": "祝你周末过得愉快！", "ex_py": "Zhù nǐ zhōumò guò de yúkuài!", "ex_en": "Wishing you a wonderful weekend!"},
    {"chapter": 16, "hanzi": "野生", "pinyin": "yěshēng", "english": "wild (flora/fauna)", "pos": "adj.", "ex_cn": "野生动物需要人类共同的保护。", "ex_py": "Yěshēng dòngwù xūyào rénlèi gòngtóng de bǎohù.", "ex_en": "Wild animals require humanity's collective protection."},
    {"chapter": 16, "hanzi": "喜爱", "pinyin": "xǐ'ài", "english": "to like, love, fond of", "pos": "v.", "ex_cn": "憨态可掬的熊猫受到了全球人民的喜爱。", "ex_py": "Hāntài-kějū de xióngmāo shòudào le quánqiú rénmín de xǐ'ài.", "ex_en": "The charmingly naive pandas won love from people all over the world."},

    # Lesson 17
    {"chapter": 17, "hanzi": "向", "pinyin": "xiàng", "english": "towards; to learn from", "pos": "prep.", "ex_cn": "我们要多向认真的人学习。", "ex_py": "Wǒmen yào duō xiàng rènzhēn de rén xuéxí.", "ex_en": "We should learn more from conscientious people."},
    {"chapter": 17, "hanzi": "认为", "pinyin": "rènwéi", "english": "to consider, think that", "pos": "v.", "ex_cn": "我认为端正学习态度最重要。", "ex_py": "Wǒ rènwéi duānzhèng xuéxí tàidu zuì zhòngyào.", "ex_en": "I consider rectifying one's study attitude to be most important."},
    {"chapter": 17, "hanzi": "聪明", "pinyin": "cōngmíng", "english": "clever, smart", "pos": "adj.", "ex_cn": "他不仅聪明，而且非常勤奋。", "ex_py": "Tā bùjǐn cōngmíng, érqiě fēicháng qínfèn.", "ex_en": "He is not only clever, but also exceedingly diligent."},
    {"chapter": 17, "hanzi": "容易", "pinyin": "róngyì", "english": "easy, likely", "pos": "adj.", "ex_cn": "学中文刚开始不容易，贵在坚持。", "ex_py": "Xué Zhōngwén gāng kāishǐ bù róngyì, guì zài jiānchí.", "ex_en": "Learning Chinese is not easy at first; persistence is precious."},
    {"chapter": 17, "hanzi": "难题", "pinyin": "nántí", "english": "difficult problem, puzzle", "pos": "n.", "ex_cn": "遇到难题时，不要害怕，向老师请教。", "ex_py": "Yùdào nántí shí, bú yào hàipà, xiàng lǎoshī qǐngjiào.", "ex_en": "When encountering difficult questions, do not fear; consult the teacher."},
    {"chapter": 17, "hanzi": "害怕", "pinyin": "hàipà", "english": "to be afraid, fear", "pos": "v.", "ex_cn": "不要害怕犯错，犯错是进步的开始。", "ex_py": "Bú yào hàipà fàncuò, fàncuò shì jìnbù de kāishǐ.", "ex_en": "Don't fear making mistakes; making mistakes is the beginning of progress."},
    {"chapter": 17, "hanzi": "回答", "pinyin": "huídá", "english": "to answer, reply; answer", "pos": "v./n.", "ex_cn": "老师点名让他回答这个问题。", "ex_py": "Lǎoshī diǎnmíng ràng tā huídá zhè ge wèntí.", "ex_en": "The teacher called his name to answer this question."},
    {"chapter": 17, "hanzi": "留学", "pinyin": "liúxué", "english": "to study abroad", "pos": "v.", "ex_cn": "许多外国学生选择来中国留学。", "ex_py": "Xǔduō wàiguó xuésheng xuǎnzé lái Zhōngguó liúxué.", "ex_en": "Many foreign students choose to come study abroad in China."},
    {"chapter": 17, "hanzi": "有用", "pinyin": "yǒuyòng", "english": "useful", "pos": "adj.", "ex_cn": "多记日常会话句子非常有用。", "ex_py": "Duō jì rìcháng huìhuà jùzi fēicháng yǒuyòng.", "ex_en": "Memorizing more daily conversation sentences is very useful."},
    {"chapter": 17, "hanzi": "只有", "pinyin": "zhǐyǒu", "english": "only (if)... (只有...才...)", "pos": "conj.", "ex_cn": "只有每天坚持练习，才能说好普通话。", "ex_py": "Zhǐyǒu měitiān jiānchí liànxí, cái néng shuō hǎo Pǔtōnghuà.", "ex_en": "Only by practicing every day can one speak good Mandarin."},

    # Lesson 18
    {"chapter": 18, "hanzi": "学会", "pinyin": "xuéhuì", "english": "to learn, master a skill", "pos": "v.", "ex_cn": "在朋友的教导下，我学会了包饺子。", "ex_py": "Zài péngyou de jiàodǎo xià, wǒ xuéhuì le bāo jiǎozi.", "ex_en": "Under my friend's guidance, I learned how to wrap dumplings."},
    {"chapter": 18, "hanzi": "春节", "pinyin": "Chūnjié", "english": "Spring Festival, Chinese New Year", "pos": "n.", "ex_cn": "春节是中国人最重要的传统节日。", "ex_py": "Chūnjié shì Zhōngguórén zuì zhòngyào de chuántǒng jiérì.", "ex_en": "Spring Festival is the Chinese people's most important traditional festival."},
    {"chapter": 18, "hanzi": "节日", "pinyin": "jiérì", "english": "festival, holiday", "pos": "n.", "ex_cn": "节日期间大家欢聚一堂包饺子。", "ex_py": "Jiérì qījiān dàjiā huānjù-yìtáng bāo jiǎozi.", "ex_en": "During festivals everyone gathers happily to wrap dumplings."},
    {"chapter": 18, "hanzi": "大概", "pinyin": "dàgài", "english": "probably, roughly, approximate", "pos": "adv./adj.", "ex_cn": "包饺子大概需要半个小时准备馅料。", "ex_py": "Bāo jiǎozi dàgài xūyào bàn ge xiǎoshí zhǔnbèi xiànliào.", "ex_en": "Wrapping dumplings roughly takes half an hour to prepare fillings."},
    {"chapter": 18, "hanzi": "只要", "pinyin": "zhǐyào", "english": "as long as... (只要...就...)", "pos": "conj.", "ex_cn": "只要多包几个，动作就熟练了。", "ex_py": "Zhǐyào duō bāo jǐ ge, dòngzuò jiù shúliàn le.", "ex_en": "As long as you wrap a few more, your movements become proficient."},
    {"chapter": 18, "hanzi": "坚持", "pinyin": "jiānchí", "english": "to persist, persevere", "pos": "v.", "ex_cn": "学外语最需要的就是坚持。", "ex_py": "Xué wàiyǔ zuì xūyào de jiù shì jiānchí.", "ex_en": "What learning a foreign language needs most is persistence."},
    {"chapter": 18, "hanzi": "毕业", "pinyin": "bìyè", "english": "to graduate", "pos": "v.", "ex_cn": "大学毕业后他打算留在北京工作。", "ex_py": "Dàxué bìyè hòu tā dǎsuàn liú zài Běijīng gōngzuò.", "ex_en": "After graduating from university, he plans to stay working in Beijing."},
    {"chapter": 18, "hanzi": "完成", "pinyin": "wánchéng", "english": "to accomplish, complete", "pos": "v.", "ex_cn": "在大家的共同努力下，任务顺利完成了。", "ex_py": "Zài dàjiā de gòngtóng nǔlì xià, rènwù shùnlì wánchéng le.", "ex_en": "Under everyone's joint efforts, the task was completed smoothly."},
    {"chapter": 18, "hanzi": "起", "pinyin": "qǐ", "english": "starting from... (从...起)", "pos": "prep.", "ex_cn": "从今天起，我每天坚持学习中文15分钟。", "ex_py": "Cóng jīntiān qǐ, wǒ měitiān jiānchí xuéxí Zhōngwén shíwǔ fēnzhōng.", "ex_en": "Starting from today, I commit to studying Chinese 15 minutes every day."},
    {"chapter": 18, "hanzi": "懂得", "pinyin": "dǒngde", "english": "to understand, know how to", "pos": "v.", "ex_cn": "在不断的实践中，我懂得了合作的重要性。", "ex_py": "Zài búduàn de shíjiàn zhōng, wǒ dǒngde le hézuò de zhòngyàoxìng.", "ex_en": "Through continual practice, I came to understand the importance of cooperation."},
    {"chapter": 18, "hanzi": "见面", "pinyin": "jiànmiàn", "english": "to meet, see someone", "pos": "v.", "ex_cn": "我们好久没见面了，真想念你们。", "ex_py": "Wǒmen hǎojiǔ méi jiànmiàn le, zhēn xiǎngniàn nǐmen.", "ex_en": "We haven't met for a long time; I really missed you guys."}
]

# Enrich word IDs
for i, w in enumerate(words_data, start=1):
    w["id"] = i

# Authentic textbook sentences from dialogues and grammar sections for all 18 lessons
sentences_data = [
    # Lesson 1
    {
        "id": 1,
        "chapter": 1,
        "context": "At home, chatting on sofa (Lesson 1 Dialogue 1)",
        "hanzi": "我以为是同乐呢，他们看上去有点儿像。",
        "pinyin": "Wǒ yǐwéi shì Tónglè ne, tāmen kànshàngqù yǒudiǎnr xiàng.",
        "english": "Oh, I thought it was Tongle. They do look a bit alike.",
        "cloze_target": "以为",
        "cloze_hint": "thought mistakenly (yǐwéi)",
        "grammar_point": "固定短语“看上去/看起来” & “以为”"
    },
    {
        "id": 2,
        "chapter": 1,
        "context": "At home, chatting on sofa (Lesson 1 Dialogue 1)",
        "hanzi": "是长得有点儿像，但是他比同乐高，身高有一米八。",
        "pinyin": "Shì zhǎng de yǒudiǎnr xiàng, dànshì tā bǐ Tónglè gāo, shēngāo yǒu yì mǐ bā.",
        "english": "Yes, they look somewhat alike, but he's taller than Tongle—about 1.8 meters.",
        "cloze_target": "比",
        "cloze_hint": "comparative marker (bǐ)",
        "grammar_point": "比较句 A 比 B + 形容词"
    },
    {
        "id": 3,
        "chapter": 1,
        "context": "At the airport baggage claim (Lesson 1 Dialogue 2)",
        "hanzi": "我好像在哪儿看到过这个箱子，是不是有人拿错了？",
        "pinyin": "Wǒ hǎoxiàng zài nǎr kàndàoguo zhè ge xiāngzi, shì bu shì yǒurén ná cuò le?",
        "english": "I feel like I saw this suitcase somewhere; did someone take it by mistake?",
        "cloze_target": "哪儿",
        "cloze_hint": "indefinite place (nǎr: somewhere)",
        "grammar_point": "疑问代词非疑问用法 (表示不确定的处所)"
    },
    {
        "id": 4,
        "chapter": 1,
        "context": "Airport arrival hall (Lesson 1 Dialogue 3)",
        "hanzi": "你说的是哪个？那个穿着黑衣服的短头发的年轻人吗？",
        "pinyin": "Nǐ shuō de shì nǎ ge? Nà ge chuānzhe hēi yīfu de duǎn tóufa de niánqīngrén ma?",
        "english": "Which one do you mean? The young man with short hair wearing black?",
        "cloze_target": "年轻",
        "cloze_hint": "young (niánqīng)",
        "grammar_point": "多项定语 (穿黑衣服的 + 短头发的 + 年轻人)"
    },
    {
        "id": 5,
        "chapter": 1,
        "context": "Li Wen's diary (Lesson 1 Text 4)",
        "hanzi": "到机场的时候，家月发现行李箱不见了，我带她去服务台找到了行李箱。",
        "pinyin": "Dào jīchǎng de shíhou, Jiāyuè fāxiàn xínglixiāng bújiàn le, wǒ dài tā qù fúwùtái zhǎodào le xínglixiāng.",
        "english": "When we arrived at the airport, Jiayue found her suitcase missing. I took her to the service desk and found it.",
        "cloze_target": "发现",
        "cloze_hint": "discovered / found out (fāxiàn)",
        "grammar_point": "动作与结果补语 (找到)"
    },

    # Lesson 2
    {
        "id": 6,
        "chapter": 2,
        "context": "At the restaurant, ordering food (Lesson 2 Dialogue 1)",
        "hanzi": "家月、李文，你们看看菜单，想吃什么就点什么。",
        "pinyin": "Jiāyuè, Lǐ Wén, nǐmen kànkan càidān, xiǎng chī shénme jiù diǎn shénme.",
        "english": "Jiayue, Li Wen, take a look at the menu, and order whatever you feel like eating.",
        "cloze_target": "什么就点什么",
        "cloze_hint": "whatever... then... (shénme jiù diǎn shénme)",
        "grammar_point": "疑问代词无条件指代任何对象"
    },
    {
        "id": 7,
        "chapter": 2,
        "context": "At the restaurant (Lesson 2 Dialogue 1)",
        "hanzi": "我现在还真是又饿又渴。",
        "pinyin": "Wǒ xiànzài hái zhēn shì yòu è yòu kě.",
        "english": "I am truly both hungry and thirsty right now.",
        "cloze_target": "又饿又渴",
        "cloze_hint": "both hungry and thirsty (yòu è yòu kě)",
        "grammar_point": "并列复句“又+形+又+形”"
    },
    {
        "id": 8,
        "chapter": 2,
        "context": "Ordering tableware (Lesson 2 Dialogue 2)",
        "hanzi": "服务员，请给我们拿两双筷子和两个勺子。",
        "pinyin": "Fúwùyuán, qǐng gěi wǒmen ná liǎng shuāng kuàizi hé liǎng ge sháozi.",
        "english": "Waiter, please bring us two pairs of chopsticks and two spoons.",
        "cloze_target": "双",
        "cloze_hint": "pair (measure word: shuāng)",
        "grammar_point": "量词搭配 (两双筷子 / 两个勺子)"
    },

    # Lesson 3
    {
        "id": 9,
        "chapter": 3,
        "context": "Looking at apartments (Lesson 3 Dialogue 1)",
        "hanzi": "这个小区挺好的，离地铁站近，周围环境也很安静。",
        "pinyin": "Zhè ge xiǎoqū tǐng hǎo de, lí dìtiězhàn jìn, zhōuwéi huánjìng yě hěn ānjìng.",
        "english": "This neighborhood is pretty good, close to the subway, and the surroundings are quiet.",
        "cloze_target": "挺好的",
        "cloze_hint": "pretty good (tǐng hǎo de)",
        "grammar_point": "固定短语“挺...的”"
    },
    {
        "id": 10,
        "chapter": 3,
        "context": "Moving plan (Lesson 3 Dialogue 2)",
        "hanzi": "咱们先去看房子，然后再去银行办一张银行卡。",
        "pinyin": "Zánmen xiān qù kàn fángzi, ránhòu zài qù yínháng bàn yì zhāng yínhángkǎ.",
        "english": "Let's first go view the apartment, and then go to the bank to apply for a bank card.",
        "cloze_target": "先",
        "cloze_hint": "first (xiān)",
        "grammar_point": "承接复句“先...然后再...”"
    },
    {
        "id": 11,
        "chapter": 3,
        "context": "Apartment appliances (Lesson 3 Dialogue 3)",
        "hanzi": "屋里有空调、洗衣机和冰箱，生活需要的东西都很全。",
        "pinyin": "Wū lǐ yǒu kōngtiáo, xǐyījī hé bīngxiāng, shēnghuó xūyào de dōngxi dōu hěn quán.",
        "english": "There are air conditioning, a washing machine, and a fridge inside; everyday necessities are all complete.",
        "cloze_target": "冰箱",
        "cloze_hint": "refrigerator (bīngxiāng)",
        "grammar_point": "家电与生活名词"
    },

    # Lesson 4
    {
        "id": 12,
        "chapter": 4,
        "context": "Borrowing camera for trip (Lesson 4 Dialogue 1)",
        "hanzi": "除了照相机以外，你还需要带别的行李吗？",
        "pinyin": "Chúle zhàoxiàngjī yǐwài, nǐ hái xūyào dài biéde xíngli ma?",
        "english": "Besides the camera, do you still need to bring any other luggage?",
        "cloze_target": "除了",
        "cloze_hint": "besides / except (chúle)",
        "grammar_point": "介词短语“除了...以外”"
    },
    {
        "id": 13,
        "chapter": 4,
        "context": "Grassland trip plan (Lesson 4 Dialogue 2)",
        "hanzi": "那里的风景跟照片上一模一样，我一直想去骑马。",
        "pinyin": "Nàlǐ de fēngjǐng gēn zhàopiàn shang yìmú-yíyàng, wǒ yìzhí xiǎng qù qímǎ.",
        "english": "The scenery there is exactly like in the pictures; I have always wanted to go ride horses.",
        "cloze_target": "一直",
        "cloze_hint": "all along / continuously (yìzhí)",
        "grammar_point": "比较句“跟...一样” & 时间副词“一直”"
    },

    # Lesson 5
    {
        "id": 14,
        "chapter": 5,
        "context": "Taking photos on the mountain (Lesson 5 Dialogue 1)",
        "hanzi": "站在阳光下面拍照才好看呢，大家看镜头！",
        "pinyin": "Zhàn zài yángguāng xiàmian pāizhào cái hǎokàn ne, dàjiā kàn jìngtóu!",
        "english": "Taking photos standing in the sunlight is only when it looks good; everyone look at the lens!",
        "cloze_target": "才",
        "cloze_hint": "only then (cái)",
        "grammar_point": "副词“才”表示条件与强调"
    },
    {
        "id": 51,
        "chapter": 5,
        "context": "Hiking experience (Lesson 5 Dialogue 2)",
        "hanzi": "爬了三个小时，我们终于爬到了山顶，风景漂亮极了。",
        "pinyin": "Pá le sān ge xiǎoshí, wǒmen zhōngyú pá dào le shāndǐng, fēngjǐng piàoliang jí le.",
        "english": "After climbing for three hours, we finally reached the top of the mountain; the view was gorgeous beyond words.",
        "cloze_target": "终于",
        "cloze_hint": "finally / at last (zhōngyú)",
        "grammar_point": "副词“终于” & 程度补语“极了”"
    },

    # Lesson 6
    {
        "id": 15,
        "chapter": 6,
        "context": "On the high-speed rail (Lesson 6 Dialogue 1)",
        "hanzi": "高铁上越来越方便了，旅客还可以用手机点外卖呢。",
        "pinyin": "Gāotiě shang yuè lái yuè fāngbiàn le, lǚkè hái kěyǐ yòng shǒujī diǎn wàimài ne.",
        "english": "It's getting more and more convenient on high-speed trains; passengers can even order takeout with mobile phones.",
        "cloze_target": "越来越",
        "cloze_hint": "more and more (yuè lái yuè)",
        "grammar_point": "固定短语“越来越+形容词”"
    },
    {
        "id": 16,
        "chapter": 6,
        "context": "Catching the train (Lesson 6 Dialogue 2)",
        "hanzi": "快检票了，时间不早了，该上车了。",
        "pinyin": "Kuài jiǎnpiào le, shíjiān bù zǎo le, gāi shàngchē le.",
        "english": "Ticket inspection is starting; it's getting late, time to board the train.",
        "cloze_target": "该",
        "cloze_hint": "it's time to (gāi)",
        "grammar_point": "固定格式“该...了”"
    },
    {
        "id": 17,
        "chapter": 6,
        "context": "Travel advice (Lesson 6 Text 4)",
        "hanzi": "如果路上堵车，我们就得坐地铁去北京南站。",
        "pinyin": "Rúguǒ lùshang dǔchē, wǒmen jiù děi zuò dìtiě qù Běijīng Nán Zhàn.",
        "english": "If there's a traffic jam on the road, we will have to take the subway to Beijing South Station.",
        "cloze_target": "如果",
        "cloze_hint": "if (rúguǒ)",
        "grammar_point": "假设复句“如果...就...”"
    },

    # Lesson 7
    {
        "id": 18,
        "chapter": 7,
        "context": "Shopping clothes (Lesson 7 Dialogue 1)",
        "hanzi": "我觉得那条黄色的裙子比短裤更好看，而且大小也很合适。",
        "pinyin": "Wǒ juéde nà tiáo huángsè de qúnzi bǐ duǎnkù gèng hǎokàn, érqiě dàxiǎo yě hěn héshì.",
        "english": "I think that yellow skirt looks better than the shorts, and the size fits suitably as well.",
        "cloze_target": "比",
        "cloze_hint": "comparative preposition (bǐ)",
        "grammar_point": "比较句 A 比 B + 更 + 形容词"
    },
    {
        "id": 19,
        "chapter": 7,
        "context": "Evaluating a dress (Lesson 7 Dialogue 2)",
        "hanzi": "这条裙子不但颜色新鲜漂亮，而且穿起来特别舒服。",
        "pinyin": "Zhè tiáo qúnzi búdàn yánsè xīnxiān piàoliang, érqiě chuān qǐlái tèbié shūfu.",
        "english": "This skirt is not only fresh and pretty in color, but also especially comfortable to wear.",
        "cloze_target": "不但",
        "cloze_hint": "not only (búdàn)",
        "grammar_point": "递进复句“不但...而且...”"
    },

    # Lesson 8
    {
        "id": 20,
        "chapter": 8,
        "context": "Health checkup & hospital discharge (Lesson 8 Dialogue 1)",
        "hanzi": "他昨天出院了，医生说他身体恢复得差不多了。",
        "pinyin": "Tā zuótiān chūyuàn le, yīshēng shuō tā shēntǐ huīfù de chàbuduō le.",
        "english": "He was discharged from the hospital yesterday; the doctor said his health has recovered almost completely.",
        "cloze_target": "出院",
        "cloze_hint": "discharged from hospital (chūyuàn)",
        "grammar_point": "离合词与程度表达 (差不多)"
    },
    {
        "id": 21,
        "chapter": 8,
        "context": "Illness advice (Lesson 8 Dialogue 2)",
        "hanzi": "生病以后你得好好休息，别太担心工作上的事情。",
        "pinyin": "Shēngbìng yǐhòu nǐ děi hǎohǎo xiūxi, bié tài dānxīn gōngzuò shang de shìqing.",
        "english": "After falling ill, you must rest well; don't worry too much about things at work.",
        "cloze_target": "以后",
        "cloze_hint": "after / afterwards (yǐhòu)",
        "grammar_point": "固定格式“...以后” & 能愿动词“得 (děi)”"
    },

    # Lesson 9
    {
        "id": 22,
        "chapter": 9,
        "context": "Tennis court encouragement (Lesson 9 Dialogue 1)",
        "hanzi": "打不好没关系，越练习球技就会越熟练。",
        "pinyin": "Dǎ bù hǎo méiguānxi, yuè liànxí qiújì jiù huì yuè shúliàn.",
        "english": "It doesn't matter if you can't play well; the more you practice, the more skillful you'll become.",
        "cloze_target": "打不好",
        "cloze_hint": "cannot play well (dǎ bù hǎo)",
        "grammar_point": "可能补语 (打不好) & “越...越...”"
    },
    {
        "id": 23,
        "chapter": 9,
        "context": "Sports competition (Lesson 9 Dialogue 2)",
        "hanzi": "为了在运动会上取得好成绩，他每天早起跑步锻炼。",
        "pinyin": "Wèile zài yùndònghuì shang qǔdé hǎo chéngjì, tā měitiān zǎoqǐ pǎobù duànliàn.",
        "english": "In order to attain good results at the sports meet, he gets up early every day to run and train.",
        "cloze_target": "为了",
        "cloze_hint": "in order to / for (wèile)",
        "grammar_point": "目的复句“为了+目的，主体+行动”"
    },

    # Lesson 10
    {
        "id": 24,
        "chapter": 10,
        "context": "Borrowing notes and books (Lesson 10 Dialogue 1)",
        "hanzi": "你明天再把课堂笔记本还给我吧，今天你先拿去复习。",
        "pinyin": "Nǐ míngtiān zài bǎ kètáng bǐjìběn huán gěi wǒ ba, jīntiān nǐ xiān ná qù fùxí.",
        "english": "You can return the classroom notebook to me tomorrow; today you take it to review first.",
        "cloze_target": "把",
        "cloze_hint": "ba-construction marker (bǎ)",
        "grammar_point": "“把”字句 (1): 把 + 宾语 + 动词 + 给"
    },
    {
        "id": 25,
        "chapter": 10,
        "context": "Math class explanation (Lesson 10 Dialogue 2)",
        "hanzi": "老师把数学难题写在黑板上，讲得特别清楚认真。",
        "pinyin": "Lǎoshī bǎ shùxué nántí xiě zài hēibǎn shang, jiǎng de tèbié qīngchu rènzhēn.",
        "english": "The teacher wrote the difficult math problem on the blackboard, explaining it very clearly and conscientiously.",
        "cloze_target": "在黑板上",
        "cloze_hint": "on the blackboard (zài hēibǎn shang)",
        "grammar_point": "“把”字句 + 动词 + 在...上"
    },

    # Lesson 11
    {
        "id": 26,
        "chapter": 11,
        "context": "Office meeting & dilemma (Lesson 11 Dialogue 1)",
        "hanzi": "看来我没办法解决这个问题，必须请经理帮忙。",
        "pinyin": "Kànlái wǒ méi bànfǎ jiějué zhè ge wèntí, bìxū qǐng jīnglǐ bāngmáng.",
        "english": "It seems I have no way to solve this problem; I must ask the manager for assistance.",
        "cloze_target": "没办法",
        "cloze_hint": "have no way / no solution (méi bànfǎ)",
        "grammar_point": "固定短语“没办法+动词”"
    },
    {
        "id": 27,
        "chapter": 11,
        "context": "Work communication (Lesson 11 Dialogue 2)",
        "hanzi": "你发邮件或者打电话给张同事都可以。",
        "pinyin": "Nǐ fā yóujiàn huòzhě dǎ diànhuà gěi Zhāng tóngshì dōu kěyǐ.",
        "english": "Either emailing or calling colleague Zhang is fine.",
        "cloze_target": "或者",
        "cloze_hint": "or (declarative: huòzhě)",
        "grammar_point": "“或者”与“还是”的辨析"
    },

    # Lesson 12
    {
        "id": 28,
        "chapter": 12,
        "context": "Weather conversation (Lesson 12 Dialogue 1)",
        "hanzi": "这个季节天气变化很快，刚才还出太阳，现在就刮起风来了。",
        "pinyin": "Zhè ge jìjié tiānqì biànhuà hěn kuài, gāngcái hái chū tàiyáng, xiànzài jiù guā qǐ fēng lái le.",
        "english": "The weather changes rapidly during this season; just now the sun was out, and now wind has started blowing.",
        "cloze_target": "变化",
        "cloze_hint": "change / variation (biànhuà)",
        "grammar_point": "趋向补语引申用法“起来”"
    },
    {
        "id": 29,
        "chapter": 12,
        "context": "Outdoor walk (Lesson 12 Dialogue 2)",
        "hanzi": "公园里的树叶全变黄了，秋天真是一个美丽的季节。",
        "pinyin": "Gōngyuán lǐ de shùyè quán biàn huáng le, qiūtiān zhēn shì yí ge měilì de jìjié.",
        "english": "The tree leaves in the park have all turned yellow; autumn is truly a beautiful season.",
        "cloze_target": "季节",
        "cloze_hint": "season (jìjié)",
        "grammar_point": "季节与天气描述"
    },

    # Lesson 13
    {
        "id": 30,
        "chapter": 13,
        "context": "Neighbor visit (Lesson 13 Dialogue 1)",
        "hanzi": "我的新邻居来自英国，要是周末有空的话，就请他们来家里做客。",
        "pinyin": "Wǒ de xīn línjū láizì Yīngguó, yàoshì zhōumò yǒukòng dehuà, jiù qǐng tāmen lái jiā lǐ zuòkè.",
        "english": "My new neighbors come from the UK; if there's free time this weekend, let's invite them over as guests.",
        "cloze_target": "的话",
        "cloze_hint": "if so (dehuà)",
        "grammar_point": "假设复句“要是...的话，就...”"
    },
    {
        "id": 31,
        "chapter": 13,
        "context": "Cultural exchange afternoon (Lesson 13 Dialogue 2)",
        "hanzi": "我们一边品尝中国茶，一边高兴地交流两国的文化。",
        "pinyin": "Wǒmen yìbiān pǐncháng Zhōngguó chá, yìbiān gāoxìng de jiāoliú liǎng guó de wénhuà.",
        "english": "We tasted Chinese tea while happily exchanging thoughts on the two countries' cultures.",
        "cloze_target": "一边",
        "cloze_hint": "simultaneously (yìbiān... yìbiān...)",
        "grammar_point": "并列复句“一边...一边...”"
    },

    # Lesson 14
    {
        "id": 32,
        "chapter": 14,
        "context": "Library search (Lesson 14 Dialogue 1)",
        "hanzi": "真不巧，你想借的那本历史书被别人借走了。",
        "pinyin": "Zhēn bù qiǎo, nǐ xiǎng jiè de nà běn lìshǐ shū bèi biérén jiè zǒu le.",
        "english": "What bad luck; that history book you wanted to borrow was borrowed by someone else.",
        "cloze_target": "被",
        "cloze_hint": "passive marker (bèi)",
        "grammar_point": "被动句: 主语 + 被 + 施事 + 动词 + 补语"
    },
    {
        "id": 33,
        "chapter": 14,
        "context": "New year party preparation (Lesson 14 Dialogue 2)",
        "hanzi": "我们先在网上看表演视频，然后一块儿决定排练哪个节目。",
        "pinyin": "Wǒmen xiān zài wǎngshang kàn biǎoyǎn shìpín, ránhòu yíkuàir juédìng páiliàn nǎ ge jiémù.",
        "english": "Let's first watch the performance videos online, and then together decide which show to rehearse.",
        "cloze_target": "然后",
        "cloze_hint": "then / afterwards (ránhòu)",
        "grammar_point": "承接复句“先...然后...” & “一块儿”"
    },

    # Lesson 15
    {
        "id": 34,
        "chapter": 15,
        "context": "Nanjing local identity (Lesson 15 Dialogue 1)",
        "hanzi": "在南京生活了这么多年，在大家看来我已经是半个南京人了。",
        "pinyin": "Zài Nánjīng shēnghuó le zhème duō nián, zài dàjiā kànlái wǒ yǐjīng shì bàn ge Nánjīng rén le.",
        "english": "Having lived in Nanjing for so many years, in everyone's eyes I am basically half a Nanjing local.",
        "cloze_target": "在大家看来",
        "cloze_hint": "in everyone's view (zài dàjiā kànlái)",
        "grammar_point": "固定短语“在...看来”"
    },
    {
        "id": 35,
        "chapter": 15,
        "context": "Travel plan according to weather (Lesson 15 Dialogue 2)",
        "hanzi": "根据导游的介绍，这个著名的景点平时有很多外地游客。",
        "pinyin": "Gēnjù dǎoyóu de jièshào, zhè ge zhùmíng de jǐngdiǎn píngshí yǒu hěn duō wàidì yóukè.",
        "english": "According to the tour guide's introduction, this famous scenic spot usually has many non-local tourists.",
        "cloze_target": "根据",
        "cloze_hint": "according to (gēnjù)",
        "grammar_point": "介词“根据”引导依据"
    },

    # Lesson 16
    {
        "id": 36,
        "chapter": 16,
        "context": "Giant panda news (Lesson 16 Dialogue 1)",
        "hanzi": "我听说关于大熊猫出国的消息，许多外国朋友非常喜爱它们。",
        "pinyin": "Wǒ tīngshuō guānyú dàxióngmāo chūguó de xiāoxi, xǔduō wàiguó péngyou fēicháng xǐ'ài tāmen.",
        "english": "I heard news regarding pandas going abroad; many foreign friends love them immensely.",
        "cloze_target": "关于",
        "cloze_hint": "regarding / concerning (guānyú)",
        "grammar_point": "介词“关于”"
    },
    {
        "id": 37,
        "chapter": 16,
        "context": "Zoo visit & panda characteristics (Lesson 16 Dialogue 2)",
        "hanzi": "一般来说，大熊猫每天有一半的时间在吃竹子，样子可爱极了。",
        "pinyin": "Yìbānláishuō, dàxióngmāo měitiān yǒu yíbàn de shíjiān zài chī zhúzi, yàngzi kě'ài jí le.",
        "english": "Generally speaking, pandas spend half their time each day eating bamboo; their look is cute in the extreme.",
        "cloze_target": "一般来说",
        "cloze_hint": "generally speaking (yìbānláishuō)",
        "grammar_point": "固定短语“一般来说”"
    },

    # Lesson 17
    {
        "id": 38,
        "chapter": 17,
        "context": "Learning attitude (Lesson 17 Dialogue 1)",
        "hanzi": "在学习上，我们要多向认真刻苦的人学习，遇到难题不要害怕。",
        "pinyin": "Zài xuéxí shang, wǒmen yào duō xiàng rènzhēn kèkǔ de rén xuéxí, yùdào nántí bú yào hàipà.",
        "english": "In our studies, we should learn more from diligent people; when encountering difficult problems, don't fear.",
        "cloze_target": "向",
        "cloze_hint": "towards / from (xiàng)",
        "grammar_point": "介词“向 someone 学习”"
    },
    {
        "id": 39,
        "chapter": 17,
        "context": "Discussion on study abroad (Lesson 17 Dialogue 2)",
        "hanzi": "她不是下个月要去中国留学吗？大家都很支持她的决定。",
        "pinyin": "Tā bú shì xià ge yuè yào qù Zhōngguó liúxué ma? Dàjiā dōu hěn zhīchí tā de juédìng.",
        "english": "Isn't she going to China to study abroad next month? Everyone strongly supports her decision.",
        "cloze_target": "不是...吗",
        "cloze_hint": "isn't it...? (bú shì... ma)",
        "grammar_point": "反问句“不是...吗？”"
    },

    # Lesson 18
    {
        "id": 40,
        "chapter": 18,
        "context": "Spring festival dumplings (Lesson 18 Dialogue 1)",
        "hanzi": "春节过节的时候，在叔叔的帮助下，我终于学会了包饺子。",
        "pinyin": "Chūnjié guòjié de shíhou, zài shūshu de bāngzhù xià, wǒ zhōngyú xuéhuì le bāo jiǎozi.",
        "english": "During the Spring Festival celebration, with uncle's help, I finally learned how to wrap dumplings.",
        "cloze_target": "学会了",
        "cloze_hint": "learned / mastered (xuéhuì le)",
        "grammar_point": "动结式“学会” & 传统节日文化"
    },
    {
        "id": 41,
        "chapter": 18,
        "context": "Learning skill encouragement (Lesson 18 Dialogue 2)",
        "hanzi": "包饺子其实不难，只要多练习几次，就能包得又快又好看。",
        "pinyin": "Bāo jiǎozi qíshí bù nán, zhǐyào duō liànxí jǐ cì, jiù néng bāo de yòu kuài yòu hǎokàn.",
        "english": "Wrapping dumplings isn't hard actually; as long as you practice a few more times, you can wrap them both fast and neat.",
        "cloze_target": "只要",
        "cloze_hint": "as long as (zhǐyào)",
        "grammar_point": "条件复句“只要...就...”"
    },
    {
        "id": 42,
        "chapter": 18,
        "context": "New year resolution (Lesson 18 Text 4)",
        "hanzi": "从新学期起，我每天坚持学习中文十五分钟，争取早日通过HSK三级考试。",
        "pinyin": "Cóng xīn xuéqī qǐ, wǒ měitiān jiānchí xuéxí Zhōngwén shíwǔ fēnzhōng, zhēngqǔ zǎorì tōngguò HSK sān jí kǎoshì.",
        "english": "Starting from the new term, I persist in studying Chinese for 15 minutes daily, striving to pass HSK Level 3 soon.",
        "cloze_target": "从...起",
        "cloze_hint": "starting from... (cóng... qǐ)",
        "grammar_point": "固定短语“从...起”"
    }
]

# Write out full JSON database
full_db = {
    "version": "1.0",
    "course": "New HSK Course 3 (《新HSK教程 3级》)",
    "publisher": "Foreign Language Teaching and Research Press (FLTRP)",
    "chapters": chapters_data,
    "words": words_data,
    "sentences": sentences_data
}

def save_to_db():
    json_path = "data/hsk3_database.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(full_db, f, ensure_ascii=False, indent=2)

    print(f"Saved {json_path} successfully!")
    print(f"Total chapters: {len(chapters_data)}")
    print(f"Total vocabulary words: {len(words_data)}")
    print(f"Total authentic sentence items: {len(sentences_data)}")

    # Create SQLite database for super fast queries and progress tracking
    db_path = "data/hsk3.db"
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chapters (
        id INTEGER PRIMARY KEY,
        title_cn TEXT,
        title_pinyin TEXT,
        title_en TEXT,
        topic TEXT,
        grammar_json TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS words (
        id INTEGER PRIMARY KEY,
        chapter_id INTEGER,
        hanzi TEXT,
        pinyin TEXT,
        english TEXT,
        pos TEXT,
        ex_cn TEXT,
        ex_py TEXT,
        ex_en TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS sentences (
        id INTEGER PRIMARY KEY,
        chapter_id INTEGER,
        context TEXT,
        hanzi TEXT,
        pinyin TEXT,
        english TEXT,
        cloze_target TEXT,
        cloze_hint TEXT,
        grammar_point TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS review_stats (
        item_type TEXT,
        item_id INTEGER,
        ease_factor REAL DEFAULT 2.5,
        interval_days INTEGER DEFAULT 0,
        repetitions INTEGER DEFAULT 0,
        last_grade INTEGER,
        last_reviewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        next_review_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (item_type, item_id)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS daily_streaks (
        study_date TEXT PRIMARY KEY,
        items_reviewed INTEGER DEFAULT 0,
        minutes_spent INTEGER DEFAULT 0
    )
    """)

    # Populate chapters
    cur.execute("DELETE FROM chapters")
    for c in chapters_data:
        cur.execute(
            "INSERT INTO chapters VALUES (?, ?, ?, ?, ?, ?)",
            (c["id"], c["title_cn"], c["title_pinyin"], c["title_en"], c["topic"], json.dumps(c["grammar"], ensure_ascii=False))
        )

    # Populate words
    cur.execute("DELETE FROM words")
    for w in words_data:
        cur.execute(
            "INSERT INTO words VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (w["id"], w["chapter"], w["hanzi"], w["pinyin"], w["english"], w["pos"], w["ex_cn"], w["ex_py"], w["ex_en"])
        )

    # Populate sentences
    cur.execute("DELETE FROM sentences")
    for s in sentences_data:
        cur.execute(
            "INSERT INTO sentences VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (s["id"], s["chapter"], s["context"], s["hanzi"], s["pinyin"], s["english"], s["cloze_target"], s["cloze_hint"], s["grammar_point"])
        )

    conn.commit()
    conn.close()
    print(f"SQLite database successfully initialized at {db_path}!")

if __name__ == '__main__':
    save_to_db()

