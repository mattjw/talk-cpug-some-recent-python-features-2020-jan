def prefixer(dictionary, prefix):
    return {f"{prefix}{key}": value for key, value in dictionary.items()}

def suffixer(dictionary, suffix):
    return {f"{key}{suffix}": value for key, value in dictionary.items()}

def prefixer_suffixer(dictionary, part):
    # breakpoint()
    print(f"Step A: {dictionary=}")
    dictionary = prefixer(dictionary, part)
    print(f"Step B: {dictionary=}")
    dictionary = suffixer(dictionary, part)
    print(f"Step C: {dictionary=}")
    return dictionary

original_dict = {
    "a": 1,
    "b": 2,
}
print(f"from: {original_dict}")

weird_dict = prefixer_suffixer(original_dict, "__")
print(f"to: {weird_dict}")
