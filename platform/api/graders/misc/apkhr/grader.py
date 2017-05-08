"""
Grader file for ApkHR problem
"""

def grade(autogen, key):
  if "cs628a{978360d545acfc8dea2bbeddec27a211}" in key.lower().strip():
    return (True, 'Good app reversing!')
  else:
    return (False, 'Nope')
