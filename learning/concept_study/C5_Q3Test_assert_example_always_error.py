# Write an assert statement that always triggers an AssertionError.
# This one is straightforward — think about what value is always False

eggs = 0
assert eggs == True
# Works — 0 == True is always False so it always triggers

# The simplest version is even shorter though:
assert False
# Since False is always False, no variables needed
