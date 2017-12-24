
# coding: utf-8

# In[27]:


alien_0 = {'color':'green', 'points':5}


# In[28]:


alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# In[16]:


alien_0 ={}
alien_0 = {'name':'atta', 'institution':'SirSyed'}
alien_0['age'] = 26
alien_0['height'] = '5.8'
print(alien_0)


# In[17]:


print("the information of "+alien_0['name']+" is age: " + str(alien_0['age']) + " ,height: " +str(alien_0['height']) )


# In[18]:


alien_0['name'] = "Ahsan"
alien_0['height']= 5.9

print("the information of "+alien_0['name']+" is age: " + str(alien_0['age']) + " ,height: " +str(alien_0['height']) )


# In[20]:





# In[23]:


print(alien_0)


# In[34]:


alien_0['speed'] = "medium"

print("The old x_position is :" + str(alien_0['x_position']))
if alien_0['speed'] == 'slow' :
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment  = 3

print("The new x_position is : " + str(alien_0['x_position']+x_increment))


# In[36]:


del alien_0['points']
print(alien_0)


# In[42]:


friend_info = {'first_name':'Ahsan' , 'last_name':'Ashraf' , 'age':'26' , 'city':'karachi'}
print("the friend_info is firstName :"+ friend_info['first_name'] + "lastName :" + friend_info['last_name'] + "Age: " + friend_info['age'])


# In[52]:


friend_numbers ={'Ahsan':10 , 'Salman' : 15 , "Saad":20}

print("Ahsan:" + str(friend_numbers['Ahsan']) + "Salman:" + str(friend_numbers['Salman']) + "Saad:" + str(friend_numbers['Saad']))


# In[54]:


friend_numbers ={'Ahsan':10 , 'Salman' : 15 , "Saad":20}

for key , value in friend_numbers.items() : 
    print(key) 
    print(value)


# In[55]:


dic = {"name":"atta"}
print(dic)


# In[57]:


for key in friend_numbers.keys():
    print(key)
for value in friend_numbers.values():
    print(value)


# In[59]:


for item in friend_numbers:
    print(item)
    print(friend_numbers[item])


# In[61]:


for item in friend_numbers.items():
    print(item[0],item[1])


# In[63]:


friend2=['zaheer' , 'Taha' ,'Ahsan']
for name in friend_numbers:
    if name in friend2:
        print(name , friend_numbers[name])

