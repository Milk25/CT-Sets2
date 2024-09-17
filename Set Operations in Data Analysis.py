customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]


def difference_in_ids():
    ids = set(customer_ids)

    print(f"These ids are unique {ids}")


difference_in_ids()