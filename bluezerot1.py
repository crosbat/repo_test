from bluezero import microbit
ubit = microbit.Microbit(adapter_addr='xx:xx:xx:xx:xx:xx',
                         device_addr='yy:yy:yy:yy:yy:yy')
my_text = 'Hello, world'
ubit.connect()

while my_text is not '':
    ubit.text = my_text
    my_text = input('Enter message: ')

ubit.disconnect()
