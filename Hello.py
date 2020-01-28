print("HelloWorld...!!!")

## Variable ##

a = 100
print(a)

## Multiple Variable Assignment

i,j,k=9,99, "Testing"
print(i);print(j);print(k)

## MultiLine

a = 10
b = 100
c = 1000
sum = a + \
      b + \
      c
print(sum)

## Arrays

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(days)
print(days[0:4:2])

### List  [ Diff between Array and list is , list can have different types of DataTypes . In Array we have same type of datatypes ]

list = [ 'vhsd', 7186 , 2.23, 'johnny', 70.2 ]
tinylist = [123, 'john']

print (list[1:3])
print (tinylist * 2)
print (list + tinylist)


## Tuples , Similar to List . Difference are Tuple are read only and defined in () . List can be update and enclosed with in[]

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
#tuple[2] = 34    # Invalid syntax with tuple
list[2] = 79     # Valid syntax with list
print(list)
print(tinylist)


## Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([])

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

