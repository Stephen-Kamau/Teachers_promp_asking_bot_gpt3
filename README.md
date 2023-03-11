# Teachers_promp_asking_bot_gpt3
### Some staffs related to bot.

### Requirements
- Implement a chat-based web application allowing teachers to enter feedback about what they taught.
- Use GPT-3 to prompt the teachers with questions about their lesson. The prompt should be generated based on the teacher's feedback.
- Store the feedback and the generated prompts in a database.
- Analyze the feedback to assess the teacher's emotional well-being. You can use any method or tool of your choice for this analysis.
- Display the emotional well-being analysis to the teacher in the web application.



### Solution.
- For this case, I used majorly Terminal Based Bot(complete) and streamlit for web(Does not retrive saved data automatical).
- The application is implimented using OpenAi library, streamlit for web, textblob for analysis of emotions in teacher's response and sqlite3 as the database for storage of all these.

### FIles:
- In this project, multiple files are present;
  - `db.py`: Used to create functions to create table, insert values, get values from table etc.
  - `db_test.py`: used for Unit test for the database functions.
  - `emotions.py`: Contains functions that retrieves the emotion of the TA's answer.
  - `api.py`: Contains code for Terminal Based Bot.
  - `streamapp.py`: The replica chatbot on web.

   
### How to run.

- To run the application, first create the a python environment if you prefer soo. i.e
    ```python -m venv botter```

- Then you need to activate it i.e ```source botter/bin/activate```

- After activating, you can install the Requirements files using;
  ```pip install -r requirements.txt```
- You then need to get an API key from the openai platform and paste it inside .env file you need to create. with key name as `OPENAI_GPT_KEY`
- After that, If you want to use Terminal Based GUI, run as follows;  
  ```python api.py```
- Else if you want Web based usse;
  ```streamlit run streamapp.py```


- There you goo!!!!
