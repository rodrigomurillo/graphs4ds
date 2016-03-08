import xml.etree.ElementTree as ET
tree = ET.parse('train.xml')
root = tree.getroot()

def parse_xml():
    data = []
    for child in root:
        temp = {}
        for item in child.getchildren():
            if item.tag == "lex":
                temp["lexes"] = [{"text":value} for value in item.text.split(',')]
            elif item.tag == "imageName":
                temp["filename"] = item.text.split("/")[-1]
            elif item.tag == "address":
                temp["address"] = item.text
                dummy = item.text.split(" ")
                if '-' in dummy[-1]:
                    temp["state"] = {"name":dummy[-2]}
                    temp["city"] = {"name":dummy[-3]}
                else:
                    temp["state"] = {"name":dummy[-1]}
                    temp["city"] = {"name":dummy[-2]}
                del dummy
            elif item.tag == "Resolution":
                temp["resolution"] = item.attrib
            elif item.tag == "taggedRectangles":
                temp["tags"] = []
                for lchild in item.getchildren():
                    temp["tags"].append({"text":lchild.find("tag").text})
        data.append(temp)
    return data

# parse_xml()

