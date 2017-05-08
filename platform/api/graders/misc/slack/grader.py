"""
Grader file for Slack problem
"""

def grade(autogen, key):
  if key == "flag{I_uSe_Slack_rEgulArly}":
    return (True, 'Good work!')
  else:
    return (False, 'Nope')
