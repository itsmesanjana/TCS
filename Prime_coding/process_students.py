def process_students(input_str):
    lines=input_str.strip().split('\n')
    n=int(lines[0])
    
    students=[line.split() for line in lines[1:]]

    older_names=[s[0] for s in students if s[3].lower()=="female"]

    female_grades=[ord(s[])]

    print(" ".join(older_names))
    print(sum(female_grades)//)
    