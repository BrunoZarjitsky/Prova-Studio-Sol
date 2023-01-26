from studio_sol_API import PasswordVerification
import string

# Return a string with accepted special characters
def get_special_characters():
    return "!@#$%^&*()-+\\/{}[]"

# Return a string with accepted lowercase letters
def get_lower_letters():
    return string.ascii_lowercase

# Return a string with accepted uppercase letters
def get_upper_letters():
    return string.ascii_uppercase

# Return a string with accepted digits
def get_digits():
    return string.digits

# Return a string with a test string
def get_test_string():
    special_characters = get_special_characters()
    lowwer_letters = get_lower_letters()
    upper_letters = get_upper_letters()
    digit_characters = get_digits()

    return special_characters + lowwer_letters + upper_letters + digit_characters

# Positive test with all rules
def test_verify_rules_pass():
    # arrange
    test_string = get_test_string()

    # act
    password_verification = PasswordVerification(
        password=test_string,
        rules=[
            {"rule": "minSize","value": len(test_string)},
            {"rule": "minLowercase", "value": len(get_lower_letters())},
            {"rule": "minUppercase", "value": len(get_upper_letters())},
            {"rule": "minSpecialChars","value": len(get_special_characters())},
            {"rule": "minDigit","value": len(get_digits())},
            {"rule": "noRepeted","value": 0},
        ]
    )

    # assert
    assert password_verification.pass_verify

# Negative test with minSize rule
def test_verify_minSize_fail():
    # arrange
    test_string = get_test_string()

    # act
    password_verification = PasswordVerification(
        password=test_string,
        rules=[
            {"rule": "minSize","value": len(test_string) + 1}
        ]
    )

    # assert
    assert not password_verification.pass_verify

# Negative test with minUppercase rule
def test_verify_minUppercase_fail():
    # arrange
    test_string = get_test_string()

    # act
    password_verification = PasswordVerification(
        password=test_string,
        rules=[
            {"rule": "minUppercase","value": len(get_upper_letters()) + 1}
        ]
    )

    # assert
    assert not password_verification.pass_verify

# Negative test with minLowercase rule
def test_verify_minLowercase_fail():
    # arrange
    test_string = get_test_string()

    # act
    password_verification = PasswordVerification(
        password=test_string,
        rules=[
            {"rule": "minLowercase","value": len(get_lower_letters()) + 1}
        ]
    )

    # assert
    assert not password_verification.pass_verify

# Negative test with minDigit rule
def test_verify_minDigit_fail():
    # arrange
    test_string = get_test_string()

    # act
    password_verification = PasswordVerification(
        password=test_string,
        rules=[
            {"rule": "minDigit","value": len(get_digits()) + 1}
        ]
    )

    # assert
    assert not password_verification.pass_verify

# Negative test with minSpecialChars rule
def test_verify_minSpecialChars_fail():
    # arrange
    test_string = get_test_string()

    # act
    password_verification = PasswordVerification(
        password=test_string,
        rules=[
            {"rule": "minSpecialChars","value": len(get_special_characters()) + 1}
        ]
    )

    # assert
    assert not password_verification.pass_verify

# Negative test with noRepeted rule
def test_verify_noRepeted_fail():
    # arrange
    test_string = "aabcd"

    # act
    password_verification = PasswordVerification(
        password=test_string,
        rules=[
            {"rule": "noRepeted","value": 0}
        ]
    )

    # assert
    assert not password_verification.pass_verify