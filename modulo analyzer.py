import sys

def analyze_modular_classes(max_n):
    mod3_classes = {0: [], 1: [], 2: []}
    
    for i in range(1, max_n + 1):
        remainder = i % 3
        mod3_classes[remainder].append(i)
        
    print("=== MODULO 3 STRUCTURAL ANALYSIS ===")
    print(f"Total range checked: 1 to {max_n}\n")
    print(f"Class 0 (n ≡ 0 mod 3) [Dead Ends - No paths lead here]:")
    print(f"   {mod3_classes[0][:15]}...")
    print(f"Class 1 (n ≡ 1 mod 3) [Targets - Can be reached via 3n+1 from evens]:")
    print(f"   {mod3_classes[1][:15]}...")
    print(f"Class 2 (n ≡ 2 mod 3) [Pass-throughs]:")
    print(f"   {mod3_classes[2][:15]}...\n")

if len(sys.argv) > 1:
    max_range = int(sys.argv[1])
else:
    max_range = 100

analyze_modular_classes(max_range)