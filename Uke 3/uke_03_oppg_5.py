år = float(input("Angi menneskeår: "))
if år <= 2:
    print(f"Dette tilsvarer {år*10.5} hundeår.")
if år > 2:
    print(f"Dette tilsvarer {21+(år-2)*4} hundeår.")