## ***Need Skills***
- Math functions
- Writing files

# Goal
- More exams!<br>
Rank the applicants by the mean score of several final exams.

# Description
- Some of the departments proposed an improvement to the algorithm.<br>
They need more than one exam results for each applicant.<br>
For example, the Physics Department needs both math and physics exams, while the Mathematics Department is satisfied with the math exam only.<br>
Let's implement this request to make our departments happy (the applicants on the other hand...) 

# Objective
- At this stage, your program should:
    1. Read an `N` integer from the input.<br>
    This integer represents the maximum number of students for each department.
    1. Read the file named `applicants.txt` once again.<br>
    The file has the same structure as in the previous stage.
    1. Consider the following exam results for departments: physics and math for the Physics department, chemistry for the Chemistry department, math for the Mathematics department, computer science and math for the Engineering Department, chemistry and physics for the Biotech department.
    1. As in the previous stage, the exams are listed in the following order for each applicant: physics, chemistry, math, computer science.
    1. For the departments that need several exams, calculate the mean score and use it to rank the applicants (use floating-point numbers with at least one decimal).<br>
    Otherwise, use the result for a single exam.
    1. Keep the rest of the steps the same as in the previous stage (once again, there should be no more than `N` accepted applicants for each department; use the same principles for sorting).
    1. Instead of printing the results (you may do it if you want), output the admission lists to files.<br>
    Create a file for each department, name it `%department_name%.txt`, for example, `physics.txt`.<br>
    Write the names of the students accepted to the department and their mean finals score to the corresponding file (one student per line).
    
# Example
- The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the output.

- Below is an extract of the input file:
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
- The terminal output:
```
> 7
```
- The examples of the output to different files:
- `biotech,txt:`
```
Randon Bradhust 80.0
Narissa Worthington 61.5
```
- `chemistry.txt:`
```
Estephanie Phelps 95.0
Crescentia Dow 94.0
Tawny Crockett 90.0
Halima Brydone 85.0
```
- `engineering.txt:`
```
Lorry Bunger 90.5
Nicolasa Sumpter 88.5
Cheyla Hankinson 87.0
Tommi Peerless 86.5
Cynthia Hermitton 75.0
Marti Mclaws 60.5
Natha Keefe 56.5
```
- `mathematics.txt:`
```
Kennon Inverarity 98.0
Aundria Guthrie 94.0
Esther Bratby 88.0
Shealynn Melville 88.0
Teneil Maclean 84.0
Dashawn Bosley 82.0
```
- `physics.txt`
```
Cressie Gillespie 83.5
Giovanna Keel 80.0
Darrah Smyth 79.5
Fatemah Desavigny 77.0
```