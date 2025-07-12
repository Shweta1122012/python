student_id ={
    'id1':{
        'name': ['alice'],
        'class': ['VI'],
        'subjects': ['maths','english','science']
    },'id2':{
        'name': ['alice'],
        'class': ['VI'],
        'subjects': ['maths','english','science']
    },'id3':{
        'name': ['joseph'],
        'class': ['VI'],
        'subjects': ['maths','english','science']
    },'id4':{
        'name': ['matthew'],
        'class': ['VI'],
        'subjects': ['maths','english','science']
    },
}


result ={}
for key,value in student_id.items():
    if value not in result.values():
        result[key]=value
print("The student id is",result)