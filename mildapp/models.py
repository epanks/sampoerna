from django.db import models


class Wilayah(models.Model):
    nmwilayah = models.CharField(max_length=60)

    def __str__(self):
        return self.nmwilayah


class Balai(models.Model):
    nmbalai = models.CharField(max_length=200, null=True)
    wilayah = models.ForeignKey(Wilayah,
                                on_delete=models.DO_NOTHING,
                                null=True)

    def __str__(self):
        return self.nmbalai


class Satker(models.Model):
    kdsatker = models.CharField(max_length=8, unique=True, primary_key=True)
    nmsatker = models.CharField(max_length=200)
    phone = models.CharField(max_length=12, null=True)
    balai = models.ForeignKey(Balai, on_delete=models.DO_NOTHING, null=True)
    wilayah = models.ForeignKey(Wilayah,
                                on_delete=models.DO_NOTHING,
                                null=True)

    def __str__(self):
        return self.nmsatker


class Ppk(models.Model):
    nmppk = models.CharField(max_length=100)
    nmjabatan = models.CharField(max_length=100)
    phone = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=255)
    kdsatker = models.ForeignKey(Satker,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    balai = models.ForeignKey(Balai, on_delete=models.DO_NOTHING, null=True)
    wilayah = models.ForeignKey(Wilayah,
                                on_delete=models.DO_NOTHING,
                                null=True)

    def __str__(self):
        return self.nmppk


class Satoutput(models.Model):
    nmsatoutput = models.CharField(max_length=45)

    def __str__(self):
        return self.nmsatoutput


class Satoutcome(models.Model):
    nmsatoutcome = models.CharField(max_length=45)

    def __str__(self):
        return self.nmsatoutcome


class Ta(models.Model):
    tahun = models.CharField(max_length=45)

    def __str__(self):
        return self.tahun


class Ks(models.Model):
    nmks = models.CharField(max_length=45)

    def __str__(self):
        return self.nmks


class Fnf(models.Model):
    nmfnf = models.CharField(max_length=45)

    def __str__(self):
        return self.nmfnf


class Sycmyc(models.Model):
    nmsycmyc = models.CharField(max_length=45)

    def __str__(self):
        return self.nmsycmyc


class Kodeoutput(models.Model):
    kdoutput = models.CharField(max_length=3, unique=True, primary_key=True)
    nmkdoutput = models.CharField(max_length=250)

    def __str__(self):
        return self.nmkdoutput


class Tag(models.Model):
    tag = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.tag


class Paket(models.Model):
    balai = models.ForeignKey(Balai, on_delete=models.DO_NOTHING, null=True)
    nmpaket = models.CharField(max_length=250)
    kdoutput = models.ForeignKey(Kodeoutput, max_length=3, null=True, on_delete=models.DO_NOTHING)
    # pagurmp = models.FloatField(null=True)
    trgoutput = models.DecimalField(max_digits=15, decimal_places=9, null=True)
    satoutput = models.ForeignKey(Satoutput,
                                  on_delete=models.DO_NOTHING,
                                  null=True)
    trgoutcome = models.DecimalField(max_digits=15, decimal_places=9, null=True)
    satoutcome = models.ForeignKey(Satoutcome,
                                   on_delete=models.DO_NOTHING,
                                   null=True)
    ta = models.ForeignKey(Ta, on_delete=models.DO_NOTHING, null=True)
    ppk = models.ForeignKey(Ppk, on_delete=models.DO_NOTHING, null=True)
    ks = models.ForeignKey(Ks, on_delete=models.DO_NOTHING, null=True)
    fnf = models.ForeignKey(Fnf, on_delete=models.DO_NOTHING, null=True)
    sycmyc = models.ForeignKey(Sycmyc, on_delete=models.DO_NOTHING, null=True)
    tag = models.ManyToManyField(Tag)
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, null=True)
    wilayah = models.ForeignKey(Wilayah,
                                on_delete=models.DO_NOTHING,
                                null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nmpaket


class Pagu(models.Model):
    paket = models.OneToOneField(Paket, on_delete=models.DO_NOTHING, primary_key=True)
    pagurmp = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    phln = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    sbsn = models.DecimalField(max_digits=15, decimal_places=2, null=True)



class Progres(models.Model):
    keuangan = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    fisik = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    paket = models.ForeignKey(Paket, on_delete=models.DO_NOTHING, null=True)


class Note(models.Model):
    nmnote = models.CharField(max_length=250, null=True)
    lampirannote = models.CharField(max_length=250, null=True)
    paket = models.ForeignKey(Paket, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.nmnote


class Lampiran(models.Model):
    nmlampiran = models.CharField(max_length=250, null=True)
    lampiran = models.CharField(max_length=250, null=True)
    paket = models.ForeignKey(Paket, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.nmlampiran


class Foto(models.Model):
    nmfoto = models.CharField(max_length=250, null=True)
    foto = models.CharField(max_length=250, null=True)
    paket = models.ForeignKey(Paket, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.nmfoto


class Sistem(models.Model):
    nmsistem = models.CharField(max_length=250, null=True)
    paket = models.ForeignKey(Paket, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.nmsistem