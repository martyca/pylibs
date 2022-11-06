from subprocess import Popen, PIPE, CalledProcessError

def terraform(*args):
  '''Execute terraform and print stdout line by line.'''
  with Popen(["terraform", *args], stdout=PIPE, bufsize=1, universal_newlines=True) as process:
    for line in process.stdout:
      print(line, end='')
  if process.returncode != 0:
    raise CalledProcessError(process.returncode, process.args)

if __name__ == "__main__":
  terraform("--version")
  terraform("--help")
