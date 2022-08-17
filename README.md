# student-search-pclub-secy-task
 Task Required To Be Done By Prospective Secretaries Of PClub IITK.

## Contents Inside The Repository
This Repository Contains The Replica Of The Site https://search.pclub.in/ Along With Additional Implementation Of IITK Family Tree Functionality.

### Images Of The Student Search Site
![](https://github.com/Ankush0077/student-search-pclub-secy-task/blob/main/Images/landing_page_no_results.jpg)

![](https://github.com/Ankush0077/student-search-pclub-secy-task/blob/main/Images/srudent_search_one_result.jpg)

![](https://github.com/Ankush0077/student-search-pclub-secy-task/blob/main/Images/student_search_many_results.jpg)

![](https://github.com/Ankush0077/student-search-pclub-secy-task/blob/main/Images/student_search_information.jpg)

![](https://github.com/Ankush0077/student-search-pclub-secy-task/blob/main/Images/student_search_family_tree.jpg)


### STEPS REQUIRED TO OPEN THE STUDENT SEARCH SITE
(**CAUTION**: Make sure python is installed in the system.)

1) First clone the repository.
2) Open the repository in terminal.
3) Activate the env environment(Most probably by command `env/scripts/activate`).
4) Change directory to core(by command `cd core` in windows).
5) The the server by the command `python manage.py runserver`

### Accessing Admin Site
To Add Data To Data Base You Need To Go To Admin Panel Of The Site. You Need To Add '/admin' To Base Url.
The Username And Password Is Both 'admin'.

![Admin Site Login Page](https://github.com/Ankush0077/student-search-pclub-secy-task/blob/main/Images/admin_site_login.jpg)

![Admin Site](https://github.com/Ankush0077/student-search-pclub-secy-task/blob/main/Images/admin_site.jpg)

![Admin Site Table](https://github.com/Ankush0077/student-search-pclub-secy-task/blob/main/Images/admin_site_students.jpg)

![Admin Site Adding Data](https://github.com/Ankush0077/student-search-pclub-secy-task/blob/main/Images/admin_site_add.jpg)

### Additional Features
This Repository Also Contains A Simple CREATE,UPDATE,READ,DELETE Site Which Is Based On A Separate Model
As Prescribed In Task 5. You Can Access That Site If You Add '/student' To Base URL.

![Student Landing Page](https://github.com/Ankush0077/student-search-pclub-secy-task/blob/main/Images/student_landing_page.jpg)

![Student Add Page](https://github.com/Ankush0077/student-search-pclub-secy-task/blob/main/Images/student_add_page.jpg)

### Summary
Thus, This Repository Implements All The CRUD Operations As Well As FIltering(Major Part) On The Basis Of Fields.

**NOTE**: Templates Are Made Mainly By The Use Of BootStrap.

Thank You.