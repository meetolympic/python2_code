'''
Created on 24-Mar-2016


The purpose of the module is define the basic email class and
collection of emails which are not bounded, actually bounded 
by implementation. Needs to check.TBD
Email object has a container which is EmailContainer.

'''
from random_words import RandomWords
from random_words import RandomEmails
from random_words import LoremIpsum
import collections
from collections import Mapping
#from objc import nil
import sys
import threading

''' ToDo: Basic version of the email class '''
    
class Email(object):
    '''
    This is the email class which is the generic class holding many attributes

    version 0.1 Date: 7 Apr, 2016:added methods subject and body to email message
    '''
    
    
    def __init__(self):
        '''
        Constructor for email class has toField, subject, body
        '''
        self.toField = "empty"
        self.subject = "empty"
        self.body = "empty"
        ''' The attribute below are used to populate the '''
        self.randomEmail = RandomEmails()
        self.randomWords = RandomWords()
        self.lorenIpsum = LoremIpsum()
        ''' Ensure that object is populated correctly '''
        self.populate()
 
    def __str__(self):
        ''' Helps to show the output '''
        return unicode("Email body : %s\n" % self.body) + unicode("Email Subject : %s\n" % self.subject) + unicode("Email to : %s\n" % self.toField)
    
    
    
    def populate(self):
        ''' Populate the toField, body and subject fields randomly '''
        self.toField = self.randomEmail.randomMail()
        #self.body = self.randomWords.random_words(count=100)
        self.body = self.lorenIpsum.get_sentences(sentences=10)
        self.subject = self.randomWords.random_words(count=4)
          
    def subject(self):
        ''' This method returns the subject of the email'''
        print self.subject

    def body(self):
        ''' This method returns the Body of the email'''
        print self.body

    def hashofemail(self):
        ''' Ensure that the unique hash is generated for the email object 
            quality of hash generated is not tested. It is worth testing it.
        '''
        return id(self)







    ''' changelog: version 0.1: removed constructor invoking populate method.
                   constructor returns faster. new method insertitems with number of arguments
                   was added to allow client to as many items as required.
        changelog: version 0.2: insertitems allows clients of the API to to insert
                   as many items as possible, it will insert minimum of 1 item if input is zero
                   or less than zero,
                   added return statement to the sizeofdict method, which was missing
                   added getnumberofentries method for easy reference
                   insertitems operation runs in a separate thread now, such that it does not
                   block the main thread.
    '''
class EmailContainer(collections.Mapping):
    ''' 
    This is the email container class, this holds number of emails 
    like thousands and millions of them stored in some suitable container 
    '''
    
    def __init__(self,maxsize=1000000):
        ''' constructor for the email container class 
            constructor do not populate the items and hence 
            construction is fast. '''
        self.x = ""
        self.maxsize = maxsize
        self.emaildict = {}
        '''for i in xrange(4000000):
            self.emaildict[i] = None '''
        
        
    def __iter__(self):
        return iter(self.emaildict)
    
    def __len__(self):
        return self.emaildict.__sizeof__()
    
    def __getitem__(self, key):
        collections.Mapping.__getitem__(self, key)
        
    def add(self, key, value):
        ''' provide add method such that easy to add key and value pair '''
        self.emaildict[key] = value
                   
    def populate(self):
        ''' This is population of dictionary object with 1000 objects'''
        for _ in xrange(10):
            self.x = Email()
            self.add(self.x.hashofemail(),self.x)
    
    def insertitems(self, numberofitems):
        ''' This method inserts items the dictionary but allows client to 
            how many items to be added  as number of items. minimum one item
            must be inserted into the dictionary. '''
        '''if numberofitems <= 1:
            numberofitems = 1
        
        for _ in xrange(numberofitems):
            self.x = Email()
            self.add(self.x.hashofemail(),self.x) 
        '''
        ''' do not block while insertion in progress '''
        t = threading.Thread(target=self.insertitermsinathread, args=[numberofitems])
        t.daemon = True
        t.start()
    
    def getsizeofdict(self):
        ''' print the size of the email container as dictionary '''
        return sys.getsizeof(self.emaildict)
    
    def getnumberofentries(self):
        ''' 
            This method tells how many entries are currently available in
            the email dictionary
        '''
        ''' make the list from keys of the dictionary and return its length'''
        return len(list(self.emaildict.keys()))
    
    def insertitermsinathread(self, numberofitems):
        ''' when number of items to be added are of higher size do the work in thread '''
        if numberofitems <= 1:
            numberofitems = 1
        
        for _ in xrange(numberofitems):
            self.x = Email()
            self.add(self.x.hashofemail(),self.x)
        
my_emails = {}
e = EmailContainer() 
e.populate()

for key,value in e.emaildict.items():
	print(value)
