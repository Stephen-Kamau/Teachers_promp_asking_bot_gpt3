# Python example using openai module
import openai


# Import the Module to add Items created to the Database,
# THE ITEMS WILL BE ANALYSED THEIR EMOTIONS BEFORE SENDING
from db import retrive_ta_feedback, populate_ta_feedback
import os
from dotenv import load_dotenv
load_dotenv()
# set the key
openai.api_key = f"{os.getenv('OPENAI_GPT_KEY')}"


def get_promt_based_on_TA_feedback(feedback):
    """
    The function uses the teachers previous response.
    :param
        feedback: Str (teachers feedback)

    :returns
        string representing the best response prompt
    """

    #create a text with the
    prompt = f"Generate THE BEST QUESTION PROMPT from a teacher who has provided this previous response:\n {feedback}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    #get the results
    return response.choices[0].text



if __name__ == "__main__":
    # At First As A random Prompt.
    #We create an Iterative loop that  Iterate util one types q
    bot_prompt = "What topics did you cover?"
    while True:
        print(f"Bot Question:> {' '.join(bot_prompt)}")
        user_input = input("Enter Your Answer:>  ")
        if user_input.lower() == "q":
            print("Thank You for Taking Part in this check All results In here {results.csv}")
            # file to write results
            file_name = 'results.csv'

            # get all data
            all_results = retrive_ta_feedback()
            with open(file_name, 'w') as file:
                # Write the header row
                file.write('Prompt,Feedback,Polarity\n')
                # Iterate through each row tuple
                for row in all_results:
                    file.write(f'{row[0]},{row[1]},{row[2]}\n')
            file.close()
            break;
        bot_prompt =  get_promt_based_on_TA_feedback(user_input).split("\n")

        #add these data to the Database
        populate_ta_feedback(f"{' '.join(bot_prompt)}", f"{user_input}")
