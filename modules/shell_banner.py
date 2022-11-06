colors = {
  'PURPLE':    '\033[95m',
  'OKBLUE':    '\033[34m',
  'OKCYAN':    '\033[96m',
  'OKGREEN':   '\033[92m',
  'INFO':      '\033[93m',
  'ERROR':     '\033[91m',
  'RESET':     '\033[0m',
  'BOLD':      '\033[1m',
  'UNDERLINE': '\033[4m'
}

def print_banner(message):
  '''Encapsulate message in pound symbols (#) to create the effect of a banner.'''
  message_length = len(message)
  print("###{}###".format("#" * message_length))
  print("## {} ##".format(message))
  print("###{}###".format("#" * message_length))

def print_purple(message):
  '''Print the message banner in the colour purple'''
  print(colors['PURPLE'], end='')
  print_banner(message)
  print(colors['RESET'], end='')

def print_blue(message):
  '''Print the message banner in the colour blue'''
  print(colors['OKBLUE'], end='')
  print_banner(message)
  print(colors['RESET'], end='')

def print_cyan(message):
  '''Print the message banner in the colour cyan'''
  print(colors['OKCYAN'], end='')
  print_banner(message)
  print(colors['RESET'], end='')

def print_ok(message):
  '''Print the message banner in the colour green'''
  print(colors['OKGREEN'], end='')
  print_banner(message)
  print(colors['RESET'], end='')

def print_info(message):
  '''Print the message banner in the colour yellow'''
  print(colors['INFO'], end='')
  print_banner(message)
  print(colors['RESET'], end='')

def print_error(message):
  '''Print the message banner in the colour red'''
  print(colors['ERROR'], end='')
  print_banner(message)
  print(colors['RESET'], end='')

if __name__ == '__main__':
  print_ok("All is well.")
  print_info("You might be interesting in this.")
  print_error("Abandon ship, all hands to battle stations!!!")
  print_cyan("Give it a little cyan flair.")
  print_blue("I'm blue daboodee...")
  print_purple("Purple the colour of royalty.")
  print_banner("Sometimes you just want a banner.")