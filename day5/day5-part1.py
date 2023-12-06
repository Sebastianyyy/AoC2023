from collections import defaultdict
d=defaultdict(list)
l=[]

def get_from_seed_to_humidity(number):
    for i in l:
        for destination,source,r in d[i]:
            if source<=number<=source+r-1:
                number=destination+(number-source)
                break
    return number
if __name__=='__main__':
    with open(file='input.txt') as f:
        lines=f.readlines()
    
    seeds=[]
    i=0
    txt=""
    while i<len(lines):
        if lines[i][0:5]=='seeds':
            seeds=list(map(int,lines[i][5:].split()[1:]))
        elif lines[i]=='seed-to-soil map:\n':
            txt="d_seed_to_soil"
            l.append(txt)
        elif lines[i]=='soil-to-fertilizer map:\n':
            txt="d_soil_to_fertilizer"
            l.append(txt)
        elif lines[i]=='fertilizer-to-water map:\n':
            txt="d_fertilizer_to_water"
            l.append(txt)     
        elif lines[i]=='water-to-light map:\n':
            txt="d_water_to_light"
            l.append(txt)
        elif lines[i]=='light-to-temperature map:\n':
            txt="d_light_to_temperature"
            l.append(txt)
        elif lines[i]=='temperature-to-humidity map:\n':
            txt="d_temperature_to_humidity"
            l.append(txt)
        elif lines[i]=='humidity-to-location map:\n':
            txt="d_humidity_to_location"
            l.append(txt)
        elif lines[i]!='\n':
            tu=tuple(map(int,lines[i].split()))
            dest=tu[0]
            source=tu[1]
            r=tu[2]
            d[txt].append(tu)
            
        i+=1
    print(min(list(map(get_from_seed_to_humidity,seeds))))
