import streamlit as st
from openai import OpenAI 
import os

client = OpenAI(base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("QUIZ_GAME_API"),)

def generate_questions(num, topic, diff_level = "medium"):

    #generate questions from AI 

    try:
        response = client.chat.completions.create(
        model="x-ai/grok-4.1-fast:free",
        messages=[
            {"role" : "system",
            "content" : "You are a well-known Quiz Generator in the world"},
      
            {"role": "user",
            "content": f"Generate {num} quiz questions about the topic {topic} with the difficulty level '{diff_level}'. "
            'Each question must have : '
            '- A "que" field : the text of the question. '
            '- An "options" field : a list of exactly 4 options, labeled "A. ", "B. ", "C. ", "D. ". '
            '- An "answer" field : a list containing the correct option letter (lowercase) and the correct answer text. '
            '- A "valid_options" field : a list of all options in the format ["a", "text1", "b", "text2", "c", "text3", "d", "text4"]. '
            'The output must be a python list of dictionaries, one question per dictionary. Respond *only* in pure JSON array format, "without any additional texts, markdown formatting or explanations." For example:\n '
       
            '[ {"que" : "What is the capital of France?", '
            '"options" : ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], '
            '"answer" : ["c", "paris"], '
            '"valid_options" : ["a", "berlin", "b", "madrid", "c", "paris", "d", "rome"] }, '

            '{"que" : "Which planet is known as the Red Planet?", '
            '"options" : ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"], '
            '"answer" : ["b", "mars"], '
            '"valid_options" : ["a", "earth", "b", "mars", "c", "jupiter", "d", "venus"]} '
            
            f'upto {num} questions. '
            'Make sure the JSON is properly formatted and can be parsed directly.]'
            } 
            ], ) 
    
    except Exception as e:
        st.warning(f"\n\nSomething went wrong! : {e}\n\nA random 10 questions of the topic 'General Knowledge' is created for you!")
        return False
        
    else:
        output = response.choices[0].message.content.strip()
        return (output)
    

