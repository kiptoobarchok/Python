#!/usr/bin/python3
import cmd
import sys
 
class custom_cmd(cmd.Cmd):
    prompt = "($) "

    def postcmd(self, stop, line):
        print(f"command execution completed. stopping commmand ({line})")
        return stop

    def precmd(self, line):
        print(f"preparing to execute command: ({line})")
        return line

    def do_greet(self, args):
        "prints a greeting"
        names = args.split()

        if len(names) == 1:
            print(f"Hello {names[0]}")

        elif len(names) == 2:
            print(f"Hello {names[0]} and {names[1]}")

        else:
            print("Hello there strangers...")
        

    def do_add(self, args):
        "perform simple calculation"
        num = args.split()

        if len(num) != 2:
            print("Error: Invalid number of args")

        else:
            try:
                num1 = int(num[0])
                num2 = int(num[1])
                res = num1 + num2
                print(f"{num1} + {num2} = {res}")
            except ValueError:
                print("Error: Invalid number of args")

    def do_exit(self, args):
        print("Bye!!")
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    custom_cmd().cmdloop()
