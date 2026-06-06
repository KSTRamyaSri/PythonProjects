import os
import sys
import time
import threading
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

GENRES = {
    "1": {
        "name": "Bedtime Fable",
        "instruction": "Write a soothing, quiet, and peaceful fable. The setting should be a cozy forest, a starry night, or a calm village. Use soft and happy tones."
    },
    "2": {
        "name": "Space Adventure",
        "instruction": "Write an exciting sci-fi space story. The setting should be a cool planet, a rocket ship, or the stars. Use fun space words like moon, rocket, and stars."
    },
    "3": {
        "name": "Whimsical Mystery",
        "instruction": "Write a fun mystery story. The characters should look for something missing, like a toy or cookies. Keep it happy and playful."
    },
    "4": {
        "name": "Underwater Kingdom",
        "instruction": "Write a magical story set under the blue sea. The setting should involve coral reefs, deep oceans, or sunken castles. Use words like fish, shells, swimming, and bubbles."
    },
    "5": {
        "name": "Dinosaur Safari",
        "instruction": "Write an adventurous story set in a land full of friendly dinosaurs. The setting should have huge green trees, volcanoes, and big footprints. Use fun dino sounds."
    },
    "6": {
        "name": "Super Hero Academy",
        "instruction": "Write an energetic story about characters learning to use silly or fun superpowers. The setting should be a high-tech school or training camp. Focus on helpfulness."
    },
    "7": {
        "name": "Inspirational Tale",
        "instruction": "Write a heartwarming, uplifting story about working hard, staying strong, and chasing your dreams. The setting should feel bright, hopeful, and encouraging."
    },
    "8": {
        "name": "Spooky Ghost Story",
        "instruction": "Write a funny, friendly, and mildly spooky ghost story. The setting should be a creaky old attic or a misty garden. Make the ghost sweet, not scary."
    }
}

# --- Loading Animation Controller ---
class Spinner:
    def __init__(self, message="🤖 Chitti is thinking... "):
        self.message = message
        self.stop_running = False
        self.thread = None

    def _spin(self):
        # The frames of our animated terminal spinner
        frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        idx = 0
        while not self.stop_running:
            # \r moves the cursor back to the start of the line, overwriting the frame
            sys.stdout.write(f"\r{self.message}{frames[idx]}")
            sys.stdout.flush()
            idx = (idx + 1) % len(frames)
            time.sleep(0.1)
        
        # Clean up the loading line completely when stopped
        sys.stdout.write("\r" + " " * (len(self.message) + 2) + "\r")
        sys.stdout.flush()

    def start(self):
        self.stop_running = False
        self.thread = threading.Thread(target=self._spin)
        self.thread.daemon = True # Allows background termination if main script crashes
        self.thread.start()

    def stop(self):
        self.stop_running = True
        if self.thread:
            self.thread.join()

def generate_storybook_tale(inputs, selected_genre_info, dynamic_mode=True):
    client = genai.Client()
    
    if dynamic_mode:
        characters_list = ", ".join(inputs['nouns'])
        prompt_content = f"""
        Create a children's storybook tale based on these parameters:
        Characters/Nouns involved: {characters_list}
        Actions/Verbs involved: {', '.join(inputs['verbs'])}
        """
    else:
        prompt_content = f"Create a beautiful, fully surprise children's story based entirely on the theme of a {selected_genre_info['name']}."
    
    system_instruction = (
        f"You are a whimsical children's book author and ASCII artist. "
        f"Your task is to write an enchanting story in the style of a {selected_genre_info['name']}.\n"
        f"GENRE RULES: {selected_genre_info['instruction']}\n\n"
        "CRITICAL LANGUAGE REQUIREMENT: Use VERY BASIC ENGLISH. Use simple words, short sentences, and "
        "easy vocabulary that a 5-year-old child can read and understand. No complex grammar.\n\n"
        "CRITICAL STRUCTURE REQUIREMENTS:\n"
        "1. Write a beautifully descriptive story (3-4 short paragraphs) in the style of classic fables.\n"
        "2. Include an engaging dialogue conversation among the characters. CAPITALIZE the input words if provided.\n"
        "3. Conclude with a clear, distinctly formatted line: 'Moral of the Story: [Insert beautiful moral here in simple terms]'.\n"
        "4. At the very end of your response, create a simple, clean ASCII art diagram or pattern (using text characters like *, #, /, \\, _, type art) that visually represents a scene or element from the story."
    )

    # Initialize and spin up the loader right before the API request goes out
    spinner = Spinner("✨ Opening the magical realm... Chitti is cooking your story... ")
    spinner.start()

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_content,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.7,
            )
        )
        spinner.stop() # Turn off the loader immediately upon data arrival
        return response.text
    except Exception as e:
        spinner.stop()
        return f"The storybook magic encountered an error: {e}"

