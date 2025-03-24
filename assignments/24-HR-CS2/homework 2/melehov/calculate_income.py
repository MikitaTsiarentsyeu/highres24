def calculate_income(principal: float, rate: float, years: int) -> float:
    return principal * (1 + rate / 100) ** years