import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout

Builder.load_string("""
<But1@Button>:
	font_size: 32
	size: 50, 50

<Menu>:
	id: Menu
	rows: 3
	padding: 20
	spacing: 30

	BoxLayout:
		But1:
			text: "Sell"
			on_press:
				root.manager.transition.direction = "right"
				root.manager.transition.duration = 0.5
				root.manager.current = "Add"
	BoxLayout:
		But1:
			text: "Sell"
			on_press:
				root.manager.transition.direction = "right"
				root.manager.transition.duration = 0.5
				root.manager.current = "Add"

<Add>:
	BoxLayout:
		Button:
			text: "Menu"
			on_press:
				root.manager.transition.direction = "left"
				root.manager.transition.duration = 0.5
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