def run_story_chatbot():
    print("\n" + "=" * 60)
    print("🤖 Hello there! I am Chitti, your personal AI storyteller companion. 📚")
    print("   My speed is 1 terahertz, memory 1 zigabyte... but my favorite")
    print("   thing to do is weave beautiful stories with you! ✨")
    print("=" * 60 + "\n")
    
    print("🤖 Chitti: Before we begin, what kind of story flavor should we create today?\n")
    for key, genre in GENRES.items():
        print(f"  [{key}] {genre['name']}")
    print("") 
        
    while True:
        genre_choice = input("👉 Select a genre number (1-8): ").strip()
        if genre_choice in GENRES:
            chosen_genre = GENRES[genre_choice]
            break
        print("❌ Invalid choice. Please pick a number from 1 to 8.")
        
    print(f"\n🤖 Chitti: Awesome! A {chosen_genre['name']} it is.")
    print("-" * 60)
    
    skip_choice = input("🤖 Chitti: Do you want to add your own characters and actions? (yes/no): ").strip().lower()
    print("-" * 60 + "\n")
    
    if skip_choice not in ['yes', 'y']:
        story_output = generate_storybook_tale(None, chosen_genre, dynamic_mode=False)
    else:
        collected_data = {"nouns": [], "verbs": []}
        
        print("🤖 Chitti: Let's add the characters or main objects for our story.\n")
        while True:
            noun = input("👉 Enter a character or object (e.g., a little bear, a shiny pebble): ").strip()
            if noun:
                collected_data['nouns'].append(noun)
                
            if len(collected_data['nouns']) < 2:
                print("\n🤖 Chitti: Brilliant! Every great story needs at least two things interacting. Let's add another.\n")
                continue
                
            print("")
            more_nouns = input("❓ Want to add another character or object? (yes/no): ").strip().lower()
            if more_nouns not in ['yes', 'y']:
                break
            print("")
                
        print(f"\n🤖 Chitti: Fantastic! Our story elements are: {', '.join(collected_data['nouns'])}.")
        print("-" * 60 + "\n")
            
        print("🤖 Chitti: Now, let's add some actions or things they do in this adventure.\n")
        while True:
            verb = input("👉 Enter an action/verb (e.g., fly, dance, discover): ").strip()
            if verb:
                collected_data['verbs'].append(verb)
                
            print("")
            more = input("❓ Want to add another action? (yes/no): ").strip().lower()
            if more not in ['yes', 'y']:
                break
            print("")
                
        print(f"\n🤖 Chitti: Amazing inputs! Closing the storybook pages and mixing your ingredients...\n")
        
        story_output = generate_storybook_tale(collected_data, chosen_genre, dynamic_mode=True)
    
    print("=" * 60)
    print(story_output)
    print("=" * 60 + "\n")

if __name__ == "__main__":
    if "GEMINI_API_KEY" not in os.environ:
        print("❌ Error: GEMINI_API_KEY is missing from your environment setup.")
        exit(1)
    run_story_chatbot()