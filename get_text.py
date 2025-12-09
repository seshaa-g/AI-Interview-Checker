from moviepy import VideoFileClip
import speech_recognition as sr

# Step 1: Extract audio from video
video = VideoFileClip("Q1.mp4")
audio = video.audio
audio.write_audiofile("extracted_audio.wav")

# Step 2: Convert audio to text
recognizer = sr.Recognizer()
with sr.AudioFile("extracted_audio.wav") as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data)

# Step 3: Save text into a file
with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Transcription saved to transcription.txt")
