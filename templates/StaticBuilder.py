
import csv

class ProjectEntry():
    def __init__(self, title : str, imageName : str, fileName : str, tags : list) -> None:
        self.title = title
        self.imageName = imageName
        self.fileName = fileName
        self.tags = tags
    
    def __str__(self) -> str:
        returnStr =  "%s [" % self.name
        for i in range(len(self.tags)):
            returnStr += self.tags[i] + ", " * (i != len(self.tags) - 1)
        returnStr += "]"
        return returnStr


'''
====================================================================================
                    READING CSV TO GET PROJECT INFORMATION
====================================================================================
'''
projects = []
with open('./projects.csv', 'r+') as csvfile:
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        projects.append(ProjectEntry(row[0], row[1], row[2], row[3:]))




def OpenTag(tagName : str, attributes : dict, content = "") -> str:
    returnStr = "<" + tagName +" "
    for attr in attributes:
        returnStr += attr + "="+ "\"" + attributes[attr] + "\" "    
    returnStr += ">" + content + "\n"
    
    return returnStr

def CloseTag(tagName : str,) -> str:
    return "</" + tagName + ">\n"

def GalleryItemString(project : ProjectEntry) -> str:
    returnStr = ""

    returnStr += OpenTag("div", {'class':'gallery_item'})
    
    returnStr += "\t" + OpenTag("a", {"class":"gallery_item_link", "target":"_blank", "href": project.fileName})
    returnStr += "\t\t" + OpenTag("img", {"src":"img/" + project.imageName, "alt":"IMAGE MISSING"})
    returnStr += "\t\t" + OpenTag("p", {"class":"gallery_item_title"}, content = project.title)
    returnStr += "\t\t" + CloseTag("p")
    returnStr += "\t" + CloseTag("a")

    # Adding the tags divs
    returnStr += "\t" + OpenTag("div", {'class':'gallery_item_tag_list'})
    for tag in  project.tags:
        returnStr += "\t\t" + OpenTag("div", {'class':'gallery_item_tag'}, content = tag)
        returnStr += "\t\t" + CloseTag("div")
    returnStr += "\t" + CloseTag('div')

    returnStr += CloseTag('div')
    return returnStr



'''
====================================================================================
                        WRITING PROJECTS TO HTML FILE
====================================================================================
'''

with open("./index.html", 'r+') as html_file:
    fileString = html_file.read()

fileParts = fileString.partition("<div class=\"gallery\">")

fileString = fileParts[0] + fileParts[1] + "\n"
for proj in projects:
    fileString += GalleryItemString(proj) + "\n"
fileString += fileParts[2]


with open("./../index_NEW.html", 'w') as html_file:
    html_file.write(fileString)
