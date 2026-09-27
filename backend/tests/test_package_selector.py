from app.conversation.package_selector import determine_package


def test_starter_package():
    assert determine_package(4.99) == "Starter Package"


def test_premium_lower_bound():
    assert determine_package(5) == "Premium Package"


def test_premium_upper_bound():
    assert determine_package(15) == "Premium Package"


def test_luxury_package():
    assert determine_package(15.01) == "Luxury Package"
