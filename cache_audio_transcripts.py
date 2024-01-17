from dotenv import load_dotenv
import openai
import os

load_dotenv()

azure_api_key_whisper = os.getenv('AZURE_OPENAI_API_KEY_WHISPER')
azure_endpoint_whisper = os.getenv('AZURE_OPENAI_ENDPOINT_WHISPER')

client = openai.AzureOpenAI(
    api_key=azure_api_key_whisper,
    azure_endpoint=azure_endpoint_whisper,
    azure_deployment="whisper",
    api_version="2023-09-01-preview",
)

def get_transcript(audio_file, path="."):
    audio_file = os.path.join(path, audio_file)

    return client.audio.transcriptions.create(
        file=open(audio_file, "rb"),
        model="whisper",
        language="de",
    ).text


audio_files = [
    "christmas2019.mp3",
    "newyear2016.mp3",
    "newyear2023.mp3",
]

indir = "PubAudio"
outdir = "."


for audio_file in audio_files:
    outfile = os.path.join(outdir, audio_file) + ".txt"
    if os.path.exists(outfile): continue
    with open(outfile, "w") as f:
        f.write(get_transcript(audio_file, indir))
