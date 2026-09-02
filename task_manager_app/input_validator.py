import re


def validate_string_input(prompt, pattern=None, allow_blank=False):
    while True:
        value = input(prompt).strip()

        if allow_blank and value == "":
            return value

        if not value:
            print("Input cannot be empty.")
            continue

        if pattern and not re.fullmatch(pattern, value):
            print("Invalid input. Please try again.")
            continue

        return value


def validate_priority(prompt="Enter priority (High/Medium/Low): "):
    while True:
        priority = input(prompt).strip().capitalize()

        if priority in ["High", "Medium", "Low"]:
            return priority

        print("Invalid priority. Please enter High, Medium, or Low.")


def validate_task_index(prompt, task_count):
    while True:
        try:
            index = int(input(prompt))

            if 1 <= index <= task_count:
                return index - 1

            print("Invalid task number.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def validate_confirmation(prompt):
    while True:
        answer = input(prompt).strip().lower()

        if answer in ["y", "n"]:
            return answer

        print("Please enter y or n.")