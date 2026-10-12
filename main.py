import json
import core
import file_operations
import ui

ui.greet_user()
          
while True:
    name, highest_score= core.check_user()
    while True:
        score = 0
        ui.get_start_input("Enter start to start: ")

        while True:
            questions = file_operations.load_file("trivia.json")
            is_correct = core.display_questions(questions)
            if is_correct:
                score = core.update_score(is_correct, score)
            else: 
                break

        ui.display_score(score)
        highest_score = core.get_highest_score(score, highest_score)
        ui.display_highest_score(highest_score)
        file_operations.update_profile(name, score, highest_score)
        resume = ui.retstart()
        if not resume:
            break
