def crearTabla(dataFrame,nombreTabla):
    archivoHTML=dataFrame.to_html()
    archivo=open(f"./tables/{nombreTabla}.html","w",encoding='utf-8')
    archivo.write(archivoHTML)
    archivo.close()