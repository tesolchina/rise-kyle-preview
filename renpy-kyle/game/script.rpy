# Kyle's Dilemma — 会计造假 (Ren'Py visual-novel build)
# Branching scenario: opening -> 3 choices -> branches -> 2 endings
# Scene backgrounds are Poe veo-3.1-lite motion clips (game/video/).

define k    = Character("Kyle", color="#43d692")
define boss = Character("Raymond", color="#b694e8")
define n    = Character(None)

image kyle    = "images/kyle_ref.jpg"
image raymond = "images/raymond_ref.jpg"

image office      = Movie(play="video/v1_kyle_desk.mp4")
image office_push = Movie(play="video/v3_boss_push.mp4")
image torn        = Movie(play="video/v4_kyle_torn.mp4")
image doorway     = Movie(play="video/v2_boss_door.mp4")
image shoulder    = Movie(play="video/v5_shoulder.mp4")
image dark        = Movie(play="video/v6_dark.mp4")

label start:
    scene office with fade
    n "大一暑假，Kyle 通过爸爸的世交，进了一家小会计师事务所实习。"
    n "第三天，老板 Raymond 把他叫进了办公室。"
    scene doorway
    show raymond at right with moveinright
    boss "Kyle 啊，坐。有个客户的事，想让你帮忙。"
    boss "他们想向银行申请贷款，但营收差一点。"
    scene office_push
    boss "你把他们的营收调高 15%% —— 就改几个数字，没人会知道。"
    n "Kyle 的实习评语和转正机会，全捏在 Raymond 手里。"
    menu:
        "Kyle 该怎么办？"
        "照做 —— 先保住实习再说":
            jump comply
        "拒绝 —— 这是做假账":
            jump refuse
        "先问清楚 —— 也许有别的办法":
            jump ask

label comply:
    scene office with dissolve
    show kyle at left
    k "（他是我爸的世交……得罪他，实习就没了。）"
    k "好的，Raymond，我今天就把报表改好。"
    scene shoulder
    n "Kyle 修改了营收数字。贷款批下来了。"
    scene dark with fade
    n "三个月后，银行贷后检查发现异常，事务所被立案调查。"
    n "Kyle 的名字，出现在了工作底稿上。"
    jump ending_bad

label refuse:
    scene torn with dissolve
    show kyle at left
    k "Raymond，调整营收要有真实交易支持，这属于虚假记载。"
    k "我不能做假账。"
    show raymond at right
    boss "（脸色一沉）……你先回去吧。"
    n "Kyle 的实习提前结束了。但底稿上，没有他的名字。"
    jump ending_good

label ask:
    scene torn with dissolve
    show kyle at left
    k "Raymond，如果营收确实有未开票收入，我们可以补充确认程序，"
    k "而不是直接调数字。这样银行那边也说得过去。"
    show raymond at right
    boss "（沉默片刻）……让我想想。"
    n "专业能力，有时候比顺从更有力量。"
    jump ending_good

label ending_bad:
    scene dark
    n "【结局 A】造假一时安全，代价在后面。"
    return

label ending_good:
    scene torn
    n "【结局 B】守住底线，路会窄一点，但走得远。"
    return
