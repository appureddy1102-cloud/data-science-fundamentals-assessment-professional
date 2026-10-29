"""Executable Python fundamentals examples and assertions; run from any directory."""
from pathlib import Path
from tempfile import TemporaryDirectory
import math

# Names should be descriptive; constants are uppercase by convention, not enforced.
TAX_RATE = 0.10
quantity = 3  # A comment explains intent; it does not execute.
price = 12.5
label = '  Data Science  '
active = True
unknown = None
print('Types:', *(type(x).__name__ for x in [quantity, price, label, active, unknown]))
print('Conversion:', int('12'), float('2.5'), str(42), isinstance(quantity, int))
print('Operators:', 7 + 2, 7 - 2, 7 * 2, 7 / 2, 7 // 2, 7 % 2, 7 ** 2)
count = 3
count += 2
print('Comparisons/logical/membership:', count == 5, count != 4, count > 3, count <= 5, active and count > 0, not active, 2 in [1, 2, 3])
print('String:', label.strip().lower(), label.strip()[0], label.strip()[0:4], label.replace('Science', 'Lab').strip())
items = ['pen', 'book']; items.append('ruler')
point = (2, 3); tags = {'a', 'a', 'b'}; record = {'name': 'Asha', 'score': 8}
print('Collections:', items, point, len(tags), record['name'])
if count > 5:
    grade = 'high'
elif count == 5:
    grade = 'medium'
else:
    grade = 'low'
print('Conditional:', grade)
kept = []
for number in range(6):
    if number == 2:
        continue
    if number == 5:
        break
    kept.append(number)
while_count = 0
while while_count < 3:
    while_count += 1
print('Loops:', kept, while_count)

def total_cost(units, unit_price):
    """Calculate gross cost; variables inside this function are local."""
    total = units * unit_price
    return total

squares = [x * x for x in range(5) if x % 2 == 0]
print('Function/comprehension:', total_cost(3, 12.5), squares, math.sqrt(16))

def parse_quantity(text):
    """Handle invalid input and demonstrate try/except/else/finally."""
    try:
        value = int(text)
    except ValueError:
        result = 'invalid integer'
    else:
        result = value * 2
    finally:
        pass  # Cleanup would run here whether or not conversion succeeds.
    return result
print('Exceptions:', parse_quantity('4'), parse_quantity('bad'))
with TemporaryDirectory() as tmp:
    file_path = Path(tmp) / 'example.txt'
    file_path.write_text('hello\n', encoding='utf-8')
    print('File:', file_path.read_text(encoding='utf-8').strip())
# Lightweight tests: failure raises AssertionError and stops the run.
assert total_cost(3, 12.5) == 37.5
assert squares == [0, 4, 16] and kept == [0, 1, 3, 4]
assert parse_quantity('4') == 8 and parse_quantity('bad') == 'invalid integer'
print('All assertions passed')
