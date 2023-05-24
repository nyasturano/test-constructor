# defines if lxml element is table
def contains_table(elem):
    return elem.tag.endswith('tbl')


# defines if lxml element contains picture
def contains_picture(elem):
    for node in elem.iter():
        if node.tag.endswith('drawing'):
            return True
    return False
