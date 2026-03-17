from logic_utils import check_guess, parse_guess


def test_parse_guess_rejects_value_below_range():
    result = parse_guess("0")

    assert result == (
        False,
        None,
        "This number is out of range. Please enter a value between 1 and 100",
    )


def test_parse_guess_rejects_value_above_range():
    result = parse_guess("101")

    assert result == (
        False,
        None,
        "This number is out of range. Please enter a value between 1 and 100",
    )


def test_guess_too_high_tells_user_to_go_lower():
    outcome, message = check_guess(60, 50)

    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low_tells_user_to_go_higher():
    outcome, message = check_guess(40, 50)

    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
