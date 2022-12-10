from pynput.keyboard import Key, Controller
import time

class TestKeyboard:
    def __init__(self):
        self.keyboard = Controller()

    def inputKey(self, key):
        self.keyboard.press(key)
        self.keyboard.release(key)

    def inputKeyWithShift(self, key):
        with self.keyboard.pressed(Key.shift):
            self.keyboard.press(key)
            self.keyboard.release(key)

    def inputKeyWithControl(self, key):
        with self.keyboard.pressed(Key.ctrl):
            self.keyboard.press(key)
            self.keyboard.release(key)

    def inputKeyWith(self, with_key, key):
        with self.keyboard.pressed(with_key):
            self.keyboard.press(key)
            self.keyboard.release(key)

    def typeString(self, string):
        self.keyboard.type(string)

if __name__ == '__main__':
    kb = TestKeyboard()
#FIXME: 몇번째 줄에서 무슨에러가 났다
    time.sleep(5) #테스트를 위해 5초 이후 입력이 시작되게 하였다
    kb.inputKey('a')
    kb.inputKey(Key.enter)
    kb.inputKeyWithShift('b')
    kb.typeString('gozz`s tistory')