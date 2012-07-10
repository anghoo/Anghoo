#coding=utf-8
#!/usr/bin/python

from xml.etree.ElementTree import parse
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import SubElement

def getDocument( path ):
    xmlElementTree = parse( path )
    return xmlElementTree

def setElementValue( element, value ):
    """
    设置Element 值
    """
    element.text = value

def getElementValue( element ):
    """
    获取element 的值
    """
    return element.text


def findElement( xmlElementTree,tagName ):
    element = xmlElementTree.find(tagName)
    if element is None:
        elementTreeRoot = xmlElementTree.getroot()
        rootTagNmae = elementTreeRoot.tag
        if rootTagNmae == tagName:
            element = elementTreeRoot
        else:
            return None
    return element

def findAllElements( xmlElementTree,tagName ):
    elements = xmlElementTree.findall(tagName)
    return elements


def findSubElementValue( element, tagName ):
    """
    根据Element获取subElement的值
    """
    subElement = element.find( tagName )
    if subElement is not None :
        return subElement.text
    return None

def writeXML( elementTree,path ):
    elementTree.write(path,encoding="UTF-8")
