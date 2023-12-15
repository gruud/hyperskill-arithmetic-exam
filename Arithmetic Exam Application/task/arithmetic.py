import random
from random import randint
# write your code here


class Quizz:

    """ Standard operators supported """
    operators = ["+", "-", "*"]

    def get_difficulty_level(self) -> int:
        """Let the user choose between the level available."""
        while True:
            print("Which level do you want? Enter a number:")
            print("1 - simple operations with numbers 2-9")
            print("2 - integral squares of 11-29")
            answer = input()
            if answer not in ['1', '2']:
                self.print_incorrect_input()
            else:
                return int(answer)

    def print_incorrect_input(self):
        """Prints a standard message to declare incorrect user input."""
        print("Incorrect format")



    def get_level1_task(self) -> str:
        """Get a random simple expression to evaluate"""
        task =  f"{randint(2, 9)} {random.choice(self.operators)} {randint(2, 9)}"
        print(task)
        return task

    def get_level2_task(self) -> str:
        """Get a quadratic expression to evaluate, print the base number"""
        base_number = random.randint(11, 29)
        print(base_number)
        return f"{base_number} ** 2"

    def get_input(self) -> int:
        """Ask for input until it is a number. Returns the valid number."""
        while True:
            answer = input()
            if answer.lstrip("+-").isnumeric():
                return int(answer)
            else:
                self.print_incorrect_input()

    def save_results(self, level, correct_answers, tasks_count):
        """Save name and result to a file if wanted."""
        print(f"Your mark is {correct_answers}/{tasks_count}. ", end="")
        print("Would you like to save the result? Enter yes or no.")
        answer = input("Would you like to save the result? Enter yes or no.\n")
        if answer in ["yes", "YES", "y", "Yes"]:
            name = input("What is your name?\n")
            result_file = open("results.txt", "a+", encoding="UTF-8")
            desc = "(simple operations with numbers 2-9)" if level == 1 else f"(integral squares of 11-29)"
            result_file.write(f"{name}: {correct_answers}/{tasks_count} in level {level} {desc}\n")
            result_file.close()
            print('The results are saved in "results.txt".')


    def start(self, tasks_count):
        """Starts the quizz"""
        correct_answers = 0
        level = self.get_difficulty_level()
        task_factory = self.get_level1_task if level == 1 else self.get_level2_task

        for i in range(tasks_count):
            task = task_factory()
            answer = self.get_input()
            if answer == eval(task):
                print("Right!")
                correct_answers += 1
            else:
                print("Wrong!")

        self.save_results(level, correct_answers, tasks_count)

def main():
    """Main program"""
    Quizz().start(tasks_count=5)


if __name__ == "__main__":
    main()
