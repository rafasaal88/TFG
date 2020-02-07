TRABAJO FIN DE GRADO EN INGENIERÍA INFORMÁTICA
Escuela Politécnica Superior (Córdoba)

# Sistema basado en IOT para

# la implantación de campañas

# de marketing

## ÍNDICE DE CONTENIDOS

- 1. INTRODUCCIÓN.................................................................................................................
- 2. OBJETIVOS..........................................................................................................................
- 3. ANTECEDENTES......................................................................................
- 4. PARTES DE QUE CONSTARÁ EL TFG............................................................................
- 5. FASES DE DESARROLLO Y CRONOGRAMA...............................................................
- 6. RECURSOS...........................................................................................................................
   - 6.1 Recursos humanos...........................................................................................................................
   - 6.2 Recursos hardware..........................................................................................................................
   - 6.3 Recursos software............................................................................................................................
- 7. BIBLIOGRAFÍA...................................................................................................................


## 1. INTRODUCCIÓN

La tecnología NFC (Near Field Communication) es ampliamente en marketing y aplicaciones
de publicidad (Ahson and Ilyas, 2011; NFC Forum, 2013; Garrido et al., 2010; Riekki et al.,
2006). Muchas de estas aplicaciones estan basadas en PoS (Point of Sale) usando objetos con
tags que proveen a los usuarios información, cupones de descuento o algún otro tipo de servicio
que anime a la promoción de un producto comercial. En dichas aplicaciones, cuando los
usuarios con un dipositivo NFC toca el PoS, inmediatamente recibe información relacionada
con la campaña de marketing.

Muchas aplicaciones han usado NFC para el marketing y publicidad (Hardy et al., 2010;
Holleis et al., 2010; Pirhonen et al., 2002; Wiedmann et al., 2009) de diferentes tipos de
productos usando descuentos que los usuarios pueden cangear en el portal web o simplemente
tocando un tag localizado en una tienda o en un PoS. En estos sistemas, los cupones tienen un
ciclo de vida totalmente administrado por el sistema. La seguridad de los cupones está
administrada a través de procesos de sincronización con el servidor. Los usuarios pueden
obtener los cupones en cualquier tienda usando un lector NFC o usando un código QR.

Diferentes aplicaciones han considerado el uso de NFC para publicidad, marketing o
identificación del usuario. Los objetos o pantallas con tags NFC pueden proveer a los usuarios
información sobre productos, campañas o servicios. La tarjeta SIM ha sido propuesta como via
para el uso de compras o de identificación en tarjetas de crédito. (Bulander et al., 2005; Murao
et al., 2011; Ozdenizci et al., 2010; Riekki et al., 2006)

Con este proyecto se pretende desarrollar una solución propia que permita implantar campañas
de marketing sobre determinados productos y pueda ser utilizada en diferentes tipos de
establecimientos con los menores cambios posibles.


## 2. OBJETIVOS

El objetivo principal del proyecto es el análisis, diseño e implementación de un sistema de
Sistema basado en IOT para la implantación de campañas de marketing asociadas a
determinados productos de un supermercado o cualquier establecimiento de venta de
productos.

La funcionalidad de la aplicación incluye:
a) Gestión y administración de las campañas de marketing mediante una aplicación web.
b) Interacción con los objetos (productos en promoción) en un entorno del Internet de las
cosas (IoT).
c) Interacción mediante dispositivos móviles haciendo uso de la tecnología NFC.
d) Análisis exploratorio de los resultados de las campañas de marketing.

El sistema debe almacenar y gestionar información sobre:

- Las diferentes campañas de marketing a gestionar. Se debe almacenar información de las
    empresas, de las campañas, de los premios asociados y, de los usuarios que se registren/
    participen. Se debe considerar que una empresa puede tener en activo diferentes
    campañas de marketing sobre diferentes productos, cada campaña puede tener
    relacionado diferentes premios.
- Los dispositivos NFC que se dan de alta en el sistema. Estos se identifican por un código
    interno y se indica la localización interna y la geolocalización en la cual se situará. Un
    Tag NFC podrá tener asignado varios servicios, por lo que deberá existir un atributo que
    determine el orden de selección de esos servicios acorde a los siguientes criterios:
    a) Secuencial: se elegirán en orden de no usado o usado hace más tiempo. Si todos
       tienen la misma antigüedad se elige al primero según su código.
    b) Aleatorio: se eligen aleatoriamente.
    c) Todos: se ejecutará un servicio tras de otro.


- Los servicios asignados a los Tags NFC. Esta información permitirá controlar y tener
    una realimentación del uso de la plataforma en diferentes experiencias.
- Todos los usuarios del sistema: el administrador de la aplicación, usuarios registrados,
    etc.
- Los servicios son de tres tipos:
    a) Interno: se ejecuta una funcionalidad por el servidor.
    b) Externo: el servidor sólo es una pasarela a una web externa.
    c) Combinado: Si no se puede ejecutar el procedimiento interno se ejecuta el externo.


