import random

print("Welcome to the EC2 Random Name Generator!")

# Step 1: Ask how many EC2 instances they need names for
num_instances = int(input("How many EC2 instances do you need names for? "))

# Step 2: Ask for their department name
department = input("Enter your department (Marketing, Accounting, FinOps): ").strip()

# Step 3: Check if the department is allowed and matches the correct capitalization
allowed_departments = ["Marketing", "Accounting", "FinOps"]
if department not in allowed_departments:
    print(f"Error: The department '{department}' is not authorized to use this Name Generator.")
    print("Please ensure you enter the department name exactly as: Marketing, Accounting, or FinOps.")
else:
    # Step 4: Generate unique names
    print("\nGenerated Unique EC2 Instance Names:")
    for i in range(num_instances):
        # Generate random characters and numbers
        random_chars = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=3))  # 3 random letters
        random_numbers = ''.join(random.choices("0123456789", k=4))               # 4 random digits
        
        # Create a unique name
        unique_name = f"{department}-{random_chars}{random_numbers}"
        print(unique_name)