from rest_framework import serializers
from home2.models import*

class producto_serializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Producto
        fields = ('url','nombre','descripcion','status','precio','stock','marca','categorias','imagen',)
        

class marca_serializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Marca
        fields = ('url','id','nombre', )
        

class categoria_serializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Categoria
        fields = ('url','nombre', )
        


