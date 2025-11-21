"""Functions to manage a users shopping cart items."""

from typing import Iterable


def add_item(
    current_cart: dict[str, int], items_to_add: Iterable[str]
) -> dict[str, int]:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart[item] = current_cart.setdefault(item, 0) + 1
    return current_cart


def read_notes(notes: Iterable[str]) -> dict[str, int]:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return dict.fromkeys(notes, 1)


def update_recipes(
    ideas: dict[str, dict[str, int]],
    recipe_updates: Iterable[tuple[str, dict[str, int]]],
) -> dict[dict[str, int]]:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    for update in recipe_updates:
        ideas |= update
    return ideas


def sort_entries(cart: dict[str, int]) -> dict[str, int]:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(
    cart: dict[str, int], isle_mapping: dict[str, list]
) -> dict[str, list]:
    """Combine users order to isle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param isle_mapping: dict - isle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    for item, [isle, refrigeration] in isle_mapping.items():
        cart[item] = [cart[item], isle, refrigeration]
    return dict(reversed(sorted(cart.items())))


def update_store_inventory(
    fulfillment_cart: dict[str, int], store_inventory: dict[str, int | str]
) -> dict[str, int | str]:
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for item, amount in fulfillment_cart.items():
        store_inventory[item][0] -= amount
        if store_inventory[item][0] <= 0:
            store_inventory[item][0] = "Out of Stock"
    return store_inventory
