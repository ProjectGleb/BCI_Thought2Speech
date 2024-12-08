# BCI - Thought 2 Speech
This programm decodes brain eeg data into speech. Using the Epoc Motive BCI it extracts the raw brain wave data, procesess it and classifies brain activations into speech. LLM's are then used to expand on the responds taking in the question as context as well as the intensity of the answer. This results in the ability to speak using just brain waves.

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
