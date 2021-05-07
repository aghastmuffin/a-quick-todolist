still = []
done = []
while True:
    user = input('>>> ')
    if user == ('add'):
        a = input('Task name: ')
        still.append(a)
    elif user == ('list'):
        print('Still have to do:')
        print(still)
        print('Have done:')
        print(done)
    else:
        if user == ('Mark as done'):
            print('Mark task as done')
            print(still)
            which = input('Which task? (Name): ')
            still.remove(which)
            done.append(which)
        elif user == ('Mark as undone'):
                print('Mark as undone')
                print(done)
                which = input('which task (name)? ')
                done.remove(which)
                still.append(which)
        else:
            if user == ('Help'):
                print('Commands: \n -add \n -Still have to do \n -Mark as undone \n -Mark as done')
            else: 
                print('Syntax unknown. do: Help')