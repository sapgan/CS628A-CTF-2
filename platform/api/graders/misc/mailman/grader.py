"""
Grader file for Mailman problem
"""

def grade(autogen, key):
  if "sapgan" in key.lower().strip():
    return (True, 'You are a true genius!')
  else:
    return (False, 'Nope')
