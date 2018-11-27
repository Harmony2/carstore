import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button

Builder.load_string("""
#:import F kivy.factory.Factory
<Quitpop@Popup>:
	id: quitpop
	title: "Quit"
	BoxLayout:
		orientation: "vertical"
		Label:
			text: "Are you sure you want to quit?"
			font_size: 40
		But1:
			text: "quit"
			on_press: quit()
		But1:
			text: "cancel"
			on_press: quitpop.dismiss()
<But1@Button>:
	font_size: 32

<Menu>:
	id: menu
	BoxLayout:
		orientation: "vertical"
		BoxLayout:
			Label:
				text: "Menu"
				font_size:40

		BoxLayout:
			But1:
				text: "Cars"
				on_press:
					root.manager.transition.direction = "right"
					root.manager.transition.duration = 0.7
					root.manager.current = "Cars"
		BoxLayout:
			But1:
				text: "Customers"

		BoxLayout:
			But1:
				text: "Employees"

		BoxLayout:
			But1:
				text: "Quit"
				on_press: F.Quitpop().open()


<Cars>:
	id: cars
	BoxLayout:
		Button:
			text: "Menu"
			on_press:
				root.manager.transition.direction = "left"
				root.manager.transition.duration = 0.7
				root.manager.current = "Menu"
""")

class Menu(Screen):
	def leave(self):
		popup = Popup(title='Quit?',
				content=Button(text="cancel"),
				size_hint=(None,None), size=(400,400))
		popup.open()

class Cars(Screen):
	pass

scrmanager = ScreenManager()

scrmanager.add_widget(Menu(name="Menu"))
scrmanager.add_widget(Cars(name="Cars"))


class RootApp(App):
	def build(self):
		return scrmanager


if __name__ == "__main__":
	RootApp().run()
