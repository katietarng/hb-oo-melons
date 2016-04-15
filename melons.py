"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """ Parent class for melon orders. """

    #Country code is set to optional param because domestic order does not have one
    def __init__(self, species, qty, country_code = None): 

        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

    def get_total(self):
        """Calculate price."""

        base_price = 5

        #Christmas melon price is 1.5 times more
        if self.species == 'Christmas melon':
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        #$3 surcharge for international orders less than 10 melons
        if self.qty < 10 and self.order_type == 'international':
            total = total + 3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
