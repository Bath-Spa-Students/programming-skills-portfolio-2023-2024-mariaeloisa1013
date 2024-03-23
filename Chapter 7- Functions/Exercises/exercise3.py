#define function, make shirt
def make_shirt(size, msg):
    print ("Your graphic shirt," + msg + " is sized " + size )

#positional calling
make_shirt('Extra Small', 'I Love SG')

#call with keyword arguments
make_shirt(size='Extra Large', msg= 'Beautiful')
