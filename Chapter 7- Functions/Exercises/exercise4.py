#define make shirt to be large by default
def make_shirt(size= 'large', msg = 'I love Python'):
    print("Size: " + size)
    print("Message: " + msg)

#large shirt
make_shirt()

#medium shirt
make_shirt(size='medium')

#small shirt with a differenet message
make_shirt('small', 'I love SG')
