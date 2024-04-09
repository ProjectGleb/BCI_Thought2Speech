# BCI - Thought 2 Speech
E/acc Hackathon winning team :) 
This programm decodes brain eeg data into speech. Using the Epoc Motive BCI it extracts the raw brain wave data, procesess it and classifies the response into Yes or No. LLM's are then used to expand on the responds taking in the question as context as well as the intensity of the answer. This results in the ability to speak using just your brain waves.
The project got to finals in a 200 people hackathon.

## Quickstart
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Running front-end
```bash
streamlit run streamlit_app.py
```
