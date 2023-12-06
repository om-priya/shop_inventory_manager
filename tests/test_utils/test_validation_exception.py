from utils.validation_exception import validation_exception


def test_true_function():
    return True


def test_false_function():
    return False


class TestValidationException:
    def test_validation_exception_true_func(self):
        expected_result = validation_exception(test_true_function)()
        assert expected_result == True

    def test_validation_exception_false_func(self, capsys):
        expected_result = validation_exception(test_false_function)()
        assert expected_result == False
