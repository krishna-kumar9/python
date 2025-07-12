'''dict={
      "name":"Krishnakumar",
      "cgpa":9.6,
      "marks":[96,98,97],
      }
#print(dict)
dict["name"]="raju"
#print(dict)
print(type(dict))
null_dict={}
null_dict["name"]="kumar"
print(null_dict)'''

'''student={
    "name":"rahulkumar",
    "subjects":{
        "phy":97,
        "chem":98,
    "math":88
    }
}
print(student["subjects"]["chem"])
print(student)
print(student["name"])
newdict={
    "nam":"rahulkumar",
    "subject":{
        "phy":97,
        "chem":98,
    "math":88
    }
}
#DICTIONARY METHODS
print(student.keys())
print(student.values())
print(student.items())
print(student.get("subjects"))
print(student.update(newdict))
print(student)
#print(student("name2")) it should return type error
print(student.get("name2"))#it should return None 
'''

#SETS IN PYTHON

'''collection={1,2,3,4}
print(collection)
print(type(collection))
print(len(collection))
empty_set=set()
print(empty_set)
print(type(empty_set))
empty_set.add(9)
empty_set.add(3)
empty_set.add(5)
empty_set.remove(3)
print(empty_set)
print(empty_set.clear())
'''

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))

    










