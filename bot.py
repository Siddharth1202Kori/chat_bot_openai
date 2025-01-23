#nothing but we import an openai packages that already have/provide several funtionality of accessing chatgpt.
import openai

#below is the place where you place your api key.
#api ley in simple words plays an important role to acting like a bridge between two application. (here your code editor of coding platform and open ai service server.) 
openai.api_key="sk-"

#below is the funtion that calls the openai functionality.
#reuses reusable block of code.
def chat_with_gpt(prompt):
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content": prompt}]    
    )
    
    #Accesses the text response returned by the model.
    return response.choices[0].message.content.strip()

#main programing loop that provide a chat countinuing and breaking point. Also take user input .
# Ensures the code runs only when executed directly, not when imported as a module.
if __name__=="__main__":
    
    #Infinite Loop that keeps the program running until a condition (break) is met.
    while True:
        #Collects user input from the console.
        user_input = input("You: ")
        if user_input.lower() in ["quit","exit,bye"]:
            break
        
        #transfer our input to through api to chatgpt.
        response = chat_with_gpt(user_input)
        
        #Displays the chatbot's response
        print("chatbot: ", response)