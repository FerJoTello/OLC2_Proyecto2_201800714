#print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
from MinorC import Tokens
from MinorC import AscendentParser
from MinorC.Translater import start_translation as translate
import traceback

if __name__ == "__main__":
    while True:
        try:
            print('Ingresa una expresion:')
            value = input()
            if value == 'fin':
                break
            instructions = AscendentParser.parse(value)
            traslation = translate(instructions)
            print(traslation)
        except Exception as e:
            print(e)
            tb = traceback.format_exc()
            print(tb)