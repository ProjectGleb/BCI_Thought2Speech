import os
from typing import Sequence
from supabase.client import create_client, Client
from dotenv import load_dotenv
from supabase.lib.client_options import ClientOptions

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def post_response_to_database(response: str) -> None:
    """Post response to Supabase."""
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    supabase.table("eeg_responses").insert({"response": response}).execute()

def get_last_response_from_database() -> str:
    """Get the last response from Supabase."""
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    response = supabase.table("eeg_responses").select("*").order(column='created_at',desc=True).execute()
    return response.data[0]

if __name__ == "__main__":
    post_response_to_database("no")
    print(get_last_response_from_database())