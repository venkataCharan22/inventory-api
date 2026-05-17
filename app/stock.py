"""Stock counting — BUG: TypeError when count is None."""


def restock(current, incoming):
    """Add incoming inventory to current count."""
    # BUG: current can be None for new SKUs, crashes
    return current + incoming


def is_in_stock(count):
    return count > 0
