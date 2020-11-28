from django.db import models


class IdentificationDocument(models.Model):
    name = models.TextField(max_length=200, default=" ")

    def __str__(self):
    	return self.name



class Study(models.Model):
    name = models.TextField(max_length=200, default=" ")

    def __str__(self):
    	return self.name



class MaritalStatus(models.Model):
    name = models.TextField(max_length=200, default=" ")

    def __str__(self):
    	return self.name
    	

class User(models.Model):
	names = models.CharField(max_length=256,null=False)
	marital_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE)
	identification_document = models.ForeignKey(IdentificationDocument, on_delete=models.CASCADE)
	study = models.ForeignKey(Study, on_delete=models.CASCADE)
	first_last_name = models.CharField(max_length=256,null=False)
	second_last_name = models.CharField(max_length=256,null=False)
	number_identification = models.CharField(max_length=256,null=False)
	birth_date = models.DateField(blank=True, null=True)
	gender = models.CharField(max_length=256,null=False)
	residence_address = models.CharField(max_length=256,null=False)
	main_phone = models.CharField(max_length=256,null=False)
	secondary_phone = models.CharField(max_length=256,null=False)
	email = models.EmailField(max_length=256,null=False)

	def __str__(self):
		return self.names

