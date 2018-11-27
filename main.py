import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.listview import ListItemButton
from kivy.properties import ObjectProperty

Builder.load_string("""
#:import F kivy.factory.Factory
#:import ListAdapter kivy.adapters.listadapter.ListAdapter
#:import ListItemButton kivy.uix.listview.ListItemButton
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
	orientation: 'vertical'
	FloatLayout:
		TextInput:
			id: plate
			size_hint: .2, .05
			pos_hint: {'x':.01,'y':.9}
			multiline: False
		TextInput:
			id: plate
			size_hint: .2, .05
			pos_hint: {'x':.22,'y':.9}
			multiline: False
		TextInput:
			id: plate
			size_hint: .2, .05
			pos_hint: {'x':.43,'y':.9}
			multiline: False

		Button:
			pos_hint: {'x':.9, 'y':.95}
			size_hint: .1, .05
			text: "Menu"
			font_size:20
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
	def addCar(self):
		pass

	def addCar(self):
		pass

	def sellCar(self):
		pass


scrmanager = ScreenManager()

scrmanager.add_widget(Menu(name="Menu"))
scrmanager.add_widget(Cars(name="Cars"))


class RootApp(App):
	def build(self):
		return scrmanager


if __name__ == "__main__":
	RootApp().run()
