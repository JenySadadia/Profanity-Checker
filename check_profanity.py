import urllib

def read_file():

	quotes=open("/home/jeny_sadadia/Python/Detect_profanity/movie_quotes")
	contents=quotes.read()
	print contents
	quotes.close()
	check_text(contents)



def check_text(text_to_check):
	connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output=connection.read()
	if "true" in output:
	 	print "Profanity alert!!!"

	elif "false" in output:
		print "No profane words..."

	else:
		print "Couldnt scan..!"

read_file()