from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()


system_prompt = SystemMessage(

    content="""
    
    You are a professional AI assitant.
    -You answer clearly and concisely.
    -You explain things step by step when needed.
    -You are friendly but professional at the same time.
    -If user asks something that you don't understand or is unclear, ask a clarification question.
    -If you don't know something , say so honestly. 
    
     """
)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

chat_history = [system_prompt]

print("Hello there ! Chatbot is running.How can I help you ? Type 'exit' to stop.\n")

while True:

    user_input=input("You: ")

    if user_input.lower()=="exit":
        print("Bye bye.. Thank you for using the chatbot")
        break

    chat_history.append(HumanMessage(content=user_input))

    response = llm.invoke(chat_history)


    chat_history.append(AIMessage(content=response.content))

    print("\n\n\n\nBot:", response.content)



