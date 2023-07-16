import zope.interface
from twisted.plugin import IPlugin
from matsim import imatsim

@zope.interface.implementer(IPlugin, imatsim.IMaterial)
class SimpleMaterial(object):

    def __init__(self, yieldStressFactor, dielectricConstant):
        self._yieldStressFactor = yieldStressFactor
        self.dielectricConstant = dielectricConstant

    def yieldStress(self, temperature):
        return self._yieldStressFactor * temperature


steelPlate = SimpleMaterial(2.06842719e11, 2.7 + 0.2j)
brassPlate = SimpleMaterial(1.03421359e11, 1.4 + 0.5j)
