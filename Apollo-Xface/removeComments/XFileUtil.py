# -*- coding: utf-8 -*-

import os
import os.path
import shutil

def copyTree( srcDir, desDir ) :
    """
    复制文件夹
    """
    print "copyTree %s to %s" % (srcDir, desDir)
    if os.path.exists( srcDir ) == True and os.path.exists( desDir ) is False:
        try :
            shutil.copytree( srcDir, desDir )
            return True
        except Exception, e :
            print e
    else :
        print "Copy Failed !!!"
    return False

def rmTree( srcDir ) :
    """
    删除文件夹
    """
    if os.path.exists( srcDir ):
        try :
            shutil.rmtree( srcDir, onerror = on_rm_error )
        except  Exception, e:
            print e

def on_rm_error( func, path, exc_info):
    # path contains the path of the file that couldn't be removed that it's read-only and unlink it.
    import stat
    os.chmod( path, stat.S_IWRITE )
    os.unlink( path )

def copyFile( srcFile, desFile ) :
    """
    复制文件
    """
    print "copy file %s to %s " % ( srcFile, desFile )
    if os.path.exists( desFile ):
        try :
            shutil.copy( srcFile, desFile )
        except Exception, e :
            print e

def deleteFile( filePath ) :
    """
    删除文件
    """
    print "delete file %s " % filePath
    if os.path.exists( filePath ):
        try :
            import stat
            os.chmod( filePath, stat.S_IWUSR )
            os.remove( filePath )
        except Exception, e:
            print e

def mkDir( dir ):
    """
    新建文件夹
    """
    if os.path.exists( dir ) is False :
        try :
            os.mkdir( dir )
        except Exception,e:
            print e