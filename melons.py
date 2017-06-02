"""Classes for melon orders."""
import random

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, country_code, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.country_code = country_code
        self.base_price = None

    def get_total(self):
        """Calculate price, including tax."""

        price = self.get_base_price()
        if self.species.lower() == 'christmas':
            price *= 1.5
        total = (1 + self.tax) * self.qty * price

        return total
    
    def get_base_price(self):
        """Get base price."""
        if not self.base_price:
            self.base_price = random.randint(5, 9)
        return self.base_price

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(DomesticMelonOrder, self).__init__(species, qty, country_code="US",
                                                 order_type="domestic", tax=0.08)
       
        # self.order_type = "domestic"
        # self.tax = 0.08

class GovernmentMelonOrder(AbstractMelonOrder):
    """ Goverment Melon Orders!!"""
    def __init__(self,species,qty):
        self.passed_inspection = False
        super(GovernmentMelonOrder, self).__init__(species, qty,country_code="US",
                                                order_type ="government", tax =0)

    def mark_inspection(self, passed):
        """Melon Secuirty Test Pass or Fail."""
        if passed:
            self.passed_inspection = True

        

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order.""" 

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super(InternationalMelonOrder, self).__init__(species, qty, country_code,
                                                    order_type="international", tax=0.17)

        # self.country_code = country_code
        # self.order_type = "international"
        # self.tax = 0.17
    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3
        return total


    
