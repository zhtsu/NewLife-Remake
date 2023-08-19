default text_speed = 8

define g = Character('她')

image bg bedroom = "bedroom.jpg"
image bg classroom = "classroom.jpg"
image bg gathering_place = "gathering_place.jpg"
image bg girl_home = "girl_home.jpg"
image girl unhappy = "girl_unhappy.png"
image girl happy = "girl_happy.png"
image girl wanttalk = "girl_want_talk.png"
image girl talk = "girl_talk.png"
image girl smile = "girl_smile.png"
image girl leave = "girl_leave.png"
image girl anger = "girl_anger.png"

label start:
    scene bg bedroom

    "{cps=12}你一直很憧憬现充丰富多彩的生活{/cps}"
    
    "{cps=12}你在网上搜到了相关教程，你决定根据这些教程去成为现充{/cps}"
    
    "{cps=12}你很认真地学习起来......{/cps}"

    "{cps=12}今天的时间过得很快，离上课只有 15 分钟了{/cps}"

    menu:
        "得赶紧去教室":
            jump classroom

        "再看一会儿":
            jump sleep


label classroom:
    scene bg classroom with dissolve

    "{cps=12}你快步跑到教室，但教室后排一个位置也没有了{/cps}"

    "{cps=12}你被迫坐在了班花旁边......{/cps}"

    play music talking

    "{cps=12}终于，第一节课结束了，不过这丝毫没有减轻你坐在班花旁边的压力{/cps}"

    "{cps=12}班花和另一边的女生聊了起来。刚决定成为现充的你决定做点什么{/cps}"

    menu:
        "活学活用，用现充的话术加入话题":
            jump talk

        "恪守死宅的孤高，不去加入话题":
            jump mute

label sleep:
    play music debu

    "{cps=12}不知不觉中你在床上睡去......{/cps}"

    "{cps=12}你做了一个梦{/cps}"

    "{cps=12}在梦中，你如愿成为现充{/cps}"

    "{cps=12}你成为了一个备受大家欢迎的人，交到许多热心的朋友{/cps}"

    "{cps=12}以后的日子里，你也将时常沉浸在虚幻的梦境中......{/cps}"

    "Bad End 1 - 放纵"

    return


label talk:
    play music earlgrey

    "{cps=12}同学们对你的转变感到很是惊讶{/cps}"

    "{cps=12}你用学习到的话术成功暂时融入了校花的小团体......{/cps}"

    "{cps=12}在某个周末你收到了班花的邀请，希望你能参加聚会{/cps}"

    menu:
        "现充生活在向我招手，冲啊":
            jump party

        "委婉拒绝，聚会不如宅家打游戏":
            jump home

label mute:
    play music debu

    scene bg bedroom with dissolve

    "{cps=12}恪守死宅之心的你拉不下面子去加入那些对你而言很无聊的话题{/cps}"

    "{cps=12}于是你暂时蛰伏起来，想要去寻找下一个机会{/cps}"

    "{cps=12}这个机会也许就在明天，也许永远不会到来{/cps}"

    "Bad End 2 - 固执"

    return


label party:
    play music party

    scene bg gathering_place

    "{cps=12}在聚会上你用从网上背下来的交友方法混的如鱼得水{/cps}"

    "{cps=12}你开始觉得自己就是成为现充的那块料{/cps}"

    show girl unhappy with fade

    "{cps=12}但是你发现班花在聚会上确有些郁郁寡欢，于是你决定{/cps}"

    menu:
        "等到一个人少的时候向班花询问有什么心事":
            jump ask

        "现在我和她还不够熟悉，不如再做观察":
            jump wait


label ask:
    play music debu

    show girl leave with dissolve

    "{cps=12}你有些急功近利的行为导致班花对你的目的升起了一丝警惕{/cps}"

    "{cps=12}而你在之后按照所谓的现充教程做出很多挽救的措施却让人更加觉得虚伪{/cps}"

    "{cps=12}最后你现充没做成还浪费了你宝贵安定学习时间，高考失利，成为了老鼠人{/cps}"

    "Bad End 3 - 笨拙"

    return

label wait:
    "{cps=12}你一边尝试着活跃气氛，一边仔细观察着班花{/cps}"

    play music rain

    "{cps=12}在聚会要结束的时候突然下起来了大雨{/cps}"

    "{cps=12}你发现班花并没有带伞，于是你决定{/cps}"

    menu:
        "将自己的伞送给班花，并谎称自己没伞":
            jump alone
        
        "向班花提出自己可以送她回家":
            jump together


