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
        
        self.assertEqual(CodMorseSerializer.convert_morse_to_text(".-"), 'A')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("-..."), 'B')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("-.-."), 'C')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("-.."), 'D')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("."), 'E')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("..-."), 'F')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("--."), 'G')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("...."), 'H')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text(".."), 'I')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text(".---"), 'J')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("-.-"), 'K')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text(".-.."), 'L')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("--"), 'M')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("-."), 'N')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("---"), 'O')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text(".--."), 'P')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("--.-"), 'Q')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text(".-."), 'R')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("..."), 'S')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("-"), 'T')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("..-"), 'U')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("...-"), 'V')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text(".--"), 'W')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("-..-"), 'X')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("-.--"), 'Y')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("--.."), 'Z')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text(".----"), '1')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("..---"), '2')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("...--"), '3')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("....-"), '4')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("....."), '5')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("-...."), '6')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("--..."), '7')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("---.."), '8')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("----."), '9')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("-----"), '0')
        self.assertEqual(CodMorseSerializer.convert_morse_to_text("aaass"), None)




