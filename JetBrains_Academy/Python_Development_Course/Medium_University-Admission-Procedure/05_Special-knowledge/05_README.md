## ***Need Skills***
- Program execution
- Load module
- Errors
- Built-in exceptions
- Exception handliing

# Goal
- GPAs are no longer needed as there are final exams after all! Also, applicants can now apply to several departments. 

# Description
- Taking only student's GPAs into consideration may not be very conclusive.<br>
It would be better if we could take the results of the finals depending on the Department.<br>
For example, for a Physics department candidate, we would check the physics finals.<br>
Try to take the sorting algorithm to the next level.<br>
In this stage, you need to sort by an exam that suits the particular Department.

# Objective
- At this stage, your program should:
    1. Read an `N` integer. This integer represents the maximum number of students for each department.
    1. Read the file named `applicants.txt` once again. The structure has changed a bit: instead of the GPA column, each line contains four columns with scores for particular exams: physics, chemistry, math, computer science (in this order).<br>
    For example, `John Ritchie 89 45 83 75 Physics Engineering Mathematics`.
    1. Take into account the following exam results for the departments: physics for the Physics department, chemistry for the Chemistry department, math for the Mathematics department, computer science for the Engineering, and chemistry (again) for the Biotech department.
    1. Do the same steps as in the previous stage: perform three stages of admission based on the applicants' priorities.<br>
    Applicants should be ranked by their exam score and, in case they have the same score, their full name in alphabetic order.<br>
    There should be no more than `N` accepted applicants for each department.<br>
    One student can only be accepted to one department.
    1. One thing has changed — output the exam result (instead of the GPA) for each student:
```
department_name
applicant1 exam1
applicant2 exam2
applicant3 exam3
<...>
```
    
# Example
- The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the output.

- Below is an example of the input file:
```
Natha Keefe 71 67 53 60 Engineering Biotech Chemistry
Crescentia Dow 86 94 85 51 Chemistry Physics Mathematics
Randon Bradhust 72 88 85 83 Biotech Engineering Chemistry
Dashawn Bosley 80 79 82 61 Mathematics Chemistry Biotech
Nicolasa Sumpter 75 82 96 81 Engineering Mathematics Biotech
Cressie Gillespie 85 92 82 70 Physics Mathematics Engineering
Tawny Crockett 71 90 80 72 Chemistry Biotech Physics
Kennon Inverarity 71 84 98 71 Mathematics Engineering Chemistry
Halima Brydone 77 85 82 86 Chemistry Physics Mathematics
Esther Bratby 55 76 88 62 Mathematics Chemistry Biotech
Lorry Bunger 75 73 84 97 Engineering Biotech Physics
Fatemah Desavigny 81 71 73 86 Physics Mathematics Engineering
Marti Mclaws 71 71 61 60 Engineering Chemistry Biotech
Estephanie Phelps 80 95 45 71 Chemistry Physics Mathematics
Tommi Peerless 72 81 81 92 Engineering Physics Mathematics
Cynthia Hermitton 70 59 62 88 Engineering Biotech Chemistry
Cheyla Hankinson 75 80 86 88 Engineering Mathematics Biotech
Giovanna Keel 84 71 76 80 Physics Mathematics Engineering
Narissa Worthington 52 71 80 73 Biotech Chemistry Mathematics
Aundria Guthrie 61 81 94 71 Mathematics Chemistry Engineering
Teneil Maclean 85 63 84 45 Mathematics Physics Chemistry
Shealynn Melville 74 76 88 62 Mathematics Chemistry Physics
Darrah Smyth 75 73 84 97 Physics Biotech Engineering
```
- This is an example of the output:
```
> 5
Biotech
Randon Bradhust 88.0
Marti Mclaws 71.0
Narissa Worthington 71.0
Natha Keefe 67.0

Chemistry
Estephanie Phelps 95.0
Crescentia Dow 94.0
Tawny Crockett 90.0
Halima Brydone 85.0
Dashawn Bosley 79.0

Engineering
Lorry Bunger 97.0
Tommi Peerless 92.0
Cheyla Hankinson 88.0
Cynthia Hermitton 88.0
Nicolasa Sumpter 81.0

Mathematics
Kennon Inverarity 98.0
Aundria Guthrie 94.0
Esther Bratby 88.0
Shealynn Melville 88.0
Teneil Maclean 84.0

Physics
Cressie Gillespie 85.0
Giovanna Keel 84.0
Fatemah Desavigny 81.0
Darrah Smyth 75.0
```