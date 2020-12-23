class Greetings:
    def print_maze(self, maze):
        for row in maze:
            row_print = ""
            for value in row:
                if value == "x":
                    row_print += f'\033[1;31;40m {value} ' + " "
                else:
                    row_print += f'\033[1;30;40m {value} ' + " "

            print(row_print,f'\033[1;37;40m')
