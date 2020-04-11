from django.db import models, transaction

class Vote(models.Model):
    association_name = models.CharField(max_length=200)
    vote  = models.IntegerField(default=0)

    def __str__(self):
        # return '%s: %d votes' %(self.association_name, self.count)
        return self.association_name

    @classmethod
    def bulk_vote(cls, association_names):
        with transaction.atomic():
            for association_name in association_names:
                if len(association_name) == 0:
                    continue
                if Vote.objects.filter(association_name=association_name).exists():
                    Vote.objects.filter(association_name=association_name).update(vote=models.F('count')+1)
                else:
                    Vote.objects.create(association_name=association_name, vote=1)


