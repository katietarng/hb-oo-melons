"""This file should have our order classes in it."""
from random import randint
from datetime import datetime

class AbstractMelonOrder(object):
    """ Parent class for melon orders. """

    #Country code is set to optional param because domestic order does not have one
    def __init__(self, species, qty, country_code = None): 

        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

    def get_base_price(self):
        """Get random base price. Add splurge pricing for weekday mornings."""

        base_price = randint(5,9)

        #Get current time and turn it into a tuple so that we can index
        current_time = datetime.now()
        current_time = current_time.timetuple()

        #In current time tuple, hour = index[3] and day = index[6]
        #Used range to define time and day bounds: 8am-11am, M-F
        if current_time[3] in range(8,12) and current_time[6] in range(0,5):
            base_price += 4

        return base_price

    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()

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


class GovernmentMelonOrder(AbstractMelonOrder):
    """A Government melon order."""

    order_type = "government"
    tax = 0.0
    passed_inspection = False

    def mark_inspection(self):
        """Set inspection status to true."""
        self.passed_inspection = True


