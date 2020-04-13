from django.db import models

# Create your models here.


class subjects(models.Model):
    dept = (
        ('CSE', 'Computer Science'),
        ('MH', 'Mech'),
        ('CV', "Civil"),
        ('ISE', 'Information Science'),
        ('EC', 'Electronics and Communication'),
        ('EEE', 'Electronics and Electrical'),
        ('TC', 'Telecommunication')
    )
    sub_name = models.CharField('sub_name', max_length=50)
    semester = models.CharField('semester', max_length=5)
    branch = models.CharField('branch', max_length=50,
                              choices=dept, null=True)
    sub_id = models.IntegerField('sub_id', primary_key =True)


class questionPaperDetails(models.Model):
    sqno = models.IntegerField('numberofSubquestions', null=True)
    a = models.IntegerField('a', null=True,default=0)
    b = models.IntegerField('b', null=True,default=0)
    c = models.IntegerField('c', null=True,default=0)
    d = models.IntegerField('d', null=True,default=0)
    br = (
        ('CSE', 'Computer Science and Engg.'),
        ('MH', 'Mechanical Engg.'),
        ('CV', "Civil Engg."),
        ('ISE', "Information science and Engg."),
        ('ECE', "Electronics and Communication and Engg."),
        ('EEE', "Electrical and Electronics Engg."),
        ('EIE', "Electronics and Instrumentation Engg."),
        ('TC', "Telecommunication Engg."),
        ('BT', "Biotechnology Engg."),
        ('CH', "Chemical Engg."),
        ('IEM', 'Industrial Engg. and Management'),
    )
    branch = models.CharField('Branch', choices=br,
                              blank=True, null=True, max_length=40)
    s = (
        ('1', 'I'),
        ('2', 'II'),
        ('3', 'III'),
        ('4', 'IV'),
        ('5', 'V'),
        ('6', 'VI'),
        ('7', 'VII'),
        ('8', 'VIII'),
    )
    semester = models.CharField('semester', choices=s,
                                blank=True, null=True, max_length=5)
    slNo=models.IntegerField('slNo',null=True)
    qno = models.IntegerField('qno',null=True)
    sub_id = models.ForeignKey('subjects',default=4444, on_delete = models.CASCADE)
    sem_id=models.IntegerField('sem_id')
    class Meta:
        unique_together = ("sub_id","sem_id","qno")

class generatebarcode(models.Model):
    semid = models.IntegerField('SemesterID')
    studentid = models.IntegerField('StudentID')
    courseid = models.IntegerField("CourseID", null=True)
    sub_id = models.ForeignKey("subjects", on_delete=models.CASCADE)
    empgrp = models.IntegerField("EmpGroup", null=True)
    Barcode = models.CharField("Barcode", max_length=10)
    create_date = models.DateField("Created_date")
    modif_date = models.DateField("Modified_date")
    create_by= models.IntegerField("Create_By")
    modified_by= models.IntegerField("Modified_by")
    print_status= models.IntegerField("Print_Status",null=True)
    class Meta:
        unique_together = ("semid","studentid","Barcode")

class tbl_studentmarks(models.Model):
    semid = models.IntegerField('SemesterID')
    studentid = models.IntegerField('StudentID')
    courseid = models.IntegerField("CourseID", null=True)
    sub_id = models.ForeignKey("subjects", on_delete=models.CASCADE)
    ia_awarded = models.IntegerField("IAAwarded",null=True)
    ia_passfail = models.IntegerField("IAPassFail")
    see_awarded = models.IntegerField("EndExamAwarded")
    see_passfail = models.IntegerField("EndExamPassFail")
    present_absent = models.IntegerField("PresentOrAbsent")
    attempt = models.IntegerField("Attempt",null=True)
    exam1 = models.IntegerField("Exam1")
    exam2 = models.IntegerField("Exam2")
    exam3 = models.IntegerField("Exam3",null=True)
    valuation3 = models.IntegerField("Valuation3")
    gracemarks = models.IntegerField("GraceMark")
    grade = models.CharField("Grade", max_length=2)
    attper = models.IntegerField("AttPer")
    eligible = models.IntegerField("EndExamEligible")
    nochange = models.IntegerField("NoChange",null=True)


