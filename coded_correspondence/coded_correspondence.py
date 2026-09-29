# Off-Platform Project: Coded Correspondence
# Decode and encode letters to Vishal using Caesar and Vigenère ciphers.
# Only the standard library is used (string module is avoided) so the
# work stays on basic loops, indexing, and string building.

alphabet = "abcdefghijklmnopqrstuvwxyz"


# ---------------------------------------------------------------------------
# Step 3 requirement (functions used from step 1 onward):
# Define caesar_decode(message, offset) and caesar_encode(message, offset)
# so any offset can be applied quickly.
#
# Solution: Vishal encodes by shifting letters LEFT (subtract offset).
# Decoding shifts RIGHT (add offset). Non-letters stay unchanged.
# Negative offsets work because Python's % wraps them into 0-25.
# ---------------------------------------------------------------------------
def caesar_decode(message, offset):
    decoded = ""
    for character in message:
        if character in alphabet:
            index = alphabet.find(character)
            new_index = (index + offset) % 26
            decoded += alphabet[new_index]
        else:
            decoded += character
    return decoded


def caesar_encode(message, offset):
    encoded = ""
    for character in message:
        if character in alphabet:
            index = alphabet.find(character)
            new_index = (index - offset) % 26
            encoded += alphabet[new_index]
        else:
            encoded += character
    return encoded


# ---------------------------------------------------------------------------
# Step 1 requirement:
# Decode Vishal's first letter. Offset is 10. Print the result.
#
# Solution: Call caesar_decode with offset 10 (letters move 10 places right).
# ---------------------------------------------------------------------------
vishal_message_one = (
    "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? "
    "y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
)
decoded_message_one = caesar_decode(vishal_message_one, 10)
print("Step 1 — decoded message (offset 10):")
print(decoded_message_one)
print()


# ---------------------------------------------------------------------------
# Step 2 requirement:
# Send Vishal a reply using the same offset. Encoding is the opposite of
# decoding (shift left by 10).
#
# Solution: Write a plaintext reply, then caesar_encode(..., 10).
# ---------------------------------------------------------------------------
reply_to_vishal = (
    "hey vishal! this cipher is fun. let's keep sending secret notes!"
)
encoded_reply = caesar_encode(reply_to_vishal, 10)
print("Step 2 — encoded reply (offset 10):")
print(encoded_reply)
print("Step 2 — check by decoding the reply:")
print(caesar_decode(encoded_reply, 10))
print()


# ---------------------------------------------------------------------------
# Step 3 requirement:
# Decode two more messages. First uses offset 10 and hints at the second.
#
# Solution: Decode the first with offset 10, read the hint, then decode the
# second with the offset named in that hint.
# ---------------------------------------------------------------------------
vishal_message_two = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
vishal_message_three = (
    "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
)
decoded_message_two = caesar_decode(vishal_message_two, 10)
print("Step 3 — first message (offset 10):")
print(decoded_message_two)

# The first message says the second offset is fourteen.
decoded_message_three = caesar_decode(vishal_message_three, 14)
print("Step 3 — second message (offset 14):")
print(decoded_message_three)
print()


# ---------------------------------------------------------------------------
# Step 4 requirement:
# Brute-force a Caesar cipher when the offset is unknown.
#
# Solution: Try every offset from 0 through 25, print each decode, and keep
# the one that reads as English. Computers make this cheap.
# ---------------------------------------------------------------------------
vishal_message_brute = (
    "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. "
    "px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
)
print("Step 4 — brute-force all Caesar offsets:")
for offset in range(26):
    print(f"Offset {offset}: {caesar_decode(vishal_message_brute, offset)}")
print()

# After reading the 26 lines, offset 7 is the readable English sentence.
print("Step 4 — decoded message (offset 7):")
print(caesar_decode(vishal_message_brute, 7))
print()


# ---------------------------------------------------------------------------
# Step 5 requirement:
# Decode a Vigenère cipher with keyword "friends".
#
# Solution: Repeat the keyword over letters only (spaces and punctuation do
# not consume a keyword letter). Encode subtracted the keyword letter's
# alphabet index; decode adds that index back, wrapping with % 26.
# Place values: a=0, b=1, ... z=25.
# ---------------------------------------------------------------------------
def vigenere_decode(message, keyword):
    decoded = ""
    keyword_index = 0
    for character in message:
        if character in alphabet:
            key_character = keyword[keyword_index % len(keyword)]
            shift = alphabet.find(key_character)
            letter_index = alphabet.find(character)
            decoded += alphabet[(letter_index + shift) % 26]
            keyword_index += 1
        else:
            decoded += character
    return decoded


vishal_vigenere_message = (
    "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal "
    "wg zztylktoikqq!"
)
decoded_vigenere = vigenere_decode(vishal_vigenere_message, "friends")
print("Step 5 — Vigenère decoded (keyword 'friends'):")
print(decoded_vigenere)
print()


# ---------------------------------------------------------------------------
# Step 6 requirement:
# Write a function that encodes with a Vigenère keyword, then send Vishal a
# message. Bonus: decode the encoded text and get the original back.
#
# Solution: Encoding subtracts the keyword letter index (the reverse of
# decode). Same rule: only letters advance the keyword.
# ---------------------------------------------------------------------------
def vigenere_encode(message, keyword):
    encoded = ""
    keyword_index = 0
    for character in message:
        if character in alphabet:
            key_character = keyword[keyword_index % len(keyword)]
            shift = alphabet.find(key_character)
            letter_index = alphabet.find(character)
            encoded += alphabet[(letter_index - shift) % 26]
            keyword_index += 1
        else:
            encoded += character
    return encoded


# Check the course example: "barry is the spy" + "dog" -> "ymlok cp fbb ejv"
example_encoded = vigenere_encode("barry is the spy", "dog")
print("Step 6 — example encode check (should be 'ymlok cp fbb ejv'):")
print(example_encoded)

message_for_vishal = (
    "vishal, brute force is too easy now. vigenere is a nicer puzzle. write soon!"
)
keyword_for_vishal = "python"
encoded_for_vishal = vigenere_encode(message_for_vishal, keyword_for_vishal)
print("Step 6 — encoded message for Vishal (keyword 'python'):")
print(encoded_for_vishal)
print("Step 6 — bonus: decode the encoded message (should match original):")
print(vigenere_decode(encoded_for_vishal, keyword_for_vishal))
