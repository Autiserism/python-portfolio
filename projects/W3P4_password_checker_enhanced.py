import re
import logging

# Configure logging (don't log passwords!)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

checks = [
    (r'[A-Z]', "Needs at least 1 uppercase letter"),
    (r'[a-z]', "Needs at least 1 lowercase letter"),
    (r'\d', "Needs at least 1 digit"),
    (r'[!@#$%^&*]', "Needs at least 1 special character (!@#$%^&*)"),
    (r'.{8,}', "Needs to be at least 8 characters long")
]

weak_patterns = [
    (r'(.)\1{2,}', "Cannot have repeated characters (aaa, 111)"),
    (r'(012|123|234|345|456|567|678|789)', "Cannot have sequential numbers"),
    (r'(abc|bcd|xyz)', "Cannot have sequential letters"),
    (r'(password|admin|user|test)', "Cannot contain common words"),
    (r'(qwerty|asdfgh)', "Cannot contain keyboard patterns")
]

def check_password(password):
    """
    Check password strength and return score with suggestions.
    Returns: (score, suggestions_list)
    """
    score = 0
    suggest_fix = []

    # Check for spaces
    if ' ' in password:
        suggest_fix.append('❌ Password cannot contain spaces')
        return 0, suggest_fix

    # Check for weak patterns (case-insensitive)
    weak_found = 0
    for pattern, description in weak_patterns:
        if re.search(pattern, password, re.IGNORECASE):
            suggest_fix.append(f'⚠️  {description}')
            weak_found += 1

    # Check requirements
    for pattern, description in checks:
        if re.search(pattern, password):
            score += 1
        else:
            suggest_fix.append(f'❌ {description}')

    # Calculate final score (max 5, penalize weak patterns)
    final_score = max(0, score - weak_found)

    # Log attempt (without password!)
    logging.info(f'Password attempt: length={len(password)}, score={final_score}/5')

    return final_score, suggest_fix

def get_strength_label(score):
    """Return strength label based on score"""
    if score == 0:
        return "Very Weak 😱"
    elif score == 1:
        return "Weak 😟"
    elif score == 2:
        return "Fair 😐"
    elif score == 3:
        return "Good 🙂"
    elif score == 4:
        return "Strong 💪"
    else:
        return "Very Strong 🔥"

# Main program
print("=" * 60)
print("PASSWORD STRENGTH CHECKER")
print("=" * 60)
print("""
A strong password must have:
  ✓ At least 1 uppercase letter
  ✓ At least 1 lowercase letter
  ✓ At least 1 number
  ✓ At least 1 special character (!@#$%^&*)
  ✓ Minimum 8 characters long

Avoid:
  ✗ Common words (password, admin, user, test)
  ✗ Sequential characters (123, abc)
  ✗ Keyboard patterns (qwerty, asdfgh)
  ✗ Repeated characters (aaa, 111)
""")
print("=" * 60)

attempts = 0
while True:
    attempts += 1
    password = input('\nEnter a strong password: ').strip()

    if not password:
        print("Password cannot be empty!")
        continue

    score, suggestions = check_password(password)
    strength = get_strength_label(score)

    print(f"\nStrength: {score}/5 - {strength}")

    if suggestions:
        print("\nImprovements needed:")
        for suggestion in suggestions:
            print(f"  {suggestion}")

    if score >= 5:
        print("\n✓ Excellent! Password accepted.")
        logging.info(f'Strong password created after {attempts} attempts')
        break
    else:
        print("\n⚠️  Try again with a stronger password.")

print("\n" + "=" * 60)
print("Password successfully set!")
print("=" * 60)
