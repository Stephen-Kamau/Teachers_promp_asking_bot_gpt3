# THis acts as a storage db for the prompts and their feedback...
import sqlite3

# module to get polarity
from emotions import analyse_polarity


# create a connection object/ to db called skizaa.db
conn = sqlite3.connect('skizaa.db')
cursor_obj = conn.cursor()

# create table for the teacher's feedback with prompt and feedback made
cursor_obj.execute('''CREATE TABLE IF NOT EXISTS ta_feedback
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              feedback TEXT,
              prompt TEXT, polarity TEXT)
              ''')

conn.commit()

# create a function that will always be called when a prompt happen.
# the function will be inserting the records to the db

def populate_ta_feedback(bot_prompt, ta_feedback, tbl_name="ta_feedback"):
    polarity = analyse_polarity(ta_feedback)
    query = f"INSERT INTO {tbl_name} (feedback, prompt, polarity) VALUES (?, ?, ?)"
    #run the query

    cursor_obj.execute(query, (ta_feedback, bot_prompt, polarity))
    #execute the query
    conn.commit()


# get a function to get all feedback made by api.
def retrive_ta_feedback(tbl_name='ta_feedback'):
    query = f"SELECT prompt,feedback, polarity from {tbl_name}"
    #run the query.
    cursor_obj.execute(query)
    #all the data is returned as results
    return cursor_obj.fetchall()

# delete everything from the table: TO be used in testing..
def clear_table(tbl_name = "ta_feedback"):
    query = f"DELETE from {tbl_name}"
    cursor_obj.execute(query)
    conn.commit()

if __name__ == "__main__":
    #add two records
    populate_ta_feedback("Hi, there, I'm your Teaching assistance", "Nice Knowing you, I'm the Ghost")
    populate_ta_feedback("What are you curently learning the ghost", "I'm Learning MAthematics and Physics")

    #get the results.
    print("Here are the current results: ")
    for res in retrive_ta_feedback():
        print(res)
        print(f"prompt: {res[0]} \n       Feedback:  {res[1]} Polarity ({res[2]}) ")
