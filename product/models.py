from django.db import models


class Product(models.Model):
    """
    상품 모델입니다.
    상품 코드, 상품 이름, 상품 설명, 상품 가격, 사이즈 필드를 가집니다.
    """
    codes = (
        ('hood-001', '후드 1'),
        ('hood-002', '후드 2'),
        ('hood-003', '후드 3'),
        ('jean-001', '청바지 1'),
        ('jean-002', '청바지 2'),
        ('jean-003', '청바지 3'),
        ('socks', '양말'),
        ('cap', '모자'),
    )
    code = models.CharField(choices=codes, max_length=10, verbose_name='제품 코드')
    name = models.CharField(max_length=10, verbose_name='제품명')
    description = models.CharField(max_length=50, verbose_name='설명')
    price = models.IntegerField(default=0, verbose_name='가격')
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1, verbose_name='사이즈')

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

# super() 함수의 첫 번째 인자는 부모 클래스의 이름인 Product이어야 하고,
# 이후에 self가 인스턴스를 참조하므로 Product 모델의 인스턴스가 정확하게
# 저장되도록 합니다. 이렇게 하면 부모 클래스인 models.Model의 save()
# 메서드가 올바르게 호출되어, 인스턴스가 데이터베이스에 저장되게 됩니다.
