# Write an assert statement that triggers an AssertionError if the variables
# eggs and bacon contain strings that are the same as each other, even if their cases are different.
# (That is, 'hello' and 'hello' are considered the same, and make 'goodbye' and 'GOODbye'. read the same)
# string method that converts any string to all lowercase: .lower()
# So "GOODbye".lower() returns "goodbye".


eggs = ("goodbye")
bacon = ("GOODbye")

assert eggs.lower() != bacon.lower()
# Read it as: "Assert that eggs and bacon are NOT the same. If they are the same, crash."
