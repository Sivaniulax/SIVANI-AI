

# SIVANI-AI: Your Personal Helper in Cooking

Welcome to SIVANI-AI! This project is a GEN-AI Streamlit web application that assists users in generating restaurant names, menu items, and detailed recipes based on selected cuisines or specific dishes. Leveraging LangChain and the Google Palm language model, SIVANI-AI makes it easy to explore diverse culinary options and recipes.

## Features

- **Generate Restaurant Names and Menu Items:** Select a cuisine to get a list of 20 dish names with short descriptions.
- **Generate Recipes:** Input a dish name to receive a detailed recipe in bullet points.
- **Easy to Use Interface:** Simple and intuitive Streamlit interface for seamless interaction.

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/sivani-ai.git
    cd sivani-ai
    ```

2. **Install Dependencies**
    Make sure you have Python 3.7+ installed. Then install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Your API Key**
    Create a file named `secret_key.py` and add your Google API key:
    ```python
    openapi_key = "your_google_api_key"
    ```

4. **Run the Application**
    ```bash
    streamlit run sivani_ai.py
    ```

## Usage

1. **Select a Cuisine**
    - Use the sidebar to select a cuisine (e.g., Indian, Italian, Mexican, Arabic, American).
    - The app will generate a list of 20 dish names with short descriptions for the selected cuisine.

2. **Enter a Dish Name**
    - Use the sidebar to enter the name of a dish.
    - The app will provide a detailed recipe in bullet points for the entered dish name.

## Project Structure

- **sivani_ai.py:** Main Streamlit app file.
- **langchain_helper.py:** Helper functions for generating restaurant names, menu items, and recipes using LangChain.
- **secret_key.py:** File containing the Google API key.
- **requirements.txt:** List of required Python packages.

## Example

### Generate Restaurant Names and Menu Items

1. Select "Italian" from the sidebar.
2. The app will display a list of 20 Italian dishes with short descriptions.

### Generate Recipes

1. Enter "Pasta Carbonara" in the text input field in the sidebar.
2. The app will provide a detailed recipe for Pasta Carbonara in bullet points.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome!



---

Happy Cooking with SIVANI-AI!

---

