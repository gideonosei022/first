from django.db import models

class Calculation(models.Model):
    operand1 = models.FloatField()
    operand2 = models.FloatField()
    operator = models.CharField(max_length=10)  # '+', '-', '*', '/'
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.operand1} {self.operator} {self.operand2} = {self.result}"