# -*- coding: utf-8 -*-

import Constants
import os
import XMLUtils
import XFileUtil
import re
import sys

def getDocument():
    configPath = os.path.join( os.path.dirname(__file__), Constants.CONFIG_NAME )
    configDoc = XMLUtils.getDocument( configPath )
    return configDoc

def getProjects( configDoc ):
    """
    get the projects that need publish
    """
    publishProjectsElement = XMLUtils.findAllElements( configDoc, "publishProjects/project/path")
    projectsDir = []
    for projectElement in publishProjectsElement:
        projectPath = XMLUtils.getElementValue( projectElement )
        projectsDir.append( projectPath )
    return projectsDir

def copyProjectsToTargetDir( apolloDir, projectsDir ):
    if projectsDir is None:
        return False
    targetDir = sys.argv[2]
    XFileUtil.rmTree( targetDir )
    XFileUtil.mkDir( targetDir )
    for projectPath in projectsDir:
        projectSrc = os.path.join( apolloDir, projectPath )
        projectTempPath = os.path.join( targetDir, projectPath )
        XFileUtil.copyTree( projectSrc, projectTempPath )

def doRemove( configDoc ):
    removeFiles( configDoc )
    removeComments()

def removeComments():
    """
    only remove java file comments
    """
    for root, dirs, files in os.walk( sys.argv[2] ):
        for name in files:
            if re.search( Constants.SUFFIX_FILE, name ):
                javaFilePath =  os.path.join( root, name )
                removeFileComments( javaFilePath )

def removeFiles( configDoc ):
    projectsElement = XMLUtils.findAllElements( configDoc, "publishProjects/project" )
    for projectElement in projectsElement:
        projectName = XMLUtils.findSubElementValue( projectElement, "path" )
        projectPath = os.path.join( sys.argv[2], projectName )
        
        # remove the dir 
        dirsElement = XMLUtils.findAllElements( projectElement, "removeFiles/dirs/dir" )
        for dirElement in dirsElement:
            dirName = XMLUtils.getElementValue( dirElement )
            if dirName is None:
                continue
            dirPath = os.path.join( projectPath, dirName )
            XFileUtil.rmTree( dirPath )
        
        #remove files 
        filesElement = XMLUtils.findAllElements( projectElement, "removeFiles/files/file" )
        for fileElement in filesElement:
            fileName = XMLUtils.getElementValue( fileElement )
            if fileName is None:
                continue
            filePath = os.path.join( projectPath, fileName )
            XFileUtil.deleteFile( filePath )
    pass

def removeFileComments( filePath ):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return ""
        else:
            return s
    print "remove comments in %s " % filePath
    fileData = open( filePath ).read()
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    data = re.sub(pattern, replacer, fileData)
    import stat
    os.chmod( filePath, stat.S_IWRITE )
    open( filePath, "wb" ).write( data )

def verifyArgs():
    if len(sys.argv) != 3:
        print "Usage: xFacePublish.py root_dir target_dir"
        sys.exit()
    if not os.path.exists(sys.argv[1]):
        print "root_dir must be exist!!"
        sys.exit()

def main():
    verifyArgs()

    configDoc = getDocument()
    apolloDir = sys.argv[1]

    projectsDir = getProjects( configDoc )
    copyProjectsToTargetDir( apolloDir, projectsDir )
    doRemove( configDoc )

if __name__ == "__main__":
    main()