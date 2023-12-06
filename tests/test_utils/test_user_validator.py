import pytest
from utils.user_validator import (
    validator,
    name_validator,
    email_validator,
    gender_validator,
    phone_validator,
    shop_validator,
    password_validator,
)
from unittest import mock

valid_input_data = [
    (r"^[A-Za-z]+([\ A-Za-z]+)*", "Om Priya"),
    (r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}", "ompriya18153789@gmail.com"),
    (r"[M,F]{1}$", "M"),
    (r"^[0-9]{10}$", "8229070126"),
    (r"^[A-Za-z]+([\ A-Za-z]+)*", "antriksh kirana"),
    (r"[0-9]{4}$", "2002"),
]

invalid_input_data = [
    (r"^[A-Za-z]+([\ A-Za-z]+)*", "Om12 Priya"),
    (r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}", "omgmail.com"),
    (r"[M,F]{1}$", "A"),
    (r"^[0-9]{10}$", "8229070"),
    (r"^[A-Za-z]+([\ A-Za-z]+)*", "antriksh12 kirana"),
    (r"[0-9]{4}$", "202"),
]


def mock_deco(func):
    return func


class TestUserValidator:
    @pytest.mark.parametrize("pattern, input_data", valid_input_data)
    def test_validator(self, pattern, input_data):
        expected = True
        mock.patch("utils.user_validator.validation_exception", mock_deco)
        actual = validator(pattern, input_data)
        assert expected == actual

    @pytest.mark.parametrize("pattern, input_data", invalid_input_data)
    def test_validator(self, pattern, input_data):
        mock.patch("utils.user_validator.validation_exception", mock_deco)
        with pytest.raises(Exception):
            actual = validator(pattern, input_data)

    @mock.patch("builtins.input")
    @mock.patch("utils.user_validator.validator")
    def test_name_validator(self, mock_validator, mock_input):
        mock_input.return_value = "om priya"
        mock_validator.return_value = True
        expected_value = name_validator()
        assert expected_value == "om priya"

    @mock.patch("builtins.input")
    @mock.patch("utils.user_validator.validator")
    def test_email_validator(self, mock_validator, mock_input):
        mock_input.return_value = "ompriya18153789@gmail.com"
        mock_validator.return_value = True
        expected_value = email_validator()
        assert expected_value == "ompriya18153789@gmail.com"

    @mock.patch("builtins.input")
    @mock.patch("utils.user_validator.validator")
    def test_gender_validator(self, mock_validator, mock_input):
        mock_input.return_value = "M"
        mock_validator.return_value = True
        expected_value = gender_validator()
        assert expected_value == "M"

    @mock.patch("utils.user_validator.maskpass.advpass")
    @mock.patch("utils.user_validator.validator")
    def test_password_validator(self, mock_validator, mock_input):
        mock_input.return_value = "Ompriya@2002"
        mock_validator.return_value = True
        expected_value = password_validator()
        assert expected_value == "Ompriya@2002"

    @mock.patch("builtins.input")
    @mock.patch("utils.user_validator.validator")
    def test_phone_validator(self, mock_validator, mock_input):
        mock_input.return_value = "8229070126"
        mock_validator.return_value = True
        expected_value = phone_validator()
        assert expected_value == "8229070126"

    @mock.patch("builtins.input")
    @mock.patch("utils.user_validator.validator")
    def test_shop_validator(self, mock_validator, mock_input):
        mock_input.return_value = "Antriksh Kirana"
        mock_validator.return_value = True
        expected_value = shop_validator()
        assert expected_value == "Antriksh Kirana"
