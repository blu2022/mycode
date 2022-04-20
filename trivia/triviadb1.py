#!/usr/bin/env python3
import html
# https://github.com/csfeeser/Python/blob/master/challenges/pyb_21_22.md

def main():
                                                                  
    trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             html.unescape("&quot;Here&#039;s lookin&#039; at you, kid.&quot;"),
             html.unescape("&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;"),
             html.unescape("&quot;Round up the usual suspects.&quot;")
            ]
        }

    question= trivia["question"]
    correct= html.unescape(trivia["correct_answer"])
    incorrect1= trivia["incorrect_answers"][0]
    incorrect2= trivia["incorrect_answers"][1]
    incorrect3= trivia["incorrect_answers"][2]

    print(question)
    print(correct)
    print(incorrect1)
    print(incorrect2)
    print(incorrect3)

main() 