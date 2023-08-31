def task1_1():
    jumbled_heroes = ["DoCtor_StRange","SpIdErMan","Moon_Night","Super_Man","Batman","HUlK"]
    indices = []
    decoded_names = []
    for i in jumbled_heroes:
        lower = i.lower()
        replace = lower.replace('_',' ')
        decoded_names.append(replace)
    print(decoded_names)
    indices = list(enumerate(jumbled_heroes))
    
    print(indices)
    length_list = lambda inputlist : len(inputlist)
    print(length_list(jumbled_heroes))

    print(jumbled_heroes)

    #name_lengths = []
    #result = map(lambda name_lengths:  name_lengths + jumbled_heroes,jumbled_heroes)
    #print(list(result))
    
    jumbled_heroes.sort()
    print(jumbled_heroes)
task1_1()        
    
