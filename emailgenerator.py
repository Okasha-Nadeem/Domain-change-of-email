#Script to update domain on every email in a company demo

# Function that will replace old email with new one
def assignNewDomain(email,old_Domain,new_Domain):
  if "@" + old_Domain in email:
    Index = email.index("@" + old_Domain)
    newEmail = email[:Index] + "@" + new_Domain
    return newEmail
  return email


#Input Email
email = input("Enter Email: ")
#Input Old Domain
old_Domain = input("Enter old domain: ")
#Input New Domain
new_Domain = input("Enter new domain: ")

#Updating using function
update = assignNewDomain(email,old_Domain,new_Domain)
print(update)

#The End
