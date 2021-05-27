from .models import Category, Marca, Product
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    marca = MarcaSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),source="category")
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(),source="marca")
    product_name = serializers.CharField(required=True,min_length=5)

    def validate_nombre(self,value):
        exists = Product.objects.filter(product_name__iexact=value).exists()
        if exists:
            raise serializers.ValidationError("Este producto ya existe")
        return value

    class Meta:
        model = Product
        fields = '__all__'
 