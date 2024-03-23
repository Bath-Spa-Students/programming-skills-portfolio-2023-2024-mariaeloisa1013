#list four people invited
ppl = ["phoebe", "alexa","marwa", "kairi"]

#assign message to variable
msg = "come have dinner with us, "

#print invitations with message for each person
print ( "invitations")
print ( "\t" + msg + ppl[0])
print ( "\t" + msg + ppl[1])
print ( "\t" + msg + ppl[2])
print ( "\t" + msg + ppl[3])

#alexa can't come
print ( "\n!! " + ppl[1] + " can't make it:(\n")

#modify list, by replacing alexa with rinoa
ppl[1] = "rinoa"

#send new invitations
print ("new invitations")
print ( "\t" + msg + ppl[0])
print ( "\t" + msg + ppl[1])
print ( "\t" + msg + ppl[2])
print ( "\t" + msg + ppl[3])


#mnot enough seats, remove guest 3
print ("\n!! Hello " + ppl[3] + ". Sadly, we only have a table for two. Sorry we can't provide any more seats.\n")
newppl = ppl.pop(3)

#not enough seats, remove guest 2
print ("!! Hello " + ppl[2] + ". Sadly, we only have a table for two. Sorry we can't provide any more seats.\n")
newppl = ppl.pop(2)

#new guest list
print ("\tnew list: ", ppl) 

#send final invitations
print ("\nnew invitations")
print ( "\t"  + msg + ppl[0] + ". You have a seat.")
print ( "\t"  + msg + ppl[1] + ". You have a seat.")

#use del to empty list
del ppl[1]
del ppl[0]
print ("\nempty list:", ppl)