label alone:
    play music debu

    hide girl unhappy with fade

    "{cps=12}班花接过了你的伞向你道谢后便走了，而你淋着大雨一路跑回家{/cps}"

    scene bg bedroom with dissolve

    "{cps=12}当你第二天想从床上爬起来的时候却发现自己浑身无力{/cps}"

    "{cps=12}想要爬下床找药吃的时候却两脚一软身体向下倒去头撞到尖锐的铁制桌子的桌角上，结束了你的一生{/cps}"

    "Bad End 4 - 倒霉"

    return


label together:
    show girl smile

    "{cps=12}班花原本还有些犹豫要不要接受你的邀请，但越来越大的雨让她最终同意了你的邀请{/cps}"

    hide bg
    hide girl

    "{cps=12}你将班花送回了家，却惊讶的发现她家是很破旧的老房子，与她那看上去光鲜亮丽的外表完全不符{/cps}"

    "{cps=12}班花看到你身上被淋湿了，犹豫了一会邀请你进去坐坐，等雨小一些了再走{/cps}"

    menu:
        "接受邀请进去坐坐":
            jump girl_home

        "委婉拒绝":
            jump refuse


label girl_home:
    play music earlgrey

    scene bg girl_home with dissolve

    "{cps=12}你走进班花的家，发现这是一个又破又小的空间{/cps}"

    "{cps=12}虽然有些拥挤，但是却被布置的相当温馨，可以看出来房子主人对房子很是上心{/cps}"

    show girl wanttalk with fade

    "{cps=12}你找到一张椅子靠着坐下，坐在你的面前是有些欲言又止的班花{/cps}"

    menu:
        "主动开口询问":
            jump girl_home_ask

        "闭口不谈":
            jump girl_home_mute


label refuse:
    play music debu

    "{cps=12}你独自走回了家{/cps}"

    "{cps=12}习惯性的拒绝让你注定不会与他人有过多交集{/cps}"

    "Bad End 5 - 无奈"

    return


label girl_home_ask:
    "{cps=12}你开口询问班花有什么想要说的{/cps}"

    "{cps=12}班花犹豫了一会最终开口说道：{/cps}"

    show girl talk

    g "{cps=12}其实我们都是一类人，对吧？{/cps}"

    "{cps=12}你有些惊讶不知道她究竟指的是哪一方面{/cps}"

    "{cps=12}她看到你不回话，也不在意，继续说道：{/cps}"

    g "{cps=12}我看得出来，你其实并不喜欢参加什么聚会，不喜欢应和着自己并不喜欢的话题，对吧？{/cps}"

    menu:
        "确实如此":
            jump yes
        
        "你在说些什么啊，我听不懂":
            jump no


label girl_home_mute:
    play music debu

    "{cps=12}尽管 你看出来了班花有些什么想要说的，但是你谨慎的选择了闭口不谈{/cps}"

    "{cps=12}最后你在雨停之后便离开了班花家{/cps}"

    jump MDD

    "Bad End 6 - 懦弱"

    return


label yes:
    show girl happy

    "{cps=12}确实就像她说的那样，这一段时间的 “现充生活” 也让你感到疲惫不堪{/cps}"

    "{cps=12}你只不过是带着一张面具生活着罢了，所谓的成为现充也不过是自己脑子一热下的想法{/cps}"

    "{cps=12}看向坐在自己对面的班花，你意识到坐在你对面的人和你一样{/cps}"

    "{cps=12}一样羡慕着所谓的现充生活，一样渴望融入别人的圈子{/cps}"

    "{cps=12}但是在别人面前带着面具般活着，强行加入自己并不喜欢的话题{/cps}"

    "{cps=12}这样的生活只会给人带来莫大的压力，这段时间的现充生活让你感到十分压抑{/cps}"

    "{cps=12}而面前这个人毫无疑问是和你一样的人，换句话来说就是同类{/cps}"

    "{cps=12}你从她身上感到一阵莫名的心安，你们聊了很多，最后成为了很好的朋友。{/cps}"

    "Happy End - 真诚"

    return


label no:
    play music debu

    show girl anger

    "你的表现很明显让眼前的人感到了失望，在接下来的一段时间里你们之间没有再说过一句话"
    "雨停之后你便离开了班花家，在那之后你们两个渐行渐远"
    
    jump MDD

    "Bad End 7 - 虚伪"

    return


label MDD:
    "{cps=12}你依旧在追求着现充生活但是那些现充的行为却让你感到极其不适{/cps}"

    "{cps=12}最后在长年的压力下你得上了抑郁症，最后一辈子郁郁寡欢{/cps}"