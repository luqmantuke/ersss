from django.db import models

gender_choices = (('Male', 'Male'), ('Female', 'Female'))
division_choices = (('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'))
combination_choices = (('PCM', 'PCM'), ('PCB', 'PCB'), ('PGM', 'PGM'), ('CBG', 'CBG'), ('HKL', 'HKL'))
grade_choices = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))

class AlevelApplication(models.Model):
    Full_name = models.CharField(max_length=900)
    Date_of_birth = models.CharField(max_length=100)
    Gender = models.CharField(choices=gender_choices, max_length=100)
    Nationaliy = models.CharField(max_length=700)
    Region = models.CharField(max_length=800)
    Religion = models.CharField(max_length=100)
    Denomination = models.CharField(max_length=100)
    Year_Of_Complilation_Form_Iv = models.CharField(max_length=50)
    Name_Of_The_Secondary_School = models.CharField(max_length=600)
    Your_National_Examination_No = models.CharField(max_length=200)
    Division = models.CharField(choices=division_choices, max_length=100)
    Points = models.CharField(max_length=100)
    First_Selection = models.CharField(choices=combination_choices, max_length=100)
    Second_Selection = models.CharField(choices=combination_choices, max_length=100)
    Fathers_Name = models.CharField(max_length=700)
    Father_Occupation = models.CharField(max_length=700)
    Father_Number = models.CharField(max_length=700)
    Mother_Name = models.CharField(max_length=700)
    Mother_Occupation = models.CharField(max_length=700)
    Mother_Number = models.CharField(max_length=700)

    def __str__(self):
        return self.Full_name

class OlevelApplication(models.Model):
    Full_name = models.CharField(max_length=900)
    Date_of_birth = models.CharField(max_length=100)
    Gender = models.CharField(choices=gender_choices, max_length=100)
    Nationaliy = models.CharField(max_length=700)
    Region = models.CharField(max_length=800)
    Religion = models.CharField(max_length=100)
    Denomination = models.CharField(max_length=100)
    Year_Of_Complilation_Class_7 = models.CharField(max_length=50)
    Name_Of_The_Primary_School = models.CharField(max_length=600)
    Your_National_Examination_No = models.CharField(max_length=200)
    Grade = models.CharField(choices=grade_choices, max_length=100)
    Fathers_Name = models.CharField(max_length=700)
    Father_Occupation = models.CharField(max_length=700)
    Father_Number = models.CharField(max_length=700)
    Mother_Name = models.CharField(max_length=700)
    Mother_Occupation = models.CharField(max_length=700)
    Mother_Number = models.CharField(max_length=700)

    def __str__(self):
        return self.Full_name