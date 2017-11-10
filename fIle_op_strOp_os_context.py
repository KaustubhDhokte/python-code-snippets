import os
file_path = os.path.join(os.getcwd(), "input.txt")
with open(file_path) as f:
    record = dict()
    output_students = list()
    ln = f.readline()
    while(ln):
        ln = ln.strip('\n')
        breaks = ln.split(', ')
        student_id = int(breaks[0])
        score = int(breaks[2])
        if student_id in record:
            if student_id not in output_students:
                if (record[student_id] + score) >= 100:
                    output_students.append(student_id)
                else:
                    record[student_id] += score
        else:
            record[student_id] = score
        ln = f.readline()
        
out_path = os.path.join(os.getcwd(), "output.txt")
with open(out_path, "w") as f:
    f.write(str(len(output_students)))