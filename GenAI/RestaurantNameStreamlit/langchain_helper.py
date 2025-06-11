from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_cohere import ChatCohere
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
cohere_api_key = env_vars.get("CohereAPIKey")

llm = ChatCohere(cohere_api_key=cohere_api_key, temperature=0.7, model="command-r")

def generate_restaurant_name_and_items(cuisine):

    promp_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. suggest a fancy name for it. say nothing extra and just return 1 name"
    )
    name_chain = LLMChain(llm=llm, prompt=promp_template_name, output_key='restaurant_name')

    promp_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu for {restaurant_name}. Return it as a comma-separated list with only dish names. Do not explain anything."
    )
    food_items_chain = LLMChain(llm=llm, prompt=promp_template_items, output_key='menu_items')

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items'],
        verbose=True
    )

    response = chain({'cuisine': cuisine})
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
