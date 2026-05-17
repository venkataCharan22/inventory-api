"""Order fulfillment — BUG: KeyError on missing SKU."""

CATALOG = {
    "widget-101": {"price": 9.99, "weight": 0.5},
}


def get_price(sku):
    """Look up a SKU's price."""
    # BUG: KeyError when SKU doesn't exist
    return CATALOG[sku]["price"]


def shipping_cost(sku, qty):
    weight = CATALOG.get(sku, {}).get("weight", 1.0)
    return round(weight * qty * 1.50, 2)
