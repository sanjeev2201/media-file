state_choices = (("Andhra Pradesh","Andhra Pradesh"),
("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),
("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),
("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),
("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),
("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),
("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),
("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),
("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),
("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),
("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),
("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),
("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),
("Puducherry","Puducherry"))

#state = models.CharField(choices=state_choices,max_length=255, null=True, blank=True)

GENDER_CHOICES = [('Male','Male'),('Female','Female'),('Transgender','Transgender')]
#Gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))

JOB_CHOICES = [('Bangalore','Bangalore'),
('Chennai','Chennai'),('Hyderabad','Hyderabad'),
('Noida','Noida'),('New delhi','New delhi')]