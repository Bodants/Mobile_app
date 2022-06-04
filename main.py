# Здесь должен быть твой код# программа с двумя экранами
from kivy.app import App
from instructions import txt_main
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

# Экран (объект класса Screen) - это виджет типа "макет" (Screen - наследник класса RelativeLayout).
# ScreenManager - это особый виджет, который делает видимым один из прописанных в нём экранов.


class MainScr(Screen):
    def __init__(self, name = 'main'):
        super().__init__(name=name)
        txt = Label(text=txt_main, markup = True,size_hint=(1,1))
        txt2 = Label(text='Введите имя')
        txt3 = Label(text='Введите возраст')
        btn1 = Button(text='Начать',size_hint=(1,0.3))
        # inp1 = TextInput(size_hint=(.3,.05))
        # inp2 = TextInput(size_hint=(1,.05))
        # btn2 = Button(text='Это кнопка2')
        # btn1.on_press = tst
 
        box = BoxLayout()
        layout = BoxLayout(orientation='vertical')

        box.add_widget(layout)
        box.add_widget(txt)

        # box.add_widget(inp1)        
        # box.add_widget(inp2)

        # box.add_widget(txt2)
        # box.add_widget(txt3)

        box.add_widget(btn1)
        # layout.add_widget(btn2)
        btn1.on_press = self.next
        self.add_widget(box)
    def next(self):
        self.manager.transition.direction = 'right' # объект класса Screen имеет свойство manager 
                                                   # - это ссылка на родителя
        self.manager.current = 'one'


# class ButtonScr(Button):
#     def __init__(self,name='but'):
class OneScr(Screen):
    def __init__(self, name='one'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = Button(text="Продолжить",size_hint=(1,0.3))
        btn.on_press = self.next
        global names, old
        txt = Label(text='Введите имя')
        names = TextInput(size_hint=(1,.2),text='')

        txt2 = Label(text='Введите возраст')
        old = TextInput(size_hint=(1,.2),text='')

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(txt)
        layout.add_widget(names)
        layout.add_widget(txt2)
        layout.add_widget(old)
        layout.add_widget(btn)
        self.add_widget(layout) # экран - это виджет, на котором могут создаваться все другие (потомки)

    def next(self):
        global names1, old1       
        names1 = names.text
        old1 = old.text
        self.manager.transition.direction = 'right' # объект класса Screen имеет свойство manager 
                                               # - это ссылка на родителя
        self.manager.current = 'first'


class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = Button(text="Продолжить",size_hint=(1,0.3))
        global inp2
        btn.on_press = self.next
        txt = Label(text='Замерьте пульс за 15 секунд')
        txt2 = Label(text='Введите результат:')
        inp2 = TextInput(size_hint=(1,.2), text ='')
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(txt)
        layout.add_widget(txt2)
        layout.add_widget(inp2)
        layout.add_widget(btn)
        self.add_widget(layout) # экран - это виджет, на котором могут создаваться все другие (потомки)

    def next(self):
        global p1
        p1 = inp2.text
        self.manager.transition.direction = 'right' # объект класса Screen имеет свойство manager 
                                                   # - это ссылка на родителя
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        txt = Label(text='Выполните 30 приседаний за 45 секунд')
        btn = Button(text="Продолжить",size_hint=(1,0.3))
        btn.on_press = self.next
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(txt)
        layout.add_widget(btn)
        self.add_widget(layout)
        # self.add_widget(txt2)
        
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'three'


class ThreeScr(Screen):
    def __init__(self, name='three'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = Button(text="Продолжить",size_hint=(1,0.3))
        btn.on_press = self.next
        global inp3,inp4
        txt = Label(text='Введите результат')
        txt2 = Label(text='Введите результат после отдыха (30 cекунд)')
        inp3 = TextInput(size_hint=(1,.2),text='')
        inp4 = TextInput(size_hint=(1,.2),text='')
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(txt)
        layout.add_widget(inp3)
        layout.add_widget(txt2)
        layout.add_widget(inp4)
        layout.add_widget(btn)
        self.add_widget(layout)

    def next(self):
        global p2,p3
        p2 = inp3.text
        p3 = inp4.text
        
        self.manager.transition.direction = 'right'
        self.manager.current = 'four'


class FourScr(Screen):


    def __init__(self, name='four'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = Button(text="Узнать результат теста Руфье:",pos_hint={'x':-.5})
        btn.on_press = self.next
        layout = BoxLayout(orientation='vertical',padding=300)
        layout.add_widget(btn)
        self.add_widget(layout)

    def next(self):
        ryf = (4*(int(p1)+int(p2)+int(p3))-200)/10
        layout = BoxLayout(orientation='vertical', padding=150)
        txt = Label(text='Имя: '+ str(names1) + '\n' +'Возраст: ' + str(old1) +'\n'+ 'Tecт Руфье: ' + str(ryf), pos_hint={'x':.2})
        layout.add_widget(txt)
        self.add_widget(layout)
    def retur(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'

class MyApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MainScr())
        sm.add_widget(OneScr())
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThreeScr())
        sm.add_widget(FourScr())        

        return sm
        


# print(ruffier.result(p1,p2,p3))


app = MyApp()
app.run()