Además, se deben considerar atributos específicos para describir si es obligado o no el
inicio de sesión del usuario, el objetivo es garantizar la seguridad en el acceso a
determinados servicios. Además, será necesario establecer otros atributos para definir si
es obligatorio conocer la geolocalización del usuario para el acceso al servicio o, para
indicar la fecha en que cada servicio ha sido ejecutado por última vez.

Por último, es importante almacenar información histórica de los servicios ejecutados,
sus contenidos y formato, de los usuarios que interaccionan con los Tags NFC, etc. Esta
información permitirá evaluar y realizar un estudio de usabilidad cuando la plataforma
esté en fase de explotación.


## 3. ANTECEDENTES

A continuación se citan dos trabajos relacionados con los objetivos del proyecto:

- _Gonzalo Cerruela García, Miguel Ángel Gómez Nieto e Irene Luque Ruiz (2014). ‘_ An
    ubiquitous solution for advertising and loyalty purposes using NFC technology.
    International Journal of Ad Hoc and Ubiquitous Computing, 2017 Vol.26 No.1, pp.29 –
    43.
- _Raúl Arroyo Lubían (2015). Trabajo de fin de grado ‘Wing Cronos: Planificador de_
    _campañas de marketing”,_ por Raúl Arroyo Lubían_._

## 4. PARTES DE QUE CONSTARÁ EL TFG............................................................................

La arquitectura del sistema estará sujeta a cambios, no obstante, se prevé que el proyecto conste
de las siguientes partes diferenciadas:

- Base de datos: En esta sección se realizará metodologia CRUD de todos los datos
    necesarios del sistema. Para ello se utilizará MariaDB para el sistema de gestión de base
    de datos.
- Backend: Pasarela encargada de controlar, modelar y realizar los computos necesarios
    entre las vistas de usuarios y el renderizado de datos por pantalla, modificación de datos,
    etc. Dispone de:
    ◦ Panel de administración para añadir nuevas campañas, productos, recetas, etc.
    ◦ API REST para la comunicación con el frontend.
    ◦ Panel de análisis de datos de las campañas.


- Frontend: Capa más cercana al usuario, la cual permite la interacción con el sistema y
    los servicios ofrecidos.
- Documentación: Manual de código, usuario y técnico.

## 5. FASES DE DESARROLLO Y CRONOGRAMA...............................................................

```
Tareas Tiempo (h)
Aprendizaje de las tecnologías a usar en el proyecto
```
- Python 6
- Django 8
- Django Rest Framework 5
- SQL 3
- MariaDB 4
- HTML5 y CSS3 7
- JavaScript 15
- VueJS 9
- TAGS NFC 3
    **Total: 60**
Desarrollo e implementación
- Análisis y diseño **50**
    - Análisis y diseño de la base de datos 4
    - Análisis y diseño de los métodos CRUD de los modelos 2
    - Análisis y diseño del panel de administración 9
    - Análisis y diseño de la interfaz de publicidad 7
    - Análisis y diseño de la interfaz de productos 7
    - Análisis y diseño del registro de usuarios 9
    - Análisis y diseño de los métodos para la API REST 12


- Programación de funcionalidades **105**
    - Despliegue de Django y MariaDB 4
    - Implementación del diseño de la base de datos 12
    - Métodos CRUD para los modelos 10
    - Interfaz de administración 22
    - Interfaz de publicidad 24
    - Interfaz de productos 18
    - Registro de usuario 16
    - Métodos para la API REST y configuración 30
    - Despliegue VueJS sobre Django REST Framework 6
    - Manejo e identificación de los tags NFC en el sistema 10
       **Total: 152**
Pruebas cíclicas **38**
Documentación **50
Total del proyecto: 300**

```
Enero Febrero Marzo
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Aprendizaje
Planteamiento
Desarrollo
Pruebas cíclicas
Documentación
```

## 6. RECURSOS
### 6.1 Recursos humanos

Esta herramienta está desarrollada por Rafael Salido Álvarez y dirigida por Gonzalo Cerruela
García.

### 6.2 Recursos hardware
- Equipo del desarrollador:
    ◦ Host: Lenovo Flex 2 Pro-
    ◦ CPU: Intel i7-45710U
    ◦ GPU: Intel Haswell-ULT / Nvidia GeForce 840m
    ◦ RAM: 16GB
- Equipo de despliegue y pruebas:
    ◦ Host: Raspberry Pi 3 Model B
    ◦ CPU: Broadcom BCM2837, Cortex-A53 (ARMv8) 64-bit Soc
    ◦ GPU: VideoCore IV 400 Mhz
    ◦ RAM: 1GB

### 6.3 Recursos software
En este apartado vamos a diferenciar las partes que tiene el proyecto y con que software va a
funcionar cada una de ellas.


