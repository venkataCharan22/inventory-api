"""Warehouse pick operations — BUG: indexes empty shelf."""

SHELVES = {
    "A1": [{"sku": "widget-101", "qty": 5}],
    "A2": [],  # empty!
}


def latest_pick(shelf_id):
    """Return the most recently restocked item from a shelf."""
    items = SHELVES.get(shelf_id, [])
    # BUG: IndexError on empty shelf
    return items[0]
