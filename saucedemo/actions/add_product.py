from screenpy import Actor, beat
from screenpy_selenium import Click, Target


class Add:
    def __init__(self, product: Target) -> None:
        self.product: Target = product

    @staticmethod
    def the_product(product: Target) -> "Add":
        return Add(product)

    @beat("{} add some product to the cart")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(Click.on(self.product))
