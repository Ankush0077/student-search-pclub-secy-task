from django.db import models

# Create your models here.
class Student(models.Model):
   imGE=models.ImageField(upload_to=True,blank=True,null=True)
   name=models.CharField(max_length=100)
   userid=models.CharField(max_length=100)
   GENDER_CHOICES=(
       ('Male','Male'),
       ('Female','Female'),
   )
   gender=models.CharField(max_length=50,choices=GENDER_CHOICES)
   roll_no=models.CharField(max_length=20)
   YEAR_CHOICES=(
       ('Y22','Y22'),
       ('Y21','Y21'),
       ('Y20','Y20'),
       ('Y19','Y19'),
       ('Y18','Y18'),
       ('Y17','Y17'),
       ('Y16','Y16'),
       ('Y15','Y15'),
       ('Y14','Y14'),
       ('Y13','Y13'),
       ('Y12','Y12'),
       ('Y11','Y11'),
       ('Y10','Y10'),
       ('Y9','Y9'),
       ('Y8','Y8'),
       ('Other','Other'),
   )
   year=models.CharField(max_length=5,choices=YEAR_CHOICES)
   BRANCH_CHOICES= (
       ('Aerospace Engineering','Aerospace Engineering'),
       ('Biological Sciences and Bioengineering','Biological Sciences and Bioengineering'),
       ('Civil Engineering','Civil Engineering'),
       ('Chemical Engineering','Chemical Engineering'),
       ('Chemistry','Chemistry'),
       ('Computer Science and Engineering','Computer Science and Engineering'),
       ('Cognitive Sciences','Cognitive Sciences'),
       ('Dean Of Academic Affairs','Dean Of Academic Affairs'),
       ('Dean Of Resource Affairs','Dean Of Resource Affairs'),
       ('Dean Of Research and Development','Dean Of Research and Development'),
       ('Economic Sciences','Economic Sciences'),
       ('Electrical Engineering','Electrical Engineering'),
       ('EEM','EEM'),
       ('Earth Sciences','Earth Sciences'),
       ('Humanities and Social Sciences','Humanities and Social Sciences'),
       ('Industrial and Management Engineering','Industrial and Management Engineering'),
       ('Laser Technology','Laser Technology'),
       ('MDes','MDes'),
       ('Mechanical Engineering','Mechanical Engineering'),
       ('Material Science and Engineering','Material Science and Engineering'),
       ('Mathematics and Statistics','Mathematics and Statistics'),
       ('Mat. and Met.Engg.','Mat. and Met.Engg.'),
       ('Materials Science Programme','Materials Science Programme'),
       ('Mathematics And Scientific Comp','Mathematics And Scientific Comp'),
       ('Nuc. Engg. and Tech Prog.','Nuc. Engg. and Tech Prog.'),
       ('Null','Null'),
       ('Physics','Physics'),
       ('Photonics Science and Engg.','Photonics Science and Engg.'),
       ('Statistics','Statistics'),
       ('Statistics And Data Science','Statistics And Data Science'),
       ('Sustainable Energy Engineering','Sustainable Energy Engineering'),
   )
   branch=models.CharField(max_length=100, choices=BRANCH_CHOICES)
   PROGRAMME_CHOICES=(
       ('BS','BS'),
       ('BS-MBA','BS-MBA'),
       ('BS-MS','BS-MS'),
       ('BS-MT','BS-MT'),
       ('BT-M.Des','BT-M.Des'),
       ('BT-MBA','BT-MBA'),
       ('BT-MS','BT-MS'),
       ('B.Tech','B.Tech'),
       ('DIIT','DIIT'),
       ('Exchange Programme','Exchange Programme'),
       ('MBA','MBA'),
       ('M.Des','M.Des'),
       ('MS-Research','MS-Research'),
       ('MSc(2 yr)','MSc(2 yr)'),
       ('MSc(Int)','MSc(Int)'),
       ('MSc-PhD(Dual)','MSc-PhD(Dual)'),
       ('MT(Dual)','MT(Dual)'),
       ('M.Tech','M.Tech'),
       ('PGPEX-VLM','PGPEX-VLM'),
       ('PhD','PhD'),
       ('Prep.','Prep.'),
       ('SURGE','SURGE'),
       ('eMasters','eMasters'),
   )
   programme=models.CharField(max_length=30, choices=PROGRAMME_CHOICES)
   room_no=models.CharField(max_length=30)
   HALL_CHOICES=(
       ('HALL 2','HALL 2'),
       ('HALL 13','HALL 13'),
       ('HALL 1','HALL 1'),
       ('HALL 3','HALL 3'),
       ('HALL 4','HALL 4'),
       ('HALL 5','HALL 5'),
       ('HALL 6','HALL 6'),
       ('HALL 7','HALL 7'),
       ('HALL 8','HALL 8'),
       ('HALL 9','HALL 9'),
       ('HALL 10','HALL 10'),
       ('HLL 11','HLL 11'),
       ('HALL 12','HALL 12'),
       ('GH','GH'),
       ('DAY','DAY'),
       ('CPWD','CPWD'),
       ('ACES','ACES'),
       ('NRA','NRA'),
       ('RA','RA'),
       ('SBRA','SBRA'),
       ('TYPE 1','TYPE 1'),
       ('TYPE 1B','TYPE 1B'),
       ('UNKN','UNKN'),
   )
   hall=models.CharField(max_length=20, choices=HALL_CHOICES)
   BLOOD_GROUP_CHOICES=(
       ('B+','B+'),
       ('B-','B-'),
       ('A+','A+'),
       ('A-','A-'),
       ('AB+','AB+'),
       ('AB-','AB-'),
       ('O+','O+'),
       ('O-','O-'),
   )
   blood_group=models.CharField(max_length=5,choices=BLOOD_GROUP_CHOICES)
   hometown=models.CharField(max_length=100, default='Kanpur')
   state=models.CharField(max_length=100, default='U.P.')
   country=models.CharField(max_length=100, default='India')
   student_guide=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
   
   SERNAME_FIELD ='roll_no'
   REQUIRED_FIELDS = ['name','gender','branch','programme',]
   
   def __str__(self):
       return self.name
   
   class Meta:
       db_table="student"