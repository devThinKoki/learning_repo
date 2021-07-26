class UniversitySystem():
    def __init__(self):
        self.applicants = load_applicants()
        self.departments = {"Biotech": (0,1), "Chemistry": (1,), "Engineering": (2, 3), "Mathematics": (2,), "Physics": (0, 2)}
        self.successful_candidates = {dept: [] for dept in self.departments.keys()}
        self.max_acceptance = int(input())

    def select_students(self, prior):
        for dept, targets in self.departments.items():
            current_applicants = self.applicants[:]
            for applicant in sort_by_score_name(self.applicants, targets):
                if applicant[2][prior] == dept:
                    if len(self.successful_candidates[dept]) < self.max_acceptance:
                        self.successful_candidates[dept].append(applicant)
                        current_applicants.remove(applicant)
            self.applicants = current_applicants

    def write_file(self):
        for dept, targets in self.departments.items():
            file_name = f"{dept}.txt"
            with open(file_name, 'w') as f:
                for accepted in sort_by_score_name(self.successful_candidates[dept], targets):
                    f.write(f"{accepted[0]} {calculate_mean(accepted, targets)}\n")

def load_applicants():
    with open(r"D:\LocalServer\learning_repo\JetBrains_Academy\Python_Development_Course\Medium_University-Admission-Procedure\07_Something-special\example.txt") as f:
        lines, applicants = f.readlines(), []
        for line in lines:
            first_name, last_name, p, c, m, cs, sp, *departments_by_priority = line.rstrip().split()
            applicants.append((f"{first_name} {last_name}", [int(p), int(c), int(m), int(cs), int(sp)], departments_by_priority))
        return applicants

def calculate_mean(applicant, targets):
    scores = [int(applicant[1][i]) for i in targets]
    return max([sum(scores) / len(scores), float(applicant[1][-1])])

def sort_by_score_name(original_list, targets):
    return sorted(original_list, key=lambda x: (-calculate_mean(x, targets), x[0]))

jet_brain = UniversitySystem()
for prior in range(3):
    jet_brain.select_students(prior)
jet_brain.write_file()