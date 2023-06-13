#Algoritmo Canny

El algoritmo de Canny es un algoritmo de análisis de imagen para la detección de bordes en imágenes, el cual se basa en 5 pasos principales. Estos pasos son:
1. Suavizado de la imagen: El primer paso consiste en aplicar un filtro Gaussiano para reducir el ruido presente en la imagen. Este filtro ayuda a eliminar los detalles de alta frecuencia que no son relevantes para la detección de bordes.
2. Cálculo del gradiente: Una vez que la imagen ha sido suavizada, se calcula el gradiente utilizando el operador Sobel. Este operador se aplica en las direcciones horizontal y vertical para obtener dos imágenes con la magnitud del gradiente en cada píxel.
3. Supresión de no máximos: Después de calcular el gradiente, se realiza la supresión de no máximos. Este paso consiste en recorrer la imagen y comparar la magnitud del gradiente en cada píxel con la de sus vecinos en la dirección del gradiente. Si el píxel actual tiene una magnitud del gradiente menor que la de sus vecinos, se establece su valor a cero. De esta manera, sólo se conservan los píxeles que corresponden a bordes.
4. Umbralización: El último paso es la umbralización, que consiste en establecer dos umbrales: uno alto y otro bajo. Los píxeles con una magnitud de gradiente superior al umbral alto se consideran bordes fuertes, mientras que los píxeles con una magnitud de gradiente inferior al umbral bajo se consideran no bordes. Los píxeles con una magnitud de gradiente entre los dos umbrales se consideran bordes débiles. 
5. Conexión de bordes: Finalmente, se realiza la conexión de bordes débiles con bordes fuertes. Esto se hace mediante el seguimiento de los bordes débiles en la dirección perpendicular al gradiente y comprobando si alguno de sus vecinos es un borde fuerte. Si es así, se considera que el borde débil forma parte del borde.

##Articulo

https://acofipapers.org/index.php/eiei/article/view/684

###Resumen del articulo

Una de las técnicas más utilizadas en radiobiología son los ensayos clonogénicos (o de formación de colonias), que buscan medir la pérdida en la capacidad de división celular en una célula tumoral después de haber sido tratada con radiación ionizante. El análisis de los datos obtenidos por esta técnica requiere del conteo de las colonias formadas a partir de cientos de células inicialmente irradiadas y cultivadas. Aunque existen algunos sistemas automáticos para el conteo de colonias, estos son en general muy costosos y/o sólo parcialmente automáticos. Por esta razón, en la mayoría de los casos el conteo se realiza de forma manual, haciendo de éste un proceso tedioso e impreciso. Para solucionar este problema, radiobiólogos, ingenieros y estudiantes de ingeniería biomédica y medicina de tres universidades, se unieron para desarrollar una estrategia que facilite la obtención de los datos de los ensayos clonogénicos. En este trabajo se presenta un nuevo método automático para el conteo de colonias de ensayos clonogénicos, basado en técnicas de procesamiento de imágenes. 

####Referencias

-Brugger S.D., Baumberger C., Jost M., Jenni W., Brugger U., Mühlemann K. (2012). Automated Counting of Bacterial Colony Forming Units on Agar Plates, PLoS ONE Vol. 7, Issue 3, e33695.
-Puck, T. T. (1956). ACTION OF X-RAYS ON MAMMALIAN CELLS. Journal of Experimental Medicine, Vol. 103, No.5, pp. 653–666.  
-Khan, AU, Torelli, A, Wolf, I, Gretz, N, AF Khan, Arif Ul Maula, Torelli, Angelo, Wolf, Ivo, Gretz, Norbert TI. (2018). AutoCellSeg: robust automatic colony forming unit (CFU)/cell analysis using adaptive image segmentation and easy-to-use post-editing techniques. SCIENTIFIC REPORTS, Vol. 8. 7302. 
-Hirst, D. G., & Robson, T. (2010). Molecular biology: the key to personalised treatment in radiation oncology? The British Journal of Radiology, Vol. 83, No. 993, 723–8. 
-Franken, N. a P., Rodermond, H. M., Stap, J., Haveman, J., & van Bree, C. (2006). Clonogenic assay of cells in vitro. Nature Protocols, Vol. 1, No. 5, 2315–9. 
-Cepeda Forero, K., Barrera Langer, M., Mosquera Paternina, A., Montoya Vega, C., Riveros Calvete, P., Mendoza Guerra, A., … Ondo Méndez, A. (2018). Radioresistencia en glioblastoma: papel de la hipoxia en la genotoxicidad inducida por radiaciones ionizantes, Ciencia E Investigación Medico Estudiantil Latinoamericana, Vol. 23, Núm. 1. 
 
