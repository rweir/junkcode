"""Plugin consumer interfaces for matsim."""

from zope.interface import Interface, Attribute


class IMaterial(Interface):
    """
    An object with specific physical properties
    """

    def yieldStress(temperature):
        """
        Returns the pressure this material can support without
        fracturing at the given temperature.

        @type temperature: C{float}
        @param temperature: Kelvins

        @rtype: C{float}
        @return: Pascals
        """

    dielectricConstant = Attribute(
        """
        @type dielectricConstant: C{complex}
        @ivar dielectricConstant: The relative permittivity, with the
        real part giving reflective surface properties and the
        imaginary part giving the radio absorption coefficient.
        """
    )
