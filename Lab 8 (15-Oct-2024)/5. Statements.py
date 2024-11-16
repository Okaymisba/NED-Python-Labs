# (a) Assign to variable message the string 'The secret of this message is that it is secret.'
message = "The secret of this message is that it is secret."

# (b) Assign to variable length the length of string message, using operator len().
length = len(message)

# (c) Assign to variable count the number of times the substring 'secret' appears in string message, using string method count().
count = message.count("secret")

# (d) Assign to variable censored a copy of string message with every occurrence of substring 'secret' replaced by 'xxxxxx', using string method replace().
censored = message.replace("secret", "xxxxxx")
