from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key
from langchain import llms

key = "AIzaSyCe6WsxepI0GejLj9fuqzjKG5-PRDSzoWg"
llm = GooglePalm(google_api_key=key, temperature=0.7)


def generate_restaurant_name_and_items(cuisine):
    # Chain 1:  recipe Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="Provide list of 20 dishes name for this {cuisine} food one by one with a very short description in a bracket."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="dish")
    '''
    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['dish'],
        template="""Suggest some menu items for {restaurant_name}. Return it as a comma separated string"""
    )
    
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")
    '''
    chain = SequentialChain(
        chains=[name_chain],
        input_variables=['cuisine'],
        output_variables=['dish']
    )

    response = chain({'cuisine': cuisine})

    return response


def generate_recipe(temp):
    # Chain 1:  recipe Name
    prompt_template_name = PromptTemplate(
        input_variables=['temp'],
        template="Provide recipe of this {temp} food in bullet points in detail way."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="a")
    '''

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['temp'],
        template="Provide the history of this {temp} in a small beautiful interesting paragraph"
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="b")
    '''
    chain = SequentialChain(
        chains=[name_chain],
        input_variables=['temp'],
        output_variables=['a']
    )

    res = chain({'temp': temp})

    return res


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
