from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        # Crie um botão
        btn = Button(text='Toque Aqui')
        # Adicione um evento para lidar com o toque
        btn.bind(on_press=self.on_button_press)
        return btn

    def on_button_press(self, instance):
        print('O botão foi tocado!')

if __name__ == '__main__':
    TestApp().run()
