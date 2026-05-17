# inventory-api

A small inventory-tracking REST API with intentional bugs for Bug2PR demos.

## Bugs in this repo

- `app/warehouse.py` — IndexError when picking from an empty shelf
- `app/stock.py` — TypeError when stock count is None
- `app/orders.py` — KeyError on missing SKU
