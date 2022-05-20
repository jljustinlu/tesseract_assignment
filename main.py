class Patient:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.num_exams = 0
        self.exams = []
    
    def add_exam(self, e_id):
        self.num_exams += 1
        self.exams.append(e_id)
    
    def remove_exam(self):
        self.num_exams -= 1

class Exam:
    def __init__(self, p_id, e_id):
        self.p_id = p_id
        self.e_id = e_id


def main():
    patients = {}
    exams = {}
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            info = line.split()
            instr = info[0]
            record = info[1]
            if instr == "ADD":
                if record == "PATIENT":
                    id = info[2]
                    name = info[3:]
                    patient = Patient(name, id)
                    if id not in patients:
                        patient[id] = patient
                elif record == "EXAM":
                    p_id = info[2]
                    e_id = info[3]
                    if e_id not in exams:
                        exam = Exam(p_id, e_id)
                        exams[e_id] = exam
                    if p_id in patients:
                        patients[p_id].add_exam(e_id)

            elif instr == "DEL":
                if record == "PATIENT":
                    id = info[2]
                    if id in patients:
                        for exam in patients[id].exams:
                            del exams[exam]
                        del patients[id]
                elif record == "EXAM":
                    id = info[2]
                    if id in exams:
                        del exams[id]
    for patient in patients:
        print(f"Name: {patient[name]}, Id: {patient[id]}, Exam Count: {patient.num_exams}")


if __name__ == "__main__":
    main()