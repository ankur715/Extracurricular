#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# In[8]:


email = 'ankur.ankur902@gmail.com'
password = 'password'
send_to_email = 'p.ankur.715@gmail.com'
subject = 'Python Email' # The subject line
message = 'smtplib, MIMEText, MIMEMultipart'


# In[9]:


msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject


# In[10]:


# attach the message to the MIMEMultipart object
msg.attach(MIMEText(message, 'plain'))


# In[11]:


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string() # You now need to convert the MIMEMultipart object to a string to send
server.sendmail(email, send_to_email, text)
server.quit()


# In[12]:


server = smtplib.SMTP('secureus24.sgcpanel.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string() # You now need to convert the MIMEMultipart object to a string to send
server.sendmail(email, send_to_email, text)
server.quit()


# In[ ]:





# In[ ]:





# In[13]:


msg = MIMEMultipart()
msg['From'] = "ankur.ankur902@gmail.com"
msg['To'] = "p.ankur.715@gmail.com"
msg['Subject'] = "Item Found!"


# In[14]:


body = "<a href=""http://ebay.com"">We found an item you might be interested in</a>"
msg.attach(MIMEText(body, 'html'))
print(msg)


# In[18]:


server = smtplib.SMTP("secureus24.sgcpanel.com", 587)
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()


# In[ ]:




