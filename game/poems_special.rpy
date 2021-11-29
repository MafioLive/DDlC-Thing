image poem_special1 = "/hxppy thxughts.png"
image poem_special2 = "/hxppy thxughts.png"
image poem_special3 = "/hxppy thxughts.png"
image poem_special4 = "/hxppy thxughts.png"
image poem_special5:
    "/hxppy thxughts.png"
    10.0
    "/hxppy thxughts.png"
image poem_special6 = "/hxppy thxughts.png"
image poem_special7a = "/hxppy thxughts.png"
image poem_special7b = "/hxppy thxughts.png"
image poem_special8 = "/hxppy thxughts.png"
image poem_special9 = "/hxppy thxughts.png"
image poem_special10 = "/hxppy thxughts.png"
image poem_special11 = "/hxppy thxughts.png"
image poem_end = ConditionSwitch(
    "persistent.clearall == True", "poem_special/poem_end_clearall.png",
    "True", "poem_special/poem_end.png")

label poem_special_1:
    $ quick_menu = False
    play sound page_turn
    show poem_special1 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_2:
    $ quick_menu = False
    play sound page_turn
    show poem_special2 with Dissolve(1.0)
    $ pause()
    play sound "sfx/giggle.ogg"
    $ quick_menu = True
    return
label poem_special_3:
    $ quick_menu = False
    play sound page_turn
    show poem_special3 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_4:
    $ quick_menu = False
    play sound page_turn
    show poem_special4 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_5:
    $ quick_menu = False
    play sound page_turn
    show poem_special5 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_6:
    $ quick_menu = False
    play sound page_turn
    show poem_special6 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_7:
    $ quick_menu = False
    play sound page_turn
    show poem_special7a as ps with Dissolve(1.0)
    $ pause()
    show poem_special7b as ps
    $ pause(0.01)
    $ quick_menu = True
    return
label poem_special_8:
    $ quick_menu = False
    play sound page_turn
    show poem_special8 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_9:
    $ quick_menu = False
    play sound page_turn
    show poem_special9 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_10:
    $ quick_menu = False
    play sound page_turn
    show poem_special10 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_11:
    $ quick_menu = False
    play sound page_turn
    show poem_special11 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
