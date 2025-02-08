# Zootopia with API

This project fetches animal data from api-ninjas.com and displays it on a webpage. If the animal doesn’t exist, it shows a custom error message.

## Installation

Clone this repository to your local environment, then use `pip` to install all the required dependencies found in `requirements.txt`.

1. Clone the repository:
   ```bash
   git clone https://github.com/dimitar27/Zootopia_with_API.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

After cloning the repository:

1. Create a `.env` file in the root directory of the project.
2. Add your API key to the `.env` file like this:

   ```
   API_KEY=your_api_key_here
   ```

Make sure to replace `your_api_key_here` with your actual API key from [api-ninjas.com](https://api-ninjas.com/).

To use this project, run the following command:
```bash
python animals_web_generator.py
```
