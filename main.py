import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.listview import ListItemButton
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView
from kivy.clock import mainthread
from kivy.uix.textinput import TextInput
from functools import partial

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
				text: "Add Car"
				on_press:
					root.manager.transition.direction = "right"
					root.manager.transition.duration = 0.4
					root.manager.current = "Cars"
		BoxLayout:
			But1:
				text: "Cars"
				on_press:
					root.manager.transition.direction = "right"
					root.manager.transition.duration = 0.4
					root.manager.current = "Sell"

		BoxLayout:
			But1:
				text: "Employees"

		BoxLayout:
			But1:
				text: "Quit"
				on_press: F.Quitpop().open()
<Sell>:
	ScrollView:
		GridLayout:
			cols: 1
			id: grid
			spacing: 10,10
			padding: 10,10
			size_hint_y: None
			height: 2000
			Button:
				text: "Menu"
				font_size:32
				on_press:
					root.manager.transition.direction = "left"
					root.manager.transition.duration = 0.4
					root.manager.current = "Menu"


<Cars>:
	id: cars
	BoxLayout:
		orientation: "vertical"
		But1:
			text: "Menu"
			on_press:
				root.manager.transition.direction = "left"
				root.manager.transition.duration = 0.4
				root.manager.current = "Menu"
		Label:
			text: "Plate"
			font_size: 32
		TextInput:
			id: plate
			multiline: False

		Label:
			text: "type"
			font_size: 32
		TextInput:
			id: type
			multiline: False

		Label:
			text: "Price"
			font_size: 32
		TextInput:
			id: price
			multiline: False

		But1:
			text: "Add"
			on_press:
				cars.add(plate.text,type.text,price.text)
				root.manager.transition.direction = "left"
				root.manager.transition.duration = 0.4
				root.manager.current = "Menu"


""")

class Menu(Screen):
	pass

class Sell(Screen):
	#@mainthread
	flags = []

	def on_enter(self):
		self.clear_widgets
		f = open('carros.txt','r')
		a = f.read()
		f.close()
		a = a.split('\n')
		a.pop()
		for i in range(0,len(a)):
			a[i] = a[i].split(":")
		for i in range(0,len(a)):
			if a[i][0] not in self.flags:
				btn = Button(text=str(a[i][0]), font_size=32)

				box = BoxLayout(orientation="vertical")
				bot = BoxLayout()
				pop = Popup(title='HELP',content=box)

				cancel = Button(text="Return",font_size=32,on_release=pop.dismiss)
				sell = Button(text="Sell",font_size=32)
				bot.add_widget(cancel)
				

				platel = Label(text='Plate:',font_size=30)
				plate = Label(text=a[i][0],font_size=25)
				box.add_widget(platel)
				box.add_widget(plate)

				typel = Label(text='Car:',font_size=30)
				typee = Label(text=a[i][1],font_size=25)
				box.add_widget(typel)
				box.add_widget(typee)

				pricel = Label(text='Price:',font_size=30)
				price = Label(text=a[i][2],font_size=25)
				box.add_widget(pricel)
				box.add_widget(price)

				sep = Label(text='----------------------------------------',font_size=30)
				box.add_widget(sep)

				buyerl = Label(text='Insert Buyer\'s unique ID:', font_size=32)
				buyeri = TextInput(multiline=False)

				box.add_widget(buyerl)
				box.add_widget(buyeri)
				#buttoncallback = partial(self.gratulation, g.text)
				removerino = partial(self.remove, a[i][0],a[i][1],a[i][2])
				sell.bind(on_press=removerino)
				box.add_widget(sell)
				box.add_widget(bot)
				
				btn.bind(on_press=pop.open)


				self.ids.grid.add_widget(btn)
				self.flags.append(a[i][0])

	def remove(self,plate,typee,price,*args):
			f = open('carros.txt','r')
			a = f.readlines()
			f.close()
			s = '%s:%s:%s\n'%(plate,typee,price)
			f = open('carros.txt','w')
			for i in a:
				print(i)
				if i != s:
					f.write(i)
			f.close()
			print(a)

class Cars(Screen):
	def add(self,plate,tipo,price):
		f = open('carros.txt','a+')
		f.write("%s:%s:%s\n"%(plate,tipo,price))
		f.close()

scrmanager = ScreenManager()

scrmanager.add_widget(Menu(name="Menu"))
scrmanager.add_widget(Sell(name="Sell"))
scrmanager.add_widget(Cars(name="Cars"))


class RootApp(App):
	def build(self):
		return scrmanager


if __name__ == "__main__":
	RootApp().run()