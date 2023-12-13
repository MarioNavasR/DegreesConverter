namespace SpriteKind {
    export const Button = SpriteKind.create()
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (CelsiustoFahrenheit) {
        CelsiusText.setPosition(118, 11)
        CelsiusNumberText.setPosition(118, 25)
        FahrenheitText.setPosition(33, 11)
        FahrenheitNumberText.setPosition(30, 25)
        CelsiustoFahrenheit = false
    } else {
        FahrenheitText.setPosition(118, 11)
        FahrenheitNumberText.setPosition(118, 25)
        CelsiusText.setPosition(29, 11)
        CelsiusNumberText.setPosition(30, 25)
        CelsiustoFahrenheit = true
    }
})
function setNums () {
    Button11 = sprites.create(img`
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
        `, SpriteKind.Button)
    Button11.setPosition(55, 105)
    Button0 = sprites.create(img`
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
        `, SpriteKind.Button)
    Button0.setPosition(35, 105)
    Button1 = sprites.create(img`
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
        `, SpriteKind.Button)
    Button1.setPosition(15, 85)
    Button2 = sprites.create(img`
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
        `, SpriteKind.Button)
    Button2.setPosition(35, 85)
    Button3 = sprites.create(img`
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
        `, SpriteKind.Button)
    Button3.setPosition(55, 85)
    Button4 = sprites.create(img`
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
        `, SpriteKind.Button)
    Button4.setPosition(15, 65)
    Button5 = sprites.create(img`
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
        `, SpriteKind.Button)
    Button5.setPosition(35, 65)
    Button6 = sprites.create(img`
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
        `, SpriteKind.Button)
    Button6.setPosition(55, 65)
    Button7 = sprites.create(img`
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
        `, SpriteKind.Button)
    Button7.setPosition(15, 45)
    Button8 = sprites.create(img`
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
        `, SpriteKind.Button)
    Button8.setPosition(35, 45)
    Button9 = sprites.create(img`
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
        `, SpriteKind.Button)
    Button9.setPosition(55, 45)
    ButtonDelete = sprites.create(img`
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
        `, SpriteKind.Button)
    ButtonDelete.setPosition(15, 105)
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Thermo.overlapsWith(Button11)) {
        Celsius += 0
        Fahrenheit += 0
        destroyTexts()
        setTexts()
    } else if (Thermo.overlapsWith(Button0)) {
        Celsius += 0
        Fahrenheit += 0
        destroyTexts()
        setTexts()
    } else if (Thermo.overlapsWith(Button1)) {
    	
    } else if (Thermo.overlapsWith(Button2)) {
    	
    } else if (Thermo.overlapsWith(Button3)) {
    	
    } else if (Thermo.overlapsWith(Button4)) {
    	
    } else if (Thermo.overlapsWith(Button5)) {
    	
    } else if (Thermo.overlapsWith(Button6)) {
    	
    } else if (Thermo.overlapsWith(Button7)) {
    	
    } else if (Thermo.overlapsWith(Button8)) {
    	
    } else if (Thermo.overlapsWith(Button9)) {
    	
    } else if (Thermo.overlapsWith(ButtonDelete)) {
    	
    }
})
function destroyTexts () {
    sprites.destroy(CelsiusText)
    sprites.destroy(FahrenheitText)
    sprites.destroy(FahrenheitNumberText)
    sprites.destroy(CelsiusNumberText)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Button, function (sprite, otherSprite) {
    otherSprite.startEffect(effects.bubbles, 50)
})
function setTexts () {
    if (CelsiustoFahrenheit) {
        FahrenheitText = textsprite.create("Fahrenheit", 0, 1)
        FahrenheitText.setPosition(118, 11)
        FahrenheitNumberText = textsprite.create("" + Fahrenheit, 0, 1)
        FahrenheitNumberText.setPosition(118, 25)
        CelsiusText = textsprite.create("Celisus", 0, 1)
        CelsiusText.setPosition(29, 11)
        CelsiusNumberText = textsprite.create("" + Celsius, 0, 1)
        CelsiusNumberText.setPosition(30, 25)
    } else {
        CelsiusText = textsprite.create("Celisus", 0, 1)
        CelsiusText.setPosition(118, 11)
        CelsiusNumberText = textsprite.create("" + Celsius, 0, 1)
        CelsiusNumberText.setPosition(118, 25)
        FahrenheitText = textsprite.create("Fahrenheit", 0, 1)
        FahrenheitText.setPosition(33, 11)
        FahrenheitNumberText = textsprite.create("" + Fahrenheit, 0, 1)
        FahrenheitNumberText.setPosition(30, 25)
    }
}
let Fahrenheit = 0
let Celsius = 0
let ButtonDelete: Sprite = null
let Button9: Sprite = null
let Button8: Sprite = null
let Button7: Sprite = null
let Button6: Sprite = null
let Button5: Sprite = null
let Button4: Sprite = null
let Button3: Sprite = null
let Button2: Sprite = null
let Button1: Sprite = null
let Button0: Sprite = null
let Button11: Sprite = null
let FahrenheitNumberText: TextSprite = null
let FahrenheitText: TextSprite = null
let CelsiusNumberText: TextSprite = null
let CelsiusText: TextSprite = null
let CelsiustoFahrenheit = false
let Thermo: Sprite = null
scene.setBackgroundColor(7)
Thermo = sprites.create(img`
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
    `, SpriteKind.Player)
CelsiustoFahrenheit = true
controller.moveSprite(Thermo, 70, 70)
setTexts()
setNums()
forever(function () {
	
})
