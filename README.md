# widget-vlc

widget: video player con vlc para `Pyside6` 

![](otros/captura.png)

## Librerias
- PySide6            6.9.3
- pymediainfo        7.0.1


## notas
- agregue el core con vlc
- agregue ui de controles
- agregue test_core para hacer pruebas del core y los controles
- agregue icons
- los labels de tiempo ya cambian
- asigne sus metodos a todos los botones
- el slide de volumen ya funciona
- [ ] obtener la duracion del video (falla:-1)
- position[float]: se muestra como porcentaje de entre 0.0 y 1.0
- he creado metodos para mover la posicion de nuevo para actualizar los labels de tiempo
- el lb_info muestra la duracion y el nombre de la captura
- al mover el slide de posicion se puede recorrer el video
- pymediainfo solo se utiliza para obtener la duracion correcta
- para ya no usar pymediainfo solo para la duracion del mismo vlc con lenght se puede implementar un retraso al llamar a la funcion para que sea correcta la devolusion
- [x] agregar retraso a la funcion length
- ahora cambia el icono de play y pause
- ya obtiene la duracion sin mediainfo (falta limpiar)
- cambie y renombre los iconos en el qrc


## to do
- [ ] acomodar y limpiar core
- [ ] acomodar y limpiar widget
- [ ] coherncia en los nombres y documentar
- [ ] widget listo para usar como modulo (ya no desde un test)

