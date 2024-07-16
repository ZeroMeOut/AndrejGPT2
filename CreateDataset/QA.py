import google.generativeai as genai
import os
import json

## Transcript dir
transcript_dir = "transcriptions"

## Getting filenames
try:
    transcript_names = next(os.walk(transcript_dir), (None, None, []))[2]
except Exception as e:
    print(f"An error occurred while accessing the transcript directory: {e}")
    exit(1)

## Func for generating QA
def QA(api_key: str, questionamount: str) -> str:
    output_dir = 'QA'
    os.makedirs(output_dir, exist_ok=True)

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=f"You would be receiving some text." 
                                  f"Your job is to generate only {questionamount} questions with answers in exactly this format: [Q] question, [A] answer."
                                  f"Do not add any thing else. Only base the generation on the text.") ## Feel free to change this
    
    for index, value in enumerate(transcript_names):
        file_path = os.path.join(transcript_dir, value)
        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                print(f"Loaded {value}")

                response = model.generate_content(data["text"])
                print(f"Generated data for {value}")
                
            output_path = os.path.join(output_dir, f"QA{index}.txt")
            with open(output_path, "w", encoding='utf-8') as file:
                file.write(response.text)
            print(f"Saved to QA{index}.txt \n")
            
        except Exception as e:
            return f"An error occurred while loading {value}: {e}"

    return 'Completed Task'

if __name__ == '__main__':
    response = QA('AIzaSyCDPZXc_8BRr5aLpIQ6r_x4j4JqTukifeY', '100') ## I tried prompting 200 then 100 but it doesn't generate up to that, welp.
    print(response)