def backup_questions():
    quiz_questions = [
    {"que": "Which planet is known as the Red Planet?",
     "options": ["A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"],
     "answer": ["c", "mars"],
     "valid_options": ["a", "venus", "b", "jupiter", "c", "mars", "d", "saturn"]},

    {"que": "Who painted the Mona Lisa?",
     "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
     "answer": ["c", "leonardo da vinci"],
     "valid_options": ["a", "vincent van gogh", "b", "pablo picasso", "c", "leonardo da vinci", "d", "michelangelo"]},

    {"que": "What is the largest organ in the human body?",
     "options": ["A. Heart", "B. Liver", "C. Skin", "D. Lungs"],
     "answer": ["c", "skin"],
     "valid_options": ["a", "heart", "b", "liver", "c", "skin", "d", "lungs"]},

    {"que": "Which country is called the Land of the Rising Sun?",
     "options": ["A. China", "B. Japan", "C. Thailand", "D. South Korea"],
     "answer": ["b", "japan"],
     "valid_options": ["a", "china", "b", "japan", "c", "thailand", "d", "south korea"]},

    {"que": "Who wrote Romeo and Juliet?",
     "options": ["A. William Shakespeare", "B. Charles Dickens", "C. George Bernard Shaw", "D. Jane Austen"],
     "answer": ["a", "william shakespeare"],
     "valid_options": ["a", "william shakespeare", "b", "charles dickens", "c", "george bernard shaw", "d", "jane austen"]},

    {"que": "What is the capital of Canada?",
     "options": ["A. Toronto", "B. Vancouver", "C. Ottawa", "D. Montreal"],
     "answer": ["c", "ottawa"],
     "valid_options": ["a", "toronto", "b", "vancouver", "c", "ottawa", "d", "montreal"]},

    {"que": "In computing, what does HTTP stand for?",
     "options": ["A. HyperText Transfer Protocol", "B. High Tech Transfer Program", "C. Hyperlink Text Type Protocol", "D. Host Transmission Tracking Process"],
     "answer": ["a", "hypertext transfer protocol"],
     "valid_options": ["a", "hypertext transfer protocol", "b", "high tech transfer program", "c", "hyperlink text type protocol", "d", "host transmission tracking process"]},

    {"que": "Which gas is most abundant in Earth’s atmosphere?",
     "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
     "answer": ["b", "nitrogen"],
     "valid_options": ["a", "oxygen", "b", "nitrogen", "c", "carbon dioxide", "d", "hydrogen"]},

    {"que": "The Great Wall of China was primarily built to protect against invasions from which group?",
     "options": ["A. Romans", "B. Mongols", "C. Persians", "D. Japanese"],
     "answer": ["b", "mongols"],
     "valid_options": ["a", "romans", "b", "mongols", "c", "persians", "d", "japanese"]},

    {"que": "Who was the first person to step on the Moon?",
     "options": ["A. Yuri Gagarin", "B. Buzz Aldrin", "C. Neil Armstrong", "D. Michael Collins"],
     "answer": ["c", "neil armstrong"],
     "valid_options": ["a", "yuri gagarin", "b", "buzz aldrin", "c", "neil armstrong", "d", "michael collins"]},

    {"que": "What is the largest animal in the world?",
     "options": ["A. African Elephant", "B. Blue Whale", "C. Giraffe", "D. Whale Shark"],
     "answer": ["b", "blue whale"],
     "valid_options": ["a", "african elephant", "b", "blue whale", "c", "giraffe", "d", "whale shark"]},

    {"que": "Which element has the chemical symbol 'O'?",
     "options": ["A. Oxygen", "B. Gold", "C. Osmium", "D. Oxide"],
     "answer": ["a", "oxygen"],
     "valid_options": ["a", "oxygen", "b", "gold", "c", "osmium", "d", "oxide"]},

    {"que": "How many continents are there on Earth?",
     "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
     "answer": ["c", "7"],
     "valid_options": ["a", "5", "b", "6", "c", "7", "d", "8"]},

    {"que": "Which country invented paper?",
     "options": ["A. India", "B. China", "C. Egypt", "D. Greece"],
     "answer": ["b", "china"],
     "valid_options": ["a", "india", "b", "china", "c", "egypt", "d", "greece"]},

    {"que": "Which is the smallest country in the world?",
     "options": ["A. Monaco", "B. San Marino", "C. Vatican City", "D. Liechtenstein"],
     "answer": ["c", "vatican city"],
     "valid_options": ["a", "monaco", "b", "san marino", "c", "vatican city", "d", "liechtenstein"]},

    {"que": "Which is the fastest land animal?",
     "options": ["A. Tiger", "B. Horse", "C. Cheetah", "D. Leopard"],
     "answer": ["c", "cheetah"],
     "valid_options": ["a", "tiger", "b", "horse", "c", "cheetah", "d", "leopard"]},

    {"que": "The currency of Japan is:",
     "options": ["A. Yuan", "B. Yen", "C. Won", "D. Ringgit"],
     "answer": ["b", "yen"],
     "valid_options": ["a", "yuan", "b", "yen", "c", "won", "d", "ringgit"]},

    {"que": "Who discovered gravity after seeing a falling apple?",
     "options": ["A. Galileo Galilei", "B. Albert Einstein", "C. Isaac Newton", "D. Nikola Tesla"],
     "answer": ["c", "isaac newton"],
     "valid_options": ["a", "galileo galilei", "b", "albert einstein", "c", "isaac newton", "d", "nikola tesla"]},

    {"que": "Which desert is the largest in the world?",
     "options": ["A. Sahara", "B. Gobi", "C. Kalahari", "D. Thar"],
     "answer": ["a", "sahara"],
     "valid_options": ["a", "sahara", "b", "gobi", "c", "kalahari", "d", "thar"]},

    {"que": "The process of plants making food using sunlight is called:",
     "options": ["A. Respiration", "B. Photosynthesis", "C. Germination", "D. Transpiration"],
     "answer": ["b", "photosynthesis"],
     "valid_options": ["a", "respiration", "b", "photosynthesis", "c", "germination", "d", "transpiration"]},

    {"que": "What is the hardest natural substance on Earth?",
     "options": ["A. Steel", "B. Diamond", "C. Graphite", "D. Quartz"],
     "answer": ["b", "diamond"],
     "valid_options": ["a", "steel", "b", "diamond", "c", "graphite", "d", "quartz"]},

    {"que": "Which is the world’s longest river?",
     "options": ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"],
     "answer": ["a", "nile"],
     "valid_options": ["a", "nile", "b", "amazon", "c", "yangtze", "d", "mississippi"]},

    {"que": "Who invented the telephone?",
     "options": ["A. Alexander Graham Bell", "B. Thomas Edison", "C. Nikola Tesla", "D. Guglielmo Marconi"],
     "answer": ["a", "alexander graham bell"],
     "valid_options": ["a", "alexander graham bell", "b", "thomas edison", "c", "nikola tesla", "d", "guglielmo marconi"]},

    {"que": "The Emerald Isle refers to which country?",
     "options": ["A. Scotland", "B. Ireland", "C. Iceland", "D. Greenland"],
     "answer": ["b", "ireland"],
     "valid_options": ["a", "scotland", "b", "ireland", "c", "iceland", "d", "greenland"]},

    {"que": "Which gas do humans exhale?",
     "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Helium"],
     "answer": ["c", "carbon dioxide"],
     "valid_options": ["a", "oxygen", "b", "nitrogen", "c", "carbon dioxide", "d", "helium"]},

    {"que": "Who is known as the Father of the Nation in India?",
     "options": ["A. Jawaharlal Nehru", "B. Subhas Chandra Bose", "C. Mahatma Gandhi", "D. Bhagat Singh"],
     "answer": ["c", "mahatma gandhi"],
     "valid_options": ["a", "jawaharlal nehru", "b", "subhas chandra bose", "c", "mahatma gandhi", "d", "bhagat singh"]},

    {"que": "Which country hosted the 2016 Summer Olympics?",
     "options": ["A. China", "B. Brazil", "C. Japan", "D. UK"],
     "answer": ["b", "brazil"],
     "valid_options": ["a", "china", "b", "brazil", "c", "japan", "d", "uk"]},

    {"que": "Which is the largest ocean on Earth?",
     "options": ["A. Atlantic Ocean", "B. Pacific Ocean", "C. Indian Ocean", "D. Arctic Ocean"],
     "answer": ["b", "pacific ocean"],
     "valid_options": ["a", "atlantic ocean", "b", "pacific ocean", "c", "indian ocean", "d", "arctic ocean"]},

    {"que": "The famous scientist Albert Einstein was born in which country?",
     "options": ["A. USA", "B. Germany", "C. Austria", "D. Switzerland"],
     "answer": ["b", "germany"],
     "valid_options": ["a", "usa", "b", "germany", "c", "austria", "d", "switzerland"]},

    {"que": "Which instrument is used to measure temperature?",
     "options": ["A. Hygrometer", "B. Thermometer", "C. Barometer", "D. Seismograph"],
     "answer": ["b", "thermometer"],
     "valid_options": ["a", "hygrometer", "b", "thermometer", "c", "barometer", "d", "seismograph"]},

    {"que": "How many players are there in a football (soccer) team?",
     "options": ["A. 9", "B. 10", "C. 11", "D. 12"],
     "answer": ["c", "11"],
     "valid_options": ["a", "9", "b", "10", "c", "11", "d", "12"]},

    {"que": "What is the capital of Australia?",
     "options": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"],
     "answer": ["c", "canberra"],
     "valid_options": ["a", "sydney", "b", "melbourne", "c", "canberra", "d", "brisbane"]},

    {"que": "Who is known as the Queen of Pop?",
     "options": ["A. Beyoncé", "B. Madonna", "C. Lady Gaga", "D. Taylor Swift"],
     "answer": ["b", "madonna"],
     "valid_options": ["a", "beyoncé", "b", "madonna", "c", "lady gaga", "d", "taylor swift"]},

    {"que": "What is the boiling point of water at sea level?",
     "options": ["A. 90°C", "B. 100°C", "C. 110°C", "D. 120°C"],
     "answer": ["b", "100°c"],
     "valid_options": ["a", "90°c", "b", "100°c", "c", "110°c", "d", "120°c"]},

    {"que": "Which is the tallest mountain in the world?",
     "options": ["A. K2", "B. Mount Everest", "C. Kangchenjunga", "D. Kilimanjaro"],
     "answer": ["b", "mount everest"],
     "valid_options": ["a", "k2", "b", "mount everest", "c", "kangchenjunga", "d", "kilimanjaro"]},

    {"que": "What is the main ingredient in sushi?",
     "options": ["A. Noodles", "B. Rice", "C. Bread", "D. Corn"],
     "answer": ["b", "rice"],
     "valid_options": ["a", "noodles", "b", "rice", "c", "bread", "d", "corn"]},

    {"que": "Who invented the light bulb?",
     "options": ["A. Nikola Tesla", "B. Alexander Graham Bell", "C. Thomas Edison", "D. Michael Faraday"],
     "answer": ["c", "thomas edison"],
     "valid_options": ["a", "nikola tesla", "b", "alexander graham bell", "c", "thomas edison", "d", "michael faraday"]},

    {"que": "What is the national flower of Japan?",
     "options": ["A. Tulip", "B. Rose", "C. Cherry Blossom", "D. Lotus"],
     "answer": ["c", "cherry blossom"],
     "valid_options": ["a", "tulip", "b", "rose", "c", "cherry blossom", "d", "lotus"]},

    {"que": "Which blood group is known as the universal donor?",
     "options": ["A. A", "B. B", "C. AB", "D. O Negative"],
     "answer": ["d", "o negative"],
     "valid_options": ["a", "a", "b", "b", "c", "ab", "d", "o negative"]},

    {"que": "The currency of the United Kingdom is:",
     "options": ["A. Dollar", "B. Pound Sterling", "C. Euro", "D. Franc"],
     "answer": ["b", "pound sterling"],
     "valid_options": ["a", "dollar", "b", "pound sterling", "c", "euro", "d", "franc"]},

    {"que": "Which country gifted the Statue of Liberty to the USA?",
     "options": ["A. Italy", "B. France", "C. Spain", "D. Germany"],
     "answer": ["b", "france"],
     "valid_options": ["a", "italy", "b", "france", "c", "spain", "d", "germany"]},

    {"que": "Who was the first woman to fly solo across the Atlantic Ocean?",
     "options": ["A. Amelia Earhart", "B. Valentina Tereshkova", "C. Sally Ride", "D. Bessie Coleman"],
     "answer": ["a", "amelia earhart"],
     "valid_options": ["a", "amelia earhart", "b", "valentina tereshkova", "c", "sally ride", "d", "bessie coleman"]},

    {"que": "Which organ purifies blood in the human body?",
     "options": ["A. Heart", "B. Liver", "C. Kidneys", "D. Lungs"],
     "answer": ["c", "kidneys"],
     "valid_options": ["a", "heart", "b", "liver", "c", "kidneys", "d", "lungs"]},

    {"que": "How many teeth does a normal adult human have?",
     "options": ["A. 28", "B. 30", "C. 32", "D. 34"],
     "answer": ["c", "32"],
     "valid_options": ["a", "28", "b", "30", "c", "32", "d", "34"]},

    {"que": "What is the national animal of China?",
     "options": ["A. Tiger", "B. Dragon", "C. Giant Panda", "D. Elephant"],
     "answer": ["c", "giant panda"],
     "valid_options": ["a", "tiger", "b", "dragon", "c", "giant panda", "d", "elephant"]},
            
            ]
    return quiz_questions
    