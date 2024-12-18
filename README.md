# Jarvis-Voice-Assistant
This code defines a voice assistant named "Jarvis" capable of performing tasks like opening websites, playing music, and responding to user queries via OpenAI's API. 
## Key Components
### Speech Recognition:
Uses the speech_recognition library to capture and interpret user commands through the microphone.
Listens for the wake word "Jarvis" to activate further processing.

### Text-to-Speech (TTS):
Integrates both pyttsx3 (offline) and gTTS (Google Text-to-Speech) to convert responses into audio output.
Temporary audio files are generated by gTTS and played using pygame.

### API Integration:
Connects to the OpenAI API using a key to process user queries not directly handled by predefined commands.
Sends the user command to GPT-based models for generating responses.

### Command Processing:
Recognizes and executes specific commands like opening popular websites or playing a song by name.
If the command does not match predefined tasks, it defaults to generating a response using the OpenAI API.

## How the Code Works

### Initialization:
Initializes the TTS engine with pyttsx3 and announces that Jarvis is starting.

### Listening for Wake Word:
Continuously listens for audio input using the microphone.
If the user says "Jarvis," the assistant activates and listens for further commands.

### Processing Commands:
#### Predefined Tasks:
Commands like "open Google" or "play [song name]" are identified using if-elif conditions.
Websites are opened using webbrowser.open.
For music, it searches for the song name in a hypothetical musiclib library and plays the corresponding link.
#### General Queries:
If the command is not predefined, it is sent to OpenAI's API (aiProcess function).
The GPT model generates a short, conversational response.

### Speaking Responses:
The response text is converted into speech.
The speak function saves the audio using gTTS and plays it using pygame.

### Error Handling:
Includes basic exception handling to manage issues like timeout errors or unrecognized speech.

## Key Features
Wake Word Activation: Keeps the assistant in a passive listening state until "Jarvis" is heard.

Dynamic Task Handling: Executes predefined tasks and delegates general queries to OpenAI.

### Modular Functions:

aiProcess: Handles GPT-based responses.

speak: Handles text-to-speech output.

processCommand: Handles task execution logic.

Extensible Design: New commands can easily be added to processCommand.

## Example Workflow
1.Jarvis hears "Jarvis" and activates.

2.The user says, "Open Google."

3.The processCommand function matches "open google" and opens the Google homepage in the web browser.

4.If the user asks, "What's the weather today?" (a general query), the aiProcess function sends the question to OpenAI, and the response is spoken aloud.
