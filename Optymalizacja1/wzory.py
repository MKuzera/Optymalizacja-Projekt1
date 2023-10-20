from dane import Dane
class Mthod:
    
    def dV_dt(self, D, V, P):
        """
        Zmiana objętość wody w zbiorniku spowodowana
        jej wypływem przez otwór o polu przekroju 𝐷 dana jest wzorem

        Args:
            a (_type_): wspolczynik lekosci
            b (_type_): współczynnik odpowiadający za lepkość cieczy
            D (_type_): przekroju odlewa
            V : objentosć

        Returns:
            dV/dt
        """
        return -1*( Dane.a * Dane.b * D * (2*Dane.g * (V/P) )**(1/2) )
    
    def dT_dt(self, Tin, Vin, T,V):
        """
        Zmiana temperatury wody w zbiorniku dana jest wzorem:

        Args:
            Tin (_type_): temp wody wejsciowej
            Vin (_type_): ovj wody wejsciowej
            T (_type_): temp w zbiorniko
            V (_type_): obj w zbirniko
        """
        return (Vin/V)*(Tin - T)
    