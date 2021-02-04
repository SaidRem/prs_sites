import codecs
import xml.etree.ElementTree as ET
import re


def more(f, n=10):
    with open(f) as c:
        lines = c.readlines()
    while lines:
        print(' '.join(lines[:n]))
        lines = lines[n:]
        if input('more?') != 'y':
            break

#with codecs.open('rates', 'rb', 'cp1251') as f:
    #content = f.read()
    #qqtree = ET.parse(content)
    #print(tree)
    #for line in content:
    #    print(line)

#with open('rates', 'r') as f:
#    for line in f:
#        print(line.decode())

#with codecs.open('rates', 'r', 'cp1251') as f:
#    content = f.readline()
#    print(content)

#with codecs.open('output', 'w', 'utf-8') as out:
#    out.write(content)
    #print(content)
    
    #findall = re.search(r'<Name>(.+)</Name>', content.decode())
    #print(findall.groups())
    #for line in f:
    #    print(line.decode())


if __name__ == '__main__':
    more('rates')


# with open('rates', 'r') as f:
#     content = f.readlines()   #.decode('cp1251')
#     print(content[0:8])
