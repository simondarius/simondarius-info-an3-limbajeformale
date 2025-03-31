def pumping_lemma_demonstration_1():
    p = 10
    s = "0" * (p + 1) + "1" * p
    
    x = ""
    y = "0" * p
    z = "0" + "1" * p
    
    pumped_string = x + z  # y^0 = ""
    num_zeros = pumped_string.count("0")
    num_ones = pumped_string.count("1")
    
    print(f"L = {{0^i 1^j | i>j}} is not regular:")
    print(f"For s = {s}, we divide it as: x='{x}', y='{y}', z='{z}'")
    print(f"xy^0z = '{pumped_string}' has {num_zeros} 0's and {num_ones} 1's")
    print(f"Since {num_zeros} <= {num_ones}, this string is not in the language.")


def pumping_lemma_demonstration_2():
    p = 10
    s = "a" * p + "b" * p
    
    x = ""
    y = "a" * p
    z = "b" * p
    
    n = 2
    pumped_string = x + y * n + z
    num_as = pumped_string.count("a")
    num_bs = pumped_string.count("b")
    
    print(f"L = {{a^i b^j | i≤j}} is not regular:")
    print(f"For s = {s}, we divide it as: x='{x}', y='{y}', z='{z}'")
    print(f"xy^{n}z = '{pumped_string}' has {num_as} a's and {num_bs} b's")
    print(f"Since {num_as} > {num_bs}, this string is not in the language.")


def pumping_lemma_demonstration_3():
    p = 5
    n = p
    s = "a" * n + "b" * n + "c" * n
    
    x = "a"
    y = "a"
    z = "a" * (n - 2) + "b" * n + "c" * n
    
    pump_factor = 2
    pumped_string = x + y * pump_factor + z
    
    num_as = pumped_string.count("a")
    num_bs = pumped_string.count("b")
    num_cs = pumped_string.count("c")
    
    print(f"L = {{a^n b^n c^n | n>0}} is not regular:")
    print(f"For s = {s}, we divide it as: x='{x}', y='{y}', z='{z}'")
    print(f"xy^{pump_factor}z = '{pumped_string}' has {num_as} a's, {num_bs} b's, {num_cs} c's")
    print(f"Since these counts are not equal, this string is not in the language.")


if __name__ == "__main__":
    pumping_lemma_demonstration_1()
    print()
    pumping_lemma_demonstration_2()
    print()
    pumping_lemma_demonstration_3()