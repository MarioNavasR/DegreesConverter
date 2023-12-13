@namespace
class SpriteKind:
    Button = SpriteKind.create()

def on_b_pressed():
    global CelsiustoFahrenheit
    if CelsiustoFahrenheit:
        CelsiusText.set_position(118, 11)
        CelsiusNumberText.set_position(118, 25)
        FahrenheitText.set_position(33, 11)
        FahrenheitNumberText.set_position(30, 25)
        CelsiustoFahrenheit = False
    else:
        FahrenheitText.set_position(118, 11)
        FahrenheitNumberText.set_position(118, 25)
        CelsiusText.set_position(29, 11)
        CelsiusNumberText.set_position(30, 25)
        CelsiustoFahrenheit = True
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def setNums():
    global Button11, Button0, Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, Button9, ButtonDelete
    Button11 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f 1 1 f f f f f f . 
                    . f f f f f f 1 1 f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Button)
    Button11.set_position(55, 105)
    Button0 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f 1 1 1 1 f f f f f . 
                    . f f f f 1 f f f f 1 f f f f . 
                    . f f f 1 f f f f f f 1 f f f . 
                    . f f f 1 f f f f f f 1 f f f . 
                    . f f f 1 f f f f f f 1 f f f . 
                    . f f f 1 f f f f f f 1 f f f . 
                    . f f f 1 f f f f f f 1 f f f . 
                    . f f f 1 f f f f f f 1 f f f . 
                    . f f f f 1 f f f f 1 f f f f . 
                    . f f f f f 1 1 1 1 f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Button)
    Button0.set_position(35, 105)
    Button1 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f 1 1 1 f f f f f . 
                    . f f f f f 1 1 1 1 f f f f f . 
                    . f f f f 1 1 f 1 1 f f f f f . 
                    . f f f 1 1 f f 1 1 f f f f f . 
                    . f f 1 1 f f f 1 1 f f f f f . 
                    . f f f f f f f 1 1 f f f f f . 
                    . f f f f f f f 1 1 f f f f f . 
                    . f f f f f f f 1 1 f f f f f . 
                    . f f f f f f f 1 1 f f f f f . 
                    . f f f f f f f 1 1 f f f f f . 
                    . f f f f f 1 1 1 1 1 1 f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Button)
    Button1.set_position(15, 85)
    Button2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f 1 1 1 1 f f f f f f . 
                    . f f f 1 1 f f 1 1 f f f f f . 
                    . f f f 1 f f f f 1 f f f f f . 
                    . f f f 1 f f f f 1 f f f f f . 
                    . f f f f f f f 1 1 f f f f f . 
                    . f f f f f f 1 1 f f f f f f . 
                    . f f f f f 1 1 f f f f f f f . 
                    . f f f f 1 1 f f f f f f f f . 
                    . f f f 1 1 f f f f f f f f f . 
                    . f f 1 1 1 1 1 1 1 1 f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Button)
    Button2.set_position(35, 85)
    Button3 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f 1 1 1 f f f f f f . 
                    . f f f f 1 f f f 1 f f f f f . 
                    . f f f f f f f f 1 f f f f f . 
                    . f f f f f f f 1 f f f f f f . 
                    . f f f f f 1 1 f f f f f f f . 
                    . f f f f f f f 1 f f f f f f . 
                    . f f f f f f f f 1 f f f f f . 
                    . f f f f 1 f f f 1 f f f f f . 
                    . f f f f f 1 1 1 f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Button)
    Button3.set_position(55, 85)
    Button4 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f 1 1 f f f f f . 
                    . f f f f f f 1 f 1 f f f f f . 
                    . f f f f f 1 f f 1 f f f f f . 
                    . f f f f 1 f f f 1 f f f f f . 
                    . f f f f 1 1 1 1 1 f f f f f . 
                    . f f f f f f f f 1 f f f f f . 
                    . f f f f f f f f 1 f f f f f . 
                    . f f f f f f f f 1 f f f f f . 
                    . f f f f f f f f 1 f f f f f . 
                    . f f f f f f f f 1 f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Button)
    Button4.set_position(15, 65)
    Button5 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f 1 1 1 1 1 1 f f f f . 
                    . f f f f 1 f f f f f f f f f . 
                    . f f f f 1 f f f f f f f f f . 
                    . f f f f 1 f f f f f f f f f . 
                    . f f f f 1 1 1 1 1 1 f f f f . 
                    . f f f f f f f f f 1 f f f f . 
                    . f f f f f f f f f 1 f f f f . 
                    . f f f f f f f f f 1 f f f f . 
                    . f f f f f f f f f 1 f f f f . 
                    . f f f f 1 1 1 1 1 1 f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Button)
    Button5.set_position(35, 65)
    Button6 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f 1 1 1 f f f f f f . 
                    . f f f f 1 f f f 1 f f f f f . 
                    . f f f 1 1 f f f 1 1 f f f f . 
                    . f f f 1 f f f f f 1 f f f f . 
                    . f f f 1 f f f f f f f f f f . 
                    . f f f 1 f 1 1 1 1 f f f f f . 
                    . f f f 1 1 f f f f 1 f f f f . 
                    . f f f f 1 f f f f 1 f f f f . 
                    . f f f f 1 f f f f 1 f f f f . 
                    . f f f f f 1 1 1 1 f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Button)
    Button6.set_position(55, 65)
    Button7 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f 1 1 1 1 1 1 f f f f . 
                    . f f f f f f f f f 1 f f f f . 
                    . f f f f f f f f f 1 f f f f . 
                    . f f f f f f f f f 1 f f f f . 
                    . f f f f f f f f 1 f f f f f . 
                    . f f f f f f f f 1 f f f f f . 
                    . f f f f f f f f 1 f f f f f . 
                    . f f f f f f f 1 f f f f f f . 
                    . f f f f f f f 1 f f f f f f . 
                    . f f f f f f f 1 f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Button)
    Button7.set_position(15, 45)
    Button8 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f 1 1 1 1 f f f f f . 
                    . f f f f 1 f f f f 1 f f f f . 
                    . f f f f 1 f f f f 1 f f f f . 
                    . f f f f 1 f f f f 1 f f f f . 
                    . f f f f f 1 1 1 1 f f f f f . 
                    . f f f f 1 f f f f 1 f f f f . 
                    . f f f f 1 f f f f 1 f f f f . 
                    . f f f f 1 f f f f 1 f f f f . 
                    . f f f f 1 f f f f 1 f f f f . 
                    . f f f f f 1 1 1 1 f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Button)
    Button8.set_position(35, 45)
    Button9 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f 1 1 1 1 f f f f f . 
                    . f f f f f 1 f f f 1 f f f f . 
                    . f f f f 1 f f f f f 1 f f f . 
                    . f f f f 1 f f f f f 1 f f f . 
                    . f f f f f 1 f f f 1 1 f f f . 
                    . f f f f f 1 1 1 1 f 1 f f f . 
                    . f f f f f f f f f f 1 f f f . 
                    . f f f f f f f f f 1 1 f f f . 
                    . f f f f f f f f 1 1 f f f f . 
                    . f f f f f 1 1 1 1 f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Button)
    Button9.set_position(55, 45)
    ButtonDelete = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f 1 1 1 1 1 1 1 f f . 
                    . f f f f 1 1 1 1 1 1 1 1 f f . 
                    . f f f 1 1 1 f 1 1 1 f 1 f f . 
                    . f f 1 1 1 1 1 f 1 f 1 1 f f . 
                    . f 1 1 1 1 1 1 1 f 1 1 1 f f . 
                    . f f 1 1 1 1 1 f 1 f 1 1 f f . 
                    . f f f 1 1 1 f 1 1 1 f 1 f f . 
                    . f f f f 1 1 1 1 1 1 1 1 f f . 
                    . f f f f f 1 1 1 1 1 1 1 f f . 
                    . f f f f f f f f f f f f f f . 
                    . f f f f f f f f f f f f f f . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Button)
    ButtonDelete.set_position(15, 105)

