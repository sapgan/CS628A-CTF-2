"""
Grader file for Robot problem
"""
def grade(autogen, key):
  if "samykamkar" in key.lower().strip():
    return (True, 'Good work!')
  else:
    return (False, 'Nope')
