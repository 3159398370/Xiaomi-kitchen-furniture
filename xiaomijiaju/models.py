from django.db import models

class Product(models.Model):
    # 产品名称
    name = models.CharField(max_length=100, verbose_name="产品名称")
    # 图片路径
    image = models.CharField(max_length=200, verbose_name="图片路径", default="img/placeholder.jpg")
    # 价格
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格")
    # 分类
    category = models.CharField(max_length=50, verbose_name="分类")

    def __str__(self):
        return self.name

    def get_image_url(self):
        # 返回静态图片路径
        if self.image:
            return f"/static/{self.image}"
        return "/static/img/placeholder.jpg"

class InstallationRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    address = models.TextField()
    product = models.CharField(max_length=50)
    date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.product}"