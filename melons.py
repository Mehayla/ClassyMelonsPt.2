"""Classes for melon orders."""

class AbstractMelon():
    "Just a simple melon"

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""
        
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == 'Christmas melons':
            base_price = 7.50

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == 'international' and self.qty < 10:
            total += 3
        
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelon):
    """A melon order for the white house (or other prts of the US Gov)"""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty, "government", 0)
        self.passed_inspection = False
    
    def mark_inspection(self):
        """Record the fact than an order has been shipped."""
        
        self.passed_inspection = True


class DomesticMelonOrder(AbstractMelon):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty, 'domestic', 0.08)


class InternationalMelonOrder(AbstractMelon):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty, 'international', 0.17) 
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