def on_a_pressed():
    global Celsius, Fahrenheit
    if Thermo.overlaps_with(Button11):
        Celsius += -1
        Fahrenheit += -2
        destroyTexts()
        setTexts()
    elif Thermo.overlaps_with(Button0):
        pass
    elif Thermo.overlaps_with(Button1):
        pass
    elif Thermo.overlaps_with(Button2):
        pass
    elif Thermo.overlaps_with(Button3):
        pass
    elif Thermo.overlaps_with(Button4):
        pass
    elif Thermo.overlaps_with(Button5):
        pass
    elif Thermo.overlaps_with(Button6):
        pass
    elif Thermo.overlaps_with(Button7):
        pass
    elif Thermo.overlaps_with(Button8):
        pass
    elif Thermo.overlaps_with(Button9):
        pass
    elif Thermo.overlaps_with(ButtonDelete):
        pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def destroyTexts():
    sprites.destroy(CelsiusText)
    sprites.destroy(FahrenheitText)
    sprites.destroy(FahrenheitNumberText)
    sprites.destroy(CelsiusNumberText)

def on_on_overlap(sprite, otherSprite):
    otherSprite.start_effect(effects.bubbles, 50)
sprites.on_overlap(SpriteKind.player, SpriteKind.Button, on_on_overlap)

