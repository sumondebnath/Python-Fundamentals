
import random

name_list = ["avater", "monkey", "shadow"]

word_choice = random.choice(name_list)

print(f"Random choicen word is {word_choice}")



display = []
for _ in word_choice:
    display.append("_")
print(display)

# flag = False
# while not flag:
#     char_input = input("Enter a letter : ").lower()
#     for pos in range(len(word_choice)):
#         if char_input == word_choice[pos]:
#             display[pos] = word_choice[pos]

#     print(display)

#     if "_" not in display:
#         print("You Win!")
#         flag = True


while "_" is not display:
    char_input = input("Enter a letter : ").lower()
    for pos in range(len(word_choice)):
        if char_input == word_choice[pos]:
            display[pos] = word_choice[pos]

    print(display)

    if "_" not in display:
        print("You Win!")
        break

