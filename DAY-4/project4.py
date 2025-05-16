# # 🎵 Mood-Based Song Recommender

# def get_songs_for_mood(mood):
#     if mood == "happy":
#         return ["Happy – Pharrell Williams", "Can't Stop the Feeling – Justin Timberlake", "On Top of the World – Imagine Dragons"]
#     elif mood == "sad":
#         return ["Let Her Go – Passenger", "Fix You – Coldplay", "Someone Like You – Adele"]
#     elif mood == "motivated":
#         return ["Stronger – Kanye West", "Eye of the Tiger – Survivor", "Believer – Imagine Dragons"]
#     elif mood == "romantic":
#         return ["Perfect – Ed Sheeran", "All of Me – John Legend", "Thinking Out Loud – Ed Sheeran"]
#     elif mood == "relaxed":
#         return ["Sunflower – Post Malone", "Better Together – Jack Johnson", "Weightless – Marconi Union"]
#     else:
#         return ["Sorry, I don't know songs for that mood. Try 'happy', 'sad', or 'motivated'."]

# # 💬 User Interaction
# print("🎵 Welcome to Moodify - Your Mood-Based Music Bot")
# user_mood = input("\nHow are you feeling today? ").lower()

# recommended_songs = get_songs_for_mood(user_mood)

# print(f"\n🎧 Recommended Songs for '{user_mood.title()}':")
# for song in recommended_songs:
#     print(f"- {song}")


'''🐍 Snake-Water-Gun Battle Arena 

🎯 Game Rules:
Snake drinks Water → Snake wins

Water drowns Gun → Water wins

Gun shoots Snake → Gun wins

'''
import random

def decide_winner(user, comp):
    if user == comp:
        return "draw"
    elif (user == "snake" and comp == "water") or \
         (user == "water" and comp == "gun") or \
         (user == "gun" and comp == "snake"):
        return "user"
    else:
        return "computer"

def play_round(round_num):
    print(f"\n🎲 Round {round_num}")
    user_choice = input("Choose (snake / water / gun): ").lower()
    comp_choice = random.choice(["snake", "water", "gun"])
    
    print(f"🧍 You chose: {user_choice}")
    print(f"💻 Computer chose: {comp_choice}")
    
    winner = decide_winner(user_choice, comp_choice)
    
    if winner == "draw":
        print("🤝 It's a draw!")
    elif winner == "user":
        print("✅ You win this round!")
    else:
        print("❌ Computer wins this round!")
    
    return winner

# 🧮 Score Tracking
user_score = 0
comp_score = 0

# 🎮 Play 3 Rounds
result1 = play_round(1)
if result1 == "user":
    user_score += 1
elif result1 == "computer":
    comp_score += 1

result2 = play_round(2)
if result2 == "user":
    user_score += 1
elif result2 == "computer":
    comp_score += 1

result3 = play_round(3)
if result3 == "user":
    user_score += 1
elif result3 == "computer":
    comp_score += 1

# 🏆 Final Result
print("\n📊 Final Score:")
print(f"You: {user_score} | Computer: {comp_score}")

if user_score > comp_score:
    print("🎉 You are the champion!")
elif user_score < comp_score:
    print("💻 Computer wins the game.")
else:
    print("🤝 It's a tie overall!")
