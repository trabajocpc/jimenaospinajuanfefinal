import pandas as pd
from data.platos import platosPopulares
from data.creartabla import crearTabla
from data.proveedores import proveedores
from data.reservas import reservas


tablaPlatos=pd.DataFrame(platosPopulares)
print(tablaPlatos)
crearTabla(tablaPlatos,"platosPopulares")

tablaReservas=pd.DataFrame(reservas)
print(tablaReservas)
crearTabla(tablaReservas,"tablareservas")

tablaProveedores=pd.DataFrame(proveedores)
print(tablaProveedores)
crearTabla(tablaProveedores,"tablaproveedores")
