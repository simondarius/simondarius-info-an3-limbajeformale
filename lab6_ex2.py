import re

def parse_language(expression):
    if not expression.startswith('{') or not expression.endswith('}'):
        print("Error: Language must be enclosed in {}.")
        return set()
        
    content = expression[1:-1].strip()
    if not content:
        return {""}
    
    elements = [elem.strip() for elem in content.split(',')]
    return set(elements)

def display_language(language):
    if not language:
        return "{}"
    if language == {""}:
        return "{ε}"
    
    elements = sorted(language)
    return "{" + ",".join(elements) + "}"

def union(lang1, lang2):
    return lang1.union(lang2)

def intersection(lang1, lang2):
    return lang1.intersection(lang2)

def concatenation(lang1, lang2):
    result = set()
    for s1 in lang1:
        for s2 in lang2:
            result.add(s1 + s2)
    return result

def difference(lang1, lang2):
    return lang1.difference(lang2)

def kleene_star(language, limit=3):
    result = {""}
    current = language.copy()
    
    result = result.union(current)
    
    for i in range(2, limit + 1):
        current = concatenation(current, language)
        result = result.union(current)
        
    return result

def main():
    print("Regular Language Operations Tool")
    
    while True:
        lang1_expr = input("\nEnter first language L1: ")
        lang2_expr = input("Enter second language L2: ")
        
        lang1 = parse_language(lang1_expr)
        lang2 = parse_language(lang2_expr)
        
        print(f"\nL1 = {display_language(lang1)}")
        print(f"L2 = {display_language(lang2)}")
        
        while True:
            print("\n1. Union (L1 ∪ L2)")
            print("2. Intersection (L1 ∩ L2)")
            print("3. Concatenation (L1 · L2)")
            print("4. Difference (L1 - L2)")
            print("5. Kleene Star (L1* or L2*)")
            print("6. Enter new languages")
            print("7. Exit")
            
            choice = input("Enter choice: ")
            
            if choice == '1':
                result = union(lang1, lang2)
                print(f"L1 ∪ L2 = {display_language(result)}")
            
            elif choice == '2':
                result = intersection(lang1, lang2)
                print(f"L1 ∩ L2 = {display_language(result)}")
            
            elif choice == '3':
                result = concatenation(lang1, lang2)
                print(f"L1 · L2 = {display_language(result)}")
            
            elif choice == '4':
                result = difference(lang1, lang2)
                print(f"L1 - L2 = {display_language(result)}")
            
            elif choice == '5':
                star_choice = input("Choose (1 for L1*, 2 for L2*): ")
                
                if star_choice == '1':
                    result = kleene_star(lang1)
                    print(f"L1* = {display_language(result)}")
                elif star_choice == '2':
                    result = kleene_star(lang2)
                    print(f"L2* = {display_language(result)}")
                else:
                    print("Invalid choice!")
            
            elif choice == '6':
                break
            
            elif choice == '7':
                return
            
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    main()