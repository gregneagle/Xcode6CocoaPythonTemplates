**Xcode 6 Cocoa-Python Templates**

This is a set of File templates and Project templates for use with Xcode 6. These have been tested with Xcode 6.2 on Mavericks.

Using the Xcode 3 templates here: http://svn.red-bean.com/pyobjc/trunk/pyobjc/pyobjc-xcode/ as a starting point, and also using the existing Xcode 4 templates as a reference, I ported the Xcode 3 templates to the Xcode 4 format.

Xcode 5 brought some changes to using Python with Xcode, which you can read about here: https://developer.apple.com/library/mac/technotes/tn2328/_index.html

This meant using the Xcode 4 Cocoa-Python templates with Xcode 5 required lots of manual tweaking before you could get a project to build.

So the templates were updated for Xcode 5.

But those templates had some issues with Xcode 6...

So here we are.

**How to use these**

Either clone this repo or download the zip and expand it. Copy the File Templates and Project Templates folders to the following path in your home directory, creating any missing intermediate directories if needed:

~/Library/Developer/Xcode/Templates/

Launch Xcode 6. The File templates should be available from the template browser available when you choose File->New->File... -- they'll be listed under Mac OS X/Cocoa-Python.

The Project templates should be available when creating a new project, also under Mac OS X/Cocoa-Python.

When creating the project, you can choose to link to Python 2.6 or Python 2.7.  Choose Python 2.6 if you want to build projects that will run under Snow Leopard; Python 2.7 was not available on OS X until Lion shipped.

**Additional references**

http://blog.boreal-kiss.net/2011/03/11/a-minimal-project-template-for-xcode-4/

http://red-glasses.com/index.php/tutorials/making-custom-templates-for-xcode-4-march-2011/

https://snipt.net/raw/b216c160f38e9b3c095222607739b21c/?nice

https://github.com/NSBoilerplate/Xcode-Project-Templates/wiki/Creating-Xcode-4.x-Project-Templates

http://www.learn-cocos2d.com/store/xcode4-template-documentation/

