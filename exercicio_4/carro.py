def a1():
    def __init__(self,cap_dep,quant_comb,consumo):
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo

    def combustivel(self):
        return self.quant_comb
    def abastece(self,quantidade):
        return self.quant_comb + quantidade
    def percorre(self,quantidade):
        if self.quant_comb < (quantidade * self.consumo):
            return "erro"
        else:
            return self.quant_comb - (quantidade*self.consumo)
