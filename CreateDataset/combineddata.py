import os
import json

## Transcript dir and QA dir
transcript_dir = "transcriptions"
QA_dir = "QA"

## Getting audio filenames
try:
    transcript_names = next(os.walk(transcript_dir), (None, None, []))[2]
    QA_names = next(os.walk(QA_dir), (None, None, []))[2]
except Exception as e:
    print(f"An error occurred while accessing the directory: {e}")
    exit(1)

def CombinedData():
    if len(transcript_names) == len(QA_names):
        output_dir = 'trainingdata'
        os.makedirs(output_dir, exist_ok=True)

        for index, value in enumerate(transcript_names):
            file_path1 = os.path.join(transcript_dir, value)
            file_path2 = os.path.join(QA_dir, QA_names[index])
            output_path = os.path.join(output_dir, "data.txt")

            try:
                with open(file_path1, 'r', encoding='utf-8') as json_file:
                    data1 = json.load(json_file)
                
                with open(file_path2, 'r', encoding='utf-8') as txt_file:
                    data2 = txt_file.read()

                with open(output_path, 'a', encoding='utf-8') as file:
                    file.write(data1["text"] + '\n\n' + data2)
                    print(f"Added {value} and {QA_names[index]}")
    
            except Exception as e:
                return f"An error occurred while appending to the file: {e}"
            
        return "Completed Task"
    else:
        return "Files in dirs not the same length"

if __name__ == '__main__':
    status = CombinedData()
    print(status)
