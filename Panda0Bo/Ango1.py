from direct.actor.Actor import Actor

class ango():
	def __init__(self):
		self.sano=Actor("Sbig.egg",{"Anaib":"Sbig-Armsjin"})
		self.sano.reparentTo(render)
		self.sano.loop("Anaib")

runi=ango()