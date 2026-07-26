def determine_package(budget: float):

    if budget < 5:
        return "Starter Package"

    elif budget <= 15:
        return "Premium Package"

    return "Luxury Package"