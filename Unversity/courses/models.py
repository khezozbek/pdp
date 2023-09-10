from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    img = models.ImageField(upload_to='img', blank=True, null=True)
    number = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.title} by {self.author}'


class Teacher(models.Model):
    MATE = 'matematika'
    INFO = 'informatika'
    KIMYO = 'kimyo'
    ONA_TILI = 'onatili'

    sci = (
        (MATE, 'matematika'),
        (INFO, 'informatika'),
        (KIMYO, 'kimyo'),
        (ONA_TILI, 'onatili'),
    )

    name = models.CharField(max_length=120)
    fris_name = models.CharField(max_length=120)
    science = models.CharField(max_length=50, choices=sci)

    def __str__(self):
        return f'{self.name} {self.fris_name}'


class User(models.Model):
    TECHER = 'techer'
    STUDENT = 'student'

    LVLS = (
        (TECHER, 'techer'),
        (STUDENT, 'student'),
    )

    roel = models.CharField(max_length=120, choices=LVLS)
    last_name = models.CharField(max_length=200)
    frst_name = models.CharField(max_length=200)
    fovarid_book = models.ManyToManyField(Book, blank=True, null=True)

    def __str__(self):
        return f'{self.last_name} {self.frst_name} {self.roel}'


class Bookrecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_to = models.DateTimeField()
    returnbook = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f'{self.user} {self.book} on {self.book_to} returnbook {self.returnbook}'