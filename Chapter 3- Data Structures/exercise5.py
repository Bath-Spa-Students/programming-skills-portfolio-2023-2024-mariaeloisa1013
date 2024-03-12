#list three people invited
ppl = ["phoebe", "alexa","marwa"]

#assign message to variable
msg = "come have dinner with us, "

#print invitations with message for each person
print ( "invitations")
print ( "\t" + msg + ppl[0])
print ( "\t" + msg + ppl[1])
print ( "\t" + msg + ppl[2])

#alexa can't come
print ( "\n" + ppl[1] + " can't make it:(\n")

#modify list, by replacing alexa with rinoa
ppl[1] = "rinoa"

#invitations pt 2
print ("new invitations")
print ( "\t"  + msg + ppl[0])
print ( "\t"  + msg + ppl[1])
print ( "\t"  + msg + ppl[2])