def setTexts():
    global FahrenheitText, FahrenheitNumberText, CelsiusText, CelsiusNumberText
    if CelsiustoFahrenheit:
        FahrenheitText = textsprite.create("Fahrenheit", 0, 1)
        FahrenheitText.set_position(118, 11)
        FahrenheitNumberText = textsprite.create("" + str(Fahrenheit), 0, 1)
        FahrenheitNumberText.set_position(118, 25)
        CelsiusText = textsprite.create("Celisus", 0, 1)
        CelsiusText.set_position(29, 11)
        CelsiusNumberText = textsprite.create("" + str(Celsius), 0, 1)
        CelsiusNumberText.set_position(30, 25)
    else:
        CelsiusText = textsprite.create("Celisus", 0, 1)
        CelsiusText.set_position(118, 11)
        CelsiusNumberText = textsprite.create("" + str(Celsius), 0, 1)
        CelsiusNumberText.set_position(118, 25)
        FahrenheitText = textsprite.create("Fahrenheit", 0, 1)
        FahrenheitText.set_position(33, 11)
        FahrenheitNumberText = textsprite.create("" + str(Fahrenheit), 0, 1)
        FahrenheitNumberText.set_position(30, 25)
Fahrenheit = 0
Celsius = 0
ButtonDelete: Sprite = None
Button9: Sprite = None
Button8: Sprite = None
Button7: Sprite = None
Button6: Sprite = None
Button5: Sprite = None
Button4: Sprite = None
Button3: Sprite = None
Button2: Sprite = None
Button1: Sprite = None
Button0: Sprite = None
Button11: Sprite = None
FahrenheitNumberText: TextSprite = None
FahrenheitText: TextSprite = None
CelsiusNumberText: TextSprite = None
CelsiusText: TextSprite = None
CelsiustoFahrenheit = False
Thermo: Sprite = None
scene.set_background_color(7)
Thermo = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . 1 2 f . . . . . . . . . . 
            . . . 1 1 2 f . . . . . . . . . 
            . . . . 1 1 2 f . . . . . . . . 
            . . . . . 1 1 2 f . . . . . . . 
            . . . . . . 1 1 2 f . . . . . . 
            . . . . . . . 1 1 2 f . . . . . 
            . . . . . . . . 1 1 2 f . . . . 
            . . . . . . . . . 1 1 2 2 2 . . 
            . . . . . . . . . . 1 2 2 2 1 . 
            . . . . . . . . . . 1 2 2 2 1 . 
            . . . . . . . . . . . 1 1 1 . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
CelsiustoFahrenheit = True
controller.move_sprite(Thermo, 70, 70)
setTexts()
setNums()

def on_forever():
    pass
forever(on_forever)
