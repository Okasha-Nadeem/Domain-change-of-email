#Script to update domain on every email in a company demo

# Function that will replace old email with new one
def assignNewDomain(email,givenDomain,new_Domain):
  if "@" + givenDomain in email:
    Index = email.index("@" + givenDomain)
    newEmail = email[:Index] + "@" + new_Domain
    return newEmail
  return email


#Input Email
email = input("Enter Email: ")
#Input Old Domain
givenDomain = input("Enter Given domain: ")
#Input New Domain
new_Domain = input("Enter new domain: ")

#Updating using function
update = assignNewDomain(email,givenDomain,new_Domain)
print(update)

#The End
