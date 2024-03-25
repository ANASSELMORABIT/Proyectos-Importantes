import random
import tkinter as tk
from tkinter import messagebox,simpledialog # IMPORTAR MODULOS DE TKINTER
while True:
    campos=["Matematica","Ingles","Fisica","Quimica","Biologia","Programacion","Geografia","Historia","Deportes","Tecnologia"] #CAMPOS
    preguntas=dict(                                                                             #DICCIONARIO DE PREGUNTAS 
        Matematica={"Hard":["¿Encuentra la intersección de los intervalos (−∞,2] y (−1,∞)(−∞,2]",
                        "Encuentra la integral indefinida ∫(exp(2x)cos(3x)) dx",
                        "Encuentra la integral indefinida ∫cos(x)^3 dx"],
                    "Medium":["Encuentra la integral indefinida ∫x²dx",
                          "Si sin(θ)= 3/5, ¿cual es el valor de cos(θ)?"
                          ,"Resuelva la ecuación cuadrática 2x²+3x+7=0"],
                    "Easy":["¿Cual es el valor de 5-3 * 2 +1+4(3-2)-(8/2)?",
                        "¿Cual es el valor de 2^(3/3)?",
                        "¿Cual es el valor de 8*7?"],},
        Ingles={"Hard":["What is the meaning of the word 'ubiquitous'?",
                    "What is the synonym for 'ephemeral'?",
                    " What is the antonym of 'ephemeral'?"],
                "Medium":[" What does the idiom 'hit the hay' mean?",
                      "What is the meaning of the word 'gregarious'?",
                      "Identify the type of sentence: 'She won the game, but she was not happy.'"],
                "Easy":[" What is the opposite of 'happy'?",
                    "¿Cuál es la traducción de la palabra 'book' al español?",
                    "Completa la siguiente frase: 'She _____ to the store.'"]},
        Fisica={"Hard":["¿Cuál es la ecuación que representa la equivalencia entre masa y energía, según la famosa fórmula de Einstein?",
                    "¿Cuál es el proceso nuclear principal que alimenta la radiación del Sol?",
                    "¿Cuál es la partícula mediadora de la fuerza electromagnética en el modelo estándar de la física de partículas?"],
                "Medium":["¿Cuál es la ley que describe cómo la corriente, la resistencia y el voltaje están relacionados en un circuito eléctrico?",
                      "¿Qué tipo de energía se asocia con la posición de un objeto en un campo gravitatorio?",
                      "¿Cómo se relaciona la velocidad angular (ω) con la frecuencia (f) y la longitud de onda (λ) en una onda senoidal?"],
                "Easy":["Según la segunda ley de Newton, ¿cuál es la relación entre la fuerza (F), la masa (m) y la aceleración (a) de un objeto?",
                    " ¿Cuál es el nombre de la ley de Newton que establece 'A toda acción le corresponde una reacción igual y opuesta'?",
                    "¿Cuál es la unidad de medida de la corriente eléctrica?"]},
        Quimica={"Hard":[": ¿Cuál es la configuración electrónica del ion cobre (Cu²⁺)?",
                    "¿Cuál es la diferencia entre entalpía y energía interna en un sistema químico?",
                    "¿Cómo afecta el aumento de la temperatura a un sistema en equilibrio químico?"],
                "Medium":["¿Cuál es el símbolo químico del elemento en el grupo 17 y período 3 de la tabla periódica?",
                    "¿Cuál es la función del cátodo en una celda electroquímica?",
                    "¿Cuál es la definición de una base de Lewis?"],
                "Easy":["¿Cómo se llama el compuesto químico con la fórmula HCl?",
                    "¿Cuál de los siguientes es un ejemplo de mezcla homogénea?",
                    "¿Cuál es la masa atómica del oxígeno (O) en la tabla periódica?"]},
        Biologia={"Hard":[" ¿Cuál es la función de la enzima RNA polimerasa en la transcripción del ADN?",
                      "¿Qué es un intrón en el contexto de la expresión génica?",
                      "¿Cuál es la función principal de los peroxisomas en las células?"],
                "Medium":["¿Cuántos huesos tiene el cuerpo humano adulto?",
                       "¿Cuál es el principal método de acción de los antibióticos?",
                       "¿Cuál es la función de la hormona insulina en el cuerpo humano?"],
                "Easy":["¿Qué estructura permite a los peces extraer oxígeno directamente del agua?",
                    "¿Cuál es el papel de los productores en una cadena alimentaria?",
                    "Si un organismo hereda un alelo dominante (A) de uno de sus padres y un alelo recesivo (a) del otro, ¿cuál será su fenotipo?"]},
        Programacion={"Hard":["En el desarrollo ágil, ¿qué significa 'Sprint'?",
                          "En el diseño de software, ¿qué es la arquitectura de microservicios y cuál es su ventaja principal?",
                          " ¿Qué es un 'semáforo' en el contexto de la programación concurrente?"],
                    "Medium":["¿Qué significa AJAX en el contexto del desarrollo web?",
                          "¿Qué es JUnit y para qué se utiliza comúnmente en Java?",
                          "En Java, ¿cuál de las siguientes implementaciones se utiliza para representar un conjunto sin duplicados?"],
                    "Easy":["¿Cómo se declara un bucle 'for' en Python?",
                        " ¿Cuál de los siguientes es un tipo de dato en Python que representa números enteros?",
                        " ¿Qué lenguaje de programación es conocido por su simplicidad y legibilidad, y utiliza la filosofía del 'Zen de Python'?"]},
        Geografia={"Hard":[": ¿Cuál es la isla más grande del mundo en términos de superficie terrestre?",
                       "¿Dónde se encuentra la Gran Barrera de Coral, uno de los ecosistemas marinos más grandes del mundo?",
                       " ¿Qué país es el principal productor mundial de petróleo?"],
                "Medium":["¿Cuál es el desierto más grande del mundo?",
                         "¿Cuál es la latitud 0°, conocida como la línea ecuatorial?",
                         "¿Cuál es el único país que comparte fronteras con Brasil?"],
                "Easy":["¿Cuál es la capital de Francia?",
                       "¿Cuál es el río más largo del mundo?",
                       "Si estás mirando hacia el norte, ¿en qué dirección está el sur?"]},
        Historia={"Hard":[" ¿Quién fue el líder supremo de los mongoles que creó uno de los imperios más grandes de la historia?",
                      " ¿En qué año ocurrió la Revolución Rusa que llevó al derrocamiento del régimen zarista?",
                      " ¿Cuándo cayó el Muro de Berlín, marcando el final simbólico de la Guerra Fría?"],
                "Medium":[" ¿Quién fue el líder religioso que desencadenó la Reforma Protestante en el siglo XVI?",
                      "¿Cuál fue la primera colonia permanente establecida por los ingleses en América del Norte en 1607?",
                      " ¿Cuál fue el imperio que gobernó gran parte de Europa, África del Norte y Asia Menor en la antigüedad?"],
                "Easy":[" ¿En qué antigua civilización se desarrolló la escritura cuneiforme?",
                    " ¿Qué navegante portugués lideró la primera expedición que circunnavegó la Tierra?",
                    "¿Cómo se llama el sistema de gobierno feudal basado en la relación de vasallaje?"]},
        Deportes={"Hard":["¿Cuál de los siguientes deportes no es parte del programa olímpico de los Juegos de Invierno?",
                      "¿En qué disciplina se destacan los atletas en el evento de los X Games conocido como 'Halfpipe'?",
                      "¿Cuántos puntos vale un drop goal en rugby?"],
                "Medium":[" ¿Cuál es la distancia de una vuelta en una piscina olímpica estándar en los eventos de natación?",
                      " ¿Cuál es el circuito de carreras más famoso asociado con la Fórmula 1?",
                      "¿Cuántos hoyos hay en un campo de golf estándar?"],
                "Easy":[" ¿Cuántos jugadores hay en un equipo de baloncesto en la cancha durante un juego?",
                    " ¿En qué país se celebró la Copa Mundial de la FIFA 2018?",
                    "¿Cuál de los siguientes torneos de tenis es uno de los cuatro Grand Slam?"]},
        Tecnologia={"Hard":[" ¿Qué tipo de cifrado utiliza la misma clave tanto para el cifrado como para el descifrado de datos?",
                        "¿Qué dispositivo se utiliza comúnmente para experimentar la realidad virtual?",
                        "¿Qué término se utiliza para describir la conexión de dispositivos cotidianos a internet para recopilar y compartir datos?"],
                    "Medium":[" ¿Qué protocolo se utiliza comúnmente para enviar y recibir correos electrónicos?",
                          "¿Cuál de las siguientes suites de oficina incluye aplicaciones como Word, Excel y PowerPoint?",
                          "¿Qué significa la abreviatura 'URL' en el contexto de la web?"],
                    "Easy":[" ¿Cuál de los siguientes es un tipo de unidad de almacenamiento de estado sólido (SSD)?",
                        "¿Qué empresa fabrica el iPhone?",
                        "¿Cuál de los siguientes no es un sistema operativo de Microsoft?"]},
    )
    opciones_preguntas=dict( #DICCIONARIO DE OPCIONES
    Matematica = {
        "Hard":{
            "Pregunta1":["A. (-1, 2]","B. (-∞, -1]","C. (-∞, 2]","D. (2, ∞)"],
            "Pregunta2":["A. (exp(2x)(2sin(3x)-3cos(3x)))/13+C","B. (exp(2x)(2sin(3x)-2cos(3x)))/13+C","C. (exp(2x)(2sin(3x)+3cos(3x)))/13+C","D. (exp(2x)(2sin(3x)+2cos(3x)))/13+C"],
            "Pregunta3":["A.  cos(x)^2.sin(x)+(1/4)cos^4(x) + C","B. cos(x)^2.sin(x)+(1/3)cos^3(x) + C","C. sin(x)- sin(x)^3/3 +C","D. cos(x)^2.sin(x)-(1/3)cos^3(x) + C"]
        },
        "Medium":{
            "Pregunta1":["A. x^3/3 +C","B. X^3/4 +C","C. X^3/5 +C","D. X²/2 +C"],
            "Pregunta2":["A. 1/5","B. 4/5","C. 3/5","D. 6/5"],
            "Pregunta3":["A. X=1 o X=2","B. X=1","C. X=2","D. No tiene solución"]
        },
        "Easy":{
            "Pregunta1":["A. 0","B. 15","C. 10","D. 1"],
            "Pregunta2":["A. 1","B. 2","C. 3","D. 4"],
            "Pregunta3":["A. 54","B. 55","C. 56","D. 57"]
        }
   },
    Ingles = {
        "Hard":{
        "Pregunta1":["A.  Rare","B.  Present everywhere","C. Temporary","D. Permanent"],
         "Pregunta2":["A. Enduring","B. Brief","C. Immortal","D. Continuous"],
        "Pregunta3":["A. Permanent","B. Ephemeral","C. Temporary","D. Momentary"]
        },
        "Medium":{
        "Pregunta1":["A. Hit with hay","B. Go to bed","C. Buy hay","D. Make the bed"],
        "Pregunta2":["A. Solitary","B. Silent","C. Sociable","D. Rebellious"],
        "Pregunta3":["A. Simple","B. Compuesta coordinada","C. Compleja","D. Compuesta"]
        },
        "Easy":{
        "Pregunta1":["A. Sad","B. Excited","C. Joyful","D. Anxious"],
        "Pregunta2":["A. Libro","B. Computadora","C. Televisión","D. Agua"],
        "Pregunta3":["A. Go","B. Goes","C. Going","D. Gone"]
        }
    },
    Fisica = {
        "Hard":{
        "Pregunta1":["A. E=mc^2","B. F=ma","C. E=mv^2","D. E=mo^2"],
        "Pregunta2":["A. Fisión nuclear","B. Fusión nuclear","C. Desintegración radiactiva","D. Captura de electrones"],
        "Pregunta3":["A. Fotón","B. Electron","C. Gluón","D. Neutron"]
        },
        "Medium":{
        "Pregunta1":["A. Ley de Faraday","B. Ley de Coulomb","C. Ley de Ohm","D. Ley de Newton"],
        "Pregunta2":["A. Energía cinética","B. Energía térmica","C. Energía potencial","D. Energía electrica"],
        "Pregunta3":["A. ω = 2πf","B.  ω = f/λ","C. ω = 2πf/λ","D. ω = fλ"]
        },
        "Easy":{
        "Pregunta1":["A. F = m/a","B. F = ma","C. F = m + a","D. F = m - a"],
        "Pregunta2":["A. Ley de la inercia","B. Ley de la gravedad","C. Ley de la acción y reacción","D. Ley de la fuerza"],
        "Pregunta3":["A. Voltio","B. Amperio","C. Ohm","D. Vatio"]
        }
    },
    Quimica = {
        "Hard":{
        "Pregunta1":["A.  1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁵","B. 1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ 3d¹⁰","C. 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁹","D. 1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ 3d¹⁰ 4p¹"],
        "Pregunta2":["A.  La entalpía es la energía almacenada en los enlaces químicos, mientras que la energía interna es la energía total del sistema.","B. La entalpía es la energía total del sistema, mientras que la energía interna es la energía liberada o absorbida durante una reacción a presión constante.","C.  La entalpía es la energía liberada o absorbida durante una reacción a presión constante, mientras que la energía interna es la energía almacenada en los enlaces químicos.","D. No hay diferencia, ambos términos se utilizan indistintamente"],
        "Pregunta3":["A. Aumenta la concentración de productos.","B. Aumenta la constante de equilibrio.","C. No tiene efecto en el equilibrio.","D. Favorece la formación de reactantes."]
        },
        "Medium":{
        "Pregunta1":["A.  Cl","B. F","C. Br","D. I"],
        "Pregunta2":["A. Oxidación","B. Reducción","C. Producción de electrones","D. Liberación de iones positivos"],
        "Pregunta3":["A. Una sustancia que dona un par de electrones.","B. Una sustancia que acepta un par de electrones.","C. Una sustancia que libera iones positivos en solución acuosa.","D. Una sustancia que aumenta la concentración de iones de hidrógeno (H⁺)."]
        },
        "Easy":{
        "Pregunta1":["A. Ácido sulfúrico","B. Ácido clorhídrico","C. Ácido nítrico","D. Ácido acético"],
        "Pregunta2":["A. Arena y agua","B. Aceite y vinagre","C. Agua y aceitunas","D. Sal y pimienta"],
        "Pregunta3":["A. 14.01 u","B. 16.00 u","C. 18.02 u","D. 20.01 u"]
        }
    },
    Biologia = {
        "Hard":{
        "Pregunta1":["A.Iniciar la traducción del ARN mensajero (ARNm).","B.Catalizar la síntesis de ARN a partir de una cadena de ADN.","C.Facilitar la replicación del ADN.","D.Mediar en la traducción del ARN de transferencia (ARNt)."],
        "Pregunta2":["A. Una región del ADN que codifica para proteínas.","B.Una secuencia de ARN que se traduce directamente en proteínas.","C. Una región del gen que se transcribe pero no se traduce en proteínas.","D.Una enzima que participa en la replicación del ADN."],
        "Pregunta3":["A.Almacenar y liberar energía en forma de ATP.","B.Sintetizar proteínas para la célula.","C.Descomponer moléculas tóxicas y grasas.","D.Regular el equilibrio de sales y minerales en la célula."]
        },
        "Medium":{"Pregunta1":["A. 206","B.156","C. 106","D. 306"],
        "Pregunta2":["A. Inhibir la síntesis de proteínas en las bacterias.","B.Romper las membranas celulares de las bacterias.","C.Estimular la replicación del ADN en las bacterias.","D.Inhibir la función de los ribosomas en las bacterias."],
        "Pregunta3":["A. Estimular la conversión de glucógeno a glucosa.","B.  Promover la absorción de calcio en los huesos.","C. Regular el metabolismo de los lípidos","D. Reducir los niveles de glucosa en sangre."]
        },
        "Easy":{"Pregunta1":["A. Branquias","B. Pulmones","C.Tráquea","D. Agallas"],
        "Pregunta2":["A. Consumir otros organismos para obtener energía.","B. Producir su propio alimento a través de la fotosíntesis.","C. Descomponer materia orgánica muerta.","D. Actuar como consumidores primarios en la cadena."],
        "Pregunta3":["A. Mostrará el fenotipo asociado al alelo recesivo (a).","B. Mostrará el fenotipo asociado al alelo dominante (A).","C. No mostrará ningún fenotipo.","D. Será estéril."]
        }
    },
    Programacion = {
        "Hard":{
        "Pregunta1":["A. Un intervalo corto de tiempo para realizar una tarea específica.","B. Una carrera rápida hacia el final del desarrollo.","C. Una fase de prueba intensiva.","D. Un proceso de planificación a largo plazo."],
        "Pregunta2":["A. Un enfoque monolítico para el desarrollo de software.","B. Una arquitectura que utiliza un solo servicio para todas las funciones.","C. Una arquitectura que estructura una aplicación como un conjunto de servicios independientes y desplegables.","D. Un enfoque descentralizado sin servicios definidos."],
        "Pregunta3":["A. Una señal de tráfico en el código.","B. Un mecanismo de sincronización para controlar el acceso a recursos compartidos.","C. Una herramienta de depuración para encontrar errores en el código.","D.  Un indicador de rendimiento del sistema."]
        },
        "Medium":{
        "Pregunta1":["A. Asynchronous JavaScript and XML.","B. Advanced JavaScript and XML.","C. Automated JavaScript and XML.","D. Associated JavaScript and XML."],
        "Pregunta2":["A. Una herramienta de desarrollo de interfaces gráficas en Java.","B. Un marco de prueba unitaria para Java.","C. Un entorno de desarrollo integrado (IDE) para Java.","D. Un servidor web para aplicaciones Java."],
        "Pregunta3":["A. `HashSet`","B. `ArrayList`","C. `LinkedList`","D. `HashMap`"]
        },
        "Easy":{
        "Pregunta1":["A. `for i in range(10)`","B. `foreach i in range(10)`","C. `repeat i in range(10)`","D. `loop i in range(10)`"],
        "Pregunta2":["A. `float`","B. `str`","C. `int`","D. `bool`"],
        "Pregunta3":["A. JAVA","B. C++","C. Ruby","D. Python"]
        }
    },
    Geografia = {
        "Hard":{
        "Pregunta1":["A. Groenlandia","B. Australia","C. Nueva Guinea","D. Madagascar"],
        "Pregunta2":["A. Mar Mediterráneo","B. Océano Pacífico","C. Océano Atlántico","D. Océano Índico"],
        "Pregunta3":["A. Arabia Saudita","B. Estados Unidos","C. Rusia","D. China"]
        },
        "Medium":{
        "Pregunta1":["A. El Sahara","B. El Gobi","C. El Kalahari","D. El Desierto de Atacama"],
        "Pregunta2":["A. El paralelo que pasa por el centro de la Tierra","B. El paralelo que pasa por el ecuador","C. El meridiano que pasa por el centro de la Tierra","D. El meridiano que pasa por Greenwich, Inglaterra"],
        "Pregunta3":["A. Perú","B. Bolivia","C. Colombia","D. Venezuela"]
        },
        "Easy":{
        "Pregunta1":["A. París","B. Lyon","C. Marsella","D. Lille"],
        "Pregunta2":["A. El Nilo","B. El Amazonas","C. El Yangtsé","D. El Mississippi"],
        "Pregunta3":["A. Al frente","B. A la derecha","C. A la izquierda","D. Detrás"]
        }
    },
    Historia = {
        "Hard":{
            "Pregunta1":["A. Kublai Khan","B. Hulagu Khan","C. Timur Lenk","D. Genghis Khan"],
            "Pregunta2":["A. 1917","B. 1918","C. 1919","D. 1920"],
            "Pregunta3":["A.10 de noviembre de 1989","B. 9 de noviembre de 1989","C. 8 de noviembre de 1989","D. 11 de noviembre de 1989"]
            },
        "Medium":{
            "Pregunta1":["A. Juan Calvino","B. Napoleón Bonaparte","C.Martin Lutero","D. Miguel de Cervantes"],
            "Pregunta2":["A. Jamestown","B. Plymouth","C. Boston","D. Nueva York"],
            "Pregunta3":["A. El Imperio Romano","B. El Imperio Bizantino","C. El Imperio Otomano","D. El Imperio Persa"]
            },
        "Easy":{
            "Pregunta1":["A. La civilización sumeria","B. La civilización egipcia","C. La civilización mesopotámica","D. La civilización romana"],
            "Pregunta2":["A. Cristóbal Colón","B. Vasco da Gama","C. Fernando de Magallanes","D. Juan Sebastián Elcano"],
            "Pregunta3":["A. Feudalismo","B. Manorialismo","C. Señorío","D. Feudatario"]
            }
    },
    Deportes = {
    "Hard": {
        "Pregunta1": ["A. Fútbol americano", "B. Esquí acrobático", "C. Curling", "D. Bobsleigh"],
        "Pregunta2": ["A. Esquí acrobático", "B. Snowboard", "C. BMX", "D. Skateboarding"],
        "Pregunta3": ["A. 1 punto", "B. 2 puntos", "C. 3 puntos", "D. 4 puntos"],
    },
    "Medium": {
        "Pregunta1": ["A. 25 metros", "B. 50 metros", "C. 75 metros", "D. 100 metros"],
        "Pregunta2": ["A. Mónaco", "B. Spa-Francorchamps", "C. Silverstone", "D. Monza"],
        "Pregunta3": ["A. 18", "B. 27", "C. 36", "D. 45"],
    },
    "Easy": {
        "Pregunta1": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "Pregunta2": ["A. Rusia", "B. Qatar", "C. Brasil", "D. Argentina"],
        "Pregunta3": ["A. Abierto de Australia", "B. Roland-Garros", "C. Wimbledon", "D. US Open"],
    },
    },
    Tecnologia= {
    "Hard": {
        "Pregunta1": ["A. Cifrado asimétrico", "B. Cifrado simétrico", "C. Cifrado de bloques", "D. Cifrado de flujo"],
        "Pregunta2": ["A. Oculus Quest 2", "B. PlayStation VR", "C. HTC Vive", "D. Samsung Gear VR"],
        "Pregunta3": ["A. Internet de las cosas (IoT)", "B. Internet de la información (II)", "C. Internet de la comunicación (IC)", "D. Internet de la tecnología (IT)"],
    },
    "Medium": {
        "Pregunta1": ["A. SMTP", "B. POP3", "C. IMAP", "D. HTTP"],
        "Pregunta2": ["A. Microsoft Office", "B. Google Workspace", "C. LibreOffice", "D. Apache OpenOffice"],
        "Pregunta3": ["A. Uniform Resource Locator", "B. Uniform Resource Loader", "C. Uniform Resource Link", "D. Uniform Resource Location"],
    },
    "Easy": {
        "Pregunta1": ["A. NAND", "B. SATA", "C. PCIe", "D. NVMe"],
        "Pregunta2": ["A. Apple", "B. Samsung", "C. Huawei", "D. Xiaomi"],
        "Pregunta3": ["A. Windows", "B. macOS", "C. Linux", "D. Chrome OS"],
    },
    }
    )
    Respuestas_Correctas=dict( # Diccionario de respuestas correctas
    Matematica={"Hard":{"Pregunta1":"C","Pregunta2":"B","Pregunta3":"C"},
                "Medium":{"Pregunta1":"A","Pregunta2":"B","Pregunta3":"D"},
                "Easy":{"Pregunta1":"A","Pregunta2":"B","Pregunta3":"C"}},
    Ingles={"Hard":{"Pregunta1":"B","Pregunta2":"B","Pregunta3":"A"},
            "Medium":{"Pregunta1":"B","Pregunta2":"C","Pregunta3":"D"},
            "Easy":{"Pregunta1":"B","Pregunta2":"A","Pregunta3":"B"}},
    Fisica={"Hard":{"Pregunta1":"A","Pregunta2":"B","Pregunta3":"A"},
            "Medium":{"Pregunta1":"C","Pregunta2":"C","Pregunta3":"A"},
            "Easy":{"Pregunta1":"B","Pregunta2":"C","Pregunta3":"B"}},
    Quimica={"Hard":{"Pregunta1":"C","Pregunta2":"C","Pregunta3":"D"},
             "Medium":{"Pregunta1":"A","Pregunta2":"B","Pregunta3":"D"},
             "Easy":{"Pregunta1":"B","Pregunta2":"D","Pregunta3":"B"}},
    Biologia={"Hard":{"Pregunta1":"B","Pregunta2":"C","Pregunta3":"C"},
              "Medium":{"Pregunta1":"A","Pregunta2":"A","Pregunta3":"D"},
              "Easy":{"Pregunta1":"A","Pregunta2":"B","Pregunta3":"B"}},
    Programacion={"Hard":{"Pregunta1":"A","Pregunta2":"B","Pregunta3":"B"},
                  "Medium":{"Pregunta1":"A","Pregunta2":"B","Pregunta3":"A"},
                  "Easy":{"Pregunta1":"A","Pregunta2":"C","Pregunta3":"D"}},
    Geografia={"Hard":{"Pregunta1":"B","Pregunta2":"B","Pregunta3":"A"},
               "Medium":{"Pregunta1":"A","Pregunta2":"B","Pregunta3":"D"},
               "Easy":{"Pregunta1":"A","Pregunta2":"B","Pregunta3":"D"}},
    Historia={"Hard":{"Pregunta1":"D","Pregunta2":"A","Pregunta3":"B"},
              "Medium":{"Pregunta1":"C","Pregunta2":"A","Pregunta3":"A"},
              "Easy":{"Pregunta1":"C","Pregunta2":"C","Pregunta3":"A"}},
    Deportes={"Hard":{"Pregunta1":"A","Pregunta2":"B","Pregunta3":"C"},
              "Medium":{"Pregunta1":"B","Pregunta2":"A","Pregunta3":"A"},
              "Easy":{"Pregunta1":"A","Pregunta2":"A","Pregunta3":"D"}},
    Tecnologia={"Hard":{"Pregunta1":"B","Pregunta2":"A","Pregunta3":"A"},
                "Medium":{"Pregunta1":"A","Pregunta2":"A","Pregunta3":"A"},
                "Easy":{"Pregunta1":"A","Pregunta2":"A","Pregunta3":"C"}}
    )
    def obtener_nivel():
        while True:
            try:
                num_nivel = int(simpledialog.askstring("Nivel", "¿Desea jugar en fácil(1), medio(2) o difícil(3)?")) # Pide al usuario que ingrese el nivel
                if 1 <= num_nivel <= 3:
                    break
            except ValueError:
                tk.messagebox.showerror("Error", "Por favor, ingrese un valor numérico")

        return ["Easy", "Medium", "Hard"][num_nivel - 1]
    def obtener_pregunta():
        Preguntas_repetidas = [] # Lista de preguntas ya utilizadas
        clave = random.choice(campos) # Se elige el campo al azar
        nivel = obtener_nivel() # Se elige el nivel
        while True:
            pregunta = random.choice(preguntas[clave][nivel]) # Se elige una pregunta al azar de la lista de preguntas del campo y nivel
            if (pregunta not in Preguntas_repetidas): # Se verifica que la pregunta no haya sido utilizada antes
                Preguntas_repetidas.append(pregunta) # Se agrega la pregunta a la lista de preguntas ya utilizadas
                break
            
        indice = preguntas[clave][nivel].index(pregunta) # Se obtiene el indice de la pregunta en la lista de preguntas del campo y nivel 
        numero_pregunta = f"Pregunta{indice + 1}" # Se obtiene el numero de la pregunta en el formato Pregunta1, Pregunta2, etc.
        opciones = opciones_preguntas[clave][nivel][numero_pregunta] # Se obtienen las opciones de la pregunta en el formato A, B, C, etc.
        return pregunta, opciones, clave, nivel, numero_pregunta # Retorna la pregunta, las opciones, el campo, el nivel y el numero de la pregunta



    def verificar_respuesta(respuesta_usuario, puntos_equipo, clave, nivel, numero_pregunta): # Función para verificar la respuesta del usuario
        respuesta_correcta = Respuestas_Correctas[clave][nivel][numero_pregunta] # Se obtiene la respuesta correcta de la lista de respuestas correctas
        if respuesta_usuario == respuesta_correcta: # Se compara la respuesta del usuario con la respuesta correcta
            if nivel == "Easy": # Se asigna el puntaje correspondiente al nivel 
                puntos_equipo.append(1)
            elif nivel == "Medium": 
                puntos_equipo.append(2)
            elif nivel == "Hard":
                puntos_equipo.append(3)
            messagebox.showinfo("Correcto", "¡Respuesta correcta!") # Se muestra un mensaje de respuesta correcta y se agrega el puntaje correspondiente
        else:
            messagebox.showerror("Incorrecto", f"Respuesta incorrecta. La respuesta correcta es {respuesta_correcta}")

    def mostrar_interfaz(pregunta, opciones, verificar_respuesta, puntos_equipo, clave, nivel, numero_pregunta): # Función para mostrar la interfaz
        root = tk.Tk() # Ventana para mostrar la interfaz
        root.title("Quiz GAME (ANASS EL MORABIT)") # Titulo de la ventana

        label_pregunta = tk.Label(root, text=pregunta, font=("Arial", 14), padx=10, pady=10) # Etiqueta de la pregunta
        label_pregunta.pack()

        respuesta_var = tk.StringVar()

        for opcion in opciones: # Botones de las opciones
            btn_opcion = tk.Radiobutton(root, text=opcion, variable=respuesta_var, value=opcion[0])
            btn_opcion.pack(anchor=tk.W)

        def responder(): # Función para responder
            respuesta_usuario = respuesta_var.get()
            verificar_respuesta(respuesta_usuario, puntos_equipo, clave, nivel, numero_pregunta)
            root.destroy()

        btn_responder = tk.Button(root, text="Responder", command=responder) # Boton para responder
        btn_responder.pack(pady=10)

        root.mainloop()

    def obtener_jugadores(): # Función para obtener los jugadores
        while True:
            try: # Instruccion para que el usuario ingrese un valor numerico
                numero_jugadores = int(input("¿Cuántos jugadores serán? (1-2) "))
                if 1 <= numero_jugadores <= 2:
                    jugadores = [input(f"¿El jugador {i + 1}?: ") for i in range(numero_jugadores)] # Lista de jugadores
                    break
            except ValueError:
                print("Por favor, ingrese un número")
        for i in range(numero_jugadores): # Imprime la lista de jugadores
            print(f"El jugador {i + 1} es {jugadores[i]}")
        return numero_jugadores, jugadores

    def jugar_turno(puntos_equipo): # Función para jugar un turno y mostrar la interfaz
        pregunta, opciones, clave, nivel, numero_pregunta = obtener_pregunta() # Se obtiene la pregunta, las opciones, el campo, el nivel y el numero de la pregunta
        print(f"El campo es {clave}") # Se imprime el campo
        mostrar_interfaz(pregunta, opciones, verificar_respuesta, puntos_equipo, clave, nivel, numero_pregunta) # Se muestra la interfaz
    def jugar():
        numero_jugadores, lista_jugadores = obtener_jugadores() # Se obtienen los jugadores
        puntos_equipo1 = [] # Puntos del equipo 1
        puntos_equipo2 = [] # Puntos del equipo 2

        if numero_jugadores == 2: # Si hay dos jugadores se jugan dos turnos a la vez
            for i in range(5):
                print(f"El jugador 1 ({lista_jugadores[0]}) va a jugar")
                jugar_turno(puntos_equipo1)
                print(f"El jugador 2 ({lista_jugadores[1]}) va a jugar")
                jugar_turno(puntos_equipo2)
        elif numero_jugadores == 1: # Si hay un jugador se juega un turno
            for i in range(10):
                jugar_turno(puntos_equipo1)
        if numero_jugadores == 2: # Si hay dos jugadores se compara el puntaje del equipo 1 con el puntaje del equipo 2
            print(f"El puntaje del equipo 1 es {sum(puntos_equipo1)}") 
            print(f"El puntaje del equipo 2 es {sum(puntos_equipo2)}")
            if sum(puntos_equipo1) > sum(puntos_equipo2):
                messagebox.showinfo("Ganador", f"El ganador es {lista_jugadores[0]}")
            elif sum(puntos_equipo1) < sum(puntos_equipo2):
                messagebox.showinfo("Ganador", f"El ganador es {lista_jugadores[1]}")
            else:
                messagebox.showinfo("Ganador", "Empate")
        elif numero_jugadores == 1: # Si hay un jugador se compara el puntaje de un equipo 
            messagebox.showinfo("Ganador", f"El puntaje es {sum(puntos_equipo1)}") 
  



    # Llamar a la función para iniciar el juego
    jugar()
    repeat=input("¿Quieres jugar de nuevo? (S/N) ")
    if repeat!="S":
        break
    