- Base de datos:

MariaDB es el Sistema Gestor de Base de Datos de nuestro proyecto. Se trata de un proyecto
open source para trabajar y almacenar con base de datos relacionales.

- Backend

El backend del sistema está desarrollado en Django, un potente framework basado en Python.
Es el encargado de comunicarse con Django Rest y MariaDB.

- Django Rest Framework

Este modulo de Django nos permite aislar completamente el backend y poder realizar la
comunicación a través de llamadas a la API REST que nos devolverá los resultados en JSON.

- Frontend

La interfaz de usuario final está diseñada en VueJS, un potente framework basado en
Javascript. Dicho framework realizará las llamadas a la API REST y mostrará los resultados
por pantalla.


## 7. BIBLIOGRAFÍA

_[Ahson and Ilyas, 2011] Ahson, S.A. and Ilyas, M. (2011) Near Field Communications
Handbook, Taylor & Francis, New York, USA._

_[Arroyo Lubían, 2015] Raúl Arroyo Lubían (2015). ‘Wing Cronos: Planificador de campañas
de marketing por Raúl Arroyo Lubían’_

_[Bulander, Decker, Schiefer and Kolmel, 2005] Bulander, R., Decker, M., Schiefer, G. and
Kolmel, B. (2005) ‘Comparison of different approaches for mobile advertising’, The Second
IEEE International Workshop on Mobile Commerce and Services, 2005, WMCS ‘05, 19 July,
pp.174–182._

_[Borrego-Jaraba, Garrido, García, Ruiz and Gómez-Nieto, 2012] Borrego-Jaraba, F.,
Garrido, P., García, G., Ruiz, I. and Gómez-Nieto, M. (2012) ‘Discount vouchers and loyalty
cards using NFC’, in Bravo, J., López-De-Ipiña, D. and Moya, F. (Eds.): Ubiquitous
Computing and Ambient Intelligence, Springer Berlin Heidelberg, pp.101–108._

_[Cerruela García, Gómez Nieto y Luque Ruiz, 2014] Gonzalo Cerruela García, Miguel Ángel
Gómez Nieto e Irene Luque Ruiz (2014). ‘An ubiquitous solution for advertising and loyalty
purposes using NFC technology (Solución obicua para publicidad y fidelización usando
tecnología NFC)’_

_[Django Framework, 15/11/2019] Django Framework, web consultada el 15/11/2019: https://
[http://www.djangoproject.com/](http://www.djangoproject.com/)_

_[Django Rest Framework, 15/11/2019] Django Rest Framework, web consultada el
15/11/2019: https://www.django-rest-framework.org/_

_[Hardy, Rukzio, Holleis, and Wagner, 2010] Hardy, R., Rukzio, E., Holleis, P. and Wagner, M.
(2010) ‘Mobile interaction with static and dynamic NFC-based displays’, Proceedings of the_


_12th International Conference on Human Computer Interaction with Mobile Devices and
Services, ACM, Lisbon, Portugal, pp.123–132._

_[Murao, Terada, Ai and Matsukura, 2011] Murao, K., Terada, T., Ai, Y. and Matsukura, R.
(2011) ‘Evaluating gesture recognition by multiple-sensor-containing mobile devices’, 15th
Annual International Symposium on Wearable Computers (ISWC), 2011, 12–15 June, pp.55–
58._

_[Pirhonen, Brewster, and Holguin, 2002] Pirhonen, A., Brewster, S. and Holguin, C. (2002)
Gestural and Audio Metaphors as a Means of Control for Mobile Devices, ACM Press, New
York, USA._

_[Ozdenizci, Coskun, Aydin and Kerem, O. 2010] Ozdenizci, B., Coskun, V., Aydin, M.N. and
Kerem, O. (2010) ‘NFC loyal: a beneficial model to promote loyalty on smart cards of mobile
devices’, International Conference for Internet Technology and Secured Transactions (ICITST),
2010, 8–11 November, London, UK, pp.1–6._

_[Python Languaje Programming, 14/11/2018] Python Languaje Programming, web consultada
el 14/11/2019: https://www.python.org/_

_[Riekki, Salminen, and Alakärppä, 2006] Riekki, J., Salminen, T. and Alakärppä, I. (2006)
‘Requesting pervasive services by touching RFID tags’, Pervasive Computing, IEEE, Vol. 5,
pp.40–46._

_[VueJS, the progressive javascript framework, 16/11/2019] VueJS, the progressive javascript
framework, web consultada el 16/11/2019: https://vuejs.org/_

_[Wiedmann, Reeh, and Schumacher, 2009] Wiedmann, K.P., Reeh, M.O. and Schumacher, H.
(2009) ‘Near field communication in mobile marketing’, in Bauer, H., Bryant, M. and Dirks, T.
(Eds.): Erfolgsfaktoren des Mobile Marketing, Springer Berlin Heidelberg, pp.305–325._
