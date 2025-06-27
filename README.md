# Llama-AI-Tourism-Chatbot

# 🧳 Tourism AI Chatbot

An intelligent and interactive **AI-powered chatbot** built to help users plan their trips based on destination, budget, travel companions, and preferred locations. This chatbot uses natural language processing and machine learning (powered by the LLaMA model) to offer personalized travel recommendations and tourist spot suggestions.

## 🚀 Features                                

- 🗺️ Suggests destinations based on user preferences (budget, area type, etc.)
- 👨‍👩‍👧‍👦 Supports travel profiles (solo, partner, friends, family)
- 💬 Interactive chatbot experience
- 💡 Smart recommendations using LLaMA model
- 🔊 Voice-enabled input and responses *(optional, if implemented)*

## 🧠 Tech Stack

- **Model**: Meta’s LLaMA (Language Model)
- **Languages**: Python
- **Frontend (if any)**: Streamlit / Gradio *(if used)*
- **Libraries**: 
  - Transformers
  - SentencePiece
  - Flask / FastAPI *(if applicable)*
  - Custom NLP preprocessing modules

## 🎯 Use Case

Users can chat with the bot to get suggestions for:
- Travel destinations based on interest (beach, hill station, heritage, etc.)
- Budget-optimized locations
- Companions (solo/family/friends) suitable places
- Things to do and places to visit in the selected destination

  Screenshot of the Project

  ![Chatbot Demo](assets/chatbot_output_1.png)

  ![Chatbot Demo](assets/chatbot_output_2.png)


Installation

1) git clone https://github.com/your-username/tourism-ai-chatbot.git
   cd tourism-ai-chatbot

2) pip install -r requirements.txt

3) python main.py

Example

"Suggest a place for a solo trip under ₹10,000"
"Where can I go with my family for a beach vacation?"
"Plan a trip to Himachal with friends"


## 📁 Project Structure

```bash
tourism-ai-chatbot/
├── app.py                 # Main application file
├── chatbot_logic.py       # Core logic for recommendations
├── model/                 # LLaMA or other model files
├── data/                  # Dataset for tourism spots
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation



