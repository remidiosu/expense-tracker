from tortoise import models, fields


class Expenses(models.Model):
    id = fields.IntField(pk=True)
    amount = fields.FloatField()
    category = fields.CharField(max_length=64)
    description = fields.TextField(null=True)
    date = fields.DateField()

    def __str__(self):
        return f"{self.date} - {self.category}: {self.amount}"
