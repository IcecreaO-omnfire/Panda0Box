from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
import time
class Magip(ShowBase):
    def __init__(self):
            sap=time.clock()
            ShowBase.__init__(self)
            sap=time.clock()-sap
            print(sap)		


    def setupCollisions(self): 
            self.playerGroundSphere = CollisionSphere(0,1.5,-1.5,1.5) 
            self.bdsto = CollisionSphere(0,4.5,-4.5,4.5) 
            self.playerGroundCol = CollisionNode('playerSphere') 
            self.world=loader.loadModel("SandPlan")
            self.world.reparentTo(render)
            self.playerGroundCol.addSolid(self.playerGroundSphere) 
            self.playerGroundCol.addSolid(self.bdsto) 
            self.debug = True
            self.colleTrav = CollisionTraverser() 


            self.playerGroundCol.addSolid(self.playerGroundSphere) 

            # bitmasks 
            self.playerGroundCol.setFromCollideMask(BitMask32.bit(0)) 
            self.playerGroundCol.setIntoCollideMask(BitMask32.allOff()) 
            self.world.setCollideMask(BitMask32.bit(0)) 

            # and done 
            self.playerGroundColNp = self.plte.attachNewNode(self.playerGroundCol) 
            self.playerGroundHandler = CollisionHandlerQueue() 
            self.colleTrav.addCollider(self.playerGroundColNp, self.playerGroundHandler) 

            # DEBUG 
            if (self.debug == True): 
                self.playerGroundColNp.show() 
                self.colleTrav.showCollisions(self.render)

    def hiup(self,task):
        self.colleTrav.traverse(self.render) 
    #for i in range(self.playerGroundHandler.getNumEntries()): 
    #    entry = self.playerGroundHandler.getEntry(i) 
print("Magip")

#lono=loader.loadModel("panda")
#rig=lono.findAllMatches("**/+GeomNode")
#ga=rig.getPath(0)

#print(ga)
