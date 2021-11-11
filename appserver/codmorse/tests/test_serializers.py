from django.test import TestCase
from codmorse.serializers import CodMorseSerializer

class SerializerTestCase(TestCase):
    def test_validations_params(self):
        """Validação de tamanho máximo do atributo recebito por parâmetro"""        
        seria = CodMorseSerializer(data={"codMorseParam": ".-sadasdasdasdasdasdasdasd"})
        self.assertEqual(seria.is_valid(), False)
        seriali = CodMorseSerializer(data={"codMorseParam": ".-"})
        self.assertEqual(seriali.is_valid(), True)

    def test_convert_morse_to_text(self):
        """Conversão de código morse para texto"""
        
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": ".-"}), 'A')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "-..."}), 'B')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "-.-."}), 'C')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "-.."}), 'D')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "."}), 'E')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "..-."}), 'F')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "--."}), 'G')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "...."}), 'H')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": ".."}), 'I')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": ".---"}), 'J')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "-.-"}), 'K')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": ".-.."}), 'L')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "--"}), 'M')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "-."}), 'N')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "---"}), 'O')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": ".--."}), 'P')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "--.-"}), 'Q')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": ".-."}), 'R')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "..."}), 'S')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "-"}), 'T')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "..-"}), 'U')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "...-"}), 'V')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": ".--"}), 'W')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "-..-"}), 'X')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "-.--"}), 'Y')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "--.."}), 'Z')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": ".----"}), '1')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "..---"}), '2')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "...--"}), '3')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "....-"}), '4')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "....."}), '5')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "-...."}), '6')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "--..."}), '7')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "---.."}), '8')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "----."}), '9')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "-----"}), '0')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text({"codMorseParam": "aaass"}), None)