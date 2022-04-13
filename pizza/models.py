from django.db import models
from django.contrib.auth.models import User

class ProperOrder(models.Model):
    order_client = models.ForeignKey(User, on_delete=models.CASCADE)
    order_timestamp = models.DateTimeField(auto_now_add=True)
    order_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    order_done = models.BooleanField(default=False)

    def __str__(self):
        return f"Order number {self.id}"


class PizzaTopping(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class PizzaType(models.Model):
    name = models.CharField(max_length=60, unique=True)
    price_sm_0 = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    price_sm_1 = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    price_sm_2 = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    price_sm_3 = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    price_sm_4 = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    price_lg_0 = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    price_lg_1 = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    price_lg_2 = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    price_lg_3 = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    price_lg_4 = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    in_order = models.ForeignKey(ProperOrder, on_delete=models.CASCADE, null=True, blank=True, related_name="pizzas")
    already_ordered = models.BooleanField(default=False)
    add_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    pizza_size = models.CharField(
        max_length=2,
        choices=(
            ("sm", "small"),
            ("lg", "large")
        ),
    )
    pizzatype = models.ForeignKey(PizzaType, on_delete=models.CASCADE, null=True)
    toppings = models.ManyToManyField(PizzaTopping, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, editable=False)

    def calculate_price(self):
        if self.toppings.all().count() > 4:
            pizza_topping_amount = 4
        else:
            pizza_topping_amount = self.toppings.all().count()
        self.price = eval("self.pizzatype.price_" + str(self.pizza_size) + "_" + str(pizza_topping_amount))

    def __str__(self):
        return f"{self.pizzatype.name} {self.get_pizza_size_display()} with {self.toppings.all().count()} topping(s)"

    class Meta:
        verbose_name_plural = "Pizza Pies"
        