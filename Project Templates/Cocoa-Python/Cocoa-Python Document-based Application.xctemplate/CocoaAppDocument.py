# -*- coding: utf-8 -*-
#
#  Document.py
#  ___PROJECTNAME___
#
#  Created by ___FULLUSERNAME___ on ___DATE___.
#  Copyright (c) ___YEAR___ ___ORGANIZATIONNAME___. All rights reserved.
#

from Foundation import *
from AppKit import *

class Document(NSDocument):
    def init(self):
        self = super(Document, self).init()
        # initialization code
        return self
        
    def windowNibName(self):
        return u"Document"
    
    def windowControllerDidLoadNib_(self, aController):
        super(Document, self).windowControllerDidLoadNib_(aController)

    def dataOfType_error_(self, typeName, outError):
        return None, NSError.errorWithDomain_code_userInfo_(NSOSStatusErrorDomain, -4, None) # -4 is unimpErr from CarbonCore
    
    def readFromData_ofType_error_(self, data, typeName, outError):
        return NO, NSError.errorWithDomain_code_userInfo_(NSOSStatusErrorDomain, -4, None) # -4 is unimpErr from CarbonCore