class detailed_marks(models.Model):
    studentid = models.IntegerField("StudentID")
    semid = models.IntegerField("SemID")
    sub_id = models.ForeignKey("subjects", on_delete=models.CASCADE)
    a1 = models.IntegerField("1a",null=True,default=0)
    b1 = models.IntegerField("1b",null=True,default=0)
    c1 = models.IntegerField("1c",null=True,default=0)
    d1 = models.IntegerField("1d",null=True,default=0)
    total1 = models.IntegerField("Total1",null=True,default=0)
    a2 = models.IntegerField("2a",null=True,default=0)
    b2 = models.IntegerField("2b",null=True,default=0)
    c2 = models.IntegerField("2c",null=True,default=0)
    d2 = models.IntegerField("2d",null=True,default=0)
    total2 = models.IntegerField("Total2",null=True,default=0)
    max1 = models.IntegerField("MaxTotal1",null=True,default=0)
    a3 = models.IntegerField("3a",null=True,default=0)
    b3 = models.IntegerField("3b",null=True,default=0)
    b3 = models.IntegerField("3b",null=True,default=0)
    c3 = models.IntegerField("3c",null=True,default=0)
    d3 = models.IntegerField("3d",null=True,default=0)
    total3 = models.IntegerField("Total3",null=True,default=0)
    a4 = models.IntegerField("4a",null=True,default=0)
    b4 = models.IntegerField("4b",null=True,default=0)
    c4 = models.IntegerField("4c",null=True,default=0)
    d4 = models.IntegerField("4d",null=True,default=0)
    total4 = models.IntegerField("Total4",null=True,default=0)
    max2 = models.IntegerField("MaxTotal2",null=True,default=0)
    a5 = models.IntegerField("5a",null=True,default=0)
    b5 = models.IntegerField("5b",null=True,default=0)
    c5 = models.IntegerField("5c",null=True,default=0)
    d5 = models.IntegerField("5d",null=True,default=0)
    total5 = models.IntegerField("Total5",null=True,default=0)
    a6 = models.IntegerField("6a",null=True,default=0)
    b6 = models.IntegerField("6b",null=True,default=0)
    c6 = models.IntegerField("6c",null=True,default=0)
    d6 = models.IntegerField("6d",null=True,default=0)
    total6 = models.IntegerField("Total6",null=True,default=0)
    max3 = models.IntegerField("MaxTotal3",null=True,default=0)
    a7 = models.IntegerField("7a",null=True,default=0)
    b7 = models.IntegerField("7b",null=True,default=0)
    c7 = models.IntegerField("7c",null=True,default=0)
    d7 = models.IntegerField("7d",null=True,default=0)
    total7 = models.IntegerField("Total7",null=True,default=0)
    a8 = models.IntegerField("8a",null=True,default=0)
    b8 = models.IntegerField("8b",null=True,default=0)
    c8 = models.IntegerField("8c",null=True,default=0)
    d8 = models.IntegerField("8d",null=True,default=0)
    total8 = models.IntegerField("Total8",null=True,default=0)
    max4 = models.IntegerField("MaxTotal4",null=True,default=0)
    a9 = models.IntegerField("9a",null=True,default=0)
    b9 = models.IntegerField("9b",null=True,default=0)
    c9 = models.IntegerField("9c",null=True,default=0)
    d9 = models.IntegerField("9d",null=True,default=0)
    total9 = models.IntegerField("Total9",null=True,default=0)
    a10 = models.IntegerField("10a",null=True,default=0)
    b10 = models.IntegerField("10b",null=True,default=0)
    c10 = models.IntegerField("10c",null=True,default=0)
    d10 = models.IntegerField("10d",null=True,default=0)
    total10 = models.IntegerField("Total10",null=True,default=0)
    max5 = models.IntegerField("MaxTotal5",null=True,default=0)
    FinalTotal = models.IntegerField("FinalTotal",null=True,default=0)
    Evaluator = models.IntegerField("Evaluator",default = 0)
    class Meta:
        unique_together = ("studentid","semid","sub_id","Evaluator")