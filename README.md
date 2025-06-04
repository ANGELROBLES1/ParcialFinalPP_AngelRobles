# ParcialFinalPP_AngelRobles

- **Serie de Fourier:** Es una serie infinita que converge puntualmente a una función periodica y continua
- **Serie:** Comunicación de datos bit a bit a través de un único canal

# Implementaciones:
  - ## Iterativa
  - ![image](https://github.com/user-attachments/assets/68b68bd4-ca86-46a0-b436-8dae625ebbbf)


  - ![image](https://github.com/user-attachments/assets/baff73d4-402e-4667-8f58-e8fbc89fe386)



  - ## Recursiva
  - ![image](https://github.com/user-attachments/assets/3224bf0c-5eef-4cd9-8b0b-d8af7d855f1d)


  - ![image](https://github.com/user-attachments/assets/4603aaf9-7c7b-4e9d-810f-a6bf89330309)



# Analisis Comparativo
- ![image](https://github.com/user-attachments/assets/0a12f4e3-2966-4bcb-a326-3b9524786df7)

  - ## **¿Cuál método resulta más eficiente?**

- Despues de varias pruebas hechas, se visualiza que el metodo de **RECURSIVIDAD** es ligeramente mejor al tiempo pero para numeros pequeños. Probe con el numero 100Y 50, ahi el metodo que gano fue el iterativo esto quiere decir que para numeros grandes el metodo de **ITERACION** es mejor.
- 
  - **¿Por qué? (Considera aspectos como la complejidad temporal, la profundidad de recursión y la legibilidad del código)**

- En el aspecto de complejidad temporal tengo claro que en el iterativo ambos son O(n) osea complejidad de tiempo lineal de un algoritmo. Sin embargo en el **iterativo** se ejecuta un solo ciclo sin demas cosas a llamar a las funciones. En el **recursivo** cada llamado de una funcion genera un movimiento en la pila al ejecutar

- Siguiendo con el aspecto de la profundidad de la **recursion** estas generan muchas llamadas que se estan apilando asi consumiendo mas memoria en su momento, en los casos por ejemplo de valores grandes como lo probe con el 100 y 50 puede ser ineficiente y puede llegar a desbordasrse la pila en el peor de los casos

- En el ultimo aspecto de legibilidad del codigo nos quiere decir que en el codigo de **recursividad** este es como mas formal y es mucho mas facil de leer para problemas como hemos hecho con los factoriales, fibonacci y demas cosas. El codigo de iteracion es mas eficiente en los terminos de recursos de uso pero es mucho mas largo incluso se me complico en su momento ademas es menos intuitivo en algunos casos



