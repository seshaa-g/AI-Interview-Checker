from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Example texts
actual_text = "What are event loops in node js? Answer: The Event Loop is the mechanism that handles asynchronous callbacks in Node.js. Node.js is single-threaded but can perform non-blocking I/O by delegating operations to the system and handling their results asynchronously."
transcribed_text = "what are even loops in node JS the event loop is a mechanism that handles asynchronous callback in node JS node JS is single threaded but can perform non blocking IO by delegating operations to the system and handling their result asynchronously"

# Similarity checks
ratio = fuzz.ratio(actual_text, transcribed_text)
partial_ratio = fuzz.partial_ratio(actual_text, transcribed_text)
token_sort_ratio = fuzz.token_sort_ratio(actual_text, transcribed_text)
token_set_ratio = fuzz.token_set_ratio(actual_text, transcribed_text)

# Weighted final score
final_score = (0.2 * ratio) + (0.3 * partial_ratio) + (0.2 * token_sort_ratio) + (0.3 * token_set_ratio)

print("Fuzz Ratio:", ratio)
print("Partial Ratio:", partial_ratio)
print("Token Sort Ratio:", token_sort_ratio)
print("Token Set Ratio:", token_set_ratio)
print("Final Score:", round(final_score, 2))
