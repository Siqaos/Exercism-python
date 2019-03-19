def is_pangram(sentence):
   alphabet = 'abcdefghijklmnopqrstuvwxyz'

   try:
       ascii_str = sentence.encode('ascii')
   except UnicodeEncodeError:
       print("there are non-ascii characters in there")
       raise SystemExit

   for charater in alphabet:
          if charater not in sentence.lower():
              return False

   return True