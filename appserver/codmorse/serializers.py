from rest_framework import serializers

class CodMorseSerializer(serializers.Serializer):
    codMorseParam = serializers.CharField(max_length=5)

    def convert_morse_to_text(cod_morse):
         return {
             ".-"   :  "A",
             "-..." :  "B",
             "-.-." :  "C",
             "-.."  :  "D",
             "."    :  "E",
             "..-." :  "F",
             "--."  :  "G",
             "...." :  "H",
             ".."   :  "I",
             ".---" :  "J",
             "-.-"  :  "K",
             ".-.." :  "L",
             "--"   :  "M",
             "-."   :  "N",
             "---"  :  "O",
             ".--." :  "P",
             "--.-" :  "Q",
             ".-."  :  "R",
             "..."  :  "S",
             "-"    :  "T",
             "..-"  :  "U",
             "...-" :  "V",
             ".--"  :  "W",
             "-..-" :  "X",
             "-.--" :  "Y",
             "--.." :  "Z",
             ".----":  "1",
             "..---":  "2",
             "...--":  "3",
             "....-":  "4",
             ".....":  "5",
             "-....":  "6",
             "--...":  "7",
             "---..":  "8",
             "----.":  "9",
             "-----":  "0",

         }.get(cod_morse, None)
        
