# Flask

## Preguntas

* **¿Qué es un objeto?**
Un objeto es la instancia de una clase. Basicamente es una representación de una entidad de la realidad.
    
* **¿Qué es inyección de dependencias?**
Es un patrón de diseño en el que se inyectan objetos a una clase en lugar de que esta clase los cree, de allí su nombre inyección.

* **¿Qué es una API?**
API es la abreviatura de Application Programming Interfaces (interfaz de programación de apliaciones). Esta permite la comunicación entre servicios mediante una serie de reglas establecidas. 

* **Diferencia entre API REST y SOAP**
    - SOAP: Es un protocolo estandar para la comunicación entre dos servicios mediante XML. Utiliza el protocolo de comunicación, aunque tambien es soportado por otros protocolos.
    - REST: Este transporta datos mediante el protocolo de comunicación HTTP y utiliza los métodos que este provee como PUT, POST, DELETE, GET. Este soporta cualquier tipo de dato ya sea JSON, XML, Imagenes, documentos, entre otros.

* **¿Qué es un lenguaje de programación tipado fuerte y debil?**
Un lenguaje de programación de tipado fuerte es aquel en que las variables poseen un tipo de dato y este no tipo no puede ser modificado a lo largo de la ejecución del programa. Un lenguaje de programación de tipado debil es aquel en el que no es necesrio definir el tipo de dato de la variable y esta puede cambiar de tipo durante la ejecución.

* **¿Qué es GIT?**
Git es un sistema de control de versiones distribuida, es decir, no depende de un repositorio central.

* **¿Qué es GIT Flow?**
Gitflow es un flujo de trabajo que se aplica a un repositorio. Cuenta con dos ramas principales que son master y develop y una serie de ramas auxiliares o de apoyo que son feature, release y hotfix.

* **¿Qué es SQL?**
SQL es un lenguaje de consultas estructuradas. Es un lenguaje estandar que se utiliza para interacción con una base de datos relacional.

* **Tipos de Join para tablas SQL**
Left Join, Right Join, Inner Join, Outer Join y Cross Join. El mas utilizado es el Inner Join, este obtiene los datos en común de dos entidades.

* **¿Qué es un CMS?**
Es un sistema de gestion de contenidos para paginas web, por ejemplo Wordpress.

* **Definir: JSON, XML, HTML**
    - JSON: Javascript Object Notation, es un formato para el intercambio de datos que es sencillo de leer y escribir, a diferencia de XML que es un poco mas complejo.
    - XML: Es un lenguaje marcado que permite escribir etiquetas personalizadas para el intercambio y organización de datos.
    - HTML: Es un lenguaje marcado de documentos que se utiliza para escribir páginas web.
* **Definir KISS, DRY, SOLID, YAGNI**
    - KISS: Es un principio que significa Keep It Simple, Stupid (Mantenlo sencilo estupido), basicamente es un principio que dice que un sistema funciona mejor si se estructura de una manera sencilla.
    - DRY: Don't Repeat Yourself es un principio que promueve la reducción de la duplicación de código, es  decir, si dos bloques de código realizan la misma tarea o una tarea similar, este bloque puede realizarse en un solo lugar.
    - SOLID: 
        - Single Responsability: Cada clase y método debe realizar solo una cosa.
        - Open / Closed: Las clases y métodos deben estar abiertos a extenciones pero cerrados a modificaciones.
        - Liskov Substitution: 
        - Interface Segregation:
        - Dependency Inversion: Cada clase debe funcionar por si sola sin depender de otra.
    - YAGNID: You Aren't Gonna Need It (No vas a necesitarlo), esta filosofía dice que no agregues funcionalidades que no vas a utiilizar. Por lo regular se agregan bloques que nos pueden servir en un futuro, pero esto tiene desventajas, por lo que se deben agregar unicamente cuando se vayan a utilizar.
