## Check out here for the ffmpeg install: https://stackoverflow.com/a/74001956/13249791
import os
import whisper
import json
import torch

## Determine the device to use: CUDA if available, otherwise CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")
 
## Load the Whisper model
try:
    model = whisper.load_model("base", device=device)
except Exception as e:
    print(f"An error occurred while loading the Whisper model: {e}")
    exit(1)

## Audio dir
audio_dir = "audio"

## Getting audio filenames
try:
    audio_names = next(os.walk(audio_dir), (None, None, []))[2]
except Exception as e:
    print(f"An error occurred while accessing the audio directory: {e}")
    exit(1)

## Function to transcribe audio files
def transcribe_audio():
    for index, value in enumerate(audio_names):
        output_dir = 'transcriptions'
        os.makedirs(output_dir, exist_ok=True)

        try:
            audio_path = os.path.join(audio_dir, value)
            audio = whisper.load_audio(audio_path)

            print(f'Processing file {index + 1}')
            result = whisper.transcribe(model, audio, language="en")

            output_path = os.path.join(output_dir, f'transcript{index}.json')
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=4)
            print('Done')
        except Exception as e:
            return f"An error occurred while processing file {value}: {e}"

    return 'Completed Task'

if __name__ == '__main__':
    response = transcribe_audio()
    print(response)
