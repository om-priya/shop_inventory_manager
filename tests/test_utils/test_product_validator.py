import pytest
from utils.product_validator import (
    validator,
    name_validator,
    price_validator,
    quantity_validator,
    discount_validator,
    category_validator,
    year_validator,
)
from unittest import mock

valid_input_data = [
    (r"^[A-Za-z]+([\ A-Za-z]+)*", "Om Priya"),
    (r"[0-9]*[.][0-9]*", "34.69"),
    (r"\d+", "32"),
    (r"[0-9]*[.][0-9]*", "2.00"),
    (r"^[A-Za-z]+([\ A-Za-z]+)*", "beverages"),
    (r"[0-9]{4}$", "2002"),
]

invalid_input_data = [
    (r"^[A-Za-z]+([\ A-Za-z]+)*", "Om23 Priya"),
    (r"[0-9]*[.][0-9]*", "3469"),
    (r"\d+", "ab"),
    (r"[0-9]*[.][0-9]*", "200"),
    (r"^[A-Za-z]+([\ A-Za-z]+)*", "beverages123"),
    (r"[0-9]{4}$", "abc"),
]


def mock_deco(func):
    return func


class TestProductValidator:
    @pytest.mark.parametrize("pattern, input_data", valid_input_data)
    def test_validator(self, pattern, input_data):
        expected = True
        mock.patch("utils.product_validator.validation_exception", mock_deco)
        actual = validator(pattern, input_data)
        assert expected == actual

    @pytest.mark.parametrize("pattern, input_data", invalid_input_data)
    def test_validator(self, pattern, input_data):
        mock.patch("utils.product_validator.validation_exception", mock_deco)
        with pytest.raises(Exception):
            actual = validator(pattern, input_data)

    @mock.patch("builtins.input")
    @mock.patch("utils.product_validator.validator")
    def test_name_validator(self, mock_validator, mock_input):
        mock_input.return_value = "om priya"
        mock_validator.return_value = True
        expected_value = name_validator()
        assert expected_value == "om priya"

    @mock.patch("builtins.input")
    @mock.patch("utils.product_validator.validator")
    def test_price_validator(self, mock_validator, mock_input):
        mock_input.return_value = "23.99"
        mock_validator.return_value = True
        expected_value = price_validator()
        assert expected_value == "23.99"

    @mock.patch("builtins.input")
    @mock.patch("utils.product_validator.validator")
    def test_quantity_validator(self, mock_validator, mock_input):
        mock_input.return_value = "23"
        mock_validator.return_value = True
        expected_value = quantity_validator()
        assert expected_value == "23"

    @mock.patch("builtins.input")
    @mock.patch("utils.product_validator.validator")
    def test_discount_validator(self, mock_validator, mock_input):
        mock_input.return_value = "2.00"
        mock_validator.return_value = True
        expected_value = discount_validator()
        assert expected_value == "2.00"

    @mock.patch("builtins.input")
    @mock.patch("utils.product_validator.validator")
    def test_category_validator(self, mock_validator, mock_input):
        mock_input.return_value = "beverages"
        mock_validator.return_value = True
        expected_value = category_validator()
        assert expected_value == "beverages"

    @mock.patch("builtins.input")
    @mock.patch("utils.product_validator.validator")
    def test_year_validator(self, mock_validator, mock_input):
        mock_input.return_value = "2002"
        mock_validator.return_value = True
        expected_value = year_validator()
        assert expected_value == "2002"
