# Wanikani User Scrapper
A simple scrapper to roughly get all active user in Wanikani community (probably not entire user)

# Dependencies
* requests https://requests.readthedocs.io/en/master/

# What's In Script
* Extracted data user will be:
  * user id
  * username
  * current level (0-60, 0 for unidentified)
  * type (free, paid, lifetime)
* Result will be in csv. You can name the file accordingly with variable `output_file_name_csv`
