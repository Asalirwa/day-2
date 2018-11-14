def countvowel (text):
  vowels="aeiouAEIOU"
  print(len([letter for letter in text if letter in vowels]))
  print ([letter for letter in text if letter in vowels])
countvowel("Hello, how are you? Am great, want to go to the beach on the weekend")
