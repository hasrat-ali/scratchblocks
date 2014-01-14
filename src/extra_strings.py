# coding=utf-8
from __future__ import unicode_literals

"""
We need extra translations for the following strings that aren't included on
translate.scratch.mit.edu:
 
 - "turn left 10 degrees"
 - "turn right 10 degrees"
 - "when green flag clicked"
 - "end" (written after a "C" block)

"""

extra_strings = {

    "de": { # German
        "drehe dich nach links um _ Grad": "turn @arrow-ccw _ degrees",
        "drehe dich nach rechts um _ Grad": "turn @arrow-cw _ degrees",
        "Wenn die grüne Flagge angeklickt": "when @green-flag clicked",
        "Ende": "end",
    },

    "pt": { # Portugese
        "gira para a esquerda _ º": "turn @arrow-ccw _ degrees",
        "gira para a direita _ º": "turn @arrow-cw _ degrees",
        "Quando alguém clicar na bandeira verde": "when @green-flag clicked",
        "fim": "end",
    },

    "it": { # Italian
        "ruota in senso antiorario di _ gradi": "turn @arrow-ccw _ degrees",
        "ruota in senso orario di _ gradi": "turn @arrow-cw _ degrees",
        "quando si clicca sulla bandiera verde": "when @green-flag clicked",
        "fine": "end",
    },

    "fr": { # French
        "tourner gauche de _ degrés": "turn @arrow-ccw _ degrees",
        "tourner droite de _ degrés": "turn @arrow-cw _ degrees",
        "quand le drapeau vert pressé": "when @green-flag clicked",
        "fin": "end",
    },

    "es": { # Spanish
        "girar a la izquierda _ grados": "turn @arrow-ccw _ degrees",
        "girar a la derecha _ grados": "turn @arrow-cw _ degrees",
        "al presionar bandera verde": "when @green-flag clicked",
        "fin": "end",
    },

    "nl": { # Dutch
        "draai _ graden naar links": "turn @arrow-ccw _ degrees",
        "draai _ graden naar rechts": "turn @arrow-cw _ degrees",
        "wanneer groene vlag wordt aangeklikt": "when @green-flag clicked",
        "einde": "end",
    },

    "zh_CN": { # Chinese (simplified)
        "左转 _ 度": "turn @arrow-ccw _ degrees",
        "右转 _ 度": "turn @arrow-cw _ degrees",
        "转动CCW _ 度": "turn @arrow-ccw _ degrees",
        "转动CW _ 度": "turn @arrow-cw _ degrees",
        "点击绿旗时": "when @green-flag clicked",
        "结束": "end",
    },

    "he": { # Hebrew
        "הסתובב שמאל _ מעלות": "turn @arrow-ccw _ degrees",
        "הסתובב ימינה _ מעלות": "turn @arrow-cw _ degrees",
        "כאשר לוחצים על דגל ירוק": "when @green-flag clicked",
        "סוף": "end",
    },

    "pl": { # Polish
        "obróć w lewo o _ stopni": "turn @arrow-ccw _ degrees",
        "obróć w prawo o _ stopni": "turn @arrow-cw _ degrees",
        "kiedy kliknięto zieloną flagę": "when @green-flag clicked",
        "koniec": "end",
    },

}
