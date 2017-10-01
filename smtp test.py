import smtplib

def authenticate():
	try:  
	    server = smtplib.SMTP('smtp.gmail.com', 587)
	    server.ehlo()
	    print "success"
	except:  
	    print 'Something went wrong or connection lost...'
authenticate()