import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

Builder.load_string("""
<But1@Button>:
	font_size: 32

<Menu>:
	BoxLayout:
		orientation: "vertical"
		Label:
			text: 'Menu'
			font_size: 40

		BoxLayout:
			But1:
				text: "Sell"
				on_press:
					root.manager.transition.direction = "right"
					root.manager.transition.duration = 0.7
					root.manager.current = "Add"
		BoxLayout:
			But1:
				text: "Quit"

<Add>:
	BoxLayout:
		Button:
			text: "Menu"
			on_press:
				root.manager.transition.direction = "left"
				root.manager.transition.duration = 0.7
				root.manager.current = "Menu"
""")

class Menu(Screen):
	pass

class Add(Screen):
	pass

scrmanager = ScreenManager()

scrmanager.add_widget(Menu(name="Menu"))
scrmanager.add_widget(Add(name="Add"))


class RootApp(App):
	def build(self):
		return scrmanager


if __name__ == "__main__":
	RootApp().run()
