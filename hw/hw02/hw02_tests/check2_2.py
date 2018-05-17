# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """You need to replace the ... in book_title_words with your answer.""" 
msg2 = """Your answer should be an array."""
msg3 = """ It looks like you included commas in the text.
          The three pieces of text in the array should be:
          'Eats'
          'Shoots'
          'and Leaves' """
msg4 = """ It looks like you didn't include both words in the last piece of text.  It should be the actual string:'and Leaves'"""
msg5 ="""Your answer is in the right form and almost there!"""
#end err msg definition
def check2_2(book_title_words):
    correctarray = np.array(['Eats','Shoots','and Leaves']) 
    #if not book_title_words != ... : 
    #    print(msg1)
    #type(book_title_words)
    if not type(book_title_words) == np.ndarray:
        print(msg2)
    elif any([',' in text for text in book_title_words]):
        print(msg3)
    elif not 'and ' in book_title_words.item(2):
        print(msg4)
    elif not np.array_equal(book_title_words,correctarray):
        print(msg5)
    else: 
        print("Your answer looks ok!")
    