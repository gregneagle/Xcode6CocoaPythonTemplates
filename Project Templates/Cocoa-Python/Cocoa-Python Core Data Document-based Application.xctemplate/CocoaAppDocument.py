# -*- coding: utf-8 -*-
#
#  Document.py
#  ___PROJECTNAME___
#
#  Created by ___FULLUSERNAME___ on ___DATE___.
#  Copyright (c) ___YEAR___ ___ORGANIZATIONNAME___. All rights reserved.
#

from Foundation import *
from CoreData import *
from AppKit import *

class Document(NSPersistentDocument):
    def init(self):
        self = super(Document, self).init()
        # initialization code
        return self
        
    def windowNibName(self):
        return u"Document"
    
    def windowControllerDidLoadNib_(self, aController):
        super(Document, self).windowControllerDidLoadNib_(aController)
        # user interface preparation code
