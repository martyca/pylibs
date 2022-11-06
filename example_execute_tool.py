import sys
sys.path.append('./modules/')
import execute_tool

execute_tool.terraform("--version")
execute_tool.terraform("--help")

