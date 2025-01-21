# Sensivalidate

this script finds sensitive data in a text. the only real validation it does is the credit card number.
if you try a random 16 digit number (i.e 1234123412341234) it wouldn't catch it because this is not a 
valid credit card number. UK bank account number, sort code and UK postcode are all just pattern match. So, if 
you try 12-12-12 then this get flagged as sort code even though it is not a real sort code.

All the regex are from ChatGPT, if you have any questions I don't have the answers. 