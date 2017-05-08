"""
Grader file for NMF problem
"""
def grade(autogen, key):
  if "bugs" in key.lower().strip():
    return (True, 'Good work!')
  else:
    return (False, 'Nope')
