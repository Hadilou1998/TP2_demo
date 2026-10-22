import pytest

from bibliotech import late_fee

@pytest.mark.parametrize(
    ("days_late", "kind", "member_type", "price", "expected"),
    [
        (0, "book", "standard",12.90, 0.0),
        (10, "book", "standard",12.90, 5.0),
        (10, "dvd", "standard",14.99, 10.0),
        (10, "dvd", "student",14.99, 5.0),
        (10, "book", "premium",12.90, 0.0),
        (100, "book", "standard", 12.90,12.90),
        (10, "cd", "standard", 9.99, 5.0),
    ]
)

def test_late_fee(days_late, kind, member_type, price, expected):
    assert late_fee(days_late, kind, member_type, price) == pytest.approx(expected)