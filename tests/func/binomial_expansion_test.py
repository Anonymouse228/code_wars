import pytest

from binomial_expansion import expand, get_coefficients, get_readable_term


expand_data_set = (
    ('(x+1)^0', '1'),
    ('(x+1)^1', 'x+1'),
    ('(x+1)^2', 'x^2+2x+1'),
    ('(x-1)^0', '1'),
    ('(x-1)^1', 'x-1'),
    ('(x-1)^2', 'x^2-2x+1'),
    ('(5m+3)^4', '625m^4+1500m^3+1350m^2+540m+81'),
    ('(2x-3)^3', '8x^3-36x^2+54x-27'),
    ('(7x-7)^0', '1'),
    ('(-5m+3)^4', '625m^4-1500m^3+1350m^2-540m+81'),
    ('(-2k-3)^3', '-8k^3-36k^2-54k-27'),
    ('(-7x-7)^0', '1'),
)

coefficients_data_set = (
    ('(x+1)^0', ('1', 'x', '+1', '0')),
    ('(x+1)^1', ('1', 'x', '+1', '1')),
    ('(x+1)^2', ('1', 'x', '+1', '2')),
    ('(x-1)^0', ('1', 'x', '-1', '0')),
    ('(x-1)^1', ('1', 'x', '-1', '1')),
    ('(x-1)^2', ('1', 'x', '-1', '2')),
    ('(5m+3)^4', ('5', 'm', '+3', '4')),
    ('(2x-3)^3', ('2', 'x', '-3', '3')),
    ('(7x-7)^0', ('7', 'x', '-7', '0')),
    ('(-5m+3)^4', ('-5', 'm', '+3', '4')),
    ('(-2k-3)^3', ('-2', 'k', '-3', '3')),
    ('(-7x-7)^0', ('-7', 'x', '-7', '0')),
)

terms_data_set = (
    (10, 'x', 2, '+10x^2'),
    (-10, 'y', 2, '-10y^2'),
    (-1, 'z', 5, '-z^5'),
    (1, 'x', 5, '+x^5'),
    (1, 'y', 1, '+y'),
    (0, 'z', 10, ''),
    (1, 'x', 0, '+1'),
    (-11, 'y', 0, '-11'),
)


@pytest.mark.parametrize('expression, expected_expression', expand_data_set)
def test_expand_equals(expression, expected_expression):
    assert expand(expression) == expected_expression


@pytest.mark.parametrize('expression, expected_coefficients', coefficients_data_set)
def test_get_coefficients_equals(expression, expected_coefficients):
    assert get_coefficients(expression) == expected_coefficients


@pytest.mark.parametrize('coefficient, x, degree, expected_term', terms_data_set)
def test_get_readable_term_equals(coefficient, x, degree, expected_term):
    assert get_readable_term(coefficient, x, degree) == expected_term
