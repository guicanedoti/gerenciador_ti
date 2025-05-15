from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Sala(models.Model): 
    nome = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE) 
    
    def __str__(self):
        return f"{self.nome} ({self.departamento.nome})" 
    
class Responsavel(models.Model): 
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.nome} - {self.matricula}" 

class Equipamento(models.Model): 
    TIPOS = [
        ('Monitor', 'Monitor'), 
        ('Teclado', 'Teclado'), 
        ('Mouse', 'Mouse'),
        ('CPU', 'CPU'), 
        ('Impressora', 'Impressora'),
        ('Outro', 'Outro'),
    ] 

    tipo = models.CharField(max_length=20, choices=TIPOS)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    numero_patrimonio = models.CharField(max_length=30, unique=True)
    status = models.CharField(max_length=20, choices=[
        ('Estoque', 'Estoque'), 
        ('Em uso', 'Em uso'),
        ('Manutenção', 'Manutenção'),
        ('Com defeito', 'Com defeito')
    ]) 
    descricao = models.TextField(blank=True) 
    
    def __str__(self):
         return f"{self.tipo} - {self.numero_patrimonio}" 

class Alocacao(models.Model): 
    equipamento = models.ForeignKey(Equipamento,on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel,on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    data_alocacao = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.equipamento} → {self.responsavel} ({self.sala})"